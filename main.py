import discord
import os
import asyncio
import logging
from groq import Groq
from flask import Flask
from threading import Thread

# Suprime logs do Flask e Werkzeug para saída mais limpa
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Crie uma instância do aplicativo web
app = Flask('')

@app.route('/')
def home():
    return "O bot está online!"

def run():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()

# --- Código do Bot Discord ---

# Pega as chaves das variáveis de ambiente
groq_api_key = os.getenv("GROQ_API_KEY")
discord_token = os.getenv("DISCORD_TOKEN")

# Verifica se as chaves foram encontradas
if not groq_api_key or not discord_token:
    print("Erro: Chaves de API e/ou Token do Discord não encontrados.")
    print("Por favor, adicione-os na seção 'Secrets' da sua plataforma online.")
    exit()

# Configura o cliente do Groq
client = Groq(api_key=groq_api_key)

# Configura o bot do Discord
intents = discord.Intents.default()
intents.message_content = True
discord_client = discord.Client(intents=intents)

@discord_client.event
async def on_ready():
    print(f'Bot está online como {discord_client.user}')

@discord_client.event
async def on_message(message):
    # 1. Ignora mensagens do próprio bot
    if message.author == discord_client.user:
        return

    # 2. Verifica se a mensagem foi enviada no canal específico
    if str(message.channel.id) == '1450307246616608889':
        try:
            # Usa o Groq para gerar a resposta
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, lambda: client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Responda sempre em português do Brasil. Seja útil e cordial."
                    },
                    {
                        "role": "user",
                        "content": message.content
                    }
                ]
            ))

            response_text = response.choices[0].message.content

            if response_text:
                # Divide a resposta se exceder 2000 caracteres (limite do Discord)
                if len(response_text) <= 2000:
                    await message.channel.send(response_text)
                else:
                    # Envia em partes
                    for i in range(0, len(response_text), 2000):
                        chunk = response_text[i:i+2000]
                        await message.channel.send(chunk)
            else:
                await message.channel.send("Desculpe, não consegui gerar uma resposta.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            await message.channel.send("Desculpe, não consegui gerar uma resposta.")

# Chama a função para rodar o servidor web
keep_alive()

# Roda o bot do Discord
discord_client.run(discord_token)
