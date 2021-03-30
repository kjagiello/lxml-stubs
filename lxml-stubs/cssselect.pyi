import sys
from typing import List, Union

from ._types import _NonDefaultNSMapArg
from ._xpath import _XPathVarArg
from .etree import XPath, _Element, _ElementTree

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

_CSSTransArg = Union[LxmlTranslator, Literal["xml", "html", "xhtml"]]

# cssselect has no stub in typeshed or official repo as of March 2021
# include minimum stuff to make this file self-contained for now

class SelectorError(Exception): ...
class SelectorSyntaxError(SelectorError, SyntaxError): ...
class ExpressionError(SelectorError, RuntimeError): ...

class GenericTranslator:
    def css_to_xpath(self, css: str, prefix: str = ...) -> str: ...

class HTMLTranslator(GenericTranslator):
    def __init__(self, xhtml: bool = ...) -> None: ...

#
# end of cssselect inclusion
#

class LxmlTranslator(GenericTranslator): ...
class LxmlHTMLTranslator(LxmlTranslator, HTMLTranslator): ...

class CSSSelector(XPath):
    css: str = ...
    def __init__(
        self,
        css: str,  # byte str unaccepted, same for elem methods
        namespaces: _NonDefaultNSMapArg = ...,
        translator: _CSSTransArg = ...,
    ) -> None: ...
    # Request for input from experts in this area:
    # Is it correct to say, cssselect doesn't support pseudo elements,
    # and all selection results should be nodesets?
    def __call__(  # type: ignore[override]
        self,
        _etree_or_element: Union[_Element, _ElementTree],
        **_variables: _XPathVarArg,
    ) -> List[_Element]: ...
