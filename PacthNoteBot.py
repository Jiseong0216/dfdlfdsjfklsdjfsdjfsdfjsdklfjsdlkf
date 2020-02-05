import discord
import datetime
import asyncio
import os

client = discord.Client()

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')

@client.event
async def on_ready():
    print('Bot start')
    game = discord.Game("봇 문의는 Unknown_- | 지성#5554 로 부탁드립니다.")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('!도움'):
        embed = discord.Embed(color=0x555555)
        embed.add_field(name="통합 Bot Information", value="V1 last updated 2020.02.05", inline=False)
        embed.add_field(name="명령어 리스트 -------- command list", value="모든 명령어에는 느낌표를 붙입니다.", inline=False)
        embed.add_field(name="!봇정보", value="", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content.startswith('.공지'):
        embed = discord.Embed(color=0x555555)
        embed.add_field(name="공지", value="봇 이름이 변경 돼었습니다. [ Vincent ]", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!봇에탄생'):
        embed = discord.Embed(color=0x555555)
        embed.add_field(name="봇탄생", value="안녕? 나는 2020년 2월 4일에 지성이가 원래 봇이 죽었다고 급하게 내가 만들어졌어!", inline=False)
        await message.channel.send(embed=embed)

      
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
