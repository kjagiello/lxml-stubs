import sys
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

# typing.AnyStr WILL be used in multiple places like string replace
# or attribute handling, where input and output ARE related.
# Previous naming of _AnyStr would be recipe for hard to discover
# typo. Borrow basestring name from Python2 here.

if sys.version_info > (3,):
    basestring = Union[str, bytes]

_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]
_NSMap = Union[Dict[Union[bytes, None], bytes], Dict[Union[str, None], str]]
_OptionalNamespace = Optional[Mapping[str, Any]]
