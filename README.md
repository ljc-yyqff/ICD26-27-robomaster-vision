# ICD 2027 哨兵导航仿真 V1

本分支的 [`icd2027_sentry_nav-main`](icd2027_sentry_nav-main/) 是 ICD 哨兵 ROS 2 Humble 仿真与导航工程的 V1 快照。`main` 分支不受此版本影响。

本版默认使用 RMUL 2026 地图和 ICD 彩色整机模型。启动方式见 [ICD_LAUNCH.md](icd2027_sentry_nav-main/ICD_LAUNCH.md)。工程由北极熊 2025 导航工程及其开源依赖改造而来，各目录保留原有许可证；原说明留在 [README_UPSTREAM.md](icd2027_sentry_nav-main/README_UPSTREAM.md)。

仓库包含运行所需的源码、仿真地图、转换脚本以及 Gazebo 使用的 OBJ/MTL/贴图。彩色整机 3MF、编译产物、日志、旧 CAD 零件库、超大 STEP/SolidWorks 装配体和旧赛季 PCD 没有纳入 Git；原始 CAD 文件仍保留在本地工作目录。RMUL 2026 当前使用仿真位姿定位，不依赖旧赛季 PCD。

版本：**V1**。仿真外观网格用于显示；轮子和云台运动仍使用现有仿真关节与碰撞参数，尚未依据 ICD 实车标定。
