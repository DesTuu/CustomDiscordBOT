from discord.ext import commands
import discord


@commands.command()
async def hello(self, ctx, *, member: discord.Member):
    await ctx.send(f'Hi {member.name}3')


async def setup(bot):
    await bot.add_command(hello)