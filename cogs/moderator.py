import asyncio
from discord.ext import commands
import discord


# Zespół L(N)WT

def is_moderator():
    async def my_check(ctx):
        moderator_role = discord.utils.get(ctx.guild.roles, name="Me")
        if moderator_role in ctx.author.roles:
            return True
        else:
            await ctx.reply("Nie posiadasz uprawnień")
            return False

    return commands.check(my_check)


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief=f"Tylko Ty widzisz tą wiadomość"
    )
    @is_moderator()
    async def mute(self, ctx, muted_member: discord.Member, duration: int, unit: str):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                # if channel.category.name not in (
                #         "Odwołania", "Przyznanie kary", "Inne", "Administracja", "Organizacyjne"):
                await channel.set_permissions(muted_role, send_messages=False)

        await muted_member.add_roles(muted_role)
        await ctx.reply(f"{muted_member.mention} został wyciszony.")

        if unit == "s":
            await asyncio.sleep(duration)
        if unit == "m":
            await asyncio.sleep(duration * 60)
        if unit == "h":
            await asyncio.sleep(duration * 3600)
        if unit == "d":
            await asyncio.sleep(duration * 86_400)
        if unit == "w":
            await asyncio.sleep(duration * 604_800)
        if unit == "mo":
            await asyncio.sleep(duration * 2_629_746)
        if unit == "y":
            await asyncio.sleep(duration * 31_556_95)

        await muted_member.remove_roles(muted_role)
        await ctx.send(f"Okres wyciszenia użytkownika {muted_member.mention} minął.")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Podaj użytkownika, którego chcesz wyciszyć.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Nie masz wystarczających uprawnień do wykonania tej akcji.")


async def setup(bot):
    await bot.add_cog(Moderator(bot))
