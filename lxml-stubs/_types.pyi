import sys
from typing import Any, Callable, Dict, List, Mapping, Optional, Tuple, Union

# typing.AnyStr WILL be used in multiple places like string replace
# or attribute handling, where input and output ARE related.
# Previous naming of _AnyStr would be recipe for hard to discover
# typo. Borrow basestring name from Python2 here.

if sys.version_info > (3,):
    basestring = Union[str, bytes]

_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]

# - Prefix and URI are encoded separately as input arg, so no need for AnyStr.
# - Namespace prefix/uri in lxml is only documented in form of mapping
#   officially.
#
#   Although some places also accept alternative structures (e.g. ElementMaker
#   accepts a list of (prefix,uri) pairs due to dict() conversion), they are
#   considered implementation detail and not guaranteed to useful globally.
#   As example, _Element.find() and friends don't accept the list form as nsmap.
#
_NSMapArg = Optional[Mapping[Optional[basestring], basestring]]

# Default NS not acceptable for XPath and XSLT
# https://lxml.de/xpathxslt.html#namespaces-and-prefixes
#
_NonDefaultNSMapArg = Optional[Mapping[basestring, basestring]]

_ExtensionArg = Optional[
    Mapping[
        Tuple[Optional[basestring], basestring],
        Callable[..., Any],  # TODO extension function not investigated yet
    ]
]
