from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from datetime import datetime
from typing import Optional

# See https://github.com/rnag/dataclass-wizard

@dataclass
class DbConfig(JSONWizard):
    username: str
    password: str
    host:     Optional[str] = None  # Marks the host attribute as optional
    db:       Optional[str] = None  # Marks the db attribute as optional


@dataclass
class Config(JSONWizard):
    debug: bool
    db_config: DbConfig
    scheduled_shutdown: Optional[datetime] = None
    scheduled_boot: Optional[datetime] = None

    class _(JSONWizard.Meta):
        skip_defaults = True    # Allows fields to be omitted if the field have default values
        key_transform_with_dump = 'SNAKE'   # JSONWizard uses camelCase when encoding to json
        key_transform_with_load = 'SNAKE'
