# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

import sys
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Sized,
    SupportsBytes,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from ._types import (
    basestring,
    _Dict_Tuple2AnyStr_Any,
    _DictAnyStr,
    _ListAnyStr,
    _NSMap,
    _OptionalNamespace,
)

if sys.version_info < (3, 8):
    from typing_extensions import Literal, Protocol
else:
    from typing import Literal, Protocol

_AnySmartStr = Union["_ElementUnicodeResult", "_ElementStringResult"]
_TagName = Union[str, bytes, QName]
# XPath object - http://lxml.de/xpathxslt.html#xpath-return-values
_XPathObject = Union[
    bool,
    float,
    _AnySmartStr,
    basestring,
    List[
        Union[
            "_Element",
            _AnySmartStr,
            basestring,
            Tuple[Optional[basestring], Optional[basestring]],
        ]
    ],
]
_T = TypeVar("_T")
_KnownEncodings = Literal[
    "ASCII",
    "ascii",
    "UTF-8",
    "utf-8",
    "UTF8",
    "utf8",
    "US-ASCII",
    "us-ascii",
]

class ElementChildIterator(Iterator["_Element"]):
    def __iter__(self) -> "ElementChildIterator": ...
    def __next__(self) -> "_Element": ...

class _ElementUnicodeResult(str):
    is_attribute: bool
    is_tail: bool
    is_text: bool
    attrname: Optional[basestring]
    def getparent(self) -> Optional["_Element"]: ...

class _ElementStringResult(bytes):
    is_attribute: bool
    is_tail: bool
    is_text: bool
    attrname: Optional[basestring]
    def getparent(self) -> Optional["_Element"]: ...

class _Element(Iterable["_Element"], Sized):
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def __getitem__(self, item: int) -> _Element: ...
    def __len__(self) -> int: ...
    def addprevious(self, element: "_Element") -> None: ...
    def addnext(self, element: "_Element") -> None: ...
    def append(self, element: "_Element") -> None: ...
    def cssselect(self, expression: str) -> List[_Element]: ...
    def find(
        self, path: str, namespaces: _OptionalNamespace = ...
    ) -> Optional["_Element"]: ...
    def findtext(
        self,
        path: str,
        default: Optional[str] = ...,
        namespaces: _OptionalNamespace = ...,
    ) -> Optional[str]: ...
    def findall(
        self, name: str, namespaces: _OptionalNamespace = ...
    ) -> List["_Element"]: ...
    def clear(self) -> None: ...
    @overload
    def get(self, key: _TagName) -> Optional[str]: ...
    @overload
    def get(self, key: _TagName, default: _T) -> Union[str, _T]: ...
    def getnext(self) -> Optional[_Element]: ...
    def getparent(self) -> Optional[_Element]: ...
    def getprevious(self) -> Optional[_Element]: ...
    def getroottree(self) -> _ElementTree: ...
    def insert(self, index: int, element: _Element) -> None: ...
    def iter(
        self, tag: Optional[_TagName] = ..., *tags: _TagName
    ) -> Iterable[_Element]: ...
    def iterchildren(
        self, tag: Optional[_TagName] = ..., reversed: bool = ..., *tags: _TagName
    ) -> Iterable[_Element]: ...
    def makeelement(
        self,
        _tag: _TagName,
        attrib: Optional[_DictAnyStr] = ...,
        nsmap: Optional[_NSMap] = ...,
        **_extra: Any
    ) -> _Element: ...
    def remove(self, element: _Element) -> None: ...
    def set(self, key: _TagName, value: basestring) -> None: ...
    def xpath(
        self,
        _path: basestring,
        namespaces: Optional[_DictAnyStr] = ...,
        extensions: Any = ...,
        smart_strings: bool = ...,
        **_variables: _XPathObject
    ) -> _XPathObject: ...
    attrib = ...  # type: _Attrib
    text = ...  # type: Optional[basestring]
    tag = ...  # type: str
    tail = ...  # type: Optional[basestring]
    nsmap = ...  # type: _NSMap
    def __iter__(self) -> ElementChildIterator: ...
    def items(self) -> Sequence[Tuple[basestring, basestring]]: ...
    def iterfind(
        self, path: str, namespace: _OptionalNamespace = ...
    ) -> Iterator["_Element"]: ...

