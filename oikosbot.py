# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()


import event_handlers

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

command_center_channel_id = 1111557645720096848

event_handlers.setup_events(bot)

@bot.command()
@commands.has_any_role("Oikos Controller")
async def say_as_oikos(ctx, arg, channel_id = 1101196152809992264):

    target_channel = bot.get_channel(channel_id)

    if ctx.channel.id == command_center_channel_id:
        if(target_channel is not None):
            await target_channel.send(arg)
    else:
        await ctx.send("This command can only be used in the command-center")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)


# Assume client refers to a discord.Client subclass...
bot.run(os.getenv('TOKEN'))
