import sys
from typing import (
    AbstractSet,
    Any,
    Callable,
    Dict,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

from .etree import QName

_KT_co = TypeVar("_KT_co", covariant=True)
_VT_co = TypeVar("_VT_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

# typing.AnyStr WILL be used in multiple places like string replace
# or attribute handling, where input and output ARE related.
# Previous naming of _AnyStr would be recipe for hard to discover
# typo. Borrow basestring from py2 here, as there is no intention
# to support py2 in this stub repo.

if sys.version_info > (3,):
    basestring = Union[str, bytes]

#
# Virtual protocols that does not exist beyond type checking
# They are borrowed from typeshed
#

class SupportsItems(Protocol[_KT_co, _VT_co]):
    def items(self) -> AbstractSet[Tuple[_KT_co, _VT_co]]: ...

class SupportsWrite(Protocol[_T_contra]):
    def write(self, __s: _T_contra) -> Any: ...

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

#
# QName is supported in several places (like tag name, node attributes)
#
_TextArg = Union[basestring, QName]

#
# Write methods can write gzip compressed data
#
_filename_or_writable = Union[basestring, SupportsWrite[Any]]
