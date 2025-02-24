from typing_extensions import Literal

from ._types import _NonDefaultNSMapArg, _XPathVarArg
from .etree import XPath, _Element, _ElementOrTree

_CSSTransArg = LxmlTranslator | Literal["xml", "html", "xhtml"]

class SelectorError(Exception): ...
class SelectorSyntaxError(SelectorError, SyntaxError): ...
class ExpressionError(SelectorError, RuntimeError): ...

# Cssselect has never had stub in typeshed or official repo.
# Only include the bare minimum init argument to make following
# classes self-contained, as long as users are not creating
# customized translators.
class LxmlTranslator: ...

class LxmlHTMLTranslator(LxmlTranslator):
    def __init__(self, xhtml: bool = ...) -> None: ...

class CSSSelector(XPath):
    # Although 'css' is implemented as plain attribute, it is
    # meaningless to modify it, because instance is initialized
    # with translated XPath expression, not the CSS expression.
    # Allowing attribute modification would cause confusion as
    # CSS expression and the underlying XPath expression don't
    # match.
    @property
    def css(self) -> str: ...
    def __init__(
        self,
        css: str,
        namespaces: _NonDefaultNSMapArg | None = ...,
        translator: _CSSTransArg = ...,
    ) -> None: ...
    def __call__(  # type: ignore[override]
        self,
        _etree_or_element: _ElementOrTree,
        **_variables: _XPathVarArg,
    ) -> list[_Element]: ...  # XPath() returns XPathObject
