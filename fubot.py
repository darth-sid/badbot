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

    ShottaFlowNLE = [
        'yeah, yeah, yeah',
        'I am a menace, keep me a rack just like tennis',
        'Im with the sh*t like Im Dennis',
        'I started this sh*t Ima finish',
        'N****s be hatin, tryna blemish my image',
        'Who want the smoke? .223 came with the scope',
        'Extended clip long as a rope',
        'We wipe his nose, just like he had him a cold',
        'I knew that boy was a ho',
        'Pull up with the gang, you know that we bangin',
        'What is your set, n****? What is you claimin?',
        'I am a beast, you cannot tame it',
        'Dont point the finger, this shit can get dangerous',
        'These n***s hatin, these n***s plottin',
        'Ooh, he got money Im runnin his wallet',
        'You say you a killer, lil n**** stop it',
        'In a shoot out your gun was droppin',
        'you really a ho',
        'you pull up i let that b**** blow',
        'And just like some tissue we wpiing your nose',
        'I was on stage with the strap at my show',
        'If you play, Ima blow, put a tag on your toe',
        'Wet a n**** up, send him straight to the doctor',
        'Two bullets in his chest, make the f*** n**** holler',
        'Im a big dog, Great Dane, n****, you a toddler',
        'B**** N****, you my son, so that make me a father, yeah'

    ]

    ShottaFlowBlueface = [
        'Yeah, Yeah, Aight',
        'B**** Im a Loc, Mac with a scope',
        'I am big homie, one phone call they go',
        'Pick the wrong side, Glock pull him courtside',
        'Now he watching it shoot from the floor',
        'Ooh, hold up, hold up, hold up, let me switch the flow',
        'Choppa got a chopper, make a wrong move, bet he pop ya',
        'B**** call me daddy, b**** call me papa',
        'That boy bologna, b****, Im vegan',
        'You know if I hit it, then it was on camera',
        'Hopped off the bus, then I hopped in a Porsche (Panamera)',
        'On Forgis, sittin on a four piece',
        'With a biscuit',
        'I play with fire, sometimes I burn bridges',
        'Bet you aint never met a n**** love swimmin',
        'Pull up like Tracy McGrady from the Pistons',
        'Gotta keep a pistol for a f*** n**** dissin',
        'Bet this chopper make him dance like a disco',

    ]

    if message.content == "yeah":
        for i in ShottaFlowNLE:
            await message.channel.send(i)
    if message.content == "blueface baby":
        for i in ShottaFlowBlueface:
            await message.channel.send(i)

client.run(TOKEN)
