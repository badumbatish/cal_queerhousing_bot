from discord.ext import commands

command_center_channel_id = 1111557645720096848

def setup_commands(bot):

    @bot.command()
    @commands.has_any_role("Oikos Controller")
    async def say_as_oikos(ctx, arg, channel_id = 1101196152809992264):

        target_channel = bot.get_channel(channel_id)

        if ctx.channel.id == command_center_channel_id:
            if(target_channel is not None):
                await target_channel.send(arg)
        else:
            await ctx.send("This command can only be used in the command-center")