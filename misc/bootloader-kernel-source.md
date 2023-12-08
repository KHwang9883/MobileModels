# 各 Android 手机厂商 Bootloader 解锁 / 内核开源 / 解锁后保修情况

> 以下所列为官方支持情况
>
> 如有错漏欢迎 PR

- ✅ 支持/是 | **可点击**
- ⏹ 部分支持/部分开源/部分保修 | **可点击**
- ❌ 不支持/否
- -- 不详/无

| 品牌 | Bootloader 解锁 | 解锁等待时长（小时） | Linux 内核开源 | 解锁后保修状态 | 是否支持回锁 | 备注 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 360 手机 | ❌ | -- | ❌ | -- | -- | -- |
| 黑鲨 (Black Shark) | ❌ | -- | ❌ | -- | -- | -- |
| 酷派 (Coolpad) | ✅ | -- | ❌ | -- | -- | -- |
| Google | [✅](https://source.android.com/source/running#unlocking-the-bootloader) | 无<br/>（秒解） | [✅](https://source.android.com/docs/setup/build/building-pixel-kernels) | ✅ | ✅ | • 启用 OEM 解锁功能需已连接到互联网并已签入 Google（即便设备不久前曾连接到互联网，也仍然可能没有签入 Google）。如需强制签入，请在拨号器中输入 *#*#CHECKIN#*#* (*#*#2432546#*#*)（不需要插入 SIM 卡）。输入此号码（不需要按“通话”）后，相应文字即会消失，并且系统会显示成功通知。<br/>• 有些设备需要运营商干预才能解锁。如需了解详情，请与您的运营商联系。 |
| 荣耀 (HONOR) | ❌ | -- | [⏹](https://www.hihonor.com/global/opensource/) | -- | -- | • 缺少部分机型内核源码 |
| 华为 (HUAWEI) | ❌ | -- | [⏹](https://consumer.huawei.com/en/opensource/) | ❌ | -- | • 官方已关闭解锁渠道<br/>• 部分机型未开源 |
| HTC | [✅](https://www.htcdev.com/bootloader/) | 无<br/>（秒解） | [✅](https://www.htcdev.com/devcenter/downloads) | ✅ | ✅ | • 解锁需注册 HTCdev 账户<br/>• 提交后会在几分钟内将解锁文件发至邮箱 |
| 联想 (Lenovo) | [✅](https://www.zui.com/iunlock) | 无<br/>（秒解） | ❌ | ⏹ | ⏹ | • 部分设备无需申请解锁文件<br/>• 申请解锁文件需登录联想账号<br/>• 提交后会在几分钟内将解锁文件发至邮箱<br/>• 解锁后若重新回锁，则不影响保修<br/>• 部分设备不允许回锁 |
| 乐视 (Letv) | ✅ | -- | ❌ | -- | -- | -- |
| LG | [❌](https://developer.lge.com/resource/mobile/RetrieveBootloader.dev) | -- | [✅](https://opensource.lge.com/index) | -- | ✅ | • 官方解锁渠道已随手机业务同步下线 |
| 魅族 (MEIZU) | [❌](https://mroot.flyme.cn/) | -- | [⏹](https://github.com/meizuosc) | ❌ | -- | • 官方仅支持 root，root 后 OTA 功能失效<br/>• 仅少部分早期机型内核开源 |
| 摩托罗拉 (Motorola) | [✅](https://motorola-global-portal.custhelp.com/app/standalone/bootloader/unlock-your-device-a) | 无<br/>（秒解） | [✅](https://github.com/MotorolaMobilityLLC) | ❌ | ⏹ | • 解锁后无法恢复出厂 `oem_locked` 状态<br/>• 解锁需绑定 My Moto Care<br/>• 提交后会在几分钟内将解锁文件发至邮箱 |
| 诺基亚 (Nokia) | ❌ | -- | [✅](https://www.nokia.com/phones/en_int/opensource) | ❌ | -- | • 官方未提供解锁 |
| 纳欣 (Nothing) | ✅ | 无<br/>（秒解） | [✅](https://github.com/NothingOSS) | ✅ | ✅ |  • 无需申请解锁码，无任何解锁限制 |
| 努比亚 (nubia) | ⏹ | -- | [⏹](https://github.com/ztemt) | -- | ✅ | • 部分新产品不再提供解锁 |
| 一加 (OnePlus) | ✅ | 无<br/>（秒解） | [✅](https://github.com/OnePlusOSS) | ✅ | ✅ | • 无需申请解锁码，无任何解锁限制 |
| OPPO | [⏹](https://www.oppo.cn/thread-397164526-1) | 720<br/>（1 月） | [✅](https://github.com/oppo-source) | ✅ |✅ | • 仅部分机型支持解锁 |
| 真我 (realme) | [⏹](https://www.realmebbs.com/post-details/1275426081138028544) | 168<br/>（7天）<br/> | [✅](https://github.com/realme-kernel-opensource) | ✅ | ✅ | • 仅部分机型支持解锁<br/>• 每个机型限制 5W 名额<br/>• 需登录欢太账号<br/>• 解锁码有 7 天时间限制，超过 7 天需要重新申请<br/> |
| 三星 (Samsung) | ✅ | 无<br/>（秒解） | [✅](https://opensource.samsung.com/main) | ❌ | ✅ | • 解锁将导致 KNOX 熔断，钱包等部分功能失效，保修丢失 |
| 索尼 (SONY) | [✅](https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader) | 无<br/>（秒解） | [✅](https://github.com/sonyxperiadev/kernel) | ❌ | ✅ | • 需申请解锁码 |
| 坚果 (Smartisan) | ✅ | -- | [⏹](https://github.com/SmartisanTech/SmartisanOS_Kernel_Source) | -- | ❌ | • 缺少部分机型内核源码 |
| vivo | ❌ | -- | [⏹](https://opensource.vivo.com/Project) | ❌ | -- | • 官方未提供解锁<br/>• 缺少部分机型内核源码 |
| 小米 (Xiaomi) | [⏹](https://web.vip.miui.com/page/info/mio/mio/testDetails?type=BL_BLOCK&id=-1) | HyperOS<br/>72<br/>（3 天）<br/>或<br/>MIUI<br/>168/360-2880<br/>（7/15 天 - 4 月） | [⏹](https://github.com/MiCode) | ❌ | ✅ | • Xiaomi HyperOS（小米澎湃 OS）的解锁权限需在小米社区申请，申请成功不代表审核通过，需等待最终审核结果；解锁权限有效期截至当年 12 月 31 日 24:00（2023 年通过申请的用户解锁权限保留至 2024 年末）<br/>• 申请解锁权限报名需满足 1) 通过《解锁资格答题测试》；2) 社区成长等级达到 5 段；3）完成实名认证<br/>• 解锁需手机插入 SIM 卡并绑定小米账号，等待时长从小米账号绑定之时起开始计算；HyperOS 绑定成功后解锁等待期为 72 小时；MIUI 绑定成功后解锁等待期为 168/360 小时起步，随账号解锁次数延长（翻倍）<br/>• HyperOS 每账号每年最多允许解锁 3 台设备；MIUI 每账号解锁成功后需间隔 30 天才能重新绑定，每年最多允许解锁 4 台设备；每个 SIM 卡每三个月内仅允许绑定 2 台机器<br/>• 已解锁设备若处于 MIUI，将不会收到小米澎湃 OS 的 OTA 推送<br/>• 部分机型未开源或无提交历史记录；自小米 12 Pro 后，开源的源码无法正常编译（“假开源”），已开源的内核源码不再随系统更新<br/>• 解锁后主板等部分部件失去保内免费维修资格，刷机等操作易触发永久性熔断机制，软件损坏将导致已购买的部分延保类保障无法使用<br/>• 有针对设备和账号的风控机制，风控后不允许解锁；若检测到解锁后的设备用于非正常用途，将封禁账号 |
| 中兴 (ZTE) | ⏹ | -- | [✅](https://opensource.ztedevices.com/) | -- | ✅ | • 部分新产品不再提供解锁 |
