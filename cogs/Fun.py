from nextcord.ext import commands
import nextcord
import random
import os
testServerId=892715222639448104
class Fun(commands.Cog):
  def __init__(self,client):
    self.client=client

  @nextcord.slash_command(name='8ball',guild_ids=[testServerId])
  async def _8ball(self,interaction):
    responses=["It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
    embed=nextcord.Embed(title="8ball",description=(f'{random.choice(responses)}'),colour=nextcord.Colour.blue())
    await interaction.send(embed=embed)

  # @nextcord.slash_command(guild_ids=[testServerId],description=": A game in which you pretend to kill someone.")
  # async def kill(self,interaction,member:Cog.MemberConverter):
  #   responses=[(':gun: You shot '+str(f'{member.mention}')+' and killed them.'),
  #   (':gun: You tried to shoot'+str(f'{member.mention}')+', but missed.'),
  #   (':bomb:You killed '+str(f'{member.mention}')+" using a bomb."),
  #   (':bomb:You try to kill'+str(f'{member.mention}')+'using a bomb but it does not detonate.\n'+str(f'{member.mention}')+' notices it and kills you in self-defense.'),
  #   (':bomb:You try to kill'+str(f'{member.mention}')+'using a bomb but it does not detonate.\n'+str(f'{member.mention}')+' does not notice it and you are able to walk away alive.'),
  #   (':gun: You tried to shoot'+str(f'{member.mention}')+', but missed.\n'+str(f'{member.mention}'+" notices it and kills you in self-defense."))
  #   ]
  #   embed=nextcord.Embed(description=f'{random.choice(responses)}',colour=nextcord.Colour.teal())
  #   await interaction.send(embed=embed)

  @nextcord.slash_command(guild_ids=[testServerId],description=": Make Sirius say something.")
  async def say(self,interaction,*,sentence):
    await interaction.channel.purge(limit=1)
    embed=nextcord.Embed(description=(str(sentence)),colour=nextcord.Colour.teal())
    await interaction.send(embed=embed)


def setup(client):
  client.add_cog(Fun(client))