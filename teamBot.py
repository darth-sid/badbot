import os,random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author ==  client.user:
        return
    counters = [
        'doodoo joke',
        'shame',
        'garlic',
        ':cross:',
        ':garlic:',
        'shame baby jail',
    ]

    jokes = [
        'that timing was legendary',
        'these yolks are eggciting',
    ]
    
    faces = [
        'heads',
        'tails',
    ]

    if message.content == '!erc':
        response = random.choice(counters)
        await message.channel.send(response)

    if message.content == '!idiot' or message.content == 'doodoo joke':
        response = random.choice(jokes)
        await message.channel.send(response)
    
    if message.content == '!coin':
        response = random.choice(faces)
        await message.channel.send(response)
    
    if message.content[0:5] == '!dice':
        sides = int(message.content[6])+1
        response = random.randrange(1,sides)
        await message.channel.send(response)

    if message.content[0:5] == '!team' and len(message.content) >= 9:
        ppl = int(message.content[6])
        teams = int(message.content[8])
        perteam = int(ppl/teams)

        chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        randomize = ['1','2','3','4']
        team1=[]
        team2=[]
        team3=[]
        team4=[]
        print(perteam)
        for i in chars[0:ppl]:
            sorted = False
            while not sorted:
                t = int(random.choice(randomize[0:teams]))
                if t==1 and len(team1)<perteam:
                    team1.append(i+',')
                    sorted = True
                elif t==2 and len(team2)<perteam:
                    team2.append(i+',')
                    sorted = True
                elif t==3 and len(team3)<perteam:
                    team3.append(i+',')
                    sorted = True
                elif t==4 and len(team4)<perteam:
                    team4.append(i+',')
                    sorted = True
                else:
                    sorted = False
        str1=' '.join(team1)
        str2=' '.join(team2)
        str3=' '.join(team3)
        str4=' '.join(team4)
        response = 'team1: '+str1[0:len(str1)-1]+'\nteam2: '+str2[0:len(str2)-1]+'\nteam3: '+str3[0:len(str3)-1]+'\nteam4: '+str4[0:len(str4)-1]
        await message.channel.send(response)
client.run(TOKEN)
