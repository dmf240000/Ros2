import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/donavyn/docker_test/ros2_ws/src/install/learning_tf2_py'
