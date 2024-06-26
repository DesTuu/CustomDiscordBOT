import asyncio
from discord.ext import commands
import discord
from app import messages

possible_units = ['s', 'm', 'h', 'd', 'w', 'mo', 'y']


def is_moderator():
    async def my_check(ctx):
        moderator_role = discord.utils.get(ctx.guild.roles, name="Zespół RedSide")
        if moderator_role in ctx.author.roles:
            return True
        else:
            await ctx.send("Nie posiadasz uprawnień", ephemeral=True)
            return False

    return commands.check(my_check)


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        brief=f"Wycisza użytkownika: /mute @Alcia 10 m Powód, unit = jednostki po ang.: s, m, h, d, w, mo, y"
    )
    @is_moderator()
    async def mute(self, ctx: commands.Context, muted_member: discord.Member, duration: int, unit: str, reason: str):
        if unit in possible_units:
            muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
            await muted_member.add_roles(muted_role)

            if muted_member:
                await ctx.send(f"{muted_member} został/a wyciszony/a na {duration}{unit},\npowód: {reason}",
                               ephemeral=True)
                await muted_member.send(
                    f"Zostałeś/aś wyciszony na {duration}{unit}.\nPowód: {reason} \n"
                    f"Kara wystawiona przez: {ctx.author} \n\n{messages.KARA_MESSAGE}")

            if unit == "s":
                await asyncio.sleep(duration)
            elif unit == "m":
                await asyncio.sleep(duration * 60)
            elif unit == "h":
                await asyncio.sleep(duration * 3600)
            elif unit == "d":
                await asyncio.sleep(duration * 86_400)
            elif unit == "w":
                await asyncio.sleep(duration * 604_800)
            elif unit == "mo":
                await asyncio.sleep(duration * 2_629_746)
            elif unit == "y":
                await asyncio.sleep(duration * 31_556_95)

            await muted_member.remove_roles(muted_role)

        else:
            await ctx.send("**Błąd! Jednostka (unit), którą wpisałeś jest niepoprawna! Użyj: s, m, h, d, w, mo lub y**",
                           ephemeral=True)

    @commands.hybrid_command(
        brief=f"Daje warna: /warn @Alcia Powód"
    )
    @is_moderator()
    async def warn(self, ctx: commands.Context, warned_member: discord.Member, reason: str):
        warn1_role = discord.utils.get(ctx.guild.roles, name="warn - 1")
        warn2_role = discord.utils.get(ctx.guild.roles, name="warn - 2")
        timeout_role = discord.utils.get(ctx.guild.roles, name="TIMEOUT")

        if warn1_role in warned_member.roles and warn2_role not in warned_member.roles:
            await warned_member.add_roles(warn2_role)
            if warned_member:
                await ctx.send(f"{warned_member} Warned 2, powód: {reason}", ephemeral=True)
                await warned_member.send(
                    f"Warned 2, \nPowód: {reason} \nKara wystawiona przez: {ctx.author} \n\n{messages.KARA_MESSAGE}")
        elif warn1_role in warned_member.roles and warn2_role in warned_member.roles:
            await warned_member.add_roles(timeout_role)
            if warned_member:
                await ctx.send(f"{warned_member} Timeout, powód: {reason}", ephemeral=True)
                await warned_member.send(
                    f"Cześć, ze względu na otrzymanie trzeciego warna zostałeś wysłany na 48h przerwy.  \n"
                    f"Powód: {reason} \nKara wystawiona przez: {ctx.author} \n\n{messages.KARA_MESSAGE}")
            await warned_member.remove_roles(warn1_role)
            await warned_member.remove_roles(warn2_role)
            await asyncio.sleep(172800)  # czas po jakim ma być usuwana ranga timeout, ustawione na 48h
            await warned_member.remove_roles(timeout_role)
        elif timeout_role in warned_member.roles:
            await ctx.send(f"Błąd! Użytkownik posiada już rangę Timeout!", ephemeral=True)
        else:
            await warned_member.add_roles(warn1_role)
            if warned_member:
                await ctx.send(f"{warned_member} Warned 1, powód: {reason}", ephemeral=True)
                await warned_member.send(
                    f"Cześć, otrzymałeś pierwszego warna. \nPowód: {reason} \n"
                    f"Kara wystawiona przez: {ctx.author} \n\n{messages.KARA_MESSAGE}")

    @commands.hybrid_command(
        brief=f"Daje timeouta od razu: /timeout @Alcia Powód, unit = jednostki po ang.: s, m, h, d, w, mo, y"
    )
    @is_moderator()
    async def timeout(self, ctx: commands.Context, t_member: discord.Member, t_duration: int, t_unit: str, reason: str):
        if t_unit in possible_units:
            timeout_role = discord.utils.get(ctx.guild.roles, name="TIMEOUT")
            warn1_role = discord.utils.get(ctx.guild.roles, name="warn - 1")
            warn2_role = discord.utils.get(ctx.guild.roles, name="warn - 2")

            if warn1_role in t_member.roles:
                await t_member.remove_roles(warn1_role)
            if warn2_role in t_member.roles:
                await t_member.remove_roles(warn2_role)

            await t_member.add_roles(timeout_role)
            await ctx.send(f"{t_member} Timeout, powód: {reason}", ephemeral=True)
            await t_member.send(
                f"Cześć, utraciłeś dostęp do kanałów.\nPowód: {reason} \n"
                f"Kara wystawiona przez: {ctx.author} \n\n{messages.KARA_MESSAGE}")

            if t_unit == "s":
                await asyncio.sleep(t_duration)
            elif t_unit == "m":
                await asyncio.sleep(t_duration * 60)
            elif t_unit == "h":
                await asyncio.sleep(t_duration * 3600)
            elif t_unit == "d":
                await asyncio.sleep(t_duration * 86_400)
            elif t_unit == "w":
                await asyncio.sleep(t_duration * 604_800)
            elif t_unit == "mo":
                await asyncio.sleep(t_duration * 2_629_746)
            elif t_unit == "y":
                await asyncio.sleep(t_duration * 31_556_95)

            await t_member.remove_roles(timeout_role)

        else:
            await ctx.send("**Błąd! Jednostka (unit), którą wpisałeś jest niepoprawna! Użyj: s, m, h, d, w, mo lub y**",
                           ephemeral=True)


async def setup(bot):
    await bot.add_cog(Moderator(bot))
