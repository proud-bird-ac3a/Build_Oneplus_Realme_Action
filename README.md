# 欧加真 SM8750/MT6991 系列通用6.6风驰移植内核自动化编译脚本 (二创)
[![STAR](https://img.shields.io/github/stars/qdykernel/Build_Oneplus_Realme_Action?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU%2BR2l0SHViPC90aXRsZT48cGF0aCBkPSJNMTIgLjI5N2MtNi42MyAwLTEyIDUuMzczLTEyIDEyIDAgNS4zMDMgMy40MzggOS44IDguMjA1IDExLjM4NS42LjExMy44Mi0uMjU4LjgyLS41NzcgMC0uMjg1LS4wMS0xLjA0LS4wMTUtMi4wNC0zLjMzOC43MjQtNC4wNDItMS42MS00LjA0Mi0xLjYxQzQuNDIyIDE4LjA3IDMuNjMzIDE3LjcgMy42MzMgMTcuN2MtMS4wODctLjc0NC4wODQtLjcyOS4wODQtLjcyOSAxLjIwNS4wODQgMS44MzggMS4yMzYgMS44MzggMS4yMzYgMS4wNyAxLjgzNSAyLjgwOSAxLjMwNSAzLjQ5NS45OTguMTA4LS43NzYuNDE3LTEuMzA1Ljc2LTEuNjA1LTIuNjY1LS4zLTUuNDY2LTEuMzMyLTUuNDY2LTUuOTMgMC0xLjMxLjQ2NS0yLjM4IDEuMjM1LTMuMjItLjEzNS0uMzAzLS41NC0xLjUyMy4xMDUtMy4xNzYgMCAwIDEuMDA1LS4zMjIgMy4zIDEuMjMuOTYtLjI2NyAxLjk4LS4zOTkgMy0uNDA1IDEuMDIuMDA2IDIuMDQuMTM4IDMgLjQwNSAyLjI4LTEuNTUyIDMuMjg1LTEuMjMgMy4yODUtMS4yMy42NDUgMS42NTMuMjQgMi44NzMuMTIgMy4xNzYuNzY1Ljg0IDEuMjMgMS45MSAxLjIzIDMuMjIgMCA0LjYxLTIuODA1IDUuNjI1LTUuNDc1IDUuOTIuNDIuMzYuODEgMS4wOTYuODEgMi4yMiAwIDEuNjA2LS4wMTUgMi44OTYtLjAxNSAzLjI4NiAwIC4zMTUuMjEuNjkuODI1LjU3QzIwLjU2NSAyMi4wOTIgMjQgMTcuNTkyIDI0IDEyLjI5N2MwLTYuNjI3LTUuMzczLTEyLTEyLTEyIiBmaWxsPSIjZmZmZmZmIj48L3BhdGg%2BPC9zdmc%2B)](https://github.com/qdykernel/Build_Oneplus_Realme_Action/stargazers)
[![FORK](https://img.shields.io/github/forks/qdykernel/Build_Oneplus_Realme_Action?style=flat&logo=greasyfork&color=%2394E61A)](https://github.com/qdykernel/Build_Oneplus_Realme_Action/forks)
[![TELEGRAM](https://img.shields.io/badge/Droidcess-频道-blue.svg?logo=telegram)](https://t.me/Droidcess)
[![DISCUSSION](https://img.shields.io/badge/%E8%AE%A8%E8%AE%BA%E5%8C%BA-discussions?logo=livechat&logoColor=FFBBFF&color=3399ff)](https://github.com/qdykernel/Build_Oneplus_Realme_Action/discussions)

##### 
一个更方便、快捷的自动化OPPO/一加/真我系列骁龙8Elite(SM8750)/天玑9400+(MT6991)机型的通用内核编译脚本（二创）。
##### 
这个项目是基于 [qdykernel/Build_Oneplus_Realme_Action](https://github.com/qdykernel/Build_Oneplus_Realme_Action) 的二次创作，在原有项目的基础上进一步扩展了以下功能：
- 集成 **Droidspaces 容器支持**（基于 [Droidspaces-OSS](https://github.com/ravindu644/Droidspaces-OSS) 官方 kABI 补丁），使内核原生支持 DroidRun 等容器运行环境，骁龙机型勾选即用；
- 新增 **可选上传内核 Image 镜像**功能，构建时可选择将 `Image` 文件与 AnyKernel3 卡刷包一同发布至 Release；
- 修复 Release 发布时文件离散问题，确保每次构建产出只有一个完整的 AnyKernel3 压缩包，解压即刷。
## 本项目的主要内容(及计划)
- 提供 OKI（官方源码）在线云编译模式，保留官方驱动/调度，集成风驰内核驱动；
- 基于 GitHub Actions，无需本地环境，手机浏览器即可触发编译，自动生成 AnyKernel3 卡刷包；
- 使用 LLVM/Clang 18 进行编译，引入 ccache 缓存及大量独家编译流程优化，首次编译约 12min，二次编译约 6min；
- 集成 Droidspaces 官方 kABI 补丁及内核配置，为骁龙机型提供原生容器运行能力；
- 支持可选上传内核 Image 镜像，方便调试、备份或配合其他工具使用。
## 已实现：
- [x] 欧加真 SM8750 通用OKI内核（基于一加13/Ace5Pro源码的 6.6.56, 6.6.57, 6.6.89 等多种版本，其他同内核版本非SM8750机型可自行测试，部分机型可完全兼容）
- [x] 欧加真 MT6991 通用OKI内核（基于一加Ace5至尊版/真我GT7源码，其他同内核版本非MT6989机型可自行测试，部分机型可完全兼容）
- [x] 欧加真 6.6 系列内核全面移植官方风驰scx调速器，在有官方风驰内核支持的机型上可实现完整原版风驰内核调度功能
- [x] ReSukiSU/SukiSU Ultra多版本KSU可选
- [x] 引入ccache缓存及大量独家编译流程优化，首次编译时间约12min，二次编译时间可稳定在约6min
- [x] 引入O2编译优化，改善内核运行性能
- [x] lz4 1.10.0 & zstd 1.5.7 算法更新&优化补丁(来自[@ferstar](https://github.com/ferstar), 移植by [@Xiaomichael](https://github.com/Xiaomichael), 6.6版本补丁重制by [@cctv18](https://github.com/cctv18))
- [x] [ADIOS IO调度器](https://github.com/firelzrd/adios)移植
- [x] 加入内核防格基带保护(By [@showdo](https://github.com/showdo))，有效防止恶意格机脚本/程序对系统分区数据的破坏
- [x] 加入Re:Kernel支持，与Freezer，NoActive等软件配合降低功耗
- [x] 添加了对[Mountify](https://github.com/backslashxx/mountify)模块的支持
- [x] **Droidspaces 容器支持（二创新增）**：基于 [Droidspaces-OSS](https://github.com/ravindu644/Droidspaces-OSS) 官方 kABI 补丁及推荐 GKI 配置，骁龙机型勾选即用，天玑机型待后续适配
- [x] **可选上传 Image 镜像（二创新增）**：构建时可勾选，将编译出的 `Image` 内核文件单独上传并随 Release 发布，方便调试或配合 KernelFlasher 使用
- [x] **修复 Release 离散问题（二创新增）**：每次构建产出统一打包为一个 `AnyKernel3_xxx.zip`，解压即标准卡刷包结构，不再出现散文件
## 待实现：
- [ ] 天玑 MT6991 平台 Droidspaces 测试与适配
- [ ] LXC/Docker 功能支持
- [ ] Nethunter 驱动移植
- [ ] 更多自定义内核伪装选项
- [ ] GKI 通用内核模式支持
- 更多优化与特性移植……
##### 
##### 
##### 
## 鸣谢
- 本项目是基于 [qdykernel/Build_Oneplus_Realme_Action](https://github.com/qdykernel/Build_Oneplus_Realme_Action) 的二次创作，在此对原作者的杰出工作致以诚挚感谢
- ReSukiSU：[ReSukiSU/ReSukiSU](https://github.com/ReSukiSU/ReSukiSU)
- SukiSU Ultra：[SukiSU-Ultra/SukiSU-Ultra](https://github.com/SukiSU-Ultra/SukiSU-Ultra)
- susfs4ksu：[ShirkNeko/susfs4ksu](https://github.com/ShirkNeko/susfs4ksu)（本项目使用 cctv18 维护的 [susfs4oki](https://github.com/cctv18/susfs4oki)）
- 风驰调度补丁：[Numbersf/SCHED_PATCH](https://github.com/Numbersf/SCHED_PATCH)
- Droidspaces-OSS：[ravindu644/Droidspaces-OSS](https://github.com/ravindu644/Droidspaces-OSS)
- 内核防格基带保护模块：[vc-teahouse/Baseband-guard](https://github.com/vc-teahouse/Baseband-guard)
- 持续为本项目提供工具链和补丁支持的：[cctv18](https://github.com/cctv18)
- 早期灵感来源：[HanKuCha/oneplus13_a5p_sukisu](https://github.com/HanKuCha/oneplus13_a5p_sukisu)

<!-- 这是一个访客统计，用来看看我的项目主页有多少人访问过 -->
<div align="center">
  <img width="0" height="0" src="https://count.getloli.com/get/@:qdykernel" />
</div>