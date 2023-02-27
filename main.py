import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import datetime
import dotenv
import os

token = dotenv.load_dotenv()
intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"We've logged in as: {bot.user}")

cogs_list = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        cogs_list.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in cogs_list:
        bot.load_extension(extension)


bot.run(os.getenv('TOKEN'))