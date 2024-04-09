from discord.ext import commands
import discord
import settings


class CommandLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        moderator_role = discord.utils.get(message.guild.roles, name="Me")  # wstaw role
        if message.content.startswith(settings.COMMAND_PREFIX) and moderator_role in message.author.roles:
            for command in self.bot.commands:
                if message.content.lower().startswith(f"{settings.COMMAND_PREFIX}{command.name.lower()}"):
                    my_channel = self.bot.get_channel(1164381123569270894)  # wpisz ID kanału
                    await my_channel.send(
                        f"Message: {message.content}\nChannel: {message.channel}\nAuthor: {message.author}")


# ctrl + alt + l

async def setup(bot):
    await bot.add_cog(CommandLogs(bot))
