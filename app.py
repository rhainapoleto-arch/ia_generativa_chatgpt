import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from src.tools import processar_pdf, consultar_base_conhecimento

# 1. Inicialização da aplicação Flask
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# 2. Configuração da pasta onde os arquivos PDF serão armazenados
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'pdfs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Restrição de extensões permitidas
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    """Verifica se o arquivo enviado possui a extensão .pdf"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    """Rota principal: carrega a interface gráfica do chatbot"""
    return render_template("index.html")


@app.route("/api/pdfs", methods=["GET"])
def listar_pdfs():
    """Endpoint API: Retorna a lista de PDFs armazenados no servidor"""
    try:
        arquivos = os.listdir(app.config['UPLOAD_FOLDER'])
        pdfs = [f for f in arquivos if f.lower().endswith('.pdf')]
        return jsonify({"status": "sucesso", "arquivos": pdfs})
    except Exception as e:
        return jsonify({"status": "erro", "arquivos": [], "mensagem": str(e)})


@app.route("/perguntar", methods=["POST"])
def perguntar():
    """Endpoint API: Recebe a pergunta do usuário e executa a busca RAG"""
    dados = request.get_json()
    pergunta_usuario = dados.get("pergunta", "")
    
    if not pergunta_usuario.strip():
        return jsonify({"resposta": "Por favor, digite uma pergunta válida."})
    
    try:
        # Invocação da ferramenta de busca RAG criada em src/tools.py
        resposta = consultar_base_conhecimento.invoke(pergunta_usuario)
        return jsonify({"resposta": resposta})
    except Exception as e:
        return jsonify({"resposta": f"Erro ao processar a requisição: {str(e)}"}), 500


@app.route("/upload", methods=["POST"])
def upload_pdf():
    """Endpoint API: Recebe, salva e vetoriza automaticamente um novo PDF"""
    if 'file' not in request.files:
        return jsonify({"status": "erro", "mensagem": "Nenhum arquivo enviado."}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"status": "erro", "mensagem": "Nenhum arquivo selecionado."}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        caminho_salvamento = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(caminho_salvamento)
        
        # Processa o PDF e atualiza a base no ChromaDB imediatamente
        try:
            processar_pdf()
            return jsonify({
                "status": "sucesso", 
                "mensagem": f"PDF '{filename}' enviado e vetorizado no ChromaDB com sucesso!"
            })
        except Exception as e:
            return jsonify({
                "status": "erro", 
                "mensagem": f"PDF salvo em disco, mas ocorreu um erro na vetorização: {str(e)}"
            }), 500
    else:
        return jsonify({"status": "erro", "mensagem": "Apenas arquivos PDF são permitidos."}), 400


@app.route("/remover/<filename>", methods=["DELETE"])
def remover_pdf(filename):
    """Endpoint API: Exclui o arquivo PDF e ressincroniza o banco vetorial"""
    filename = secure_filename(filename)
    caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(caminho_arquivo):
        try:
            # 1. Apaga o arquivo físico da pasta pdfs/
            os.remove(caminho_arquivo)

            # 2. Recria a base vetorial sem o arquivo apagado
            processar_pdf()

            return jsonify({
                "status": "sucesso",
                "mensagem": f"PDF '{filename}' removido e base de conhecimento atualizada!"
            })
        except Exception as e:
            return jsonify({"status": "erro", "mensagem": f"Erro ao excluir arquivo: {str(e)}"}), 500
    else:
        return jsonify({"status": "erro", "mensagem": "Arquivo não encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)