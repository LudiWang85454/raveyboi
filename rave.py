# External imports
import asyncio
import os
import discord
from rave_music import get_song
from discord.ext.commands import Bot
from dotenv import load_dotenv

# No internal imports

client = Bot(command_prefix='!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER = os.getenv('USER_IS_GONE')


@client.event
async def on_voice_state_update(member, before, after):
    if str(member) == USER:
        if before.channel and not after.channel:
            channel = before.channel
            voice_player = await channel.connect()
            voice_player.play(discord.FFmpegPCMAudio('crab_rave.mp3'))
            player.start()

client.run(TOKEN)
