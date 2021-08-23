import discord

from player import Player

class Sound(object):

    """Docstring for Sound. """

    def __init__(self, path: str):
        """TODO: to be defined.

        Args:
            path (str): TODO


        """
        self._path = path

    def play(self, vc: discord.VoiceChannel, player: Player):
        """TODO: Docstring for play.

        Args:
            vc (discord.VoiceChannel): TODO
            player (Player): TODO

        Returns: TODO

        """
        pass

