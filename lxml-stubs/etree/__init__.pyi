# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

from typing import (
    Any,
    Callable,
    Collection,
    Iterable,
    Iterator,
    Mapping,
    Reversible,
    SupportsBytes,
    TypeVar,
    Union,
    overload,
)

from typing_extensions import Literal, TypeGuard, final

from .._types import (
    SupportsLaxedItems,
    _AnyStr,
    _AttrName,
    _AttrVal,
    _ElemPathArg,
    _FileReadSource,
    _FileWriteSource,
    _NonDefaultNSMapArg,
    _NSMapArg,
    _OutputMethodArg,
    _TagName,
    _XPathExtFuncArg,
    _XPathObject,
    _XPathVarArg,
)
from ..cssselect import _CSSTransArg
from ._classlookup import (
    CommentBase as CommentBase,
    CustomElementClassLookup as CustomElementClassLookup,
    ElementBase as ElementBase,
    ElementClassLookup as ElementClassLookup,
    EntityBase as EntityBase,
    FallbackElementClassLookup as FallbackElementClassLookup,
    PIBase as PIBase,
)
from ._parser import (
    ETCompatXMLParser as ETCompatXMLParser,
    HTMLParser as HTMLParser,
    HTMLPullParser as HTMLPullParser,
    ParseError as ParseError,
    ParserError as ParserError,
    ParserTarget as ParserTarget,
    XMLParser as XMLParser,
    XMLPullParser as XMLPullParser,
    XMLSyntaxError as XMLSyntaxError,
    _BaseParser as _BaseParser,
    _FeedParser as _FeedParser,  # unused but must be present for mypy tests
    get_default_parser as get_default_parser,
    set_default_parser as set_default_parser,
)
from ._xmlerror import (
    ErrorDomains as ErrorDomains,
    ErrorLevels as ErrorLevels,
    ErrorTypes as ErrorTypes,
    PyErrorLog as PyErrorLog,
    RelaxNGErrorTypes as RelaxNGErrorTypes,
    _BaseErrorLog,
    _ErrorLog,
    clear_error_log as clear_error_log,
    use_global_python_log as use_global_python_log,
)
from ._xpath import (
    ETXPath as ETXPath,
    XPath as XPath,
    XPathDocumentEvaluator as XPathDocumentEvaluator,
    XPathElementEvaluator as XPathElementEvaluator,
    XPathError as XPathError,
    XPathEvaluator as XPathEvaluator,
    XPathSyntaxError as XPathSyntaxError,
)

#
# Basic variables and constants
#

_T = TypeVar("_T")
_ET = TypeVar("_ET", bound=_Element)

# Note that _TagSelector filters element type not by classes,
# but checks for element _factory functions_ instead
# (that is Element(), Comment() and ProcessingInstruction()).
_TagSelector = Union[_TagName, _ElemFactory[_Element]]
# For tostring() encoding. In theory it should be any encoding name
# except "unicode", but is not representable in current typing system.
# Settle for commonly seen encodings in XML.
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
_ElementOrTree = _Element | _ElementTree

class _SmartStr(str):
    """Smart string is a private str subclass documented in
    [return types](https://lxml.de/xpathxslt.html#xpath-return-values)
    of XPath evaluation result. This stub-only class can be utilized like:

    ```python
    if TYPE_CHECKING:
        from lxml.etree import _SmartStr
    def is_smart_str(s: str) -> TypeGuard[_SmartStr]:
        return hasattr(s, 'getparent')
    if is_smart_str(result):
        parent = result.getparent() # identified as lxml.etree._Element
    ```
    """

    is_attribute: bool
    is_tail: bool
    is_text: bool
    attrname: str | None
    def getparent(self) -> _Element | None: ...

