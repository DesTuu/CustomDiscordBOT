import discord
from discord.ext import commands

import settings
from my_token import DISCORD_BOT_TOKEN

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=settings.COMMAND_PREFIX, intents=intents, activity=discord.Game(name="/help"))

bot.remove_command('help')


@commands.hybrid_command(brief=f"Wyświetla wszystkie komendy i ich opisy")
async def help(ctx: commands.Context) -> None:
    embed = discord.Embed(title="Dostępne Komendy", color=discord.Color.blue())
    commands_sorted = sorted(bot.commands, key=lambda cmd: cmd.name)
    for command in commands_sorted:
        if not command.hidden and command.name != 'help':
            embed.add_field(name=f"{command.name}", value=command.brief, inline=False)
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    cog_files = [cog_file for cog_file in settings.COG_DIR.glob('*.py') if cog_file.stem != '__init__']
    for cog_file in cog_files:
        await bot.load_extension(f"cogs.{cog_file.stem}")
    bot.add_command(help)

    await bot.tree.sync()

    settings.on_ready_message(bot)


if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
