import discord
from discord.ext import commands

import settings
from my_token import DISCORD_BOT_TOKEN

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=settings.COMMAND_PREFIX, intents=intents, activity=discord.Game(name="$help"))


# class CustomHelpCommand(commands.DefaultHelpCommand):
#     def get_command_signature(self, command):
#         return f"{settings.COMMAND_PREFIX}{command.qualified_name} {command.signature}"
#
#     async def send_bot_help(self, mapping):
#         embed = discord.Embed(title="Help", description="Commands:", color=discord.Color.blurple())
#         for cog, cmds in mapping.items():
#             if cog is not None:
#                 cog_name = cog.qualified_name if cog is not None else "No Category"
#                 embed.add_field(name=cog_name,
#                                 value="\n".join([f"{settings.COMMAND_PREFIX}{c.name} {c.brief}" for c in cmds]),
#                                 inline=False)
#         await self.get_destination().send(embed=embed)
#
#
# bot.help_command = CustomHelpCommand()


@bot.event
async def on_ready():
    cog_files = [cog_file for cog_file in settings.COG_DIR.glob('*.py') if cog_file.stem != '__init__']
    for cog_file in cog_files:
        await bot.load_extension(f"cogs.{cog_file.stem}")

    await bot.tree.sync()

    settings.on_ready_message(bot)


if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
