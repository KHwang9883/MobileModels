# Mobile Models

[![issues](https://img.shields.io/github/issues/KHwang9883/MobileModels?color=green)](https://github.com/KHwang9883/MobileModels/issues)
[![prs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/KHwang9883/MobileModels/pulls)
[![stars](https://img.shields.io/github/stars/KHwang9883/MobileModels.svg?color=yellow)](https://github.com/KHwang9883/MobileModels)
[![forks](https://img.shields.io/github/forks/KHwang9883/MobileModels.svg?color=orange)](https://github.com/KHwang9883/MobileModels)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Collecting device names, models and internal codenames.

[Issue submission](https://github.com/KHwang9883/MobileModels/issues) and [Pull Requests](https://github.com/KHwang9883/MobileModels/pulls) are welcomed if you find mistakes.

Unlisted brands usually not include international models.

| Name | Brand | Range |
| :-: | :-: | :-: |
| [apple_all_en](brands/apple_all_en.md) | Apple | iPhone, iPad, iPod touch, Apple Watch, Apple TV and Apple Vision |
| [asus_en](brands/asus_en.md) | ASUS | ROG Phone, Zenfone |
| [blackshark_en](brands/blackshark_en.md) | Black Shark | All models |
| [google](brands/google.md) | Google | Google Pixel phones, tablets & watch |
| [honor_global_en](brands/honor_global_en.md) | HONOR | All international models |
| [huawei_global_en](brands/huawei_global_en.md) | HUAWEI | HUAWEI Mate, Pura, nova & Y series, MediaPad & MatePad series |
| [meizu_en](brands/meizu_en.md) | Meizu | All models |
| [mitv_global_en](brands/mitv_global_en.md) | Xiaomi | All international/Indian Xiaomi & Redmi TV models (excluding Chinese models) |
| [nothing](brands/nothing.md) | Nothing | All models |
| [oneplus_en](brands/oneplus_en.md) | OnePlus | All models |
| [oppo_global_en](brands/oppo_global_en.md) | OPPO | International models since 2018 |
| [samsung_global_en](brands/samsung_global_en.md) | Samsung | International models since 2019 |
| [sony](brands/sony.md) | Sony | All models since 2015 |
| [realme_global_en](brands/realme_global_en.md) | realme | All international models |
| [vivo_global_en](brands/vivo_global_en.md) | vivo | International models since 2019 |
| [xiaomi_en](brands/xiaomi_en.md) | Xiaomi | Xiaomi/Redmi/POCO phones & tablets |

## Python Parsing Tools

This project provides Python scripts to parse all brand Markdown files and convert the data into structured JSON format for programmatic use.

### Features

- 🔍 **Auto Parsing**: Traverse all Markdown files in the `brands` directory
- 📊 **Data Extraction**: Extract model codes, device names, codenames and complete information
- 💾 **JSON Output**: Generate structured JSON data files
- 🔎 **Quick Query**: Command-line tool with multiple query methods

### Usage

#### 1. Parse Data

```bash
# Parse all Markdown files and generate mobile_models.json
python3 parse_mobile_models.py
```

#### 2. Query Data

```bash
# Query by model code
python3 query_mobile_models.py --code A1203

# Search by device name
python3 query_mobile_models.py --device iPhone --limit 5

# Search by model name
python3 query_mobile_models.py --model "Galaxy" --limit 10

# View brand statistics
python3 query_mobile_models.py --stats

# View help information
python3 query_mobile_models.py --help
```

#### 3. Data Statistics

After parsing, you can get:
- **43 brand files**
- **7,700+ mobile models**
- Complete brand information and mapping relationships

### Data Format

The generated JSON file uses the following structure:

```json
{
  "brand_file": {
    "brand_info": {
      "title": "Brand Title",
      "scope": "Coverage Scope",
      "codename": "Codename Support",
      "overseas": "International Models Info"
    },
    "mappings": [
      {
        "model_code": "Model Code",
        "model_name": "Model Name",
        "device_name": "Device Name",
        "codename": "Codename",
        "model_id": "Model ID"
      }
    ],
    "total_models": count
  }
}
```

### Script Files

- `parse_mobile_models.py` - Main parsing script
- `query_mobile_models.py` - Query tool script
- `mobile_models.json` - Generated data file

## Changelog

[CHANGELOG_en.md](CHANGELOG_en.md)

## References

- [TENAA](http://zd.taf.org.cn)
- [CQCCMS](http://webdata.cqccms.com.cn/webdata/query/CCCCerti.do)
- [MIIT](https://ythzxfw.miit.gov.cn/resultQuery)
- [China Telecom Tianyi Devices](http://surfing.tydevice.com/)
- [Google Play Supported Devices](http://storage.googleapis.com/play_public/supported_devices.html)
- [Wi-Fi Alliance](https://www.wi-fi.org)
- [Bluetooth Launch Studio](https://launchstudio.bluetooth.com/Listings/Search)
- [Xiaomi Firmware Updater](https://xiaomifirmwareupdater.com/)
- [Huawei Open Source Release Center](https://consumer.huawei.com/en/opensource/)
- [ReaMEIZU](https://reameizu.com/)
- [The Apple Wiki](https://theapplewiki.com/)
- [ipsw.me](https://ipsw.me)
- [XDA Developers](https://www.xda-developers.com)
- [Huawei Firmware Database](https://pro-teammt.ru/en/online-firmware-database-ru/)
- [XSMS IMEI Database](http://xsms.com.ua/phone/imei/all/1)
- [Android Dumps](https://dumps.tadiphone.dev/dumps)
- [Lenovo Android タブレット一覧](https://idomizu.dev/archives/20150)

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
