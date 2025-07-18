import os
import discord
#from openai import OpenAI
from google import genai
from google.genai import types
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

#print(dir(genai))
load_dotenv()


# def apiOpenia():
#     load_dotenv()
#     OPENAI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")
#     OPENAI_PROJECT = os.getenv("OPENAI_PROJECT")
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#     client = OpenAI(api_key=OPENAI_API_KEY,
#                     organization="",
#                     project="")

#     try:
#         campo = input("Digite o nome do campo (ou 'sair' para encerrar): ")
#         mensagens = [
#         {'role': 'system', 'content': 'Você é um assistente, e sabe tudo sobre o jogo LastWar mobile, e tudo que perguntarem sobre o jogo, você irá responder. Podendo usar como base para as respostas o site https://www.lastwartutorial.com/'},
#         {'role': 'user', 'content': campo}
#         ]

#         response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=mensagens,
#         max_tokens=500,
#         temperature=0.7,
#         )

#         resposta_chat = response.choices[0].message.content
#         print(resposta_chat)
#     except Exception as e:
#         print(f"Ocorreu um erro ao processar o campo: {e}")

#apiOpenia()

# def criar_agente_last_war():
#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#     genai.configure(api_key=GEMINI_API_KEY)
#     #model = genai.GenerativeModel("gemini-1.5-flash")

#     # Configurar o chat com a ferramenta de busca Google Search ativada
#     search_tool = {"google_search": {}}
#     chat = genai.Chat(model="gemini-1.5-flash", config={"tools": [search_tool]})

#     campo = input("Digite sua pergunta sobre LastWar: ")

#     prompt = (
#         "Você é um assistente e sabe tudo sobre o jogo LastWar mobile. "
#         "Tudo que perguntarem sobre o jogo, você irá responder, podendo usar como base para as respostas o site https://www.lastwartutorial.com/. "
#         f"Pergunta do utilizador: {campo}"
#     )

#     # response = chat.generate_content(
#     #     prompt,
#     #     generation_config={
#     #         "max_output_tokens": 500,
#     #         "temperature": 0.7,
#     #     }
#     # )

#     response = chat.send_message(prompt)

#     print("\nResposta do Agente LastWar:")
#     print(response.candidates[0].content.parts[0].text)
#     print("-" * 50)

    # resposta_chat = response.text
    # print("\nResposta do Agente LastWar:")
    # print(resposta_chat)
    # print("-" * 50)



######FUNCIONANDO ABAIXO
def textHtml():
    # Passo 1: buscar conteúdo da URL
    url = "https://www.lastwartutorial.com"
    response = requests.get(url)
    if response.status_code != 200:
        print("Não foi possível acessar o site.")
        return

    # Passo 2: extrair texto relevante (exemplo: títulos)
    soup = BeautifulSoup(response.text, "html.parser")
    #textos = [h2.get_text() for h2 in soup.find_all("h2")]

    # Juntar os textos para enviar ao Gemini
    #contexto = "\n".join(textos)
    return soup

fonte = textHtml()


def criar_agente_last_war(fonte_url):
    # lista_urls = [
    #     "https://www.lastwartutorial.com/heroes",
    #     "https://www.lastwartutorial.com/desert-storm/"
    # ]
    fonte = fonte_url
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    #genai.configure(api_key=GEMINI_API_KEY)

    client = genai.Client(api_key=GEMINI_API_KEY)

    campo = input("Digite sua pergunta sobre LastWar: ")

    # prompt = (
    #     "Você é um assistente especialista no jogo LastWar mobile. "
    #     "Para responder, utilize informações disponíveis na web, "
    #     "especialmente do site https://www.lastwartutorial.com/. "
    #     "Procure por informações relevantes e forneça uma resposta clara e concisa. "
    #     "Procure não ser longo nas respostas "
    #     "e evite repetir informações. "
    #     "Se não encontrar informações, responda que não sabe. "
    #     f"Pergunta do usuário: {campo}"
    # )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=campo,
        config=types.GenerateContentConfig(
            system_instruction="Você é um assistente especialista no jogo LastWar mobile.  "
                               f"fonte de dados das repostas : pesquise na internet e use informações do site {fonte}. "
                               "Pegue a url que esta na lista, que tenha alguma semelhanca com o que foi solicitado pelo usuario. Exemplo, se for falado de heroes, pegar a url /heroes, se falar de tempestade do deserto, pegar a url /desert-storm... "
                               "Se não encontrar informações, responda que não sabe. Não inventa informações falsas. ",
        
    ),
    )

    print("\nResposta do Agente LastWar:")
    print(response.text)
    print("-" * 50)
    return response.text

def discord_bot():
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f"Logado como {bot.user}")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

if __name__ == "__main__":
    print("Bem-vindo ao Agente LastWar com Gemini e busca na web!")
    #print(textHtml())
    criar_agente_last_war(fonte_url=fonte)

