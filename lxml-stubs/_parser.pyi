#
# Typing info for Non-public members of lxml/parser.pxi
#

import sys
from abc import abstractmethod
from typing import Any, Dict, Optional, Union, overload

from ._types import SupportsItems, _NSMapArg, _TextArg, basestring
from ._xmlerror import _ErrorLog
from .etree import ElementClassLookup, _Element, _ImmutableMapping, _ResolverRegistry

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

class _BaseParser:
    @property
    def target(self) -> Optional[ParserTarget]: ...
    @property
    def error_log(self) -> _ErrorLog: ...
    @property
    def resolvers(self) -> _ResolverRegistry: ...
    @property
    def version(self) -> str: ...
    def copy(self) -> _BaseParser: ...
    def makeelement(
        self,
        _tag: _TextArg,
        attrib: Optional[SupportsItems[_TextArg, basestring]] = ...,
        nsmap: _NSMapArg = ...,
        **_extra: basestring,
    ) -> _Element: ...
    # Marked as deprecated, identical to snake case method
    def setElementClassLookup(
        self, lookup: Optional[ElementClassLookup] = ...
    ) -> None: ...
    def set_element_class_lookup(
        self, lookup: Optional[ElementClassLookup] = ...
    ) -> None: ...

class _FeedParser(_BaseParser):
    def close(self) -> _Element: ...
    def feed(self, data: basestring) -> None: ...
    @property
    def feed_error_log(self) -> _ErrorLog: ...

# https://lxml.de/parsing.html#the-target-parser-interface
# Only close() method is mandatory, therefore in extreme case, a vanilla class
# object with noop close() method is a valid null parser target.
# See also _PythonSaxParserTarget in src/lxml/parsertarget.pxi.
#
# It can potentially be utilized to autofill method stubs in some IDEs;
# ====================================================================
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     try:
#         from lxml.etree import ParserTarget
#     except ImportError:
#         ParserTarget = object
# else:
#     ParserTarget = object
#
# class MyParserTarget(ParserTarget):
#     # IDEs should be smart enough to pull in definitions, except for
#     # start() which can take 2 or 3 extra arguments
#     def data(self, data: str) -> None:
#         # do your stuff...
#     def close(self) -> str:
#         return 'closed!'
#
# mytarget = MyParserTarget()
# parser = lxml.etree.XMLPullParser(target=mytarget)
# ====================================================================
class ParserTarget(Protocol):
    @abstractmethod
    def close(self) -> Any: ...
    def comment(self, text: str) -> None: ...
    def data(self, data: str) -> None: ...
    def end(self, tag: str) -> None: ...
    @overload
    def start(
        self,
        tag: str,
        attrib: Union[Dict[str, str], _ImmutableMapping],
    ) -> None: ...
    @overload
    def start(
        self,
        tag: str,
        attrib: Union[Dict[str, str], _ImmutableMapping],
        nsmap: Union[Dict[str, str], _ImmutableMapping],
    ) -> None: ...
    # Methods below are undocumented. Lxml has described
    # 'start-ns' and 'end-ns' events however.
    def pi(self, target: str, data: Optional[str]) -> None: ...
    # Default namespace prefix is '' here, not None
    def start_ns(self, prefix: str, uri: str) -> None: ...
    def end_ns(self, prefix: str) -> None: ...
    def doctype(
        self,
        root_tag: Optional[str],
        public_id: Optional[str],
        system_id: Optional[str],
    ) -> None: ...
