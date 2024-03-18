from discord.ext import commands


class Quiet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief=f"Nie dostaniesz pingu od tej wiadomości"
    )
    async def silent(self, ctx):
        await ctx.message.reply(f"{ctx.message.author.mention} won!", silent=True)

    @commands.command(
        brief=f"Tylko Ty widzisz tą wiadomość"
    )
    async def reply(self, ctx):
        await ctx.reply('Hello')


async def setup(bot):
    await bot.add_cog(Quiet(bot))
