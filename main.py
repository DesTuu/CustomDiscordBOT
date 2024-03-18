import discord
from discord.ext import commands

import settings
import settings as app
from my_token import DISCORD_BOT_TOKEN

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=app.COMMAND_PREFIX, intents=intents, activity=discord.Game(name="Jestę Botę"))


class CustomHelpCommand(commands.DefaultHelpCommand):
    def get_command_signature(self, command):
        return f"{app.COMMAND_PREFIX}{command.qualified_name} {command.signature}"

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", description="Commands:", color=discord.Color.blurple())
        for cog, commands in mapping.items():
            if cog is not None:
                cog_name = cog.qualified_name if cog is not None else "No Category"
                embed.add_field(name=cog_name,
                                value="\n".join([f"{settings.COMMAND_PREFIX}{c.name}: {c.brief}" for c in commands]),
                                inline=False)
        await self.get_destination().send(embed=embed)


bot.help_command = CustomHelpCommand()


@bot.event
async def on_ready():
    cog_files = [cog_file for cog_file in app.COG_DIR.glob('*.py') if cog_file.stem != '__init__']
    for cog_file in cog_files:
        await bot.load_extension(f"cogs.{cog_file.stem}")


if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
