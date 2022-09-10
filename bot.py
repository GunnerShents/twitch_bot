from twitchio.ext import commands
from twitchio.client import Client
from dotenv import load_dotenv
import os, random
import playsound
from gtts import gTTS

load_dotenv()
auth_code = os.environ["ACCESS_TOKEN"]

def extract_number(sentence):
        number = []
        words = sentence.split()
        for i in words:
            if i.isdecimal():
                number.append(int(i))
        if len(number) == 0 or number[0] < 2:
                number = [6]
        if len(number) > 0 and number[0] > 100:
            number = [100] 
        return number[0]

def find_name (message):
    words = message.split()
    for word in words:
        if word[0] == '@':
            return word

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=auth_code, prefix='!', initial_channels=['TWITCH_NAME']) 

        self.rps_challenges = {}

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def speak(self, ctx: commands.Context, *, message: str):
        
        speech = gTTS(text=message)
        speech.save("DataFlair.mp3")
        playsound.playsound("DataFlair.mp3")
        os.remove("DataFlair.mp3")
        # await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def dice(self, ctx: commands.Context):
        # import pdb; pdb.set_trace()
        die = extract_number(ctx.message.content)
        result = random.randint(1, die)
        await ctx.send(f'{ctx.author.name} rolled {result} with a {die} die!')
    
    @commands.command()
    async def discord(self, ctx: commands.Context):
        link = "DISCORD_CHANNEL"
        await ctx.send(f"Come join discord {link}")

    @commands.command()
    async def github(self, ctx: commands.Context):
        link = "GITHUB"
        await ctx.send(f"GitHub repo {link}")

    @commands.command()
    async def rps(self, ctx: commands.Context):
        rps = ['Rock','Paper','Scissors']
        result = random.choice(rps)
        await ctx.send(f"{ctx.author.name}, Rock, paper, scissors shoot : {result}")

    @commands.command()
    async def help(self, ctx: commands.Context):
        command_list = '-'.join(self.commands.keys())
        await ctx.send(f'{command_list}')
        

    @commands.command()
    async def project(self, ctx: commands.Context):
        with open('project.txt') as f:
            content = f.readlines()
        await ctx.send(f'{content[-1]}')

#only run the bot if this file is run as a script
if __name__=="__main__":
    bot = Bot()
    bot.run()
    # bot.run() is blocking and will stop execution of any below code here until stopped or closed.

