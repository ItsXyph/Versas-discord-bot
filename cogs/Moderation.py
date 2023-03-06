import nextcord
from nextcord.ext import commands
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
    async def purge(self, interaction: Interaction, limit : int):
        embed = nextcord.Embed(color=nextcord.Colour.blurple(), title=f"{limit} Messages were purged.", timestamp=datetime.datetime.now())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1048935994323370024/1079520156398653450/v-letter-logo-icon-for-business-and-company-vector.jpg")
        embed.set_author(name=self.bot.user.name, icon_url="https://cdn.discordapp.com/attachments/1048935994323370024/1079520156398653450/v-letter-logo-icon-for-business-and-company-vector.jpg")
        await interaction.channel.purge(limit = limit)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name = "kick", description = "Kicks a given member", guild_ids=[TEST_GUILD_ID, VERSAS_GUILD_ID])
    async def kick(self, interaction: Interaction, member: nextcord.Member, reason):
        await interaction.response.send_message(f"{member} Has been kicked for {reason}")
        await member.kick()


    @nextcord.slash_command(name = "ban", description = "Bans a given user", guild_ids = [TEST_GUILD_ID, VERSAS_GUILD_ID])
    async def ban(self, interaction: Interaction, user: nextcord.User, reason):
        await interaction.response.send_message(f"{user} has been banned for {reason}")
        await user.ban()

    @nextcord.slash_command(name = "unban", description = "Unbans a given user", guild_ids = [TEST_GUILD_ID, VERSAS_GUILD_ID])
    async def unban(self, interaction: Interaction, user: nextcord.User):
        await interaction.response.send_message(f"{user} has been unbanned")
        await interaction.guild.unban(user)

    
    @nextcord.slash_command(name = "mute", description = "Mutes a member for a given time", guild_ids = [TEST_GUILD_ID, VERSAS_GUILD_ID])
    async def mute(self, interaction: Interaction, member: nextcord.Member, duration):
        multiplier = 1
        if "s".lower() in duration:
            multiplier = 1
        elif "m".lower() in duration:
            multiplier = 60
        elif "h".lower() in duration:
            multiplier = 3600        
        elif 'd'.lower() in duration:
            multiplier = 86400

def setup(bot):
    bot.add_cog(Moderation(bot))