class ElementBase(_Element): ...

class _ElementTree:
    parser = ...  # type: XMLParser
    def getpath(self, element: _Element) -> str: ...
    def getroot(self) -> _Element: ...
    def write(
        self,
        file: Union[basestring, IO[Any]],
        encoding: basestring = ...,
        method: basestring = ...,
        pretty_print: bool = ...,
        xml_declaration: Any = ...,
        with_tail: Any = ...,
        standalone: bool = ...,
        compression: int = ...,
        exclusive: bool = ...,
        with_comments: bool = ...,
        inclusive_ns_prefixes: _ListAnyStr = ...,
    ) -> None: ...
    def write_c14n(
        self,
        file: Union[basestring, IO[Any]],
        with_comments: bool = ...,
        compression: int = ...,
        inclusive_ns_prefixes: Iterable[basestring] = ...,
    ) -> None: ...
    def _setroot(self, root: _Element) -> None: ...
    def xpath(
        self,
        _path: basestring,
        namespaces: Optional[_DictAnyStr] = ...,
        extensions: Any = ...,
        smart_strings: bool = ...,
        **_variables: _XPathObject
    ) -> _XPathObject: ...
    def xslt(
        self,
        _xslt: XSLT,
        extensions: Optional[_Dict_Tuple2AnyStr_Any] = ...,
        access_control: Optional[XSLTAccessControl] = ...,
        **_variables: Any
    ) -> _ElementTree: ...

class __ContentOnlyElement(_Element): ...
class _Comment(__ContentOnlyElement): ...

class _ProcessingInstruction(__ContentOnlyElement):
    target: basestring

class _Attrib:
    def __setitem__(self, key: basestring, value: basestring) -> None: ...
    def __delitem__(self, key: basestring) -> None: ...
    def update(
        self,
        sequence_or_dict: Union[
            _Attrib, Mapping[basestring, basestring], Sequence[Tuple[basestring, basestring]]
        ],
    ) -> None: ...
    def pop(self, key: basestring, default: basestring) -> basestring: ...
    def clear(self) -> None: ...
    def __repr__(self) -> str: ...
    def __copy__(self) -> _DictAnyStr: ...
    def __deepcopy__(self, memo: Dict[Any, Any]) -> _DictAnyStr: ...
    def __getitem__(self, key: basestring) -> basestring: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def get(self, key: basestring, default: basestring = ...) -> Optional[basestring]: ...
    def keys(self) -> _ListAnyStr: ...
    def __iter__(self) -> Iterator[basestring]: ...  # actually _AttribIterator
    def iterkeys(self) -> Iterator[basestring]: ...
    def values(self) -> _ListAnyStr: ...
    def itervalues(self) -> Iterator[basestring]: ...
    def items(self) -> List[Tuple[basestring, basestring]]: ...
    def iteritems(self) -> Iterator[Tuple[basestring, basestring]]: ...
    def has_key(self, key: basestring) -> bool: ...
    def __contains__(self, key: basestring) -> bool: ...
    def __richcmp__(self, other: _Attrib, op: int) -> bool: ...

class QName:
    localname = ...  # type: str
    namespace = ...  # type: str
    text = ...  # type: str
    def __init__(
        self,
        text_or_uri_or_element: Union[None, basestring, _Element],
        tag: Optional[basestring] = ...,
    ) -> None: ...

class _XSLTResultTree(_ElementTree, SupportsBytes):
    def __bytes__(self) -> bytes: ...

class _XSLTQuotedStringParam: ...

# https://lxml.de/parsing.html#the-target-parser-interface
class ParserTarget(Protocol):
    def comment(self, text: basestring) -> None: ...
    def close(self) -> Any: ...
    def data(self, data: basestring) -> None: ...
    def end(self, tag: basestring) -> None: ...
    def start(self, tag: basestring, attrib: Dict[basestring, basestring]) -> None: ...

class ElementClassLookup: ...

