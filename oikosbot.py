# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()


import event_handlers
import oikos_commands
import oikos_messages
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

command_center_channel_id = 1111557645720096848

event_handlers.setup_events(bot)
oikos_commands.setup_commands(bot)
oikos_messages.setup_messages(bot)


# Assume client refers to a discord.Client subclass...
bot.run(os.getenv('TOKEN'))
