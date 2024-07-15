# 各 Android 手机厂商 Bootloader 解锁 / 内核开源 / 解锁后保修情况

> 以下所列为官方支持情况
>
> 如有错漏欢迎 PR
> 
> TEE 失效会导致部分 app 指纹/人脸支付失效，部分银行/政府 app 无法使用，网飞、迪士尼等海外流媒体应用无法开启高画质。
>
> 如果不支持自签名 AVB，回锁 Bootloader 需要恢复原厂 ROM。

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
    - 中国大陆销售的 ROG 机型不支持解锁
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
- **Bootloader 解锁**: [✅](https://source.android.com/source/running#unlocking-the-bootloader)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: ✅
- **Linux 内核开源**: [✅](https://source.android.com/docs/setup/build/building-pixel-kernels)
- **备注**:
    - 启用 OEM 解锁功能需已连接到互联网并已签入 Google（即便设备不久前曾连接到互联网，也仍然可能没有签入 Google）。如需强制签入，请在拨号器中输入 *#*#CHECKIN#*#* (*#*#2432546#*#*)（不需要插入 SIM 卡）。输入此号码（不需要按“通话”）后，相应文字即会消失，并且系统会显示成功通知。
    - 有些设备需要运营商干预才能解锁。如需了解详情，请与您的运营商联系。
    - [DivestOS](https://divestos.org) 和 [GrapheneOS](https://grapheneos.org) 官方提供 Custom AVB Key，刷入之后即可回锁（无需恢复到原厂 ROM）

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
- **Bootloader 解锁**: [✅](https://www.htcdev.com/bootloader/)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [❌](https://divestos.org/pages/devices)
- **Linux 内核开源**: [✅](https://www.htcdev.com/devcenter/downloads)
- **备注**:
    - 解锁需注册 HTCdev 账户
    - 提交后会在几分钟内将解锁文件发至邮箱

## 联想 (Lenovo)
- **Bootloader 解锁**: [✅](https://www.zui.com/iunlock)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ⏹
- **是否支持回锁**: ⏹
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: 不详
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
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: 不详
- **Linux 内核开源**: ❌

## LG
- **Bootloader 解锁**: [❌](https://developer.lge.com/resource/mobile/RetrieveBootloader.dev)
- **Linux 内核开源**: [✅](https://opensource.lge.com/index)
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [❌](https://divestos.org/pages/devices)
- **备注**: 官方解锁渠道已随手机业务同步下线

## 魅族 (MEIZU)
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: [⏹](https://github.com/meizuosc)
- **备注**:
    - [官方仅支持 root](https://mroot.flyme.cn/)，root 后 OTA 功能失效
    - 仅少部分早期机型内核开源

## 摩托罗拉 (Motorola)
- **Bootloader 解锁**: [✅](https://motorola-global-portal.custhelp.com/app/standalone/bootloader/unlock-your-device-a)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ⏹
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [❌](https://divestos.org/pages/devices)
- **Linux 内核开源**: [✅](https://github.com/MotorolaMobilityLLC)
- **备注**:
    - 解锁后无法恢复出厂 `oem_locked` 状态
    - 解锁后 OTA 功能失效
    - 解锁需绑定 My Moto Care
    - 提交后会在几分钟内将解锁文件发至邮箱
    - 解锁后会熔断 TEE，不可恢复

## 诺基亚 (Nokia, HMD)
- **Bootloader 解锁**: ❌
- **Linux 内核开源**: [✅](https://www.nokia.com/phones/en_int/opensource)
- **备注**: 官方未提供解锁

## Nothing
- **Bootloader 解锁**: ✅
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [✅](https://github.com/chenxiaolong/avbroot/issues/299)
- **Linux 内核开源**: [✅](https://github.com/NothingOSS)
- **备注**:
    - 无需申请解锁码，无任何解锁限制
    - 解锁后会暂时屏蔽 TEE，回锁后恢复

## 努比亚 (nubia) & 红魔 (Red Magic)
- **Bootloader 解锁**: ⏹
- **解锁后保修状态**: 不详
- **是否支持回锁**: ⏹
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: 不详
- **Linux 内核开源**: [⏹](https://github.com/ztemt)
- **备注**: 新产品不再提供解锁；旧产品更新系统后也不再提供解锁

## 一加 (OnePlus)
- **Bootloader 解锁**: ✅
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [⏹](https://github.com/chenxiaolong/avbroot/issues/299)
- **Linux 内核开源**: [✅](https://github.com/OnePlusOSS)
- **备注**:
    - 无需申请解锁码，无任何解锁限制
    - 解锁后会暂时屏蔽 TEE，回锁后恢复
    - [仅一加 6/6T 及之前的老机型自签名 AVB，从一加 7 开始不再支持（即只支持刷回原厂 ROM 的情况下回锁）](https://divestos.org/pages/devices)

## OPPO
- **Bootloader 解锁**: [⏹](https://www.oppo.cn/thread-397164526-1)
- **解锁等待时长**: 720 小时 (1 月)
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: 不详
- **Linux 内核开源**: [✅](https://github.com/oppo-source)
- **备注**:
    - 仅部分机型支持解锁
    - 解锁后会暂时屏蔽 TEE，回锁后恢复

## 真我 (realme)
- **Bootloader 解锁**: [⏹](https://www.realmebbs.com/post-details/1275426081138028544)
- **解锁等待时长**: 5-15 小时
- **解锁后保修状态**: ✅
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: 不详
- **Linux 内核开源**: [✅](https://github.com/realme-kernel-opensource)
- **备注**:
    - 仅部分机型支持解锁
    - 每个机型月限 50,000 名额
    - 需登录欢太账号
    - 深度测试资格有 7 天时间限制，超过 7 天未实际执行解锁需要重新申请
    - 同一个欢太账号 30 天内只能申请一台机器，多次申请会提示重复申请
    - 解锁后会暂时屏蔽 TEE，回锁后恢复

## 三星 (Samsung)
- **Bootloader 解锁**: ⏹
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [⏹](https://divestos.org/pages/devices)
- **Linux 内核开源**: [✅](https://opensource.samsung.com/main)
- **备注**:
    - 解锁将导致 KNOX 熔断，钱包等功能失效，保修丢失；部分机型解锁还将导致相机永久无法工作（如 Galaxy Fold 系列）
    - 美版设备不支持解锁
    - 仅部分地区的设备系统支持无损互刷
    - 仅部分机型支持在保留非原厂 ROM 的情况下回锁

## 索尼 (SONY)
- **Bootloader 解锁**: [✅](https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader)
- **解锁等待时长**: 无 (秒解)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [⏹](https://github.com/chenxiaolong/avbroot/issues/80#issuecomment-1475963837)
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
    - **国行 HyperOS 机型:** [⚠️](https://web.vip.miui.com/page/info/mio/mio/testDetails?type=BL_BLOCK&id=-1)
    - **非国行 HyperOS 机型及 MIUI 机型:** ✅
- **解锁等待时长**:
    - **HyperOS 机型:** 72 小时 (3 天)
    - **MIUI 机型:** 168/360-2880 小时 (7/15 天 - 4 月)
- **解锁后保修状态**: ❌
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: [❌](https://github.com/chenxiaolong/avbroot/issues/299)
- **Linux 内核开源**: [⏹](https://github.com/MiCode)
- **备注**:
    - 对于国行 HyperOS 机型：
        - Xiaomi HyperOS 的解锁权限需在小米社区申请，申请成功不代表审核通过，需等待最终审核结果；解锁权限有效期截至当年 12 月 31 日 24:00
        - 申请解锁权限报名需满足 1) 通过《解锁资格答题测试》；2) 社区成长等级达到 5 段；3）完成实名认证
        - 每账号每年最多允许解锁 3 台设备
        - 解锁需手机插入 SIM 卡并绑定小米账号，等待时长从小米账号绑定之时起开始计算
        - 每个 SIM 卡每三个月内仅允许绑定 2 台机器
        - 已解锁设备若处于 MIUI，将不会收到小米澎湃 OS 的 OTA 推送
        - 有针对设备和账号的风控机制，风控后不允许解锁；若检测到解锁后的设备用于非正常用途，将封禁账号
        - 答题开放时间为 8:00-8:15，大周每周二周四开放，小周每周二开放（包含节假日的周不开放），可任选其中一个时段参与，每次参与需间隔 7 天；每场答题的最迟进场时间为该场次答题开始后的 10 分钟；答题成绩每周一晚上 23:59 失效
        - 用户即使满足解锁申请条件，如在社交媒介（包括但不限于各论坛、微博、微信、QQ 群等）对小米有过恶意诋毁、谩骂、造谣等情况，在申请时不填写申请理由、或使用 AI 生成申请理由、或申请理由出现过辱骂威胁等内容，或出现被判定为作弊的行为（包括但不限于：答题测试的填空题复制粘贴其他网站的答案、答案雷同或相似度高，寻找“代答”服务，使用脚本或工具达到申请条件等），或有其他违反小米账号使用协议的相关情形，申请不予通过
        - 有机型已增加运行其他地区系统的 [限制](https://x.com/kacskrz/status/1809956388182905108)，表现为无法通过初次开机引导
    - 对于非国行 HyperOS 机型：
        - 需使用 Xiaomi Community 5.3.31 或以上版本申请，且申请条件仅需满足  1) 小米账号注册满 30 天；2) 当日申请限额未满
        - 每账号每年最多允许解锁 3 台设备
        - 解锁需手机插入 SIM 卡并绑定小米账号，等待时长从小米账号绑定之时起开始计算
        - 每个 SIM 卡每三个月内仅允许绑定 2 台机器
        - 已解锁设备若处于 MIUI，将不会收到小米澎湃 OS 的 OTA 推送
    - 对于 MIUI 机型：
        - 绑定成功后解锁等待期为 168/360 小时起步，随账号解锁次数延长（翻倍）
        - 每账号解锁成功后需间隔 30 天才能重新绑定，每年最多允许解锁 4 台设备
        - 解锁需手机插入 SIM 卡并绑定小米账号，等待时长从小米账号绑定之时起开始计算
    - 其他：
        - 部分机型未开源或无提交历史记录
        - 部分机型源码无法正常编译
        - 已开源的内核源码不随系统更新
        - 刷机等操作极易触发隐藏的永久性 TEE 熔断机制
        - 解锁后无论是否人为导致，主板等部件均失保内去免费维修资格。软件损坏也将导致已购买的部分延保类保障无法使用。TEE 未熔断时回锁后**有可能**恢复保修权益，具体请咨询您所在地的小米之家
        - 无法无损刷其他地区的系统；且部分新设备刷入其他地区系统后会出现硬件不工作的情况

## 中兴 (ZTE)
- **Bootloader 解锁**: ❌
- **是否支持回锁**: ✅
    - **在保留非原厂 ROM 的情况下回锁（自签名 AVB）**: ❌
- **Linux 内核开源**: [✅](https://opensource.ztedevices.com/)
- **备注**: 部分新产品不再提供解锁