class FallbackElementClassLookup(ElementClassLookup):
    fallback: Optional[ElementClassLookup]
    def __init__(self, fallback: Optional[ElementClassLookup] = ...): ...
    def set_fallback(self, lookup: ElementClassLookup) -> None: ...

class CustomElementClassLookup(FallbackElementClassLookup):
    def lookup(
        self, type: str, doc: str, namespace: str, name: str
    ) -> Optional[Type[ElementBase]]: ...

class _BaseParser:
    def copy(self) -> _BaseParser: ...
    def makeelement(
        self,
        _tag: basestring,
        attrib: Optional[Union[_DictAnyStr, _Attrib]] = ...,
        nsmap: Optional[_NSMap] = ...,
        **_extra: Any
    ) -> _Element: ...
    def setElementClassLookup(
        self, lookup: Optional[ElementClassLookup] = ...
    ) -> None: ...
    def set_element_class_lookup(
        self, lookup: Optional[ElementClassLookup] = ...
    ) -> None: ...

class _FeedParser(_BaseParser):
    def close(self) -> _Element: ...
    def feed(self, data: basestring) -> None: ...

class XMLParser(_FeedParser):
    def __init__(
        self,
        encoding: Optional[basestring] = ...,
        attribute_defaults: bool = ...,
        dtd_validation: bool = ...,
        load_dtd: bool = ...,
        no_network: bool = ...,
        ns_clean: bool = ...,
        recover: bool = ...,
        schema: Optional[XMLSchema] = ...,
        huge_tree: bool = ...,
        remove_blank_text: bool = ...,
        resolve_entities: bool = ...,
        remove_comments: bool = ...,
        remove_pis: bool = ...,
        strip_cdata: bool = ...,
        collect_ids: bool = ...,
        target: Optional[ParserTarget] = ...,
        compact: bool = ...,
    ) -> None: ...
    resolvers = ...  # type: _ResolverRegistry

class HTMLParser(_FeedParser):
    def __init__(
        self,
        encoding: Optional[basestring] = ...,
        collect_ids: bool = ...,
        compact: bool = ...,
        huge_tree: bool = ...,
        no_network: bool = ...,
        recover: bool = ...,
        remove_blank_text: bool = ...,
        remove_comments: bool = ...,
        remove_pis: bool = ...,
        schema: Optional[XMLSchema] = ...,
        strip_cdata: bool = ...,
        target: Optional[ParserTarget] = ...,
    ) -> None: ...

class _ResolverRegistry:
    def add(self, resolver: Resolver) -> None: ...
    def remove(self, resolver: Resolver) -> None: ...

class Resolver:
    def resolve(self, system_url: str, public_id: str): ...
    def resolve_file(
        self, f: IO[Any], context: Any, *, base_url: Optional[basestring], close: bool
    ): ...
    def resolve_string(
        self, string: basestring, context: Any, *, base_url: Optional[basestring]
    ): ...

class XMLSchema:
    def __init__(
        self,
        etree: Union[_Element, _ElementTree] = ...,
        file: Union[basestring, IO[Any]] = ...,
    ) -> None: ...
    def assertValid(self, etree: Union[_Element, _ElementTree]) -> None: ...

class XSLTAccessControl: ...

class XSLT:
    def __init__(
        self,
        xslt_input: Union[_Element, _ElementTree],
        extensions: _Dict_Tuple2AnyStr_Any = ...,
        regexp: bool = ...,
        access_control: XSLTAccessControl = ...,
    ) -> None: ...
    def __call__(
        self,
        _input: Union[_Element, _ElementTree],
        profile_run: bool = ...,
        **kwargs: Union[basestring, _XSLTQuotedStringParam]
    ) -> _XSLTResultTree: ...
    @staticmethod
    def strparam(s: basestring) -> _XSLTQuotedStringParam: ...

def Comment(text: Optional[basestring] = ...) -> _Comment: ...
def Element(
    _tag: basestring,
    attrib: Optional[_DictAnyStr] = ...,
    nsmap: Optional[_NSMap] = ...,
    **extra: basestring
) -> _Element: ...
def SubElement(
    _parent: _Element,
    _tag: basestring,
    attrib: Optional[_DictAnyStr] = ...,
    nsmap: Optional[_NSMap] = ...,
    **extra: basestring
) -> _Element: ...
def ElementTree(
    element: _Element = ...,
    file: Union[basestring, IO[Any]] = ...,
    parser: XMLParser = ...,
) -> _ElementTree: ...
def ProcessingInstruction(
    target: basestring, text: basestring = ...
) -> _ProcessingInstruction: ...

