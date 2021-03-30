#
# Making some compromise for HTML, in that iteration of subelements
# and xpath evaluation would produce HTML elements instead of the base
# etree._Element. It is technically "correct" that those operations
# may not produce HTML elements when XML nodes are manually inserted
# into documents or fragments. However, arguably 99.9% of user cases
# don't involve such manually constructed hybrid element trees.
# Making it absolutely "correct" harms most users by losing context.
#

from typing import (
    Any,
    AnyStr,
    Callable,
    Collection,
    Iterable,
    Iterator,
    List,
    Literal,
    Mapping,
    MutableMapping,
    MutableSet,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from .. import etree
from .._xpath import _XPathObject
from .._types import (
    SupportsItems,
    _ExtensionArg,
    _NonDefaultNSMapArg,
    _NSMapArg,
    _TextArg,
    basestring,
)
from ..cssselect import _CSSTransArg

_T = TypeVar("_T")

_HANDLE_FAILURES = Optional[Literal["ignore", "discard"]]
XHTML_NAMESPACE: str = ...

# Class attr access only require get(), __delitem__ and __setitem__
# Though _Attrib is dict-like, it is not 100% compatible with any
# existing ABC container types. More work pending.
class _AttribMapping(Mapping[str, str]):
    def __delitem__(self, key: str) -> None: ...
    def __setitem__(self, key: str, value: str) -> None: ...

class Classes(MutableSet[str]):
    _attributes: _AttribMapping
    def __init__(
        self,
        attributes: _AttribMapping,
    ) -> None: ...
    def update(self, values: Iterable[str]) -> None: ...
    def toggle(self, value: str) -> bool: ...

class HtmlMixin:
    classes: Classes
    label: Optional[LabelElement]
    @property
    def base_url(self) -> Optional[str]: ...
    @property
    def forms(self) -> List[FormElement]: ...
    @property
    def body(self) -> HtmlElement: ...
    @property
    def head(self) -> HtmlElement: ...
    # Differs from _Element.set(): value has default here
    def set(self, key: _TextArg, value: Optional[_TextArg] = ...) -> None: ...
    def drop_tree(self) -> None: ...
    def drop_tag(self) -> None: ...
    def find_rel_links(
        self,
        # Can be bytes, but guaranteed to not match any element on py3
        rel: str,
    ) -> List[HtmlElement]: ...
    def find_class(
        self,
        class_name: basestring,
    ) -> List[HtmlElement]: ...
    @overload
    def get_element_by_id(self, id: basestring) -> HtmlElement: ...
    @overload
    def get_element_by_id(
        self, id: basestring, default: _T, *_: Any
    ) -> Union[HtmlElement, _T]: ...
    def text_content(self) -> str: ...
    # Note the difference of return type from _Element.cssselect
    def cssselect(
        self, expr: basestring, translator: _CSSTransArg = ...
    ) -> List[HtmlElement]: ...
    #
    # Link functions
    #
    def make_links_absolute(
        self,
        base_url: Optional[str] = ...,  # exception with bytes
        resolve_base_href: bool = ...,
        handle_failures: _HANDLE_FAILURES = ...,
    ) -> None: ...
    def resolve_base_href(
        self,
        handle_failures: _HANDLE_FAILURES = ...,
    ) -> None: ...
    # (element, attribute, link, pos)
    def iterlinks(self) -> Iterator[Tuple[HtmlElement, Optional[str], str, int]]: ...
    def rewrite_links(
        self,
        link_repl_func: Callable[[AnyStr], AnyStr],
        resolve_base_href: bool = ...,
        base_href: Optional[AnyStr] = ...,
    ) -> None: ...

# These are HtmlMixin methods converted to standard functions,
# with element or HTML string as first argument followed by all
# pre-existing args. Quoting from source:
#
#   ... the function takes either an element or an HTML string.  It
#   returns whatever the function normally returns, or if the function
#   works in-place (and so returns None) it returns a serialized form
#   of the resulting document.
#
# Copying signatures will do, except that these funcs accept an
# extra copy=bool keyword.
# Note that these funcs operate on attributes that only make sense on
# normal HtmlElements. Lxml raises exception otherwise anyway.
def find_rel_links(
    doc: Union[basestring, HtmlElement],
    rel: str,
    *,
    copy: bool = ...,
) -> List[HtmlElement]: ...
def find_class(
    doc: Union[basestring, HtmlElement],
    class_name: basestring,
    *,
    copy: bool = ...,
) -> List[HtmlElement]: ...
def make_links_absolute(
    doc: Union[AnyStr, HtmlElement],
    base_url: Optional[str] = ...,
    resolve_base_href: bool = ...,
    handle_failures: _HANDLE_FAILURES = ...,
    *,
    copy: bool = ...,
) -> AnyStr: ...
def resolve_base_href(
    doc: Union[AnyStr, HtmlElement],
    handle_failures: _HANDLE_FAILURES = ...,
    *,
    copy: bool = ...,
) -> AnyStr: ...
def iterlinks(
    doc: Union[AnyStr, HtmlElement],
    *,
    copy: bool = ...,
) -> Iterator[Tuple[HtmlElement, Optional[str], str, int]]: ...
def rewrite_links(
    doc: Union[AnyStr, HtmlElement],
    link_repl_func: Callable[[AnyStr], AnyStr],
    resolve_base_href: bool = ...,
    base_href: Optional[AnyStr] = ...,
    *,
    copy: bool = ...,
) -> AnyStr: ...

#
# Types of different HTML elements
#

class HtmlElement(etree.ElementBase, HtmlMixin):
    # Copy the definition of cssselect() and set() from HtmlMixin
    # instead of using something like "set = HtmlMixin.set", since
    # IDE users may get confused about type(self) = HtmlMixin
    def cssselect(
        self, expr: basestring, translator: _CSSTransArg = ...
    ) -> List[HtmlElement]: ...
    def set(self, key: _TextArg, value: Optional[_TextArg] = ...) -> None: ...
    # Many methods overrided to return HTML elements
    # It is not a simple return type replacement though, since
    # XML and HTML elements have different inheritance structure (!),
    # and some operations only make sense on subset of HTML elements
    @overload  # type: ignore[override]
    def __getitem__(self, x: int) -> _AnyHtmlElement: ...
    @overload
    def __getitem__(self, x: slice) -> List[_AnyHtmlElement]: ...
    def __iter__(self) -> Iterator[_AnyHtmlElement]: ...
    def __reversed__(self) -> Iterator[_AnyHtmlElement]: ...
    def getparent(self) -> Optional[_AnyHtmlElement]: ...
    def getnext(self) -> Optional[_AnyHtmlElement]: ...
    def getprevious(self) -> Optional[_AnyHtmlElement]: ...
    @overload
    def itersiblings(
        self,
        tag: Optional[Sequence[etree._TagFilter]] = ...,
        preceding: bool = ...,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def itersiblings(
        self,
        tag: etree._TagFilter,
        *tags: etree._TagFilter,
        preceding: bool = ...,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iterancestors(
        self,
        tag: Optional[Sequence[etree._TagFilter]] = ...,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iterancestors(
        self,
        tag: etree._TagFilter,
        *tags: etree._TagFilter,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iterdescendants(
        self,
        tag: Optional[Sequence[etree._TagFilter]] = ...,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iterdescendants(
        self,
        tag: etree._TagFilter,
        *tags: etree._TagFilter,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iterchildren(
        self,
        tag: Optional[Sequence[etree._TagFilter]] = ...,
        reversed: bool = ...,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iterchildren(
        self,
        tag: etree._TagFilter,
        *tags: etree._TagFilter,
        reversed: bool = ...,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iter(
        self,
        tag: Optional[Sequence[etree._TagFilter]] = ...,
    ) -> Iterator[_AnyHtmlElement]: ...
    @overload
    def iter(
        self,
        tag: etree._TagFilter,
        *tags: etree._TagFilter,
    ) -> Iterator[_AnyHtmlElement]: ...
    def makeelement(
        self,
        _tag: _TextArg,
        attrib: Optional[SupportsItems[_TextArg, _TextArg]] = ...,
        nsmap: _NSMapArg = ...,
        **_extra: _TextArg,
    ) -> HtmlElement: ...
    #
    # XXX Subtle difference: find() and friends in xml.etree.ElementTree
    # would include comment and processing instructions, but
    # for lxml this is NOT the case (undocumented or bug? LP #1921675)
    #
    def find(
        self, path: etree._ElemPathArg, namespaces: _NSMapArg = ...
    ) -> Optional[HtmlElement]: ...
    def findall(  # type: ignore[override]
        self,
        path: etree._ElemPathArg,
        namespaces: _NSMapArg = ...,
    ) -> List[HtmlElement]: ...
    # findtext() doesn't need any override
    def iterfind(
        self,
        path: etree._ElemPathArg,
        namespaces: _NSMapArg = ...,
    ) -> Iterator[HtmlElement]: ...
    def xpath(  # type: ignore[override]
        self,
        _path: basestring,
        namespaces: _NonDefaultNSMapArg = ...,
        extensions: _ExtensionArg = ...,
        smart_strings: bool = ...,
    ) -> _XPathObject[_AnyHtmlElement]: ...

class HtmlComment(etree.CommentBase, HtmlMixin): ...
class HtmlEntity(etree.EntityBase, HtmlMixin): ...
class HtmlProcessingInstruction(etree.PIBase, HtmlMixin): ...

_AnyHtmlElement = Union[
    HtmlComment,
    HtmlElement,
    HtmlEntity,
    HtmlProcessingInstruction,
]

_AnyInputElement = Union[
    InputElement,
    SelectElement,
    TextareaElement,
]

# Only useful when somebody wants to create custom markup language
# parser (or extension based on HTMLParser)
class HtmlElementClassLookup(etree.CustomElementClassLookup):
    def __init__(
        self,
        classes: Optional[MutableMapping[str, Type[HtmlElement]]] = ...,
        mixins: Optional[Mapping[str, Type[object]]] = ...,
    ) -> None: ...
    def lookup(
        self,
        # See etree.CustomElementClassLookup
        node_type: Union[Literal["element", "comment", "PI", "entity"], Any],
        document: Any,  # TODO
        namespace: Optional[str],
        name: str,
    ) -> Optional[Type[_AnyHtmlElement]]: ...

class FormElement(HtmlElement):
    @property
    def inputs(self) -> InputGetter: ...
    @property
    def fields(self) -> FieldsDict: ...
    @fields.setter  # SupportsItems[]
    def fields(self, value: Any) -> None: ...
    action: str
    method: str
    def form_values(self) -> List[Tuple[str, Optional[str]]]: ...

# TODO more explicit overload return type for open_http = None
def submit_form(
    form: FormElement,
    extra_values: Optional[List[Tuple[str, str]]] = ...,
    open_http: Optional[
        Callable[
            [str, str, List[Tuple[str, str]]], Any  # open_http(method, url, values)
        ]
    ] = ...,
) -> Any: ...

class FieldsDict(MutableMapping[str, str]):
    inputs: InputGetter
    def __init__(self, inputs: InputGetter) -> None: ...

# Quoting from source: it's unclear if this is a dictionary-like object
# or list-like object
class InputGetter(Collection[_AnyInputElement]):
    form: FormElement
    def __init__(self, form: FormElement) -> None: ...
    # __getitem__ is special here: for checkbox group and radio group,
    # it returns special list-like object instead of HtmlElement
    def __getitem__(
        self, name: str
    ) -> Union[_AnyInputElement, RadioGroup, CheckboxGroup]: ...
    def keys(self) -> List[str]: ...
    def items(
        self,
    ) -> List[Tuple[str, Union[_AnyInputElement, RadioGroup, CheckboxGroup]]]: ...

class InputMixin:
    name: Optional[str]  # setter: Optional[basestring]

class TextareaElement(InputMixin, HtmlElement):
    value: str

class SelectElement(InputMixin, HtmlElement):
    @property
    def value(self) -> Union[str, MultipleSelectOptions]: ...
    @value.setter  # Union[basestring, Collection[str]]
    def value(Self, value: Any) -> None: ...
    @property
    def multiple(self) -> bool: ...
    @multiple.setter  # anything truthy or falsy
    def multiple(self, value: Any) -> None: ...
    @property
    def value_options(self) -> List[str]: ...

class MultipleSelectOptions(MutableSet[str]):
    select: SelectElement
    def __init__(self, select: SelectElement) -> None: ...
    @property
    def options(self) -> Iterator[HtmlElement]: ...

class RadioGroup(List[InputElement]):
    value: Optional[str]
    @property
    def value_options(self) -> List[str]: ...

class CheckboxGroup(List[InputElement]):
    @property
    def value(self) -> CheckboxValues: ...
    @value.setter  # Iterable[str]
    def value(self, value: Any) -> None: ...
    @property
    def value_options(self) -> List[str]: ...

class CheckboxValues(MutableSet[str]):
    group: CheckboxGroup = ...
    def __init__(self, group: CheckboxGroup) -> None: ...

class InputElement(InputMixin, HtmlElement):
    type: str
    value: Optional[str]
    @property
    def checkable(self) -> bool: ...
    @property
    def checked(self) -> bool: ...
    @checked.setter
    def checked(self, value: Any) -> None: ...

class LabelElement(HtmlElement):
    for_element: Optional[HtmlElement]  # setter: None disallowed

# Encoding issue is similar to etree.tostring()
def tostring(
    doc: Union[etree._Element, etree._ElementTree],
    pretty_print: bool = ...,
    include_meta_content_type: bool = ...,
    encoding: Optional[Any] = ...,
    method: etree._OutputMethods = ...,
    with_tail: bool = ...,
    doctype: Optional[str] = ...,
) -> bytes: ...

# Intended for debugging only
# def open_in_browser(doc: Any, encoding: Optional[Any] = ...) -> None: ...

class HTMLParser(etree.HTMLParser): ...
class XHTMLParser(etree.XMLParser): ...

html_parser: HTMLParser
xhtml_parser: XHTMLParser

# Boils down to _BaseParser.makeelement()
def Element(
    _tag: _TextArg,
    attrib: Optional[SupportsItems[_TextArg, _TextArg]] = ...,
    nsmap: _NSMapArg = ...,
    **extra: _TextArg,
) -> HtmlElement: ...

# Calls etree.fromstring(html, parser, **kw) which has signature
# fromstring(text, parser, *, base_url)
def document_fromstring(
    html: basestring,
    parser: Optional[etree._BaseParser] = ...,
    ensure_head_body: bool = ...,
    *,
    base_url: Optional[str] = ...,
) -> HtmlElement: ...
def fragments_fromstring(
    html: basestring,
    no_leading_text: bool = ...,
    base_url: Optional[str] = ...,
    parser: Optional[etree._BaseParser] = ...,
    **kw: Any,
) -> List[_AnyHtmlElement]: ...
def fragment_fromstring(
    html: basestring,
    create_parent: bool = ...,
    base_url: Optional[str] = ...,
    parser: Optional[etree._BaseParser] = ...,
    **kw: Any,
) -> _AnyHtmlElement: ...
def fromstring(
    html: basestring,
    base_url: Optional[str] = ...,
    parser: Optional[etree._BaseParser] = ...,
    **kw: Any,
) -> _AnyHtmlElement: ...
def parse(
    filename_or_url: Any,
    parser: Optional[etree._BaseParser] = ...,
    base_url: Optional[str] = ...,
    **kw: Any,
) -> etree._ElementTree: ...