class DocInfo:
    @property
    def root_name(self) -> str | None: ...
    public_id: str | None
    system_id: str | None
    @property
    def xml_version(self) -> str | None: ...
    @property
    def encoding(self) -> str | None: ...
    @property
    def standalone(self) -> bool | None: ...
    URL: str | None
    @property
    def doctype(self) -> str: ...
    @property
    def internalDTD(self) -> DTD | None: ...
    @property
    def externalDTD(self) -> DTD | None: ...
    def __init__(self, tree: _ElementOrTree) -> None: ...
    def clear(self) -> None: ...

# The base of _Element is *almost* an amalgam of MutableSequence[_Element]
# plus mixin methods for _Attrib.
# Extra methods follow the order of _Element source approximately
class _Element(Collection[_Element], Reversible[_Element]):
    #
    # Common properties
    #
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: _TagName) -> None: ...
    @property
    def attrib(self) -> _Attrib: ...
    @property
    def text(self) -> str | None: ...
    @text.setter
    def text(self, value: _AnyStr | QName | CDATA | None) -> None: ...
    @property
    def tail(self) -> str | None: ...
    @tail.setter
    def tail(self, value: _AnyStr | CDATA | None) -> None: ...
    #
    # _Element-only properties
    # Following props are marked as read-only in comment,
    # but 'sourceline' and 'base' provide __set__ method
    # --- and they do work.
    #
    @property
    def prefix(self) -> str | None: ...
    @property
    def sourceline(self) -> int | None: ...
    @sourceline.setter
    def sourceline(self, value: int) -> None: ...
    @property
    def nsmap(self) -> dict[str | None, str]: ...
    @property
    def base(self) -> str | None: ...
    @base.setter
    def base(self, value: _AnyStr | None) -> None: ...
    #
    # Accessors
    #
    def __delitem__(self, __k: int | slice) -> None: ...
    @overload
    def __getitem__(self, __x: int) -> _Element: ...
    @overload
    def __getitem__(self, __x: slice) -> list[_Element]: ...
    @overload
    def __setitem__(self, __x: int, __v: _Element) -> None: ...
    @overload
    def __setitem__(self, __x: slice, __v: Iterable[_Element]) -> None: ...
    def __contains__(self, __x: object) -> bool: ...
    def __len__(self) -> int: ...
    # There are a hoard of element iterators used in lxml, but
    # they only differ in implementation detail and don't affect typing.
    def __iter__(self) -> Iterator[_Element]: ...
    def __reversed__(self) -> Iterator[_Element]: ...
    def set(self, key: _AttrName, value: _AttrVal) -> None: ...
    def append(self, element: _Element) -> None: ...
    def extend(self, elements: Iterable[_Element]) -> None: ...
    def clear(self, keep_tail: bool = ...) -> None: ...
    def insert(self, index: int, element: _Element) -> None: ...
    def remove(self, element: _Element) -> None: ...
    def index(
        self, child: _Element, start: int | None = ..., end: int | None = ...
    ) -> int: ...
    @overload
    def get(self, key: _AttrName) -> str | None: ...
    @overload
    def get(self, key: _AttrName, default: _T) -> str | _T: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[str]: ...
    def items(self) -> list[tuple[str, str]]: ...
    #
    # extra Element / ET methods
    #
    def addnext(self, element: _Element) -> None: ...
    def addprevious(self, element: _Element) -> None: ...
    def replace(self, old_element: _Element, new_element: _Element) -> None: ...
    def getparent(self) -> _Element | None: ...
    def getnext(self) -> _Element | None: ...
    def getprevious(self) -> _Element | None: ...
    def itersiblings(
        self,
        tag: _TagSelector | None = ...,
        *tags: _TagSelector,
        preceding: bool = ...,
    ) -> Iterator[_Element]: ...
    def iterancestors(
        self, tag: _TagSelector | None = ..., *tags: _TagSelector
    ) -> Iterator[_Element]: ...
    def iterdescendants(
        self, tag: _TagSelector | None = ..., *tags: _TagSelector
    ) -> Iterator[_Element]: ...
    def iterchildren(
        self,
        tag: _TagSelector | None = ...,
        *tags: _TagSelector,
        reversed: bool = ...,
    ) -> Iterator[_Element]: ...
    def getroottree(self) -> _ElementTree: ...
    def iter(
        self, tag: _TagSelector | None = ..., *tags: _TagSelector
    ) -> Iterator[_Element]: ...
    def itertext(
        self,
        tag: _TagSelector | None = ...,
        *tags: _TagSelector,
        with_tail: bool = ...,
    ) -> Iterator[str]: ...
    def makeelement(
        self,
        _tag: _TagName,
        # Final result is sort of like {**attrib, **_extra}
        attrib: SupportsLaxedItems[str, _AnyStr] | None = ...,
        nsmap: _NSMapArg | None = ...,
        **_extra: _AnyStr,
    ) -> _Element: ...
    def find(
        self, path: _ElemPathArg, namespaces: _NSMapArg | None = ...
    ) -> _Element | None: ...
    # Original method has no star. If somebody only supplies
    # 'path' and 'default' argument as positional one, it
    # would be misinterpreted as namespaces argument in first
    # overload form. Add star here to guard against such situation.
    @overload
    def findtext(
        self,
        path: _ElemPathArg,
        *,
        namespaces: _NSMapArg | None = ...,
    ) -> str | None: ...
    @overload
    def findtext(
        self,
        path: _ElemPathArg,
        default: _T,
        namespaces: _NSMapArg | None = ...,
    ) -> str | _T: ...
    def findall(
        self, path: _ElemPathArg, namespaces: _NSMapArg | None = ...
    ) -> list[_Element]: ...
    def iterfind(
        self, path: _ElemPathArg, namespaces: _NSMapArg | None = ...
    ) -> Iterator[_Element]: ...
    def xpath(
        self,
        _path: _AnyStr,
        namespaces: _NonDefaultNSMapArg | None = ...,
        extensions: _XPathExtFuncArg | None = ...,
        smart_strings: bool = ...,
        **_variables: _XPathVarArg,
    ) -> _XPathObject: ...
    def cssselect(
        self,
        expr: str,
        *,
        translator: _CSSTransArg = ...,
    ) -> list[_Element]: ...
    # Following methods marked as deprecated upstream
    def getchildren(self) -> list[_Element]: ...  # = list(self)
    def getiterator(
        self,
        tag: _TagSelector | None,
        *tags: _TagSelector,
    ) -> Iterator[_Element]: ...

