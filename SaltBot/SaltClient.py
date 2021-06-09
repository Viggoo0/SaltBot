import discord
import MetadataManager
import DataManager
from DataClasses import GuildSettings, Context


class SaltClient(discord.Client):

    """ TODO: Docstring for SaltClient. """

    async def on_ready(self):
        """ TODO: docstring for on_ready"""
        print("Bot ready!")

    async def on_message(self, message):
        """ TODO: docstring for on_message_receive"""
        print(message)
