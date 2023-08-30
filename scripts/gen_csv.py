#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File  : mo_models.py
# Author: anyongjin
# Date  : 2022/11/12
'''
将设备型号从MarkDown读取为CSV格式的脚本
输出列：设备编号，设备类型，品牌代码，品牌名，型号编码，型号昵称，型号名称，版本名称
'''
import os
import re
import traceback
import pandas as pd
from typing import Optional, List
from os.path import dirname, abspath

source_dir = os.path.join(dirname(dirname(abspath(__file__))), 'brands')

device_type: Optional[str] = None  # 设备类型：手机，电视，手环
root_brand: Optional[str] = None  # 品牌代码
root_brand_title: Optional[str] = None  # 品牌名
devc_code: Optional[str] = None  # 设备型号代码
devc_code_alias: Optional[str] = None  # 设备型号昵称
devc_model_names: List[str] = []  # 设备型号正式名


_re_title = re.compile(r'^#+')
_re_blanks = re.compile(r'\s+')
_re_char = re.compile(r'([+]+|[^\W_])')
_re_word = re.compile(r'([a-zA-Z0-9]+|[^\W_]{,3})')
_re_non_word = re.compile(r'[\W_]+')
# 匹配model和版本的正则
_re_model_ver = re.compile(r'^`(([^`]+)`\s*)+:\s*')
_re_model_item = re.compile(r'`([^`]+)`')
# 匹配设备类型的正则
_re_device_type = re.compile(r'(手机|手表|手环|平板|电视主机|盒子|(智能)?电视|笔记本电脑|设备|Mobile|Phone|Pad|Pod|Tablet|Watch|WATCH|Device|\bTV\b|学习智慧屏|智慧屏)')
_device_map = dict(
    手机='mob',
    mobile='mob',
    phone='mob',
    电视='tv',
    智能电视='tv',
    学习智慧屏='pad',
    智慧屏='tv',
    设备='device',
    手表='watch',
    手环='band',
    笔记本电脑='computer',
    tablet='pad',
    平板='pad',
    电视主机='tv_hub',
    盒子='tv_hub'
)

pd_cols = 'model,dtype,brand,brand_title,code,code_alias,model_name,ver_name'.split(',')
pd_rows = []


def _process_h1(line: str):
    # 设置设备类型，品牌名
    global device_type, root_brand, root_brand_title
    assert root_brand, 'root_brand is required'
    # 替换无用描述词
    line = re.sub(r'(Global|早期|国行)', '', line)
    # 查找品牌结束位置
    end_pos, device_type = _read_device_type(line)
    brand_str = line[: end_pos]
    # 只获取长度不小于2的有效单词
    words = [mat.group() for mat in re.finditer(r'\w{2,}', brand_str) if len(mat.group()) >= 2]
    if not words:
        raise ValueError(f'no brand found in h1: {line}')
    if len(words) == 1:
        root_brand_title = words[0]
        return
    root_brand_title = root_brand
    for w in words:
        if root_brand.lower() == w.lower():
            continue
        root_brand_title = w
        break


def _read_device_type(line: str, raise_err: bool = True):
    type_mat = _re_device_type.search(line)
    if not type_mat:
        if raise_err:
            raise ValueError(f'unknown h1 format: {line}')
        else:
            return -1, None
    dtype = type_mat.group().lower()
    dtype = _device_map.get(dtype, dtype)
    return type_mat.start(), dtype


def _process_bold_model(line: str):
    '''
    处理加粗的设备型号行
    :param line:
    :return:
    '''
    global device_type, devc_code, devc_code_alias, devc_model_names
    _reset_context('code')
    code_mat = re.search(r'\[\`([^`]+)\`\]', line)
    code_nmat = re.search(r'\(\`([^`]+)\`\)', line)
    md_start, md_end = 0, len(line)
    if code_mat:
        devc_code = code_mat.group(1)
        md_start = code_mat.end()
    if code_nmat:
        devc_code_alias = code_nmat.group(1)
        md_end = code_nmat.start()
    model_name = _strip_text(line[md_start: md_end])
    # 检查设备类型是否变化
    dtype = _read_device_type(model_name, False)[1]
    if dtype and dtype != device_type:
        device_type = dtype
    # 检查是否一行有多个品牌，以/分割
    model_names = _try_split_by_splash(model_name)
    model_names = [_strip_text(mname) for mname in model_names]
    # 检查是否包含品牌，包含则去除
    devc_model_names = []
    for mname in model_names:
        brand_start = mname.find(root_brand)
        if brand_start >= 0:
            # 型号包含品牌名，去除
            mname = _strip_text(mname[brand_start + len(root_brand):])
            dtype_mat = _re_device_type.search(mname)
            if dtype_mat:
                mname = _strip_text(mname[dtype_mat.end():])
        devc_model_names.append(mname)


