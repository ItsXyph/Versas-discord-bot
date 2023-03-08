import nextcord
from nextcord.ext import commands
from nextcord.ext import application_checks
from nextcord import Interaction
import datetime
import dotenv
import os

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    TEST_GUILD_ID = 1073148950439268422
    VERSAS_GUILD_ID = 1048740762004766840

    @nextcord.slash_command(name = "purge", description = "Purges a set amount of messages.", guild_ids=[TEST_GUILD_ID, VERSAS_GUILD_ID])
    @application_checks.has_permissions(manage_messages=True)
    async def purge(self, interaction: Interaction, limit : int):
        embed = nextcord.Embed(color=nextcord.Colour.blurple(), title=f"{limit} Messages were purged.", timestamp=datetime.datetime.now())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1048935994323370024/1079520156398653450/v-letter-logo-icon-for-business-and-company-vector.jpg")
        embed.set_author(name=self.bot.user.name, icon_url="https://cdn.discordapp.com/attachments/1048935994323370024/1079520156398653450/v-letter-logo-icon-for-business-and-company-vector.jpg")
        await interaction.channel.purge(limit = limit)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name = "kick", description = "Kicks a given member", guild_ids=[TEST_GUILD_ID, VERSAS_GUILD_ID])
    @application_checks.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, member: nextcord.Member, reason):
        await interaction.response.send_message(f"{member} Has been kicked for {reason}")
        await member.kick()

    @nextcord.slash_command(name = "ban", description = "Bans a given user", guild_ids = [TEST_GUILD_ID, VERSAS_GUILD_ID])
    @application_checks.has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction, user: nextcord.User, reason):
        await interaction.response.send_message(f"{user} has been banned for {reason}")
        await user.ban()

    @nextcord.slash_command(name = "unban", description = "Unbans a given user", guild_ids = [TEST_GUILD_ID, VERSAS_GUILD_ID])
    @application_checks.has_permissions(ban_members=True)
    async def unban(self, interaction: Interaction, user: nextcord.User):
        await interaction.response.send_message(f"{user} has been unbanned")
        await interaction.guild.unban(user)

    @nextcord.slash_command(name = "mute", description = "Mutes a member for a given time", guild_ids = [TEST_GUILD_ID, VERSAS_GUILD_ID])
    @application_checks.has_role("Staff")
    async def mute(self, interaction: Interaction, member: nextcord.Member, duration = "1w", reason = None):
            if duration[-1].lower() == "s".lower():
                await member.timeout(datetime.timedelta(seconds = int(duration[:-1])))
                if reason == None:
                    await interaction.response.send_message(f"{member.mention} has been muted for {duration[:-1]} second(s).")
                else:
                    await interaction.response.send_message(f'{member.mention} has been muted for {duration[:-1]} second(s) for:\n {reason}')
            elif duration[-1].lower() == "m".lower():
                await member.timeout(datetime.timedelta(minutes=int(duration[:-1])))
                if reason == None:
                    await interaction.response.send_message(f"{member.mention} has been muted for {duration[:-1]} minute(s).")
                else:
                    await interaction.response.send_message(f'{member.mention} has been muted for {duration[:-1]} minute(s) for:\n {reason}')
            elif duration[-1].lower() == "h".lower():
                await member.timeout(datetime.timedelta(hours=int(duration[:-1])))
                if reason == None:
                    await interaction.response.send_message(f"{member.mention} has been muted for {duration[:-1]} hour(s)")
                else:
                    await interaction.response.send_message(f'{member.mention} has been muted for {duration[:-1]} hour(s) for:\n {reason}')
            elif duration[-1].lower() == 'd'.lower():
                await member.timeout(datetime.timedelta(days=int(duration[:-1])))
                if reason == None:
                    await interaction.response.send_message(f"{member.mention} has been muted for {duration[:-1]} day(s).")
                else:
                    await interaction.response.send_message(f'{member.mention} has been muted for {duration[:-1]} days(s) for:\n {reason}')
            elif duration[-1].lower() == 'w'.lower():
                await member.timeout(datetime.timedelta(weeks=int(duration[:-1])))
                if reason != "":
                    await interaction.response.send_message(f"{member.mention} has been muted for {reason}.")
                else:
                    await interaction.response.send_message(f'{member.mention} has been muted.')
            else:
                await interaction.response.send_message("I'm sorry, this input is incorrect. Input a number (I.E: 10) followed by either s, m, h, or d (seconds, minutes, hours or days).", ephemeral=True)

    @nextcord.slash_command(name = "unmute", description="Unmutes a member/removes timeout.", guild_ids=[TEST_GUILD_ID, VERSAS_GUILD_ID])
    @application_checks.has_role("Staff")
    async def unmute(self, interaction: Interaction, member: nextcord.Member, reason = None):
        await member.edit(timeout=None)
        if reason == None:
            await interaction.response.send_message(f"{member.mention} was unmuted.")
        else:
            await interaction.response.send_message(f"{member.mention} was unmuted for {reason}.")


    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, nextcord.ApplicationError):
            await ctx.response.send_message("You don't have the permission to run this command.", ephemeral=True)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, nextcord.ApplicationError):
            await ctx.response.send_message("You don't have the permission to run this command.", ephemeral=True)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, nextcord.ApplicationError):
            await ctx.response.send_message("You don't have the permission to run this command.", ephemeral=True)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, nextcord.ApplicationError):
            await ctx.response.send_message("You don't have the permission to run this command.", ephemeral=True)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, nextcord.ApplicationError):
            await ctx.response.send_message("You don't have the permission to run this command.", ephemeral=True)

def setup(bot):
    bot.add_cog(Moderation(bot))