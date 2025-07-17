import google.generativeai as genai, types
import os
from dotenv import load_dotenv

# --- Configuração da API Key ---
load_dotenv()

def t2():
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    client = genai.GenerativeModel("gemini-1.5-flash")

    # Define the grounding tool
    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    # Configure generation settings
    config = types.GenerateContentConfig(
        tools=[grounding_tool]
    )

    # Make the request
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Who won the euro 2024?",
        config=config
    )

    # Print the grounded response
    print(response.text)


def criar_agente_last_war():
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

    campo = input("Digite sua pergunta sobre LastWar: ")

    prompt = (
        "Você é um assistente e sabe tudo sobre o jogo LastWar mobile. "
        "Tudo que perguntarem sobre o jogo, você irá responder, podendo usar como base para as respostas o site https://www.lastwartutorial.com/. "
        f"Pergunta do utilizador: {campo}"
    )

    response = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": 500,
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

    