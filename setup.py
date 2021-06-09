from setuptools import setup, find_packages
from os.path import join, dirname
import re

REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():
    init_py = join(dirname(__file__), 'gcore', '__init__.py')

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = 'Cannot find version in {init_py}'.format(init_py=init_py)
            raise RuntimeError(msg)


install_requires = [
    'Django==2.2.22',
    'gitpython']


setup(
    name='gcore',
    version=read_version(),
    description='info about git',
    platforms=['POSIX'],
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)