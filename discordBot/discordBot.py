import os
import discord
from discord.ext import commands # discord.ext 为接命令的机器人
from dotenv import load_dotenv
from tqdm import tqdm



load_dotenv() # 加载环境变量
token = os.getenv("DISCORD_BOT_TOKEN")
if token:
    print("✅ Token is loaded: " + token)
else:
	print("❌ Token is not loaded")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents) # command_prefix="!" 表示用什么命令唤起机器人




# ⚡️给机器人增加命令
@bot.command() # 装饰器, 让下面的内容成为一个机器人命令
async def ping(ctx):
    await ctx.send("你好") # ctx 表示命令的上下文，ctx.send 表示发送消息
    
    
# tqdm(...) 
bot.run(token) # 登录机器人