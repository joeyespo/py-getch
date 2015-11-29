"""\
py-getch
--------

Portable getch() for Python.


Links
`````

* `Source code <https://github.com/joeyespo/py-getch>`_

"""

import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='py-getch',
    version='1.0.1',
    description='Portable getch() for Python.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='https://github.com/joeyespo/py-getch',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=read('requirements.txt').splitlines(),
    zip_safe=False,
    entry_points={},
)
