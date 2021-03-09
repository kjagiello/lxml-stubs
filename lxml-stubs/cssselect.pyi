from typing import Any, Dict, List, Optional, Union

from lxml import etree

from ._types import _DictAnyStr

# dummy for missing stubs
def __getattr__(name) -> Any: ...

class CSSSelector(etree.XPath):
    def __init__(
        self, css: str, namespaces: Optional[_DictAnyStr] = ..., translator: str = ...
    ): ...
    def __call__(self, element: etree._Element) -> List[etree._Element]: ...
