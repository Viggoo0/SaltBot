import os
import discord
from dotenv import load_dotenv
from salt_client import SaltClient
import MetadataManager

metadata = MetadataManager.get_metadata()

# Load .env
load_dotenv()
if metadata["debug"]:
    print("### STARTING DEBUG BOT ###")
    TOKEN = os.getenv("DISCORD_DEBUG_TOKEN")
else:
    print("### STARTING BOT ###")
    TOKEN = os.getenv("DISCORD_TOKEN")

# Load opus library for better audio
discord.opus.load_opus("libopus.so.0")

# Start client
client = SaltClient()
client.run(TOKEN)
