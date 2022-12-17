from nextcord.ext import commands
import datetime
import pytz
import asyncio
import nextcord
import os
testServerId=892715222639448104

class Tasks(commands.Cog):
  def __init__(self,client):
    self.client=client
  
  @nextcord.slash_command(guild_ids=[testServerId])
  async def tasks(self,interaction,date,*,task):
    async def wait_until(self,date):
      print(date)
      t=pytz.timezone('Asia/Kolkata')
      now=datetime.datetime.now(t)
      await interaction.send(nextcord.Embed(title="Tasks",description="Task Registered",colour=nextcord.colour.green()))
      await asyncio.sleep((date-now).seconds)
      a=nextcord.Embed(title="Tasks",description=(str(task)),colour=nextcord.colour.green())
      await interaction.send(a)


def setup(client):
  client.add_cog(Tasks(client))