class _ElementTree:
    @property
    def parser(self) -> _BaseParser | None: ...
    @property
    def docinfo(self) -> DocInfo: ...
    def find(
        self, path: str, namespaces: _NSMapArg | None = ...
    ) -> _Element | None: ...
    def findtext(
        self,
        path: str,
        default: str | None = ...,
        namespaces: _NSMapArg | None = ...,
    ) -> str | None: ...
    def findall(
        self, path: str, namespaces: _NSMapArg | None = ...
    ) -> list[_Element]: ...
    def getpath(self, element: _Element) -> str: ...
    def getroot(self) -> _Element: ...
    def iter(
        self, tag: _TagSelector | None = ..., *tags: _TagSelector
    ) -> Iterable[_Element]: ...
    @overload  # method=c14n
    def write(
        self,
        file: _FileWriteSource,
        *,
        method: Literal["c14n"],
        exclusive: bool = ...,
        with_comments: bool = ...,
        compression: int | None = ...,
        inclusive_ns_prefixes: Iterable[_AnyStr] | None = ...,
    ) -> None: ...
    @overload  # method=c14n2
    def write(
        self,
        file: _FileWriteSource,
        *,
        method: Literal["c14n2"],
        with_comments: bool = ...,
        compression: int | None = ...,
        strip_text: bool = ...,
    ) -> None: ...
    @overload  # other write methods
    def write(
        self,
        file: _FileWriteSource,
        *,
        encoding: str | type[str] | None = ...,
        method: _OutputMethodArg,
        pretty_print: bool = ...,
        xml_declaration: bool | None = ...,
        with_tail: bool = ...,
        standalone: bool | None = ...,
        doctype: str | None = ...,
        compression: int | None = ...,
    ) -> None: ...
    @overload  # catch all
    def write(
        self,
        file: _FileWriteSource,
        *,
        encoding: str | type[str] | None = ...,
        method: _OutputMethodArg | Literal["c14n", "c14n2"] = ...,
        pretty_print: bool = ...,
        xml_declaration: bool | None = ...,
        with_tail: bool = ...,
        standalone: bool = ...,
        doctype: str | None = ...,
        compression: int | None = ...,
        exclusive: bool = ...,
        with_comments: bool = ...,
        inclusive_ns_prefixes: Iterable[_AnyStr] | None = ...,
        strip_text: bool = ...,
    ) -> None: ...
    def write_c14n(
        self,
        file: _FileWriteSource,
        *,
        exclusive: bool = ...,
        with_comments: bool = ...,
        compression: int | None = ...,
        inclusive_ns_prefixes: Iterable[_AnyStr] | None = ...,
    ) -> None: ...
    def _setroot(self, root: _Element) -> None: ...
    def xinclude(self) -> None: ...
    def xpath(
        self,
        _path: _AnyStr,
        namespaces: _NonDefaultNSMapArg | None = ...,
        extensions: _XPathExtFuncArg | None = ...,
        smart_strings: bool = ...,
        **_variables: _XPathVarArg,
    ) -> _XPathObject: ...
    def xslt(
        self,
        _xslt: XSLT,
        extensions: Any = ...,
        access_control: XSLTAccessControl | None = ...,
        **_variables: Any,
    ) -> _ElementTree: ...

