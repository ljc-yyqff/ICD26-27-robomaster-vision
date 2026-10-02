# ICD 2027 哨兵导航仿真 V1

ROS 2 Humble 工作空间。默认 Gazebo 场地为 RMUL 2026，机器人外观由本地彩色整机 3MF 转换生成。仓库包含运行所需的彩色网格和贴图，不包含原始 3MF。启动步骤见 [ICD_LAUNCH.md](ICD_LAUNCH.md)。

构建前请安装工程所需的 ROS 2 Humble、Gazebo 与依赖；在本目录使用原项目的 `colcon build --symlink-install` 构建，然后加载 `install/setup.bash`。本目录还保留一些北极熊旧模型和旧赛季地图供参考，默认仿真入口使用 ICD 模型。

V1 未上传编译缓存、旧 CAD 零件库、大型 STEP/SolidWorks 文件和旧赛季 PCD。`README_UPSTREAM.md` 保存了原工程说明与来源信息；目录中的第三方模块保留各自许可证。
