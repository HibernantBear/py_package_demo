from setuptools import setup, find_packages

setup(
    name='py_package_demo',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
