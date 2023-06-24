from dataclasses import dataclass, field, Field, MISSING
from dataclasses_json import config, dataclass_json, LetterCase
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
def datetime_field(null: bool = True) -> Field | None:
    f = field(
        default=None if null else MISSING,
        metadata=config(
            encoder=to_iso,
            decoder=from_iso,
            mm_field=fields.DateTime(format='iso'),
            exclude=lambda x: x is None,
        ),
    )

    return f


def null_field() -> Field | None:
    return field(
        default=None,
        metadata=config(
            exclude=lambda x: x is None,
        )
    )

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DbConfig(object):
    username: str
    password: str
    host:     Optional[str] = null_field()  # Marks the host attribute as optional
    db:       Optional[str] = null_field()  # Marks the db attribute as optional


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Config(object):
    debug: bool
    db_config: DbConfig
    created_at: datetime = datetime_field(null=False)  # Required field
    scheduled_shutdown: Optional[datetime] = datetime_field()
    scheduled_boot: Optional[datetime] = datetime_field()
    # If we declare the following filed as Optional[str] = None, we will get
    # {... "telemetryHost": null ...} in the json object. We need to omit
    # this field in json if its value is None.
    # So instead of this `telemetry_host: Optional[str] = None`, do the following:
    telemetry_host: Optional[str] = null_field()

