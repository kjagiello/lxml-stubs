from typing import Any, Callable, Mapping, Optional, Type, TypeVar

from ._types import basestring
from .etree import _Element

_T = TypeVar("_T")

class ElementMaker:
    def __init__(
        self,
        typemap: Optional[Mapping[Type[_T], Callable[[_Element, _T], None]]] = ...,
        namespace: Optional[str] = ...,
        nsmap: Optional[Mapping[Optional[basestring], basestring]] = ...,
        # makeelement is callable of same arg as etree.Element()
        makeelement: Optional[Callable[..., _Element]] = ...,
    ) -> None: ...
    def __call__(
        self,
        tag: str,
        # Although default ElementMaker only accepts _Element and types
        # interpretable by default typemap (that is str, CDATA and dict)
        # as children, typemap can be expanded to make sure item of any
        # type is accepted. So it can't be typed.
        *children: Any,
        **attrib: basestring,
    ) -> _Element: ...
    # __getattr__ here is special. ElementMaker is a factory that generates
    # element of *any* tag, as long as tag name does not conflict with basic
    # object methods (yes, including python keywords like "class" and "for",
    # which are common in HTML)
    def __getattr__(self, name: str) -> Callable[..., _Element]: ...

E: ElementMaker = ...
