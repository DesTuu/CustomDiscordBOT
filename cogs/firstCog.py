from discord.ext import commands
import discord


class FirstCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        member = ctx.author.nick
        """A simple command that responds with 'Hello!'"""
        await ctx.send(f"Hello {member}!")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if "help" in message.content:
            await message.add_reaction("☑️")


async def setup(bot):
    await bot.add_cog(FirstCog(bot))
