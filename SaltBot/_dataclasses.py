import discord
from dataclasses import dataclass, MISSING
from typing import List, Union


@dataclass
class Context:

    """ TODO: Docstring for Context. """

    message: str
    author: discord.User
    args: List[str]
    guild: discord.Guild
    textCh: discord.TextChannel
    voiceCh: Union[None, discord.VoiceChannel]


@dataclass
class GuildSettings:

    """ TODO: Docstring for GuildSettings. """

    isHelpCh: bool
    guild: discord.Guild
    helpChName: str = "SaltBotHelp"

    @staticmethod
    def from_dict(source: dict) -> "GuildSettings":
        """TODO: Docstring for from_dict.

        Args:
            source (dict): TODO

        Returns: TODO

        """
        fields = GuildSettings.__dataclass_fields__

        # Initialize keys not in source
        for k in [k for k in fields.keys() if k not in source]:
            if fields[k].default is MISSING:
                source[k] = fields[k].type()
            else:
                source[k] = fields[k].default

        # Trim source to only include relevant keys
        source = { k: source[k] for k in fields.keys() }

        return GuildSettings(**source)

    @staticmethod
    def to_dict(source: "GuildSettings") -> dict:
        """TODO: Docstring for to_dict.

        Args:
            source (GuildSettings): TODO

        Returns: TODO

        """
        return source.__dict__.copy()
