from setuptools import setup
import os
from glob import glob
package_name = 'memory_usage'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yuhei Mitsuno',
    maintainer_email='s23c1137@s.chibakoudai.jp',
    description='ロボットシステム学のサンプル',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'memory_usage_publisher = memory_usage.memory_usage_publisher:main',
            'listener = memory_usage.listener:main'
        ],
    },
)
