from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class DbConfig(JSONWizard):
    username: str
    password: str
    host:     str = None  # Marks the host attribute as optional
    db:       str = None  # Marks the db attribute as optional


@dataclass
class Config(JSONWizard):
    debug: bool
    db_config: DbConfig

    class _(JSONWizard.Meta):
        skip_defaults = True    # Allows fields to be omitted if the field have default values
