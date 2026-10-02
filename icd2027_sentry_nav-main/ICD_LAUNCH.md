# ICD 2027 哨兵仿真启动

两个终端都从新的 Bash 会话开始，只加载本工作空间。无需设置 `ROS_DOMAIN_ID`。

终端 1，启动 Gazebo（地图由 `external/icd2027sentry_gazebo_simulator/icd2027sentry_gazebo_simulator/config/gz_world.yaml` 选择，当前为 `rmul_2026`）：

```bash
cd /path/to/ICD26-27-robomaster-vision/icd2027_sentry_nav-main
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch icd2027sentry_gazebo_simulator icd2027sentry_bringup_sim.launch.py
```

终端 2，启动导航和 RViz：

```bash
cd /path/to/ICD26-27-robomaster-vision/icd2027_sentry_nav-main
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch icd2027sentry_nav_bringup icd2027sentry_navigation_simulation.launch.py world:=rmul_2026 slam:=False
```

北极熊工作空间使用独立终端。两套仿真仍使用相同的机器人 ROS 命名空间与部分话题；不要同时启动。

## ICD 外观模型

Gazebo 和 RViz 共用 `icd2027sentry_gz_resources/resource/models/icd_sentry/meshes/icd_sentry_colored.obj`，由本地彩色整机 3MF 转换而来。仓库不包含原始 3MF。OBJ、MTL 和贴图需放在同一目录；重新导出装配体后可用 `tools/convert_icd_colored_3mf.py` 重新生成。

目前整机网格只用于显示。车轮和云台的碰撞、惯量及运动关节仍采用已有仿真参数，网格中的轮子不会随车轮关节单独旋转。装甲板数字 7 是贴在原装甲板外表面的仿真几何体。