def _get_ver_name_with_model(ver_full: str, model_name: str):
    '''
    从最精细的版本中去除型号信息。可能不完全包含版本名称，而是包含版本的一部分
    :param ver_full:
    :param model_name:
    :return:
    '''
    ver_words = _re_char.finditer(ver_full)
    model_first_word = _re_word.search(model_name).group().lower()
    ver_start = ver_full.lower().find(model_first_word)
    if ver_start < 0:
        return ver_full
    model_chars = [mat.group() for mat in _re_char.finditer(model_name)]
    model_idx = 0
    for ver_mat in ver_words:
        if ver_mat.start() < ver_start:
            continue
        if model_idx >= len(model_chars):
            return '#' + _strip_text(ver_full[ver_mat.start():])
        ver_word = ver_mat.group()
        md_word = model_chars[model_idx]
        if ver_word.lower() == md_word.lower():
            model_idx += 1
            continue
        clean_ver = _strip_text(ver_full[ver_mat.start():])
        return '#' + clean_ver
    return '#'


def _strip_text(text: str):
    # 去除头部无效字符
    start = _re_char.search(text)
    if not start:
        return ''
    text = text[start.start():]
    # 去除尾部无效字符
    end_pos = len(text) - _re_char.search(text[::-1]).start()
    clean_text = text[:end_pos]
    # 补全缺失的括号
    brackets, prepend, appends = [], [], []
    brac_map = {'(': ')', '（': '）', ')': '(', '）': '（'}
    for c in clean_text:
        if c in {'(', '（'}:
            btype = 1
        elif c in {')', '）'}:
            btype = 2
        else:
            continue
        if btype == 1:
            brackets.append(c)
        elif len(brackets) > 0:
            brackets.pop()
        else:
            prepend.append(brac_map[c])
    for brac in brackets:
        appends.append(brac_map[brac])
    return ''.join([*prepend, clean_text, *appends])


def _get_ver_name(ver_full: str):
    ver_names, last_err = [], None
    for i, mname in enumerate(devc_model_names):
        try:
            ver_names.append((i, _get_ver_name_with_model(ver_full, mname)))
        except ValueError as e:
            last_err = e
    if not ver_names:
        raise last_err
    ver_item = sorted(ver_names, key=lambda x: len(x[1]))[0]
    return ver_item[1] if not ver_item[0] else f'{ver_item[0]}{ver_item[1]}'


def _try_split_by_splash(type_name: str):
    # 检查是否是/分割的多个版本。多个版本一般前几个单词相同
    ver_full_names = [vname.strip() for vname in type_name.split('/')]
    if len(ver_full_names) > 1:
        name1_arr = _re_non_word.split(ver_full_names[0])
        name2_arr = _re_non_word.split(ver_full_names[1])
        if name1_arr[0] != name2_arr[0]:
            # 首个单词不同，不认为是多个版本
            return [type_name]
    return ver_full_names


def _process_model_ver(line: str, mat: re.Match):
    global device_type, root_brand, root_brand_title, devc_code, devc_code_alias, devc_model_names
    model_text = mat.group()
    models = [m.group(1) for m in _re_model_item.finditer(model_text)]
    ver_full = _strip_text(line[mat.end():])
    ver_full_names = _try_split_by_splash(ver_full)
    for full_name in ver_full_names:
        ver_name = _get_ver_name(full_name)
        for model in models:
            pd_rows.append((model, device_type, root_brand, root_brand_title, devc_code, devc_code_alias,
                       '|'.join(devc_model_names), ver_name))


def _process_line(line: str):
    global device_type
    if line.startswith('-'):
        return
    title_mat = _re_title.search(line)
    title_level = len(title_mat.group(0)) if title_mat else 0
    pure_line = line[title_level:].strip()
    if title_level == 1:
        _process_h1(pure_line)
    elif title_level == 2:
        dtype = _read_device_type(pure_line, False)[1]
        if dtype:
            device_type = dtype
        # 系列，子品牌，不同产品类型
        return
    elif title_level:
        raise ValueError(f'unknown title type: {title_level}, {line}')
    elif pure_line.startswith('**') and pure_line.endswith('**'):
        _process_bold_model(pure_line[2: -2])
    elif detail_mat := _re_model_ver.search(pure_line):
        _process_model_ver(pure_line, detail_mat)
    else:
        raise ValueError(f'unknown line: {line}')


def _reset_context(level: str):
    '''
    重置上下文: brand, code
    :param level:
    :return:
    '''
    global device_type, root_brand_title, devc_code, devc_code_alias, devc_model_names
    if level == 'brand' or level == 'all':
        device_type = None
        root_brand_title = None
    if level == 'code' or level == 'all':
        devc_code = None
        devc_code_alias = None
        devc_model_names = []


def sync_brands(name: str):
    global root_brand
    _reset_context('all')
    root_brand = re.split(r'[\W_]+', name)[0].replace('shouji', '')
    full_path = os.path.join(source_dir, name)
    with open(full_path, 'r', encoding='utf-8') as fdata:
        for line in fdata:
            try:
                line = line.strip()
                if not line:
                    continue
                _process_line(line)
            except Exception as e:
                print(f'exception process {root_brand}: {e}')
                traceback.print_exc()


if __name__ == '__main__':
    fnames = os.listdir(source_dir)
    for name in fnames:
        # if name.endswith('_en.md'):
        #     continue
        print(f'process: {name}')
        sync_brands(name)
    df = pd.DataFrame(pd_rows, columns=pd_cols)
    df.to_csv('./models.csv', index=False)
    print('generate complete, out file: ./models.csv')
