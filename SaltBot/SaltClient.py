import discord
import MetadataManager
import DataManager
from DataClasses import GuildSettings, Context
from Player import Player


class SaltClient(discord.Client):

    """ TODO: Docstring for SaltClient. """

    async def on_ready(self):
        """ TODO: docstring for on_ready"""
        print("Bot ready!")

        guild: discord.Guild = self.guilds[0]
        channel = guild.voice_channels[0]

        player = Player(channel)
        player.connect()

    async def on_message(self, message):
        """ TODO: docstring for on_message_receive"""
        print(message)
