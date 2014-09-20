TinkerPy
========

This Python 2 and 3 project (tested with CPython 2.7 and 3.3  as well as PyPy
2) contains the package `tinkerpy` which provides:

*   functionality related to Python 2 versus 3
*   special mapping implementations
*   some useful decorators
*   SAX handlers
*   other functionality like a class handling integers represented as strings
    (StrIntegers) special list implementation (AllowingList), the flatten()
    function to flatten data structures composed of iterables and a function to
    create anonymous classes (anonymous_class())
*   a Finite State Machine implementation

This project uses the MIT License, so you may freely use, distribute and
modify it, provided you include the content of `License.txt`.

Install using [setuptools](https://pypi.python.org/pypi/setuptools):

    easy_install tinkerpy


You might also be interested in:

* [TinkerPy on PyPi](https://pypi.python.org/pypi/TinkerPy)
* [TinkerPy Documentation](http://pythonhosted.org/TinkerPy/)


## Release History

**0.2.3**
*   *Added:* `tinkerpy.StrIntegers`, `tinkerpy.ProxyDict`,
    `tinkerpy.update_globals`, `tinkerpy.metaclass`, `tinkerpy.int_to_str`,
    `tinkerpy.Unicode` and `tinkerpy.PY_VERSION_GT_2`.
*   *Added:* The module `tinkerpy.fsm` implements a finite state machine API.

**0.2.2**
*   *Added:* `tinkerpy.AllowingList`

**0.2.1**
*   *Added:* `tinkerpy.LexicalHandler` and `tinkerpy.DeclarationHandler`.
*   *Removed:* `tinkerpy.utf16chr` as there is `unichr()` in the standard
    library.
*   *Improved:* Made `tinkerpy.namespace` compatible with PyPy.

**0.2.0**
*   *Added:* Support for Python 3.
*   *Added:* `tinkerpy.py2or3` to handle Python 2 versus 3 ambiguities.
*   *Added:* `tinkerpy.STRING_TYPES` containing the string types of the
    platform.

**0.1.0**
*   *Initial release.*