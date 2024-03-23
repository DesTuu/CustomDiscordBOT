import pathlib

COMMAND_PREFIX = f"$"

BASE_DIR = pathlib.Path(__file__).parent

COG_DIR = BASE_DIR / "cogs"


def get_guild_names(bot):
    for i in bot.guilds:
        yield i.name


def on_ready_message(bot):
    if len(set(get_guild_names(bot))) >= 2:
        print(f"Bot znajduje się na takich serwerach jak: {', '.join(get_guild_names(bot))}")
    else:
        print(f"Bot znajduje się na tylko na jednym serwerze: {', '.join(get_guild_names(bot))}")
