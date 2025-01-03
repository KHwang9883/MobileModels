# 各 Android 手机厂商 Bootloader 解锁 / 内核开源 / 解锁后保修情况

> 以下所列为官方支持情况
>
> 如有错漏欢迎 PR
> 
> 关于「自定义信任根」功能，请参考 [Android 开发者文档](https://source.android.com/docs/security/features/verifiedboot/device-state?hl=zh-cn#user-settable-root-of-trust)

- ✅ 支持/是 | **可点击**
- ⚠️ 名义上支持但实际上近乎不支持 | **可点击**
- ⏹ 部分支持/部分开源/部分保修 | **可点击**
- ❌ 不支持/否

## 360
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: ❌

## 华硕 (ASUS)
- **Bootloader 解锁**: ❌
- **是否支持回锁**: ❌
- **Linux 内核开源**: [✅](https://www.asus.com/support/download-center/)
- **备注**:
    - 中国大陆销售的 ROG 设备不支持解锁
    - 目前因解锁造成的漏洞，官方已关闭解锁渠道，所有机型（包括 ROG、ZenFone）均无法解锁

## 黑鲨 (Black Shark) 
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: ❌

## 酷派 (Coolpad)
- **Bootloader 解锁**: ✅
- **解锁等待时长**: 不详
- **解锁后保修状态**: 不详
- **是否支持回锁**: 不详
- **Linux 内核开源**: ❌

## Google
- **Bootloader 解锁**: [⏹](https://source.android.com/source/running#unlocking-the-bootloader)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ✅
- **Linux 内核开源**: [✅](https://source.android.com/docs/setup/build/building-pixel-kernels)
- **备注**:
    - 启用 OEM 解锁功能需已连接到互联网并已签入 Google（即便设备不久前曾连接到互联网，也仍然可能没有签入 Google）。如需强制签入，请在拨号器中输入 `*#*#2432546#*#*`
    - 有些设备需要运营商干预才能解锁。如需了解详情，请与您的运营商联系
    - 美国 Verizon 版本 Pixel 均不支持 OEM 解锁

## 荣耀 (HONOR)
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: [⏹](https://www.hihonor.com/global/opensource/)
- **备注**: 缺少部分机型内核源码

## 华为 (HUAWEI)
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: [⏹](https://consumer.huawei.com/en/opensource/)
- **备注**:
    - 官方已关闭解锁渠道
    - 部分机型未开源

## HTC
- **Bootloader 解锁**: [⏹](https://www.htcdev.com/bootloader/)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ❌
- **Linux 内核开源**: [✅](https://www.htcdev.com/devcenter/downloads)
- **备注**:
    - 解锁需注册 HTCdev 账户
    - 提交后会在几分钟内将解锁文件发至邮箱
    - 2018 年 6 月之后推出的机型均不支持解锁

## 联想 (Lenovo)
- **Bootloader 解锁**: [✅](https://www.zui.com/iunlock)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ⏹
- **是否支持回锁**: ⏹
    - **是否支持自定义信任根**: ⏹
- **Linux 内核开源**: ❌
- **备注**:
    - 申请解锁文件需登录联想账号
    - 部分设备无需申请解锁文件
    - 提交后会在几分钟内将解锁文件发至邮箱
    - 解锁后若重新回锁，则不影响保修
    - 部分设备不允许回锁
    - 部分机型解锁后会熔断 TEE，不可恢复

## 乐视 (Letv)
- **Bootloader 解锁**: ✅
- **解锁等待时长**: 不详
- **解锁后保修状态**: 不详
- **是否支持回锁**: 不详
- **Linux 内核开源**: ❌

## LG
- **Bootloader 解锁**: [❌](https://developer.lge.com/resource/mobile/RetrieveBootloader.dev)
- **Linux 内核开源**: [✅](https://opensource.lge.com/index)
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ❌
- **备注**: 官方解锁渠道已随手机业务同步下线

## 魅族 (MEIZU)
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: [⏹](https://github.com/meizuosc)
- **备注**:
    - [官方仅支持 root](https://mroot.flyme.cn/)，root 后 OTA 功能失效
    - 仅少部分早期机型内核开源

## 微软 (Microsoft)
- **Bootloader 解锁**: ✅
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ✅
- **Linux 内核开源**: [✅](https://github.com/microsoft/surface-duo-oss)
- **备注**:
    - 解锁 Bootloader 不需要解锁网络锁
    - 仅限搭载 Android 系统的设备

## 摩托罗拉 (Motorola)
- **Bootloader 解锁**: [✅](https://motorola-global-portal.custhelp.com/app/standalone/bootloader/unlock-your-device-a)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ⏹
    - **是否支持自定义信任根**: ❌
- **Linux 内核开源**: [✅](https://github.com/MotorolaMobilityLLC)
- **备注**:
    - 解锁后无法恢复出厂 `oem_locked` 状态
    - 解锁后 OTA 功能失效
    - 解锁需绑定 My Moto Care
    - 提交后会在几分钟内将解锁文件发至邮箱
    - 部分机型解锁后会熔断 TEE，不可恢复

## 诺基亚 (HMD Nokia)
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: [✅](https://www.nokia.com/phones/en_int/opensource)
- **备注**: 官方未提供解锁

## Nothing
- **Bootloader 解锁**: ✅
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ✅
- **Linux 内核开源**: [✅](https://github.com/NothingOSS)
- **备注**:
    - 无需申请解锁码，无任何解锁限制
    - 解锁后会暂时屏蔽 TEE，回锁后恢复

## 努比亚 (nubia) & 红魔 (Red Magic)
- **Bootloader 解锁**: ⏹
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: 不详
- **是否支持回锁**: ⏹
    - **是否支持自定义信任根**: 不详
- **Linux 内核开源**: [⏹](https://github.com/ztemt) [⏹](https://opensource.ztedevices.com/)
- **备注**: 努比亚官方不提供解锁；红魔 9 系列及后续的新产品不再提供解锁；红魔 8 等旧产品更新系统后也不再提供解锁

## 一加 (OnePlus)
- **Bootloader 解锁**: ✅
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ⏹
- **Linux 内核开源**: [✅](https://github.com/OnePlusOSS)
- **备注**:
    - 无需申请解锁码，无任何解锁限制
    - 解锁后会暂时屏蔽 TEE，回锁后恢复（解锁后的 TEE 功能除 SOTER key 外已可永久修复）
    - 一加 9 系列及之前的设备支持自定义信任根。之后的设备由于已知问题尚未解决，暂不支持该功能

## OPPO
- **Bootloader 解锁**: [⏹](https://www.oppo.cn/thread-397164526-1)
- **解锁等待时长**: 720 小时 (1 月)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: 不详
- **Linux 内核开源**: [✅](https://github.com/oppo-source)
- **备注**:
    - 仅部分机型支持解锁
    - 申请深度测试需登录欢太账号
    - 解锁后会暂时屏蔽 TEE，回锁后恢复（解锁后的 TEE 功能除 SOTER key 外已可永久修复）

## 真我 (realme)
- **Bootloader 解锁**: [⏹](https://www.realmebbs.com/post-details/1275426081138028544)
- **解锁等待时长**: 168 小时（7 天）
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: 不详
- **Linux 内核开源**: [✅](https://github.com/realme-kernel-opensource)
- **备注**:
    - 在中国大陆地区通过正规渠道购买，且目前软件没有停止维护的真我手机均支持解锁
    - GT 系列发布会后一个月第一次首次开放 300 名额，次月开始至停止维护每月 1 日释放 200 名额
    - 其他系列发布会后一个月第一次首次开放 200 名额，次月开始至停止维护每月 1 日释放 200 名额
    - 申请深度测试需登录欢太账号
    - 深度测试资格有 7 天时间限制，超过 7 天未实际执行解锁需要重新申请
    - 手机被root后，如有需要，可以联系realme服务中心协助刷机。若能刷回官方版本，则不影响手机保修状态，但是无法享受退换货服务；若不能刷回官方版本或因此而导致手机硬件故障，则不在保修范围内，需视情况付费维修
    - 解锁后会暂时屏蔽 TEE，回锁后恢复（解锁后的 TEE 功能除 SOTER key 外已可永久修复）

## 三星 (Samsung)
- **Bootloader 解锁**: ⏹
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ⏹
- **Linux 内核开源**: [✅](https://opensource.samsung.com/main)
- **备注**:
    - 解锁将导致 KNOX 熔断，钱包、健康等功能失效，保修丢失；部分机型解锁还将导致相机永久无法工作（如 Galaxy Fold 系列）
    - 美版设备不支持解锁
    - 仅部分地区的设备系统支持免解锁互刷（但支持 ID Attestation 的设备在互刷后会破坏该功能，导致 RKP 模式下 TEE 无法正常获取密钥，从而失效）

## 索尼 (SONY)
- **Bootloader 解锁**: [✅](https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ⏹
- **Linux 内核开源**: [✅](https://github.com/sonyxperiadev/kernel)
- **备注**:
    - 需申请解锁码
    - 部分机型解锁将导致相机永久无法工作

## 坚果 (Smartisan)
- **Bootloader 解锁**: ⏹
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: 不详
- **是否支持回锁**: ❌
- **Linux 内核开源**: [⏹](https://github.com/SmartisanTech/SmartisanOS_Kernel_Source)
- **备注**:
    - Pro 3 及以后的消费版机型不支持解锁
    - 缺少部分机型内核源码

## vivo
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: [⏹](https://opensource.vivo.com/Project)
- **备注**:
    - 官方未提供解锁
    - 缺少部分机型内核源码

## 小米 (Xiaomi)
- **Bootloader 解锁**:
    - **国行机型:** [⚠️](https://web.vip.miui.com/page/info/mio/mio/testDetails?type=BL_BLOCK&id=-1)
    - **非国行机型:** [⚠️](https://c.mi.com/global/post/710306/)
- **解锁等待时长**:
    - **HyperOS 机型:** 72 小时 (3 天)
    - **MIUI 机型:** 168/360-2880 小时 (7/15 天 - 4 月)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ❌
- **Linux 内核开源**: [⏹](https://github.com/MiCode)
- **备注**:
    - 对于 HyperOS 机型：
        - 已解锁设备若处于 MIUI，将不会收到 HyperOS 的 OTA 推送
        - 2025年起每账号每年最多允许解锁 1 台设备
        - 对于国行 HyperOS 机型：
            - 需使用小米社区 APP 申请，申请成功不代表审核通过，需等待最终审核结果
            - 解锁权限有效期截至当年 12 月 31 日 23:59
            - 申请解锁权限需满足: 1) 通过《解锁资格答题测试》；2) 社区成长等级达到 5 段；3）完成实名认证
            - 答题开放时间不固定，每次参与需间隔 7 天；每场答题的最迟进场时间为该场次答题开始后的 10 分钟；答题成绩每周一晚上 23:59 失效
            - 用户即使满足解锁申请条件，如在社交媒介（包括但不限于各论坛、微博、微信、QQ 群等）对小米有过恶意诋毁、谩骂、造谣等情况，在申请时不填写申请理由、或使用 AI 生成申请理由、或申请理由出现过辱骂威胁等内容，或出现被判定为作弊的行为（包括但不限于：答题测试的填空题复制粘贴其他网站的答案、答案雷同或相似度高，寻找“代答”服务，使用脚本或工具达到申请条件等），或有其他违反小米账号使用协议的相关情形，申请不予通过
            - 2024 年资格获取已截止，2025 年资格获取将于 1 月开启
        - 对于非国行 HyperOS 机型：
            - 需使用 Xiaomi Community 5.3.31 或以上版本申请
            - 解锁权限有效期为一年，自申请成功时开始计算
            - 申请解锁权限需满足: 1) 小米账号注册满 30 天；2) 当日申请限额未满
            - 全球每日申请限额 50 名
            - 2025年起每账号每年最多允许解锁 1 台设备
    - 对于 MIUI 机型：
        - 绑定成功后解锁等待期为 168/360 小时起，随账号解锁次数延长（翻倍）
    - 通用：
        - 每账号每年最多允许解锁 4 台设备（HyperOS 与 MIUI 合并计算）
        - 每个 SIM 卡每三个月内仅允许绑定 2 台机器
        - 每账号解锁设备需间隔 30 天
        - 解锁需手机插入 SIM 卡并绑定小米账号，等待时长从小米账号绑定之时起开始计算
        - 有针对设备和账号的风控机制，风控后不允许解锁；若检测到解锁后的设备用于非正常用途，将封禁账号
        - 部分机型未开源、开源不全或无提交历史记录，已开源的内核源码不再随系统更新
        - 小米 12/12 Pro (不含)后的机型源码均无法正常编译或使用
        - 刷机等操作极易触发隐藏的永久性 TEE 熔断机制，不可恢复
        - 解锁后无论是否人为导致，主板等部件均失保内去免费维修资格。软件损坏也将导致已购买的部分延保类保障无法使用
        - 无法无损刷其他地区的系统，部分型号已在开机向导中加入禁止互刷的限制；且部分新设备刷入其他地区系统后会出现硬件不工作的情况
        - 红米 Note 13 全系及其海外对应机型不支持解锁
        - 操作解锁时需要使用与设备地区相同地区的账户，否则不予解锁

## 中兴 (ZTE)
- **Bootloader 解锁**: ❌
- **是否支持回锁**: ✅
    - **是否支持自定义信任根**: ❌
- **Linux 内核开源**: [✅](https://opensource.ztedevices.com/)
- **备注**: 部分新产品不再提供解锁
