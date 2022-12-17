from keep_alive import keep_alive
import os
import nextcord
intents = nextcord.Intents.default()
intents.message_content = True
#from nextcord import Interaction, CommandOption, ChannelType
from nextcord.ext import commands
os.chdir("cogs")

my_secret = os.environ['my_secret']
testServerId=892715222639448104

command_prefix="!"
cogs=['cogs.Fun','cogs.General','cogs.Memes','cogs.Mod_Permissions','cogs.Timezone_dependent','cogs.Music']
client=commands.Bot(command_prefix,intents=intents)



@client.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.CommandNotFound):
    message=nextcord.Embed(title="Error",description=('This command does not exist.'),colour=nextcord.Colour.blue())
    await ctx.send(embed=message)
  if isinstance(error,commands.MissingPermissions):
    message=nextcord.Embed(title="Error",description=('You do not have the required admin permissions to run the command.'),colour=nextcord.Colour.blue())
    await ctx.send(embed=message)


@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="the '"+command_prefix+"' command to be invoked"))
    print('We have logged in as {0.user}'.format(client))
    return
  
@client.slash_command(name="testing",guild_ids=[testServerId])
async def test(interaction: Interaction):
  await interaction.response.send_message("Hi!")

keep_alive()
for cog in cogs:
	client.load_extension(cog)
	
try:
  client.run(my_secret)
except:
  os.system("kill 1")