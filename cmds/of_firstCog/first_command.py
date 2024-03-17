from discord.ext import commands
import discord

@commands.command()
async def hello11(self, ctx, *, member: discord.Member):
    await ctx.send(f'Hi {member.name}11')

async def setup(bot):
    bot.add_command(hello)