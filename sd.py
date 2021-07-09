import discord 
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '_')


@client.event
async def on_ready():
  print("Jestem starymDojcem a overwatch jest zakazany na tym serwie")

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)


@client.event
async def on_message(message):    
  
  rules = '''10 przykazań bożych
  1.Tomczyk jebany będzie
  2.Hubert kickowany regularnie będzię
  3.Szanować administratora będziesz
  4.Nie będziesz dawać admina Tomczykowi
  5.Nie będziesz pożądać Dominiki ani niczego co Kamila jest
  6.Nie będziesz pożądać rangi bliźniego swego
  7.Nie będziesz puszczać Clown fiesty bo to dla Jasia drażniące jest
  8.Nie będziesz AC/DC requestować bo to obrzydliwe jest
  9.Na serwer wchodzić będziesz po 22'''

  commands = [
  ["_zasady", rules],
  ["_siema", "No siema, co tam mordo słychać?"], 
  ["_kto jest jebany w tym miesiącu?", "Tomczyk kurwa XD"],
  ["_dawaj mema kurwo", "https://cdn.discordapp.com/attachments/455236204477022208/819578013347479552/LOL117.mp4"]]

  if message.author == client.user:
    return

  # when user typing in right channel   
  if str(message.channel) == "kanal-dla-bota":
    # if user doesn't know commands
    if str(message.content) == "_komendy":
      for count, task in enumerate(commands, start=1):
        tmp = f"```json\n{count}.\t{task[0]}```"
        await message.channel.send(tmp)
    # when user tried type something with prefix
    elif str(message.content)[0] == "_" and str(message.content)[1]:  
      await message.channel.send("Nie znam tej komendy. Sprawdź '_komendy'")
    # if task is in commands 
    for task in commands:
      if message.content.startswith(task[0]):
        await message.channel.send(task[1])
  
  
client.run(os.getenv("TOKEN"))