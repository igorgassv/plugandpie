import sys
from setuptools import setup, find_packages


VERSION = '0.1-alpha.0'

setup(
    name='plugandpie',
    version=VERSION,
    description='Device driver and automation for common sensors',
    author='Victor Villas',
    author_email='villasv@outlook.com',
    license='GPLv3+',
    url='https://github.com/villasv/plugandpie',
    packages=find_packages(),
    long_description=open('README.rst').read() + open('CHANGELOG.rst').read(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha ",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: System :: Hardware :: Monitoring"
    ],
    keywords='plugandpie plug and play raspberrypi sensor',
)
