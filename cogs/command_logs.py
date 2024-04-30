from discord.ext import commands
import discord
import settings


class CommandLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        if isinstance(interaction,
                      discord.Interaction) and interaction.type == discord.InteractionType.application_command:
            author_id = interaction.user.id
            guild_id = interaction.guild_id
            guild = self.bot.get_guild(guild_id)
            member = guild.get_member(author_id)
            roles = member.roles
            moderator_role = discord.utils.get(guild.roles, name="Zespół RedSide")
            info_channel = self.bot.get_channel(1227321966067716250)  # wpisz ID kanału
            if moderator_role in roles:
                command_name = interaction.data["name"]
                if command_name:
                    arguments = []
                    for option in interaction.data.get("options", []):
                        arguments.append(option["value"])

                    cmd_channel_id = interaction.channel_id
                    cmd_channel = self.bot.get_channel(cmd_channel_id)
                    user = await self.bot.fetch_user(arguments[0])
                    username = user.mention
                    await info_channel.send(f"{str(member.name).title()} właśnie użył komendy: {command_name}\n"
                                            f"Na kanale: {cmd_channel.name}\n"
                                            f"Na użytkowniku: {username}\n"
                                            f"Na określony czas: {arguments[1:-1]}\n"
                                            f"Powód: {arguments[-1]}")
                else:
                    await info_channel.send(f"{member.name} tried to use ur command")



async def setup(bot):
    await bot.add_cog(CommandLogs(bot))
