from _typeshed import Incomplete

class PostBucketRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        org_id: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        rp: Incomplete | None = ...,
        retention_rules: Incomplete | None = ...,
        schema_type: Incomplete | None = ...,
    ) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def rp(self): ...
    @rp.setter
    def rp(self, rp) -> None: ...
    @property
    def retention_rules(self): ...
    @retention_rules.setter
    def retention_rules(self, retention_rules) -> None: ...
    @property
    def schema_type(self): ...
    @schema_type.setter
    def schema_type(self, schema_type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
