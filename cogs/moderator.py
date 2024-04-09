import asyncio
from discord.ext import commands
import discord


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
    async def mute(self, ctx, muted_member: discord.Member, duration: int, unit: str, *reason):
        muted_member_id = muted_member.id
        muted_user = self.bot.get_user(muted_member_id)
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

        await muted_member.add_roles(muted_role)
        if muted_user:
            await muted_user.send(f"Zostałeś/aś wyciszony na {duration} {unit}, powód: {' '.join(reason)}")

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
        # if muted_user:
        #     await muted_user.send(f"Okres wyciszenia użytkownika {muted_member.mention} minął.")

    @commands.command(
        brief=f"Tylko Ty widzisz tą wiadomość"  # Opis komendy przy użyciu $help
    )
    @is_moderator()
    async def warn(self, ctx, warned_member: discord.Member, *reason):
        warned_member_id = warned_member.id
        warned_user = self.bot.get_user(warned_member_id)

        warn1_role = discord.utils.get(ctx.guild.roles, name="warn - 1")
        warn2_role = discord.utils.get(ctx.guild.roles, name="warn - 2")
        timeout_role = discord.utils.get(ctx.guild.roles, name="TIMEOUT")

        if warn1_role in warned_member.roles and warn2_role not in warned_member.roles:
            await warned_member.add_roles(warn2_role)
            if warned_user:
                await warned_user.send(f"Warned 2, powód: {' '.join(reason)}")
        elif warn1_role in warned_member.roles and warn2_role in warned_member.roles:
            await warned_member.add_roles(timeout_role)
            if warned_user:
                await warned_user.send(f"Timeout, powód: {' '.join(reason)}")
            await warned_member.remove_roles(warn1_role)
            await warned_member.remove_roles(warn2_role)
            await asyncio.sleep(10)
            await warned_member.remove_roles(timeout_role)
        else:
            await warned_member.add_roles(warn1_role)
            if warned_user:
                await warned_user.send(f"Warned 1, powód: {' '.join(reason)}")

        # await muted_member.add_roles(warned_role)
        # await muted_member.remove_roles(warned_role_role)


async def setup(bot):
    await bot.add_cog(Moderator(bot))
