from sound import Sound
from player import Player
from metadata import GuildSettings

class SoundManager(object):

    """Docstring for SoundManager. """

    @staticmethod
    def setSoundDir(soundDir: str):
        """TODO: Docstring for setSoundDir.

        Args:
            soundDir (str): TODO

        Returns: TODO

        """
        pass

    @staticmethod
    def getSound(self, name: str) -> Sound:
        """TODO: Docstring for getSound.

        Args:
            name (str): TODO

        Returns: TODO

        """
        pass

class PlayerManager(object):

    """Docstring for PlayerManager. """

    def __init__(self):
        """TODO: to be defined. """
        self._players: Dict[int, Player]

    def getPlayer(self, guildID: int) -> Player:
        """TODO: Docstring for getPlayer.

        Args:
            guildID (int): TODO

        Returns: TODO

        """
        pass

class MetadataManager(object):

    """Docstring for MetadataManager. """

    @staticmethod
    def getGuildSettings(guildID: int) -> GuildSettings:
        """TODO: Docstring for getGuildSettings.

        Args:
            guildID (int): TODO

        Returns: TODO

        """
        pass

    @staticmethod
    def updateGuildSettings(guildID: int, newSettings: GuildSettings):
        """TODO: Docstring for updateGuildSettings.

        Args:
            guildID (int): TODO
            newSettings (GuildSettings): TODO

        Returns: TODO

        """
        pass

    @staticmethod
    def getMetadata():
        """TODO: Docstring for getMetadata.
        Returns: TODO

        """
        pass
