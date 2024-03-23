from discord.ext import commands
from app import messages
import discord


class NewChannelMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if isinstance(channel, discord.TextChannel) and "queue" in channel.name:
            await channel.send(messages.QUEUE_MESSAGE)

        if isinstance(channel, discord.TextChannel) and channel.category.name == "Weryfikacja":
            await channel.send(messages.WERYFIKACJA_MESSAGE)


async def setup(bot):
    await bot.add_cog(NewChannelMessage(bot))
