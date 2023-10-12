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
async def hello(ctx): # 定义 hello 命令
    """基础命令"""
    await ctx.send("🌞 天气晴朗")

@bot.hybrid_command()
async def addnum(ctx, a: int, b: int): # 定义 addnum 命令
    """给传入的参数做加法的命令"""
    await ctx.send(a + b)
    
    
# 👇石头剪刀布小游戏
class PlayView(discord.ui.View):
    def get_content(self, label):
        counter = { # ⚡️定义输了的情况
			"剪刀": "石头",
   			"石头": "布",
			"布": "剪刀"
		}
        return f"你出了 {label}, 电脑出了 {counter[label]}, 你输了"

	# 出剪刀的情况
    @discord.ui.button(label="剪刀", style=discord.ButtonStyle.green, emoji="✌️")
    async def scissors(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=self.get_content(button.label)) 
    
	# 出石头的情况
    @discord.ui.button(label="石头", style=discord.ButtonStyle.green, emoji="✊")
    async def rock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=self.get_content(button.label)) 
        
	# 出布的情况
    discord.ui.button(label="布", style=discord.ButtonStyle.green, emoji="👋")
    async def paper(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=self.get_content(button.label)) 
    
    # 退出游戏
    @discord.ui.button(label="不玩了", style=discord.ButtonStyle.red) # ⚡️ discord 消息卡片的按钮组件
    async def stop(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="⛔️ 游戏结束", view=None) # ⚡️ interaction.response.edit_message 为修改当前 message 的内容 content

@bot.hybrid_command()
async def play(ctx): # 定义 play 命令
    """石头剪刀布小游戏"""
    await ctx.send("选择你要出什么", view=PlayView()) # 🔥🔥 调用 PlayView() 类, 让用户可以通过按钮选择出什么


    
# tqdm(...) 
bot.run(token) # 登录机器人