# Behaves like MutableMapping but deviates a lot in details
@final
class _Attrib:
    @property
    def _element(self) -> _Element: ...
    def __setitem__(self, __k: _AttrName, __v: _AttrVal) -> None: ...
    def __delitem__(self, __k: _AttrName) -> None: ...
    # explicitly checks for dict and _Attrib
    def update(
        self,
        sequence_or_dict: _Attrib
        | dict[Any, Any]  # Compromise with MutableMapping key/val invariance
        | Iterable[tuple[_AttrName, _AttrVal]],
    ) -> None: ...
    # Signature is pop(self, key, *default), yet followed by runtime
    # check and raise exception if multiple default argument is supplied
    @overload
    def pop(self, key: _AttrName) -> str | None: ...
    @overload
    def pop(self, key: _AttrName, default: _T) -> str | _T: ...
    def clear(self) -> None: ...
    def __getitem__(self, __k: _AttrName) -> str: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    @overload
    def get(self, key: _AttrName) -> str | None: ...
    @overload
    def get(self, key: _AttrName, default: _T) -> str | _T: ...
    def keys(self) -> list[str]: ...
    def __iter__(self) -> Iterator[str]: ...
    def iterkeys(self) -> Iterator[str]: ...
    def values(self) -> list[str]: ...
    def itervalues(self) -> Iterator[str]: ...
    def items(self) -> list[tuple[str, str]]: ...
    def iteritems(self) -> Iterator[tuple[str, str]]: ...
    def has_key(self, key: _AttrName) -> bool: ...
    def __contains__(self, key: _AttrName) -> bool: ...
    # richcmp dropped, mapping has no concept of inequality comparison

# Qualified Name helper
class QName:
    @overload
    def __init__(
        self,
        text_or_uri_or_element: _TagName | _Element,
        tag: _TagName | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        text_or_uri_or_element: None,
        tag: _TagName,
    ) -> None: ...
    @property
    def localname(self) -> str: ...
    @property
    def namespace(self) -> str | None: ...
    @property
    def text(self) -> str: ...
    # Emulate __richcmp__()
    def __ge__(self, other: _TagName) -> bool: ...
    def __gt__(self, other: _TagName) -> bool: ...
    def __le__(self, other: _TagName) -> bool: ...
    def __lt__(self, other: _TagName) -> bool: ...

