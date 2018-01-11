from setuptools import setup
from codecs import open
from os import path


package_root = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(package_root, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


with open(path.join(package_root, 'VERSION')) as version_file:
    version = version_file.read().strip()


setup(
    name='yaml-builder',
    version=version,
    description='A wrapper around PyYaml for building complex yaml files',
    long_description=long_description,
    url='https://github.com/spockNinja/yaml-builder',
    author='Jacob Foster',
    packages=['yaml_builder'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='yaml compose build cloudformation tool',

    install_requires=['PyYAML'],

    entry_points={  # Optional
        'console_scripts': [
            'build-yaml=yaml_builder:main',
        ],
    },
)
