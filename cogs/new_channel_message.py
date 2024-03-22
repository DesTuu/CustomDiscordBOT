from discord.ext import commands

class New_channel_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if "queue" in channel.name:
            await channel.send("Przykładowa wiadomość")

        if channel.category.name == "Weryfikacja":
            await channel.send("Nowy kanał w kategorii Weryfikacja")

async def setup(bot):
    await bot.add_cog(New_channel_message(bot))
