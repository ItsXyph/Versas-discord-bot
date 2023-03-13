import nextcord
from nextcord.ext import commands
from nextcord.ext import application_checks
from nextcord import Interaction

class Boosters(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    TEST_GUILD_ID = 1073148950439268422
    VERSAS_GUILD_ID = 1048740762004766840

    @nextcord.slash_command(name = "check_boost", description = "Checks if somebody is a booster", guild_ids = [TEST_GUILD_ID, VERSAS_GUILD_ID])
    async def check_boost(self, interaction: Interaction, member: nextcord.Member):
        await interaction.response.send_message(member.premium_since)
    


def setup(bot):
    bot.add_cog(Boosters(bot))