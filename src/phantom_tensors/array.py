# pyright: strict
from typing import TYPE_CHECKING, Any, Tuple

import typing_extensions as _te
from typing_extensions import Protocol, runtime_checkable

from phantom_tensors._internals import check

from ._internals import check

__all__ = ["SupportsArray"]


Shape = _te.TypeVarTuple("Shape")


@runtime_checkable
class SupportsArray(Protocol[_te.Unpack[Shape]]):

    if not TYPE_CHECKING:
        _cache = {}

        @classmethod
        def __class_getitem__(cls, key):
            if not isinstance(key, tuple):
                key = (key,)

            class PhantomHasShape:
                __bound__ = (object,)
                __args__ = key

                def __array__(self) -> Any:
                    ...

                def shape(self) -> Tuple[int, ...]:
                    ...

                @classmethod
                def __instancecheck__(cls, __instance: Any) -> bool:
                    return check(key, __instance.shape)

            return PhantomHasShape

    def __array__(self) -> Any:
        ...

    @property
    def shape(self) -> Tuple[_te.Unpack[Shape]]:
        ...
