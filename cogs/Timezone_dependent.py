import datetime
import nextcord
import pytz
from nextcord.ext import commands
testServerId=892715222639448104

def weekday(a):
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    a1 = (str(switcher.get(a)))
    return a1

def tillbday():
    t = pytz.timezone('Asia/Kolkata')
    at = datetime.datetime.now(t)
    a1 = at.year
    bday = datetime.datetime(int(a1), 2, 17, 0, 0, 0)
    if ((bday.month) < a1):
        a1 = a1 + 1
    bday = datetime.datetime(int(a1), 2, 17, 0, 0, 0)
    a = at.replace(tzinfo=None)
    tillbday = bday - a
    return tillbday.days


class Timezone_dependent(commands.Cog):
  def __init__(self,client):
    self.client=client

  @nextcord.slash_command(guild_ids=[testServerId],description=": To check the time\n(calibrated according to IST)")
  async def time(self,interaction):  #to check the time
    z = pytz.timezone('Asia/Kolkata')
    y = datetime.datetime.now(z)
    x = y.strftime("%H:%M:%S")
    message=nextcord.Embed(title="Time",description=(str('The time right now in India is: ') + x),colour=nextcord.Colour.blue())
    await interaction.send(embed=message)

  @nextcord.slash_command(guild_ids=[testServerId],description=": To check the day and date\n(calibrated according to IST)")
  async def dayanddate(self,interaction):  #To check the day and date
    z = pytz.timezone('Asia/Kolkata')
    y = datetime.datetime.now(z)
    x = y.strftime("%d/%m/%Y")
    w1 = datetime.date.today()
    w2 = (w1.weekday())
    message=nextcord.Embed(title="Day and Date",description=str('Day: ' + (weekday(w2)+('\nDate: ' + x))),colour=nextcord.Colour.blue())
    await interaction.send(embed=message)

  @nextcord.slash_command(guild_ids=[testServerId],description=": To find out the days remaining for birthday.")
  async def birthday(self,interaction):  #to check the numbers of days remaining for birthday
    message=nextcord.Embed(title="Birthday",description=(str("Days remaining for birthday: ") + str(tillbday()) +str(" days")),colour=nextcord.Colour.blue())
    await interaction.send(embed=message)


def setup(client):
  client.add_cog(Timezone_dependent(client))