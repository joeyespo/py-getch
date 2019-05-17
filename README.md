Py-Getch [![Current version on PyPI](http://img.shields.io/pypi/v/py-getch.svg?style=flat-square)][pypi] [![Downloads/month on PyPI](http://img.shields.io/pypi/dm/py-getch.svg?style=flat-square)][pypi]
========

Portable **getch()** for Python.


Motivation
----------

More than a few times, I've had liked to just write `getch()` instead of
`raw_input()`. This is the missing cross-platform functionality you've been
looking for.


Installation
------------

Install with [pip][]:

```bash
$ pip install py-getch
```


Usage
-----

```python
from getch import getch, pause

key = getch()
print('You pressed:', key)
pause()
```


API
---

Wait for a keypress:

```python
ch = getch()
```

This works like you'd expect, except that it returns a string.

You can also pause with the standard `'Press any key to continue. . . '` message:

```python
pause()
```

Or pause with a custom message:

```python
pause('Press any key to exit.')
```

You can have Python exit automatically with:

```python
from getch import pause_exit

pause_exit(status=0, message='Press any key to exit.')
```


Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository, make your changes, and add yourself to [Authors.md](./AUTHORS.md)
3. Send a pull request

If your PR has been waiting a while, feel free to [ping me on Twitter][twitter].


[pypi]: http://pypi.python.org/pypi/py-getch/
[pip]: http://pypi.python.org/pypi/pip
[twitter]: http://twitter.com/joeyespo
