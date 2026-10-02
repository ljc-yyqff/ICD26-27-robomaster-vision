#!/usr/bin/env python3
"""Publish a simulation TF when lidar odometry is unavailable."""

import time

import rclpy
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from tf2_ros import TransformBroadcaster


class GazeboGroundTruthTf(Node):
    def __init__(self):
        super().__init__("gazebo_ground_truth_tf")
        self.declare_parameter("spawn_x", 0.0)
        self.declare_parameter("spawn_y", 0.0)
        self.spawn_x = self.get_parameter("spawn_x").value
        self.spawn_y = self.get_parameter("spawn_y").value
        self.last_lio_odometry = None
        self.broadcaster = TransformBroadcaster(self)
        self.create_subscription(
            Odometry, "odometry", self.on_lio_odometry, qos_profile_sensor_data
        )
        self.create_subscription(
            Odometry,
            "chassis_odometry_gt",
            self.on_ground_truth,
            qos_profile_sensor_data,
        )

    def on_lio_odometry(self, _message):
        self.last_lio_odometry = time.monotonic()

    def on_ground_truth(self, message):
        if (
            self.last_lio_odometry is not None
            and time.monotonic() - self.last_lio_odometry < 1.0
        ):
            return

        transform = TransformStamped()
        transform.header.stamp = message.header.stamp
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_footprint"
        transform.transform.translation.x = message.pose.pose.position.x - self.spawn_x
        transform.transform.translation.y = message.pose.pose.position.y - self.spawn_y
        transform.transform.translation.z = message.pose.pose.position.z
        transform.transform.rotation = message.pose.pose.orientation
        self.broadcaster.sendTransform(transform)


def main():
    rclpy.init()
    node = GazeboGroundTruthTf()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
