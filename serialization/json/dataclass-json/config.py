from dataclasses import dataclass, field, Field
from dataclasses_json import config, cfg, dataclass_json, LetterCase, Undefined
from datetime import datetime
from marshmallow import fields
from typing import Optional


# We have to do this it this way since datetime.isoformat and datetime.formisoformat
# don't handle None.
def to_iso(dt: datetime) -> str | None:
    return datetime.isoformat(dt) if (dt is not None) else None


def from_iso(text: str) -> datetime | None:
    return datetime.fromisoformat(text) if (text is not None) else None


# We need to pass the encoder and decoder to dataclass_json.
#
# See https://github.com/lidatong/dataclasses-json#Overriding
# Note:
# One annoying thing about dataclass-json is that it doesn't skip a field if it's None during
# json encoding. This results in `{... "scheduledShutdown": null, ...}`.
def datetime_converter() -> Field | None:
    return field(
        default=None,
        metadata=config(
            encoder=to_iso,
            decoder=from_iso,
            mm_field=fields.DateTime(format='iso'),
            exclude=lambda x: x is None,
        )
    )


cfg.global_config.encoders


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DbConfig(object):
    username: str
    password: str
    host:     Optional[str] = None  # Marks the host attribute as optional
    db:       Optional[str] = None  # Marks the db attribute as optional


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Config(object):
    debug: bool
    db_config: DbConfig
    scheduled_shutdown: Optional[datetime] = datetime_converter()
    scheduled_boot: Optional[datetime] = datetime_converter()