PI = ProcessingInstruction

def HTML(
    text: basestring,
    parser: Optional[HTMLParser] = ...,
    base_url: Optional[basestring] = ...,
) -> _Element: ...
def XML(
    text: basestring,
    parser: Optional[XMLParser] = ...,
    base_url: Optional[basestring] = ...,
) -> _Element: ...
def cleanup_namespaces(
    tree_or_element: Union[_Element, _ElementTree],
    top_nsmap: Optional[_NSMap] = ...,
    keep_ns_prefixes: Optional[Iterable[basestring]] = ...,
) -> None: ...
def parse(
    source: Union[basestring, IO[Any]], parser: XMLParser = ..., base_url: basestring = ...
) -> _ElementTree: ...
def fromstring(
    text: basestring, parser: XMLParser = ..., *, base_url: basestring = ...
) -> _Element: ...
@overload
def tostring(
    element_or_tree: Union[_Element, _ElementTree],
    encoding: Union[Type[str], Literal["unicode"]],
    method: str = ...,
    xml_declaration: bool = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool = ...,
    doctype: str = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Any = ...,
) -> str: ...
@overload
def tostring(
    element_or_tree: Union[_Element, _ElementTree],
    # Should be anything but "unicode", cannot be typed
    encoding: Optional[_KnownEncodings] = ...,
    method: str = ...,
    xml_declaration: bool = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool = ...,
    doctype: str = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Any = ...,
) -> bytes: ...
@overload
def tostring(
    element_or_tree: Union[_Element, _ElementTree],
    encoding: Union[str, type] = ...,
    method: str = ...,
    xml_declaration: bool = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool = ...,
    doctype: str = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Any = ...,
) -> basestring: ...

class _ErrorLog: ...
class Error(Exception): ...

class LxmlError(Error):
    def __init__(self, message: Any, error_log: _ErrorLog = ...) -> None: ...
    error_log = ...  # type: _ErrorLog

class DocumentInvalid(LxmlError): ...
class LxmlSyntaxError(LxmlError, SyntaxError): ...
class ParseError(LxmlSyntaxError): ...
class XMLSyntaxError(ParseError): ...
class _Validator: ...

class DTD(_Validator):
    def __init__(
        self, file: Union[basestring, IO[Any]] = ..., *, external_id: Any = ...
    ) -> None: ...
    def assertValid(self, etree: _Element) -> None: ...

class XPath:
    def __init__(
        self,
        path: basestring,
        *,
        namespaces: Optional[basestring] = ...,
        extensions: Optional[basestring] = ...,
        regexp: bool = ...,
        smart_strings: bool = ...
    ) -> None: ...
    def __call__(
        self,
        _etree_or_element: Union[_Element, _ElementTree],
        **_variables: _XPathObject
    ) -> _XPathObject: ...

_ElementFactory = Callable[[Any, Dict[basestring, basestring]], _Element]
_CommentFactory = Callable[[basestring], _Comment]
_ProcessingInstructionFactory = Callable[[basestring, basestring], _ProcessingInstruction]

class TreeBuilder:
    def __init__(
        self,
        element_factory: Optional[_ElementFactory] = ...,
        parser: Optional[_BaseParser] = ...,
        comment_factory: Optional[_CommentFactory] = ...,
        pi_factory: Optional[_ProcessingInstructionFactory] = ...,
        insert_comments: bool = ...,
        insert_pis: bool = ...,
    ) -> None: ...
    def close(self) -> _Element: ...
    def comment(self, text: basestring) -> None: ...
    def data(self, data: basestring) -> None: ...
    def end(self, tag: basestring) -> None: ...
    def pi(self, target: basestring, data: Optional[basestring] = ...) -> Any: ...
    def start(self, tag: basestring, attrib: Dict[basestring, basestring]) -> None: ...
