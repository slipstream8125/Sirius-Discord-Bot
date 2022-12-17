import nextcord
import asyncio
from nextcord.ext import commands
testServerId=892715222639448104


class DurationConverter(commands.Converter):
  async def convert(self,ctx,argument):
    amount=argument[:-1]
    unit=argument[-1]

    if amount.isdigit() and unit in ['s','m','h','hrs','hr','mins','sec']:
      return(int(amount),unit)

    raise commands.BadArgument(message="Not a valid duration")


class Mod_Permissions(commands.Cog):
  def __init__(self,client):
    self.client=client



  @commands.command(brief=": To ban an idiot from the server")
  @commands.has_permissions(administrator=True)
  async def ban(self,ctx,member:commands.MemberConverter ,*,reason=None):
      await member.ban(reason=reason)
      await ctx.channel.purge(limit=1)
      message=nextcord.Embed(title="Ban",description=(str(f'{member.mention} has been banned from this server\n')+str("Reason: ")+str(reason)),colour=nextcord.Colour.red())
      await ctx.guild.get_channel(904963667165065246).send(embed=message)
      await ctx.guild.get_channel(893142532085665792).send(embed=message)

  @commands.command(brief=": To temporarily ban someone",help=("Write the duration suffix as:\n's' or 'sec' for seconds\n'm' or 'mins' for minutes\n'hr' or 'hrs' for hours"))
  @commands.has_permissions(administrator=True)
  async def tempban(self,ctx,member:commands.MemberConverter,duration:DurationConverter,*,reason=None):

    multiplier={'s':1,'sec':1,'m':60,'mins':60,'h':3600,'hr':3600,'hrs':3600}
    amount,unit=duration

    await ctx.guild.ban(member)
    message=nextcord.Embed(title="Tempban",description=(str(f'{member.mention} has been temporarily banned from this server for ')+str(f'{amount}{unit}\n')+str("Reason: ")+str(reason)),colour=nextcord.Colour.red())
    await ctx.guild.get_channel(904963667165065246).send(embed=message)
    await ctx.guild.get_channel(893142532085665792).send(embed=message)
    await asyncio.sleep(amount *multiplier[unit])
    await ctx.guild.unban(member)

  @commands.command(brief=": To unban someone",help="The pattern for writing the unban command is Account_Name#tag")
  @commands.has_permissions(administrator=True)
  async def unban(self,ctx, *,member):
      banned_users = await ctx.guild.bans()

      member_name, member_discriminator = member.split('#')
      for ban_entry in banned_users:
         user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          await ctx.channel.purge(limit=1)
  
  @commands.command(brief=": To kick an idiot from the server")
  @commands.has_permissions(administrator=True)
  async def kick(self,ctx,member: commands.MemberConverter,*,reason=None):
    await member.kick(reason=reason)
    await ctx.channel.purge(limit=1)
    message=nextcord.Embed(title="Kick",description=(str(f"{member.mention} has been kicked from this server.\n"+"Reason: ")+str(reason)),colour=nextcord.Colour.red())
    await ctx.guild.get_channel(893142532085665792).send(embed=message)

  @nextcord.slash_command(guild_ids=[testServerId],description=": To clear messages" )
  @commands.has_permissions(administrator=True)
  async def clear(self,interaction, amount=1):
    await interaction.channel.purge(limit=int(amount))
    message=nextcord.Embed(title="Clear Messages",description="Cleared "+str(amount)+" message(s)",colour=nextcord.Colour.red())
    await interaction.send(embed=message)





def setup(client):
  client.add_cog(Mod_Permissions(client))