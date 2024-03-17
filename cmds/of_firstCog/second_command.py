from discord.ext import commands
import discord


@commands.command()
async def hello22(self, ctx, *, member: discord.Member):
    await ctx.send(f'Hi {member.name}22')


async def setup(bot):
    await bot.add_command(hello)