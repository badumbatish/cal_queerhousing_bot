
def setup_messages(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        await bot.process_commands(message)