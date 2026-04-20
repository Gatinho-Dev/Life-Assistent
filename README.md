# 🤖 Life Assistant

> Um bot inteligente para Discord com IA (Groq), capaz de responder mensagens, conversar em DM e enviar conteúdos automaticamente no privado.

---

## 🧠 Sobre o projeto

O **Life Assistant** é um bot desenvolvido para funcionar como um assistente dentro do Discord.

Ele usa inteligência artificial para:
- responder perguntas
- conversar naturalmente
- lembrar contexto recente
- enviar mensagens automaticamente na DM quando solicitado

---

## 🚀 Como funciona

O bot depende de duas coisas essenciais:

### 🔑 Token do Discord
Permite que o bot conecte e funcione dentro do Discord.

### 🧠 API da Groq
Permite que o bot gere respostas com inteligência artificial.

👉 Sem esses dois, o bot **não funciona**.

---

## 📦 Instalação

```bash
git clone https://github.com/SEU-USUARIO/life-assistant.git
cd life-assistant
pip install -r requirements.txt
```

---

## ⚙️ Configuração (.env)

Crie um arquivo `.env` na raiz do projeto:

```env
DISCORD_TOKEN=SEU_TOKEN_AQUI
GROQ_API_KEY=SUA_API_KEY_AQUI
```

---

## 🤖 Como pegar o TOKEN do Discord

1. Acesse: https://discord.com/developers/applications  
2. Clique em **New Application**  
3. Vá em **Bot**  
4. Clique em **Add Bot**  
5. Copie o Token  
6. Cole no `.env`

⚠️ Nunca compartilhe esse token.

---

## 🧠 Como pegar a API da Groq

1. Acesse: https://console.groq.com  
2. Crie uma conta  
3. Vá em **API Keys**  
4. Clique em **Create API Key**  
5. Copie a chave  
6. Cole no `.env`

---

## ▶️ Como rodar

```bash
python main.py
```

---

## 💬 Uso

- Marque o bot no servidor
- Ou responda uma mensagem dele

Exemplo:
```
@Life Assistant me manda isso na dm
```

👉 Ele responde no canal e também na DM

---

## 📄 Licença

MIT

---

## 💡 Autor

Furry's Life Inc
