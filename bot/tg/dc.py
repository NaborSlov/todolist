from dataclasses import dataclass
from typing import List

import marshmallow
import marshmallow_dataclass


@dataclass
class MessageFrom:
    id: int
    is_bot: bool
    first_name: str
    username: str

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class Chat:
    id: int
    username: str
    first_name: str
    type: str

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class Message:
    message_id: int
    date: int
    text: str
    from_: MessageFrom
    chat: Chat

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class UpdateObj:
    update_id: int
    message: Message

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]

    class Meta:
        unknown = marshmallow.EXCLUDE


get_updates_schema = marshmallow_dataclass.class_schema(GetUpdatesResponse)
send_message_schema = marshmallow_dataclass.class_schema(SendMessageResponse)
