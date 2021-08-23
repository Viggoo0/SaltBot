from dataclasses import dataclass

@dataclass
class GuildSettings(object):

    """Docstring for GuildSettings. """

    guildID: int
    helpChannelName: str
    isHelpChannel: bool

