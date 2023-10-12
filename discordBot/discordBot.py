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




# ⚡️给机器人增加命令 ————————————————————————————————————————————————
@bot.command() # 装饰器, 让下面的内容成为一个机器人命令
async def say(ctx): # say 表示【命令名】 => !say 就可以调用这个命令
    await ctx.send("👋 你好") # ctx 表示命令的上下文，ctx.send 表示发送消息
      
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)
    
    
    
    
# 👇让机器人可以通过 / 唤起命令 ——————————————————————————————————————
@bot.command()
@commands.has_permissions(administrator=True) # 有管理员权限的用户才能使用
async def synccommands(ctx):
    await bot.tree.sync() # bot.tree.sync 同步命令(每天只能用 200 次), 让服务器知道这些命令可以通过 / 唤起
    await ctx.send("同步完成")
    

@bot.hybrid_command()
async def hello(ctx):
    """基础命令"""
    await ctx.send("🌞 天气晴朗")

@bot.hybrid_command()
async def addnum(ctx, a: int, b: int):
    """给传入的参数做加法的命令"""
    await ctx.send(a + b)
    
    
# 👇石头剪刀布小游戏
@bot.hybrid_command()
async def play(ctx):
    await ctx.send("选择你要出什么", view=PlayView())


    
# tqdm(...) 
bot.run(token) # 登录机器人