from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

# We do *not* want `typing.AnyStr` because it is a `TypeVar`, which is an
# unnecessary constraint. It seems reasonable to constrain each
# List/Dict argument to use one type consistently, though, and it is
# necessary in order to keep these brief.
_AnyStr = Union[str, bytes]

_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]
_NSMap = Union[Dict[Union[bytes, None], bytes], Dict[Union[str, None], str]]
_OptionalNamespace = Optional[Mapping[str, Any]]
