import platform
from setuptools import setup
from setuptools import find_packages
from setuptools import Extension
import os

extra_compile_args = [
    '-std=c++11',
    '-O3',
    '-Wall',
    '-Wextra',
    '-Wconversion',
    '-fno-strict-aliasing',
    '-fno-rtti',
]


if platform.system() == 'Darwin':
    extra_compile_args += ['-mmacosx-version-min=10.7', '-stdlib=libc++']
    from distutils.sysconfig import get_config_var
    from distutils.version import LooseVersion
    if 'MACOSX_DEPLOYMENT_TARGET' not in os.environ:
        current_system = LooseVersion(platform.mac_ver()[0])
        python_target = LooseVersion(
            get_config_var('MACOSX_DEPLOYMENT_TARGET'))
        if python_target < '10.9' and current_system >= '10.9':
            os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.9'

    
            
setup(
    name="python-rocksdb",
    version='0.7.0',
    description="Python bindings for RocksDB",
    keywords='rocksdb',
    author='Ming Hsuan Tu',
    author_email="qrnnis2623891@gmail.com",
    url="https://github.com/twmht/python-rocksdb",
    license='BSD License',
    setup_requires=['setuptools>=25', 'Cython>=0.20'],
    install_requires=['setuptools>=25'],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('.'),
    ext_modules=[Extension(
        'rocksdb._rocksdb',
        ['rocksdb/_rocksdb.pyx'],
        extra_compile_args=extra_compile_args,
        language='c++',
        libraries=['rocksdb', 'snappy', 'bz2', 'z', 'lz4'],
    )],
    extras_require={
        "doc": ['sphinx_rtd_theme', 'sphinx'],
        "test": ['pytest'],
    },
    include_package_data=True,
    zip_safe=False,
)
