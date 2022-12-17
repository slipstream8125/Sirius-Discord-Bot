import nextcord
from nextcord.ext import commands
import os
testServerId=892715222639448104
class Memes(commands.Cog):

  def __init__(self,client):
    self.client=client

  @nextcord.slash_command(guild_ids=[testServerId],description=": for the Obi-Wan meme")
  async def hellothere(self,interaction):
    await interaction.send(
        'https://tenor.com/view/hello-there-hi-there-greetings-gif-9442662')

  @nextcord.slash_command(guild_ids=[testServerId],description=": for General Grievious' reply to Obi-Wan in the meme.")
  async def generalkenobi(self,interaction):  #star wars meme
    await interaction.send(
        'https://tenor.com/view/grevious-general-kenobi-star-wars-gif-11406339')

def setup(client):
  client.add_cog(Memes(client))