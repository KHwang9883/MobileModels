# 说明
这是用于将markdown格式的设备型号介绍转为csv格式的python脚本。  
输出列：设备编号，设备类型，品牌代码，品牌名，型号编码，型号昵称，型号名称，版本名称  

**设备编号(model)**  
能从浏览器UserAgent中获取到的设备编号，如华为P40对应"ANA-AL00"  
一个model可能对应多个版本，也可能多个model对应一个版本。  
**设备类型(device_type)**  
包含：手机、手表、平板、电视、电视盒子、笔记本、pod等  
对应csv的值：mob,watch,pad,tv,tv_hub,computer,pod  
会从一级标题、二级标题、加粗行中尝试提取  
**品牌代码(brand)**  
从brands目录下的文件名中提取第一个单词  
**品牌名(brand_title)**  
从一级标题中按正则提取  
**型号编码(code)**  
从加粗行的前面中括号中提取  
**型号昵称(code_alias)**  
从加粗行的尾部小括号中提取  
**型号名称(model_name)**  
从加粗行去掉code和code_alias后剩余的内容  
注意：一行可能有多个型号名称，以"/"分割  
**版本名称(ver_name)**  
从model行，提取冒号之后的内容，再去掉model_name的重合部分，只保留版本信息  
有些版本名称可能没有完全包含model_name，而是只包含其中一部分，还有些可能完全没包含model_name  
输出ver_name中，如果包含model_name，然后去掉了一部分，则规定以"#"开头。  
如果有多个model_name，且包含的不是第1个，则"#"前面会添加索引
