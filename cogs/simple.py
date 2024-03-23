from discord.ext import commands


class Simple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='survey',
        aliases=['s'],
        brief=f"treśćankiety - niech zagłosują za lub przeciw w ankiecie",
        enabled=True,
        hidden=False,
    )
    async def survey(self, ctx, *message):
        message = await ctx.send(" ".join(message))
        await ctx.message.delete()
        await message.add_reaction("\U00002705")
        await message.add_reaction("❔")
        await message.add_reaction("\U0000274c")


async def setup(bot):
    await bot.add_cog(Simple(bot))
