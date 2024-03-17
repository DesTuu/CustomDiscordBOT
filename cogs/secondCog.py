from discord.ext import commands


class SecondCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello2(self, ctx):
        """A simple command that responds with 'Hello!'"""
        await ctx.send("Hello2!")


async def setup(bot):
    await bot.add_cog(SecondCog(bot))
