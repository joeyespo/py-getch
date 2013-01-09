"""\
Py-Getch
--------

Portable getch() for Python.


Links
`````

* `Source code <https://github.com/joeyespo/py-getch>`_

"""

import os
import sys
from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='py-getch',
    version='0.0.1',
    description='Portable getch() for Python.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='https://github.com/joeyespo/py-getch',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=read('requirements.txt'),
    zip_safe=False,
    entry_points={},
)
