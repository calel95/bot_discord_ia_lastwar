import os
from dotenv import load_dotenv
from urllib.parse import urljoin
from google import genai
from google.genai import types
from bs4 import BeautifulSoup
import requests
import csv
import re

# --- Configuração da API Key ---
load_dotenv()

def t2():
    base_url = "https://www.lastwartutorial.com"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    menu_links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        # Filtrar apenas links internos relevantes do menu
    #if any(section in href for section in ['heroes', 'squads', 'buildings']):
        full_url = urljoin(base_url, href)
        if  ".com/" in full_url and not "#" in full_url and not "play.google.com" in full_url and not "apps.apple.com" in full_url:
            #print(full_url)
            menu_links.append(full_url)

    #print(menu_links)

    for url in menu_links:
        response = requests.get(url)
        section_soup = BeautifulSoup(response.text, "html.parser")
        #print(section_soup) #pega todo o html da pagina principal
        trata_nome_url = (url.split('.com/', 1)[1]).replace('/', '')
        nome_do_arquivo = f"data/{trata_nome_url}.txt"

        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            for section in section_soup:
                texto = section.get_text(strip=True)
                if texto:  # evitar escrever vazios
                    arquivo.write(texto + "\n\n")
                    #print(texto)  # se quiser ver o que está salvando


def criar_agente_last_war():
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")

    campo = input("Digite sua pergunta sobre LastWar: ")

    prompt = (
        "Você é um assistente e sabe tudo sobre o jogo Last War: Survival. "
        "Tudo que perguntarem sobre o jogo, você irá responder. "
        f"Pergunta do usuario: {campo}"
    )

    response = model.generate_content(
        prompt,
        generation_config={
            #"max_output_tokens": 500,
            "temperature": 0.7,
        }
    )

    resposta_chat = response.text
    print("\nResposta do Agente LastWar:")
    print(resposta_chat)
    print("-" * 50)


if __name__ == "__main__":
    print("Bem-vindo ao Agente LastWar com Gemini!")
    t2()

    # conteudo = t2()
    # nome_do_arquivo = "data/meu_arquivo.txt"

    # with open(nome_do_arquivo, "w") as arquivo:
    #     arquivo.write(conteudo)

    # print(f"Arquivo '{nome_do_arquivo}' salvo com sucesso!")

    