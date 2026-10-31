import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

modelo_deploy = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print(f"--- Agente conectado ao modelo: {modelo_deploy} ---")
print("Digite sua pergunta abaixo (ou digite 'sair' para encerrar):\n")

while True:
    # Recebe a pergunta direto do seu teclado no terminal
    pergunta_usuario = input("Você: ")
    
    if pergunta_usuario.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat de teste.")
        break
        
    if not pergunta_usuario.strip():
        continue

    try:
        # Envia a pergunta para o Azure usando o fine-tuned
        resposta = client.chat.completions.create(
            model=modelo_deploy,
            messages=[
                {"role": "system", "content": "Você é um assistente técnico especializado com base nos dados de infraestrutura."},
                {"role": "user", "content": pergunta_usuario}
            ],
            temperature=0.3
        )
        
        print("\nAgente:", resposta.choices[0].message.content)
        print("-" * 50)
        
    except Exception as e:
        print(f"\n[Erro na requisição]: {e}\n")