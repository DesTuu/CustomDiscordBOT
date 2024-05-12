from discord.ext import commands
import discord
import settings


class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        moderator_role = discord.utils.get(member.guild.roles, name="Zespół RedSide")

        # Action if member mute his micro:

        if before.channel and after.channel:
            if not before.self_mute and after.self_mute:
                muted_micro_channel = self.bot.get_channel(1186401279921111131)

                if moderator_role in member.roles:
                    await muted_micro_channel.send(f"**{member.nick}/{member.name}** właśnie **wyciszył** swój mikrofon.")
                else:
                    await muted_micro_channel.send(f"{member.mention} właśnie **wyciszył** swój mikrofon.")
            if before.self_mute and not after.self_mute:
                if moderator_role in member.roles:
                    await muted_micro_channel.send(f"**{member.nick}/{member.name}** właśnie **włączył** swój mikrofon.")
                else:
                    await muted_micro_channel.send(f"{member.mention} właśnie **włączył** swój mikrofon.")

        # Action if member leave the channel:

        if before.channel is not None and after.channel is None:
            user_disconnected_channel = self.bot.get_channel(1239107359737909330)
            if moderator_role in member.roles:
                await user_disconnected_channel.send(
                    f"**{member.nick}/{member.name}** właśnie opuścił kanał **{before.channel.name}**.")
            else:
                await user_disconnected_channel.send(f"{member.mention} właśnie opuścił kanał **{before.channel.name}**.")


async def setup(bot):
    await bot.add_cog(Logs(bot))
