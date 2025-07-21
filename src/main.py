import os
import sys
from dotenv import load_dotenv
from urllib.parse import urljoin
from google import genai
from google.genai import types
from bs4 import BeautifulSoup
import requests
import csv
import re
from pathlib import Path


# --- Configuração da API Key ---
load_dotenv()

def extract_content_full_urls():
    """
    Extrai conteúdo de URLs do site Last War Tutorial e salva em arquivos de texto.
    """
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

def carrega_arquivos_como_fonte():
    
    caminho_pasta = Path('./data')

    arquivos = [file.name for file in caminho_pasta.iterdir() if file.is_file()]
    arquivos_carregados = []
    client = genai.Client()


    for file in arquivos:
        uploaded_file = client.files.upload(file=f"{caminho_pasta}/{file}", config={"mime_type": "text/plain"})
        print(f"Arquivo {file} carregado como '{uploaded_file.name}'.  carregado com sucesso!")
        #sys.stdout.flush()
        arquivos_carregados.append(uploaded_file)
    return arquivos_carregados
    

def criar_agente_last_war():
    """
    Cria um agente LastWar que responde perguntas sobre o jogo Last War: Survival usando a API Gemini.
    """
    client = genai.Client()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    arquivos_existentes = client.files.list()

    if not arquivos_existentes:
        print("Nenhum arquivo carregado. Carregando arquivos...")
        arquivos_existentes = carrega_arquivos_como_fonte()

    campo = input("Digite sua pergunta sobre LastWar: ")

    prompt = (
        "Você é um especialista em Last War: Survival. "
        "Responda baseado APENAS nas informações dos documentos fornecidos. "
        f"Pergunta: {campo}"
    )

    content_parts = [prompt] + arquivos_existentes

    response = model.generate_content(
        content_parts,
        generation_config={
            #"max_output_tokens": 500,
            "temperature": 0.7,
        }
    )

    resposta_chat = response.text
    print("\nResposta do Agente LastWar:")
    print(resposta_chat)
    print("-" * 50)

def remover_todos_arquivos():

    client = genai.Client()
    arquivos = client.files.list()
    print(f"Encontrados {len(arquivos)} arquivos...")
    for arquivo in arquivos:
        print(arquivo.name)

    confirmacao = input("Deseja remover todos os arquivos? (s/n): ")
    if confirmacao.lower() == 's':
        for arquivo in arquivos:
            client.files.delete(arquivo.name)
            print(f"Arquivo {arquivo.name} removido com sucesso!")

if __name__ == "__main__":
    print("Bem-vindo ao Agente LastWar com Gemini!")
    #extract_content_full_urls()
    carrega_arquivos_como_fonte()

    # conteudo = t2()
    # nome_do_arquivo = "data/meu_arquivo.txt"

    # with open(nome_do_arquivo, "w") as arquivo:
    #     arquivo.write(conteudo)

    # print(f"Arquivo '{nome_do_arquivo}' salvo com sucesso!")

    