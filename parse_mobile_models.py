#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
手机机型信息库解析脚本
解析brands目录下的markdown文件，提取手机型号与机型名称的映射关系
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any


class MobileModelsParser:
    def __init__(self, brands_dir: str = "brands"):
        """
        初始化解析器
        
        Args:
            brands_dir: brands目录路径
        """
        self.brands_dir = Path(brands_dir)
        self.models_data = {}
        
    def parse_all_files(self) -> Dict[str, Any]:
        """
        解析所有markdown文件
        
        Returns:
            包含所有映射关系的字典
        """
        if not self.brands_dir.exists():
            raise FileNotFoundError(f"brands目录不存在: {self.brands_dir}")
            
        # 遍历brands目录下的所有markdown文件
        for md_file in self.brands_dir.glob("*.md"):
            print(f"正在解析: {md_file.name}")
            brand_data = self.parse_markdown_file(md_file)
            if brand_data:
                self.models_data[md_file.stem] = brand_data
                
        return self.models_data
    
    def parse_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        """
        解析单个markdown文件
        
        Args:
            file_path: markdown文件路径
            
        Returns:
            该文件的解析结果
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"读取文件失败 {file_path}: {e}")
            return {}
            
        # 提取文件头部信息
        brand_info = self.extract_brand_info(content)
        
        # 提取映射关系
        mappings = self.extract_mappings(content)
        
        return {
            "brand_info": brand_info,
            "mappings": mappings,
            "total_models": len(mappings)
        }
    
    def extract_brand_info(self, content: str) -> Dict[str, str]:
        """
        提取品牌信息（从文件头部的元信息）
        
        Args:
            content: markdown文件内容
            
        Returns:
            品牌信息字典
        """
        brand_info = {}
        
        # 提取标题
        title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
        if title_match:
            brand_info["title"] = title_match.group(1).strip()
            
        # 提取汇总范围
        scope_match = re.search(r'-\s*汇总范围[:：]\s*(.+)', content)
        if scope_match:
            brand_info["scope"] = scope_match.group(1).strip()
            
        # 提取codename信息
        codename_match = re.search(r'-\s*codename[:：]\s*(.+)', content)
        if codename_match:
            brand_info["codename"] = codename_match.group(1).strip()
            
        # 提取海外机型信息
        overseas_match = re.search(r'-\s*是否包含海外机型[:：]\s*(.+)', content)
        if overseas_match:
            brand_info["overseas"] = overseas_match.group(1).strip()
            
        return brand_info
    
    def extract_mappings(self, content: str) -> List[Dict[str, Any]]:
        """
        提取映射关系
        
        Args:
            content: markdown文件内容
            
        Returns:
            映射关系列表
        """
        mappings = []
        
        # 按行处理
        lines = content.split('\n')
        current_device = None
        current_codename = None
        current_model_id = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # 匹配设备标题行，格式如: **[`M68AP`] iPhone (`iPhone1,1`):**
            device_match = re.match(r'\*\*\[?`?([^`\]]*)`?\]?\s*([^(]*?)(?:\s*\(`?([^)`]*)`?\))?\s*[:：]\*\*', line)
            if device_match:
                current_codename = device_match.group(1).strip() if device_match.group(1) else None
                current_device = device_match.group(2).strip()
                current_model_id = device_match.group(3).strip() if device_match.group(3) else None
                continue
                
            # 匹配型号映射行，格式如: `A1203`: iPhone 或 `HUAWEI MT1-T00`: 华为 Ascend Mate 移动版
            model_match = re.match(r'`([^`]+)`[:：]\s*(.+)', line)
            if model_match and current_device:
                model_code = model_match.group(1).strip()
                model_name = model_match.group(2).strip()
                
                mapping = {
                    "model_code": model_code,
                    "model_name": model_name,
                    "device_name": current_device
                }
                
                if current_codename:
                    mapping["codename"] = current_codename
                    
                if current_model_id:
                    mapping["model_id"] = current_model_id
                    
                mappings.append(mapping)
                
        return mappings
    
    def save_to_json(self, output_file: str = "mobile_models.json", indent: int = 2):
        """
        保存解析结果到JSON文件
        
        Args:
            output_file: 输出文件路径
            indent: JSON缩进
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.models_data, f, ensure_ascii=False, indent=indent)
            print(f"解析结果已保存到: {output_file}")
        except Exception as e:
            print(f"保存文件失败: {e}")
    
    def print_statistics(self):
        """
        打印统计信息
        """
        total_files = len(self.models_data)
        total_models = sum(brand_data.get("total_models", 0) for brand_data in self.models_data.values())
        
        print(f"\n=== 解析统计 ===")
        print(f"处理文件数: {total_files}")
        print(f"总型号数: {total_models}")
        print(f"\n各品牌型号数:")
        
        for brand_file, brand_data in self.models_data.items():
            brand_name = brand_data.get("brand_info", {}).get("title", brand_file)
            model_count = brand_data.get("total_models", 0)
            print(f"  {brand_name}: {model_count} 个型号")


def main():
    """
    主函数
    """
    print("开始解析手机机型信息库...")
    
    # 创建解析器实例
    parser = MobileModelsParser()
    
    try:
        # 解析所有文件
        parser.parse_all_files()
        
        # 保存到JSON文件
        parser.save_to_json()
        
        # 打印统计信息
        parser.print_statistics()
        
        print("\n解析完成！")
        
    except Exception as e:
        print(f"解析过程中出现错误: {e}")


if __name__ == "__main__":
    main()
