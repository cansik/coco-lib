from datetime import datetime
from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, config
from marshmallow import fields


@dataclass_json
@dataclass
class Info:
    year: int
    version: str
    description: str
    contributor: str
    url: str
    date_created: datetime = field(
        metadata=config(
            encoder=lambda d: d.strftime('%Y/%m/%d'),
            decoder=lambda s: datetime.strptime(s, '%Y/%m/%d'),
            mm_field=fields.DateTime(format='%Y/%m/%d')
        )
    )


@dataclass_json
@dataclass
class Image:
    id: int
    width: int
    height: int
    file_name: str
    license: int
    flickr_url: str
    coco_url: str
    date_captured: datetime = field(
        metadata=config(
            encoder=lambda d: d.strftime('%Y-%m-%d %H:%M:%S'),
            decoder=lambda s: datetime.strptime(s, '%Y-%m-%d %H:%M:%S'),
            mm_field=fields.DateTime(format='iso')
        )
    )
    

@dataclass_json
@dataclass
class License:
    id: int
    name: str
    url: str