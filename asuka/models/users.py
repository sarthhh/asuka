# MIT License

# Copyright (c) 2022 Sarthak

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from __future__ import annotations

import typing

from asuka.builders import DiscordObject


class PartialUser(DiscordObject):
    id: int
    username: str
    discriminator: str
    is_mfa_enabled: bool

    def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
        self.id = data["id"]
        self.username = data["username"]
        self.discriminator = data["discriminator"]
        self.mfa_enabled = data.get("mfa_enabled")

    def __repr__(self) -> str:
        return f"{self.username}#{self.discriminator}"

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, DiscordObject):
            raise NotImplemented
        return self.id == obj.id


class BotUser(PartialUser):
    ...
