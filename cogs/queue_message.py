from discord.ext import commands

class Queue_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        # guild_id = "979427975692947546"
        if "queue" in channel.name:
            await channel.send("Przykładowa wiadomość")

async def setup(bot):
    await bot.add_cog(Queue_message(bot))
