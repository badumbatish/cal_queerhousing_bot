def setup_events(bot):
    async def on_ready(bot):
        print(f'Logged in as {bot.user.name}')
        print('------')