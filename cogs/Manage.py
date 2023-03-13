import nextcord
from nextcord.ext import commands
from nextcord.ext import application_checks
from nextcord import Interaction

class Manage(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    TEST_GUILD_ID = 1073148950439268422
    VERSAS_GUILD_ID = 1048740762004766840    

    @nextcord.slash_command(name = "create_channel", description="Creates a channel", guild_ids=[TEST_GUILD_ID, VERSAS_GUILD_ID])
    async def create_channel(self, interaction: Interaction, name):
        await nextcord.guild.Guild._create_channel(self, name, )


def setup(bot):
    bot.add_cog(Manage(bot))