from dataclasses import dataclass
import lyra.parser
from lyra.common import MISSING_IMPLEMENTATION, TODO
from abc import ABC as AbstractBaseClass, abstractmethod
from typing import Generic, TypeVar, Optional, Any, cast
from collections.abc import Iterable
from lyra.parser import (
    BaseParamType,
    ParamType,
    Object,
    Option
)


T = TypeVar('T') # Tipo del objeto a transformar
P = TypeVar('P') # Tipo del parámetro devuelto

# x: Option[T] | T -> T
def unwrap_if_option(x: Option | Any) -> Any:
    return x.value if isinstance(x, Option) else x

STRING_PARAM_TYPES = {
    lyra.parser.StringChoiceWidget,
    lyra.parser.StringListArrayWidget,
    lyra.parser.StringListWidget
}

class Transformer(AbstractBaseClass, Generic[T, P]):
    @classmethod
    @abstractmethod
    def transform(cls, obj: T) -> P:
        MISSING_IMPLEMENTATION()

@dataclass
class Parameter:
    name: str
    innertype: type | str
    default: any
    required: bool
    valid_values: Optional[Iterable[Any]] = None
    bound: Optional[str] = None

    def __str__(self):
        if isinstance(self.innertype, type):
            innertype_str = self.innertype.__name__
        else:
            innertype_str = self.innertype

        if self.default is None and not self.required:
            innertype_str = f"Optional[{innertype_str}]"

        if (self.default is not None 
            or (self.default is None and not self.required)):
            default_str = f" = {repr(self.default)}"
        else:
            default_str = ""

        if self.bound:
            return f"{self.name}: {innertype_str}{default_str}@{self.bound}"
        return f"{self.name}: {innertype_str}{default_str}"
    

global AVAILABLE_TRANSFORMERS
AVAILABLE_TRANSFORMERS = dict()

class ParamTypeTransformer(Transformer[ParamType, Parameter]):
    def __init_subclass__(cls):
        AVAILABLE_TRANSFORMERS[cls.__name__] = cls
        return super().__init_subclass__()
    

MISSING_TRANSFORMER_DATACLASS_OPTIONS = dict(
      init        = True
    , repr        = True
    , eq          = True
    , order       = False
    , unsafe_hash = True
    , frozen      = False
    , match_args  = True
    , kw_only     = False
    , slots       = False
)

@dataclass(**MISSING_TRANSFORMER_DATACLASS_OPTIONS)
class MissingTransformer:
    transformer_name: str
    data: Optional[Any] = None

def transform_node(x: ParamType, **transform_kwargs) -> MissingTransformer | Parameter:
    transformer_name = type(x).__name__ + 'Transformer'
    transformer = AVAILABLE_TRANSFORMERS.get(transformer_name, None)

    if not transformer:
        return MissingTransformer(transformer_name, data=x)
    
    return transformer.transform(x, **transform_kwargs)

def transform_form(form: list[ParamType]) -> list[MissingTransformer | Parameter]:
    return [
        str(y)
        for x in form
        
        # Algunas transformaciones (como la de ExclusiveGroupWidget) pueden
        # mutar la lista. Que los pise con 'None' significa que los consumió
        # y son children de algún tipo superior.
        if x is not None
        for y in (transform_node(x, tree=form), )

        # Algunas funciones pueden devolver None, por lo que se filtran.
        if y is not None
    ]

class StringListWidgetTransformer(ParamTypeTransformer):
    @classmethod
    def transform(cls, obj: ParamType, **_) -> Parameter:
        assert isinstance(obj, lyra.parser.StringListWidget)
        return Parameter(
            name = obj.name,
            innertype = str,
            default = obj.default.value if obj.default else None,
            required = obj.required,
            valid_values = [x.value for x in obj.options]
        )
    
class StringListArrayWidgetTransformer(ParamTypeTransformer):
    @classmethod
    def transform(cls, obj: ParamType, **_) -> Parameter:
        assert isinstance(obj, lyra.parser.StringListArrayWidget)
        return Parameter(
            name = obj.name,
            innertype = str,
            default = None, # TODO: Are there any StringListArrays with 'default'?
            required = obj.required,
            valid_values = [
                unwrap_if_option(x)
                for g in obj.groups
                for x in g.options
            ]
        )
    
class FreeEditionWidgetTransformer(ParamTypeTransformer):
    @classmethod
    def transform(cls, obj: ParamType, **_) -> Parameter:
        assert isinstance(obj, lyra.parser.FreeEditionWidget)
        return Parameter(
            name = obj.name,
            innertype = str,
            default = None,
            required = False
        )

class ExclusiveGroupWidgetTransformer(ParamTypeTransformer):
    @classmethod
    def transform(cls, obj: ParamType, tree: list[ParamType], **_) -> Parameter:
        assert isinstance(obj, lyra.parser.ExclusiveGroupWidget)
        children = dict()
        for i, child in enumerate(tree):
            if child.name not in obj.children:
                continue

            children[child.name] = (
                child if issubclass(type(child), BaseParamType) else
                transform_node(child, parent=cls)
            )

            tree[i] = None # Piso el valor para indicar que fue consumido.

        innertypes = [None for _ in obj.children]
        
        for i, child in enumerate(children):
            typename = type(children[child]).__name__.split('Widget')[0]
            typename += 'Type'
            innertypes[i] = typename

        innertype = 'Union[' + ', '.join(innertypes) + ']'

        default = children.get(obj.default, None)
        if default is not None:
            default = default.name

        return Parameter(
            name = obj.name,
            innertype = innertype,
            default = default,
            required = False,
        )


class StringChoiceWidgetTransformer(ParamTypeTransformer):
    @classmethod
    def transform(cls, obj: ParamType, **_) -> Parameter:
        assert isinstance(obj, lyra.parser.StringChoiceWidget)
        return Parameter(
            name = obj.name,
            innertype = str,
            default = obj.default.value if obj.default else None,
            required = obj.required,
            valid_values = [x.value for x in obj.options]
        )


class LicenceWidgetTransformer(ParamTypeTransformer):
    @classmethod
    def transform(cls, obj: ParamType, tree: list[ParamType], **_) -> Parameter:
        assert isinstance(obj, lyra.parser.LicenceWidget)
        return None