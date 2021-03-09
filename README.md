<!-- start-no-pypi -->
[![Python Tests](https://github.com/abelcheung/lxml-stubs/workflows/Python%20Tests/badge.svg)](https://github.com/abelcheung/lxml-stubs/actions?query=workflow%3A%22Python+Tests%22)
<!-- end-no-pypi -->


## Relationship with official lxml-stubs
This fork is an attempt to move forward with unstable changes, while official
one is under semi-dormant state for months. If upstream were become active
again, some selected changes can be submitted in future.

Right now this repo uses all unmerged PR as basis (20, 24, 25, 26), and all
further changes will go into `rewrite` branch. Following incompatible changes
are planned in mind:

- Python 3 only (complexity for this stub project is already high enough
  without the numerous `str`/`byte` argument/input/output combinations)


## About
This repository contains external type annotations (see
[PEP 484](https://www.python.org/dev/peps/pep-0484/)) for the
[lxml](http://lxml.de/) package.


## Installation
To use these stubs with [mypy](https://github.com/python/mypy), you have to
install the `lxml-stubs` package.

    pip install lxml-stubs


## Contributing
Contributions should follow the same style guidelines as
[typeshed](https://github.com/python/typeshed/blob/master/CONTRIBUTING.md).


## History
These type annotations were initially included included in
[typeshed](https://www.github.com/python/typeshed), but lxml's annotations
were found to be frequently problematic and have therefore been deleted from
typeshed.

The code was extracted by Jelle Zijlstra from the original typeshed codebase
and moved to a separate repository using `git filter-branch`.


## Authors
Numerous people have contributed to the lxml stubs; see the git history for
details.
