TinkerPy
========

This Python 2 and 3 project (tested with 2.7 and 3.3) contains the package
`tinkerpy` which provides:

*   funtionality related to Python 2 versus 3
*   special dictionary implementations
*   a function to flatten data structures composed of iterables
*   some useful decorators
*   a function to create an UTF-16 string from an Unicode codepoint

This project uses the MIT License, so you may freely use, distribute and
modify it, provided you include the content of `License.txt`.

Install using [setuptools](https://pypi.python.org/pypi/setuptools) (only
Python 2) or [distribute](http://pythonhosted.org/distribute/):

    easy_install tinkerpy


You might also be interested in:

* [TinkerPy on PyPi](https://pypi.python.org/pypi/TinkerPy)
* [TinkerPy Documentation](http://pythonhosted.org/TinkerPy/)


## Release History

**0.2.0**
*   *Added:* Support for Python 3.
*   *Added:* `py2or3` to handle Python 2 versus 3 ambiguities.
*   *Added:* `STRING_TYPES` containing the string types of the platform.

**0.1.0**
*   *Initial release.*