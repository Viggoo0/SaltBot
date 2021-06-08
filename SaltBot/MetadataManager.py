# -*- coding: utf-8 -*-
"""
    SaltBot.MetadataManager
    ~~~~~~~~~~~~~~~~~~~~~~~

    Module containing methods for interfacing with SaltBot metadata

    :copyright: (c) 2021 by Oskari Tuormaa.
    :license: MIT, see LICENSE for more details.
"""


import yaml
import os
import discord
from _dataclasses import Context, GuildSettings
from typing import Union


metadata_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "metadata.yaml")


def get_metadata() -> dict:
    """TODO: Docstring for get_metadata.
    Returns: TODO

    """
    with open(metadata_path, "r") as fd:
        metadata = yaml.safe_load(fd)

    return metadata


def save_metadata(metadata: dict):
    """TODO: Docstring for save_metadata.

    Args:
        metadata (dict): TODO

    Returns: TODO

    """
    with open(metadata_path, "w") as fd:
        yaml.safe_dump(metadata, fd)


def get_guild_settings(guild: discord.Guild) -> Union[GuildSettings, None]:
    """TODO: Docstring for get_guild_settings.

    Args:
        guild (discord.Guild): TODO

    Returns: TODO

    """
    metadata = get_metadata()

    if guild.id in metadata["guilds"]:
        temp: dict = metadata["guilds"][guild.id]

        # Clean up dict and remove convenience data
        temp["guild"] = guild
        temp.pop("guildName")

        return GuildSettings.from_dict(metadata["guilds"][guild.id])

    return GuildSettings.from_dict({"guild": guild})


def update_guild_settings(settings: GuildSettings) -> None:
    """TODO: Docstring for update_guild_settings.

    Args:
        guild (discord.Guild): TODO
        settings (dict): TODO

    Returns: TODO

    """
    metadata = get_metadata()

    temp = GuildSettings.to_dict(settings)

    # Clean up dict and add data for convenience
    temp.pop("guild")
    temp["guildName"] = settings.guild.name

    metadata["guilds"][settings.guild.id] = temp

    save_metadata(metadata)
