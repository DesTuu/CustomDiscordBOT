from discord.ext import commands
from app import settings
import discord


class New_channel_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if isinstance(channel, discord.TextChannel) and "queue" in channel.name:
            await channel.send(settings.QUEUE_MESSAGE)

        if isinstance(channel, discord.TextChannel) and channel.category.name == "Weryfikacja":
            await channel.send(settings.WERYFIKACJA_MESSAGE)


async def setup(bot):
    await bot.add_cog(New_channel_message(bot))
