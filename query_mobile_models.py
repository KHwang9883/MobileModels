#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
手机机型信息查询脚本
用于查询解析后的手机机型数据
"""

import json
import argparse
from typing import Dict, List, Any, Optional


class MobileModelsQuery:
    def __init__(self, json_file: str = "mobile_models.json"):
        """
        初始化查询器
        
        Args:
            json_file: JSON数据文件路径
        """
        self.json_file = json_file
        self.data = self.load_data()
        
    def load_data(self) -> Dict[str, Any]:
        """
        加载JSON数据
        
        Returns:
            解析后的数据字典
        """
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"数据文件不存在: {self.json_file}")
            print("请先运行 parse_mobile_models.py 生成数据文件")
            return {}
        except Exception as e:
            print(f"加载数据文件失败: {e}")
            return {}
    
    def search_by_model_code(self, model_code: str) -> List[Dict[str, Any]]:
        """
        根据型号代码搜索
        
        Args:
            model_code: 型号代码，如 "A1203"
            
        Returns:
            匹配的结果列表
        """
        results = []
        model_code = model_code.upper().strip()
        
        for brand_file, brand_data in self.data.items():
            mappings = brand_data.get("mappings", [])
            for mapping in mappings:
                if mapping.get("model_code", "").upper() == model_code:
                    result = mapping.copy()
                    result["brand_file"] = brand_file
                    result["brand_title"] = brand_data.get("brand_info", {}).get("title", brand_file)
                    results.append(result)
                    
        return results
    
    def search_by_device_name(self, device_name: str) -> List[Dict[str, Any]]:
        """
        根据设备名称搜索
        
        Args:
            device_name: 设备名称，如 "iPhone"
            
        Returns:
            匹配的结果列表
        """
        results = []
        device_name = device_name.lower().strip()
        
        for brand_file, brand_data in self.data.items():
            mappings = brand_data.get("mappings", [])
            for mapping in mappings:
                if device_name in mapping.get("device_name", "").lower():
                    result = mapping.copy()
                    result["brand_file"] = brand_file
                    result["brand_title"] = brand_data.get("brand_info", {}).get("title", brand_file)
                    results.append(result)
                    
        return results
    
    def search_by_model_name(self, model_name: str) -> List[Dict[str, Any]]:
        """
        根据机型名称搜索
        
        Args:
            model_name: 机型名称，如 "华为"
            
        Returns:
            匹配的结果列表
        """
        results = []
        model_name = model_name.lower().strip()
        
        for brand_file, brand_data in self.data.items():
            mappings = brand_data.get("mappings", [])
            for mapping in mappings:
                if model_name in mapping.get("model_name", "").lower():
                    result = mapping.copy()
                    result["brand_file"] = brand_file
                    result["brand_title"] = brand_data.get("brand_info", {}).get("title", brand_file)
                    results.append(result)
                    
        return results
    
    def get_brand_statistics(self) -> Dict[str, int]:
        """
        获取各品牌统计信息
        
        Returns:
            品牌统计字典
        """
        stats = {}
        for brand_file, brand_data in self.data.items():
            brand_title = brand_data.get("brand_info", {}).get("title", brand_file)
            model_count = brand_data.get("total_models", 0)
            stats[brand_title] = model_count
            
        return dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))
    
    def print_results(self, results: List[Dict[str, Any]], limit: int = 10):
        """
        打印搜索结果
        
        Args:
            results: 搜索结果列表
            limit: 显示结果数量限制
        """
        if not results:
            print("未找到匹配的结果")
            return
            
        print(f"找到 {len(results)} 个匹配结果:")
        print("-" * 80)
        
        for i, result in enumerate(results[:limit]):
            print(f"{i+1}. 型号代码: {result.get('model_code', 'N/A')}")
            print(f"   机型名称: {result.get('model_name', 'N/A')}")
            print(f"   设备名称: {result.get('device_name', 'N/A')}")
            if result.get('codename'):
                print(f"   代号: {result.get('codename')}")
            if result.get('model_id'):
                print(f"   型号ID: {result.get('model_id')}")
            print(f"   品牌: {result.get('brand_title', 'N/A')}")
            print()
            
        if len(results) > limit:
            print(f"... 还有 {len(results) - limit} 个结果未显示")


def main():
    """
    命令行主函数
    """
    parser = argparse.ArgumentParser(description="手机机型信息查询工具")
    parser.add_argument("--code", "-c", help="根据型号代码搜索")
    parser.add_argument("--device", "-d", help="根据设备名称搜索")
    parser.add_argument("--model", "-m", help="根据机型名称搜索")
    parser.add_argument("--stats", "-s", action="store_true", help="显示品牌统计信息")
    parser.add_argument("--limit", "-l", type=int, default=10, help="结果显示数量限制")
    parser.add_argument("--json", "-j", default="mobile_models.json", help="JSON数据文件路径")
    
    args = parser.parse_args()
    
    # 创建查询器
    query = MobileModelsQuery(args.json)
    
    if not query.data:
        return
    
    # 显示统计信息
    if args.stats:
        stats = query.get_brand_statistics()
        print("=== 品牌统计信息 ===")
        for brand, count in stats.items():
            print(f"{brand}: {count} 个型号")
        return
    
    # 执行搜索
    results = []
    
    if args.code:
        results = query.search_by_model_code(args.code)
        print(f"搜索型号代码: {args.code}")
    elif args.device:
        results = query.search_by_device_name(args.device)
        print(f"搜索设备名称: {args.device}")
    elif args.model:
        results = query.search_by_model_name(args.model)
        print(f"搜索机型名称: {args.model}")
    else:
        print("请指定搜索条件，使用 -h 查看帮助")
        return
    
    # 显示结果
    query.print_results(results, args.limit)


if __name__ == "__main__":
    main()
