import discord
from discord.ext import commands
import app
import os

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=app.COMMAND_PREFIX, intents=intents, activity=discord.Game(name="Jestę Botę"))


@bot.event
async def on_ready():
    # for cmd_file in app.CMD_DIR.glob('*.py'):
    #     if cmd_file.name != '__init__.py':
    #         await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    await bot.load_extension("cogs.example")


if __name__ == "__main__":
    bot.run(os.environ['DISCORD_TOKEN'])

