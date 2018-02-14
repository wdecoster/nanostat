# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
exec(open('nanostat/version.py').read())

setup(
    name='NanoStat',
    version=__version__,
    description='Calculate statistics for Oxford Nanopore sequencing data and alignments',
    long_description=open(path.join(here, "README.rst")).read(),
    url='https://github.com/wdecoster/nanostat',
    author='Wouter De Coster',
    author_email='decosterwouter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nanopore sequencing statistics',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['nanoget>=0.15.0', 'nanomath>=0.18.1'],
    package_data={'NanoStat': []},
    package_dir={'nanostat': 'nanostat'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'NanoStat=nanostat.NanoStat:main',
        ],
    },
)
