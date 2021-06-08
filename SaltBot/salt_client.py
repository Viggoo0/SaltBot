import discord
import MetadataManager
from _dataclasses import GuildSettings, Context


class SaltClient(discord.Client):

    """Docstring for SaltClient. """

    async def on_ready(self):
        """docstring for on_ready"""
        print("Bot ready!")

    async def on_message(self, message):
        """docstring for on_message_receive"""
        print(message)
