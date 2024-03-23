from discord.ext import commands
import random


class Hybrid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def lottery(self, ctx):
        member = ctx.author.nick
        x = random.choice(range(100))
        if x > 50:
            await ctx.send(f"Congratulations {member}! You have won free VIP on our server!")
        else:
            await ctx.send(f"Sorry {member}... You didn't won this time... Try again tomorrow!")


async def setup(bot):
    await bot.add_cog(Hybrid(bot))
