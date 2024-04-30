from discord.ext import commands
import discord
import settings


class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = self.bot.get_channel(1164381123569270894)  # Replace YOUR_CHANNEL_ID with the channel ID
        moderator_role = discord.utils.get(member.guild.roles, name="Zespół RedSide")
        if before.channel and after.channel:
            if not before.self_mute and after.self_mute:
                if moderator_role in member.roles:
                    await channel.send(f"{member.nick} ({member.name}) turned **off** their microphone.")
                else:
                    await channel.send(f"{member.mention} turned **off** their microphone.")
            if before.self_mute and not after.self_mute:
                if moderator_role in member.roles:
                    await channel.send(f"{member.nick} ({member.name}) turned **on** their microphone.")
                else:
                    await channel.send(f"{member.mention} turned **on** their microphone.")


async def setup(bot):
    await bot.add_cog(Logs(bot))
