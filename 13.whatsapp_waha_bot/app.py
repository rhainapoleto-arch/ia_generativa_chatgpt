import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from services import gerar_resposta_ia

# Carrega as variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurações do WAHA obtidas do .env
WAHA_URL = os.getenv("WAHA_URL")
WAHA_API_KEY = os.getenv("WAHA_API_KEY")

def enviar_mensagem_waha(chat_id: str, mensagem: str) -> bool:
    """Envia a mensagem gerada pela IA de volta para o WhatsApp através da API do WAHA."""
    url = f"{WAHA_URL}/api/sendText"
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": WAHA_API_KEY
    }
    payload = {
        "session": "default",
        "chatId": chat_id,
        "text": mensagem
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.status_code in [200, 201]
    except Exception as e:
        print(f"Erro ao enviar mensagem via WAHA: {e}")
        return False

@app.route("/webhook", methods=["POST"])
def webhook():
    """Endpoint que recebe os eventos de mensagens do WAHA."""
    dados = request.get_json()
    
    if not dados or "payload" not in dados:
        return jsonify({"status": "ignored"}), 200

    payload = dados.get("payload", {})
    
    # Evita responder às próprias mensagens do bot
    if payload.get("fromMe", False):
        return jsonify({"status": "ignored_from_me"}), 200

    chat_id = payload.get("from")
    mensagem_usuario = payload.get("body", "")

    if chat_id and mensagem_usuario:
        print(f"\n📩 Mensagem recebida de {chat_id}: '{mensagem_usuario}'")
        
        # 1. Processa a mensagem com a Azure OpenAI + RAG (services.py)
        resposta_ia = gerar_resposta_ia(mensagem_usuario)
        print(f"🤖 Resposta gerada: '{resposta_ia}'")
        
        # 2. Envia de volta para o WhatsApp
        enviado = enviar_mensagem_waha(chat_id, resposta_ia)
        if enviado:
            print("✅ Mensagem enviada com sucesso para o WhatsApp!")
        else:
            print("❌ Falha no envio da mensagem via WAHA.")

    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"🚀 Servidor Flask iniciado na porta {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)