class _XSLTResultTree(_ElementTree, SupportsBytes):
    def __bytes__(self) -> bytes: ...

class _XSLTQuotedStringParam: ...

class XMLSchema(_Validator):
    def __init__(
        self,
        etree: _ElementOrTree = ...,
        file: _FileReadSource = ...,
    ) -> None: ...
    def __call__(self, etree: _ElementOrTree) -> bool: ...

class XSLTAccessControl: ...

class XSLT:
    def __init__(
        self,
        xslt_input: _ElementOrTree,
        extensions: Any = ...,
        regexp: bool = ...,
        access_control: XSLTAccessControl = ...,
    ) -> None: ...
    def __call__(
        self,
        _input: _ElementOrTree,
        profile_run: bool = ...,
        **kwargs: _AnyStr | _XSLTQuotedStringParam,
    ) -> _XSLTResultTree: ...
    @staticmethod
    def strparam(s: _AnyStr) -> _XSLTQuotedStringParam: ...
    @property
    def error_log(self) -> _ErrorLog: ...

#
# Element types and content node types
#

# __ContentOnlyElement is just a noop layer in class inheritance
# Maybe re-add if decided to override various _Element methods
# or simply discouple __ContentOnlyElement from _Element

# class __ContentOnlyElement(_Element): ...

class _Comment(_Element):
    # Signature of "tag" incompatible with supertype "_Element"
    @property  # type: ignore[misc]
    def tag(self) -> _ElemFactory[_Comment]: ...  # type: ignore[override]

class _ProcessingInstruction(_Element):
    @property  # type: ignore[misc]
    def tag(self) -> _ElemFactory[_ProcessingInstruction]: ...  # type: ignore[override]
    @property
    def target(self) -> str: ...
    @target.setter
    def target(self, value: _AnyStr) -> None: ...
    @overload
    def get(self, key: _AttrName) -> str | None: ...
    @overload
    def get(self, key: _AttrName, default: _T) -> str | _T: ...
    @property
    def attrib(self) -> dict[str, str]: ...  # type: ignore[override]

class _Entity(_Element):
    @property  # type: ignore[misc]
    def tag(self) -> _ElemFactory[_Entity]: ...  # type: ignore[override]
    @property  # type: ignore[misc]
    def text(self) -> str: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: _AnyStr) -> None: ...

class CDATA:
    def __init__(self, data: _AnyStr) -> None: ...

# Element factory functions
#

# Most arguments for factories functions are optional, so accurate
# typing can't be done. Opt for generic aliases instead.
_ElemFactory = Callable[..., _ET]

def Comment(text: _AnyStr | None = ...) -> _Comment: ...
def ProcessingInstruction(
    target: _AnyStr, text: _AnyStr | None = ...
) -> _ProcessingInstruction: ...

PI = ProcessingInstruction

