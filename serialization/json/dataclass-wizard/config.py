from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class DbConfig(JSONWizard):
    username: str
    password: str
    host:     str = None  # Assign a default value to mark the host field in json optional
    db:       str = None  # Assign a default value to mark the host field in json optional


@dataclass
class Config(JSONWizard):
    debug: bool
    db_config: DbConfig

    class _(JSONWizard.Meta):
        skip_defaults = True    # Allows fields to be omitted if the field have default values
