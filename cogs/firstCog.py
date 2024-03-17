from discord.ext import commands
import settings as app


class FirstCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello1(self, ctx):
        """A simple command that responds with 'Hello!'"""
        await ctx.send("Hello1!")


async def setup(bot):
    await bot.add_cog(FirstCog(bot))
