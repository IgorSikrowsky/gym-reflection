from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='gym_reflection',
      version='0.0.1',
      author='Giuseppe and Kyle',
      install_requires=['gym>=0.10.5']
 )