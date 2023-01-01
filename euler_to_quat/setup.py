from setuptools import setup

package_name = 'euler_to_quat'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chinmayee',
    maintainer_email='cprabhakar@wpi.edu',
    description='Converting Euler Angles to Quaternion representations',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['listener = euler_to_quat.euler_quat:main'
        ],
    },
)
