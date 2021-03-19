#
# Internal classes and functions from lxml/xpath.pxi
#

from typing import List, Optional, Tuple, TypeVar, Union

from ._types import basestring
from ._xmlerror import _ErrorLog
from .etree import _Element, _ElementUnicodeResult

_ET = TypeVar("_ET", bound=_Element)

# XPath object - http://lxml.de/xpathxslt.html#xpath-return-values
# TODO Generic alias to parameterize returned element type
# really wish smart string / normal string can be parameterized too
#
# This is always a pain in butt for users, since they have to assert
# result is of specific type before continuing (or ignore type checker
# altogether). Probably returning typing.Any means smoother experience.
#
_XPathObject = Union[
    bool,
    float,
    _ElementUnicodeResult,
    str,
    List[
        Union[
            _ET,
            _ElementUnicodeResult,
            str,
            Tuple[Optional[str], Optional[str]],
        ]
    ],
]

# XPath() accepts most types from XPathObject as input variables
# see extensions.pxi _wrapXPathObject()
_XPathVarArg = Union[
    basestring,
    bool,
    int,
    float,
    List[
        Union[
            _Element,
            basestring,
        ]
    ],
]

class _XPathEvaluatorBase:
    @property
    def error_log(self) -> _ErrorLog: ...
    # evaluate() is deprecated
