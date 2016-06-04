import sys
from setuptools import setup, find_packages


VERSION = '0.0.0'
PY3 = sys.version_info[0] >= 3

setup(
    name='plugandpie',
    version=VERSION,
    description='Device driver and automation for common sensors',
    author='Victor Villas',
    author_email='villasv@outlook.com',
    license='GPLv3+',
    url='https://github.com/villasv/Plutonium',
    packages=find_packages(),
    long_description=open('README.md').read() + open('CHANGELOG.md').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or "
        "later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plugandpie plug and play raspberrypi sensor',
)
