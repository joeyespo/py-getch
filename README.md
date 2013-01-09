Py-Getch
========

Portable **getch()** for Python.


Motivation
----------

More than a few times, I'd like to just write `getch()` instead of `raw_input()`.
This is the missing cross-platform functionality you've been looking for.

I don't anticipate this to be used in any major projects. Rather, installed
globally and used in those one-off scripts that you'd like to have just a bit
more professionalism with. Using `raw_input` for single-key capture and pause
mechanism makes a hacked-together script feel even more like just that.


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
print 'You pressed', key
pause()
```


API
---

```python
getch()
```

Works like you'd expect, except that it returns a string.

```python
pause(message='Press any key to continue. . . ')
```

For proper pause functionality.


[pip]: http://pypi.python.org/pypi/pip
