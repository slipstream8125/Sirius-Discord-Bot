import nextcord
from nextcord.ext import commands
import os
testServerId=892715222639448104
class General(commands.Cog):
  def __init__(self,client):
    self.client=client
    

  @nextcord.slash_command(name="ping",description=": To check the latency",guild_ids=[testServerId])  #to check the latency
  async def ping(self,interaction):
    message=nextcord.Embed(title="Ping",description=(str("Latency= ") +str(f'{int(commands.latency * 1000)}ms')),colour=nextcord.Colour.blue())
    await interaction.send(embed=message)

  @nextcord.slash_command(guild_ids=[testServerId],description=": for bug reports")
  async def bugreport(self,interaction):  #for bug reports
    embed=nextcord.Embed(title='Bug reports',description='Please be a bit patient if you face any issues with the bot\nThe creator of this bot is still learning to code and may need some time to resolve the bugs.\nUse this google form to report bugs:\n<https://forms.gle/nxQxe9NLLy6b7TyR6>',colour=nextcord.Colour.blue())
    await interaction.send(embed=embed)

  @nextcord.slash_command(guild_ids=[testServerId],description=": info about the bot")
  async def about(self,interaction):
    embed=nextcord.Embed(title="About the Bot",description="Sirius is a bot created using nextcord",colour=nextcord.Colour.blue())
    await interaction.send(embed=embed)
  
  @nextcord.slash_command(guild_ids=[testServerId],description=": Websites to refer to make a bot like this")
  async def sources(self,interaction):
    embed=nextcord.Embed(title="Sources(to make a bot just like this one)",description=("<https://www.freecodecamp.org/news/create-a-discord-bot-with-python/> \n"+
  "<https://betterprogramming.pub/how-to-make-discord-bot-commands-in-python-2cae39cbfd55> \n"+
  "<https://youtube.com/playlist?list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ>\n"+
  "For music from YouTube,use:\n<https://github.com/pawel02/image_bot/blob/main/music_cog.py>")
  ,colour=nextcord.Colour.blue())
    await interaction.send(embed=embed)
    

def setup(client):
  client.add_cog(General(client))