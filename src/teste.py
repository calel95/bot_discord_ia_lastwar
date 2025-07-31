import os
import discord
from discord.ext import commands
#from openai import OpenAI
from google import genai
from google.genai import types
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from main import *
from datetime import date, datetime, timedelta

print(datetime.now())
print(date.today())

aa = datetime.now()

print(aa.day)



#print(dir(genai))
# load_dotenv()


# # def apiOpenia():
# #     load_dotenv()
# #     OPENAI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")
# #     OPENAI_PROJECT = os.getenv("OPENAI_PROJECT")
# #     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# #     client = OpenAI(api_key=OPENAI_API_KEY,
# #                     organization="",
# #                     project="")

# #     try:
# #         campo = input("Digite o nome do campo (ou 'sair' para encerrar): ")
# #         mensagens = [
# #         {'role': 'system', 'content': 'Você é um assistente, e sabe tudo sobre o jogo LastWar mobile, e tudo que perguntarem sobre o jogo, você irá responder. Podendo usar como base para as respostas o site https://www.lastwartutorial.com/'},
# #         {'role': 'user', 'content': campo}
# #         ]

# #         response = client.chat.completions.create(
# #         model="gpt-4o-mini",
# #         messages=mensagens,
# #         max_tokens=500,
# #         temperature=0.7,
# #         )

# #         resposta_chat = response.choices[0].message.content
# #         print(resposta_chat)
# #     except Exception as e:
# #         print(f"Ocorreu um erro ao processar o campo: {e}")

# #apiOpenia()


# DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# intents = discord.Intents.default()
# intents.message_content = True
# intents.presences = True

# bot = commands.Bot(command_prefix="!", intents=intents)

# @bot.event
# async def on_ready():
#     print(f'Bot logado como {bot.user.name} ({bot.user.id})')
#     print('Pronto para receber comandos!')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
    
#     if bot.user.mentioned_in(message) and not message.mention_everyone:
#         question = message.content.replace(f'<@{bot.user.id}>', '').strip()
#         if question:
#             await message.channel.send(f"Olá {message.author.mention}! Me perguntou: '{question}'")
#             await message.channel.send("Estou processando sua pergunta sobre Last War: Mobile...")
            
#             try:
#                 bot_answer = criar_agente_last_war(question=question)
#                 #bot_answer = "Essa é uma ótima pergunta sobre Last War: Mobile! A IA ainda está aprendendo a responder, mas logo terei a resposta para você!"
                
#                 await message.channel.send(f"{message.author.mention}, aqui está a resposta: {bot_answer}")

#             except Exception as e:
#                 await message.channel.send(f"Desculpe, {message.author.mention}, houve um erro ao processar sua pergunta: `{e}`")
#                 print(f"Erro na IA: {e}")
#         return # Para não processar a mensagem como comando também

#     # Processa comandos (se você usar commands.Bot)
#     await bot.process_commands(message)

# # --- Comandos do Bot (Opcional, se você usar comandos como !help ou /status) ---
# @bot.command(name='teste')
# async def ping(ctx):
#     """Responde com 'Pong!' para testar se o bot está online."""
#     await ctx.send('Testado com sucesso!!')

# # --- Inicia o Bot ---
# if __name__ == "__main__":
#     if DISCORD_TOKEN:
#         bot.run(DISCORD_TOKEN)
#     else:
#         print("Erro: O token do Discord não foi encontrado. Por favor, configure a variável de ambiente DISCORD_TOKEN.")



