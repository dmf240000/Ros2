from setuptools import find_packages
from setuptools import setup

setup(
    name='pendulum_msgs',
    version='0.35.1',
    packages=find_packages(
        include=('pendulum_msgs', 'pendulum_msgs.*')),
)
