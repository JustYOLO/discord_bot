# Bot.py
import os, discord
import random as r
from shuffle import shuffle
from dotenv import load_dotenv
from User import User

class Bot(discord.Client):
    async def on_ready(self) -> None:
        print(f'We have logged in as {client.user}')
        for guild in client.guilds:
            print(f"connected in {guild}")
        self.__players = []

    async def on_message(self, message) -> None:
        if message.author == client.user:
            return # prevents 'recursion' problem (bot reply himself)
        elif message.content.startswith('!'):
            # accepts message only starts with '!'
            msg = message.content[1:]
            name = message.author.global_name

            if msg.startswith("hello"):
                await message.channel.send("Hello!")
                print(message.author.global_name)

            elif msg.startswith("사용법"):
                await message.channel.send("!참가 라고 적으세요!\n10명이 !참가 를! 적으면 랜덤하게 팀을 만들어 줍니다.\n처음부터 시작하고 싶으시면 !리셋")

            elif msg.startswith("리셋"):
                self.__players.clear()
                await message.channel.send("리셋 되었습니다.")

            # !t is for testing purpose
            elif msg.startswith("t"):
                tmp, name = message.content.split(' ')
                self.__players.append(User(name, 5))
                if len(self.__players) == 10:
                    await message.channel.send(shuffle(self.__players).output())
                    self.__players.clear()
            
            elif msg.startswith("참가"):
                if not self.does_have_user(name): # if user not in participants list    
                    self.__players.append(User(name, 5))
                    await message.channel.send(f"{name}님이 참가신청 했습니다. ({len(self.__players)}/10)")
                    if len(self.__players) == 10:
                        await message.channel.send(shuffle(self.__players).output())
                        self.__players.clear()
                else: 
                    await message.channel.send(f"{name}님은 이미 참가 신청하셨습니다.")
        else: return
    
    def does_have_user(self, user_name: str) -> bool:
        for user in self.__players:
            if user_name == user.getName():
                return True
        return False

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = Bot(intents=intents)
client.run(TOKEN)