def Entity(name: _AnyStr) -> _Entity: ...
def Element(  # Args identical to _Element.makeelement
    _tag: _TagName,
    attrib: SupportsLaxedItems[str, _AnyStr] | None = ...,
    nsmap: _NSMapArg | None = ...,
    **_extra: _AnyStr,
) -> _Element: ...
def SubElement(
    _parent: _Element,
    _tag: _TagName,
    attrib: SupportsLaxedItems[str, _AnyStr] | None = ...,
    nsmap: _NSMapArg | None = ...,
    **_extra: _AnyStr,
) -> _Element: ...
def ElementTree(
    element: _Element = ...,
    *,
    file: _FileReadSource = ...,
    parser: _BaseParser | None = ...,
) -> _ElementTree: ...
def HTML(
    text: _AnyStr,
    parser: _BaseParser | None = ...,
    *,
    base_url: _AnyStr | None = ...,
) -> _Element: ...
def XML(
    text: _AnyStr,
    parser: _BaseParser | None = ...,
    *,
    base_url: _AnyStr | None = ...,
) -> _Element: ...
def cleanup_namespaces(
    tree_or_element: _ElementOrTree,
    top_nsmap: _NSMapArg | None = ...,
    keep_ns_prefixes: Iterable[_AnyStr] | None = ...,
) -> None: ...
def parse(
    source: _FileReadSource, parser: _BaseParser | None = ..., base_url: _AnyStr = ...
) -> _ElementTree: ...
def fromstring(
    text: _AnyStr, parser: _BaseParser | None = ..., *, base_url: _AnyStr = ...
) -> _Element: ...
@overload  # Native str, no XML declaration
def tostring(
    element_or_tree: _ElementOrTree,
    *,
    encoding: type[str] | Literal["unicode"],
    method: _OutputMethodArg = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool | None = ...,
    doctype: str | None = ...,
) -> str: ...
@overload  # byte str, no XML declaration
def tostring(
    element_or_tree: _ElementOrTree,
    *,
    encoding: _KnownEncodings | None = ...,
    method: _OutputMethodArg = ...,
    xml_declaration: bool | None = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool | None = ...,
    doctype: str | None = ...,
) -> bytes: ...

# Under XML Canonicalization (C14N) mode, most arguments are ignored,
# some arguments would even raise exception outright if specified.
@overload  # method="c14n"
def tostring(
    element_or_tree: _ElementOrTree,
    *,
    method: Literal["c14n"],
    exclusive: bool = ...,
    inclusive_ns_prefixes: Iterable[_AnyStr] | None = ...,
    with_comments: bool = ...,
) -> bytes: ...
@overload  # method="c14n2"
def tostring(
    element_or_tree: _ElementOrTree,
    *,
    method: Literal["c14n2"],
    with_comments: bool = ...,
    strip_text: bool = ...,
) -> bytes: ...
@overload  # catch all
def tostring(
    element_or_tree: _ElementOrTree,
    *,
    encoding: str | type[str] = ...,
    method: str = ...,
    xml_declaration: bool | None = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool | None = ...,
    doctype: str | None = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Any = ...,
) -> _AnyStr: ...

class Error(Exception): ...

class LxmlError(Error):
    def __init__(self, message: Any, error_log: _BaseErrorLog | None = ...) -> None: ...
    error_log: _BaseErrorLog = ...

class DocumentInvalid(LxmlError): ...
class LxmlSyntaxError(LxmlError, SyntaxError): ...

class _Validator:
    def assert_(self, etree: _ElementOrTree) -> None: ...
    def assertValid(self, etree: _ElementOrTree) -> None: ...
    def validate(self, etree: _ElementOrTree) -> bool: ...
    @property
    def error_log(self) -> _ErrorLog: ...

class DTD(_Validator):
    def __init__(
        self, file: _FileReadSource = ..., *, external_id: Any = ...
    ) -> None: ...
    def __call__(self, etree: _ElementOrTree) -> bool: ...

class TreeBuilder(ParserTarget):
    def __init__(
        self,
        *,
        element_factory: _ElemFactory[_Element] | None = ...,
        parser: _BaseParser | None = ...,
        comment_factory: _ElemFactory[_Comment] | None = ...,
        pi_factory: _ElemFactory[_ProcessingInstruction] | None = ...,
        insert_comments: bool = ...,
        insert_pis: bool = ...,
    ) -> None: ...
    def close(self) -> _Element: ...
    def start(
        self, tag: str, attrib: _Attrib, nsmap: Mapping[str, str] = ...
    ) -> None: ...

def iselement(element: Any) -> TypeGuard[_Element]: ...
