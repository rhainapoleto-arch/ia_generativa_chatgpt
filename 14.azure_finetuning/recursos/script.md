
# Endereço de documentação criação Chave API OpenAI
https://developers.openai.com/api/reference/overview#authentication

# Vídeo Referência do Projeto
https://youtu.be/fOYZJdwkrIQ?si=mL87K5GsZmIszqoH

1. Vamos começar criando nosso ambiente virtual venv
python -m venv 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate

2. Vamos criar nosso arquivo .env para proteger nossas chaves de API
AZURE_OPENAI_API_KEY="sua_chave_aqui"
AZURE_OPENAI_ENDPOINT="https://seu-recurso.openai.azure.com/"
AZURE_OPENAI_API_VERSION="2024-05-01-preview"

3. Instalar a biblioteca dotenv, que ira carregar a chave do arquivo .env
pip install openai python-dotenv

4. Instalar a biblioteca da OpenAI
pip install openai

Quando usamos o ChatGPT no dia a dia. Acabamos criando um tipo de FineTuning diário
Pois vamos treinando o agente de forma gradativa.
Nesse caso quando vamos treinar nosso próprio agente.
Preciso seguir um script de construção que oriente nosso agente

# Exemplo 1: Cenário de Infraestrutura e Redes (Foco em comandos de Firewall)
{"messages": [{"role": "system", "content": "Você é um assistente sênior de infraestrutura de TI, especializado em firewalls OPNsense e Proxmox. Seja direto e objetivo."}, {"role": "user", "content": "Como eu configuro o disco paralelo de 2TB no Proxmox como unidade de backup?"}, {"role": "assistant", "content": "Para usar um disco paralelo como repositório de backup no Proxmox, acesse a interface web, vá em Datacenter > Storage > Add > Directory. Defina o ID (ex: backup-disco), aponte o caminho do ponto de montagem do novo disco (ex: /mnt/backup2tb) e selecione o tipo de conteúdo como 'VZDump backup file'."}]}

# Exemplo 2: Cenário de Programação e Banco de Dados (Foco em Scripts Python/SQL)
{"messages": [{"role": "system", "content": "Você é um desenvolvedor Python especialista em automação e integração com bancos de dados relacionais como MariaDB."}, {"role": "user", "content": "Como faço para tratar erros de conexão ao tentar salvar registros em massa usando o conector do MariaDB?"}, {"role": "assistant", "content": "Você deve envolver a operação de inserção em um bloco try-except e garantir o uso do método commit() ou rollback() em caso de exceção. Exemplo:\n\ntry:\n    cursor.executemany(sql, dados)\n    conexao.commit()\nexcept Exception as e:\n    conexao.rollback()\n    print(f'Erro na transação: {e}')\nfinally:\n    cursor.close()"}]}

# Exemplo 3: Cenário de Atendimento e Normas Institucionais (Foco em Suporte a Alunos)
{"messages": [{"role": "system", "content": "Você é um representante de atendimento ao estudante da FATEC. Responda de forma cordial, clara e institucional."}, {"role": "user", "content": "Quais são os passos para submeter uma denúncia formal ou solicitação à Comissão de Self-Evaluation (CPA)?"}, {"role": "assistant", "content": "Para submeter uma manifestação à CPA, o corpo discente deve redigir o documento formal contendo a exposição dos fatos, anexar as evidências pertinentes e encaminhar por meio dos canais oficiais institucionais da unidade ou da Ouvidoria competente do Centro Paula Souza."}]}

IA aprende o tom de voz (system), compreende o problema exato (user) e entrega a estrutura de raciocínio desejada (assistant) para qualquer nicho específico que eles decidam treinar!

5. Demostrar aos alunos o validador de JSON que usaremos para treinar o nosso agente

Tipos de arquivos aceitos: CSV, TSV, XLSX, JSON, JSONL

5.1. Exemplo de Arquivo CSV (Comma-Separated Values)
O formato CSV é baseado em texto plano onde os dados são separados por vírgulas (ou ponto e vírgula), organizados em linhas e colunas (como uma tabela de Excel simplificada). A primeira linha costuma ser o cabeçalho.

5.2. Aqui está um exemplo prático do formato TSV (Tab-Separated Values) para você apresentar aos seus alunos:

O TSV é muito parecido com o CSV, mas em vez de usar vírgulas para separar as colunas, ele utiliza tabulações (a tecla Tab do teclado). É muito utilizado quando os seus dados textuais contêm muitas vírgulas, o que evitaria quebra de formatação.


5.3. O XLSX é o formato padrão do Microsoft Excel baseado em arquivos compactados em XML (OpenXML). Diferente dos arquivos de texto plano (como CSV, TSV e JSONL), ele é um formato binário estruturado em planilhas.

Como funciona na prática para IA: O arquivo XLSX organiza os dados em linhas e colunas tradicionais (células), permitindo que o usuário utilize abas, fórmulas e formatações visuais.

Uso em Fine-Tuning: Embora os modelos de IA e as ferramentas de treinamento não leiam um arquivo XLSX diretamente (sendo necessário convertê-lo para JSONL antes do envio), o Excel é amplamente utilizado por analistas e desenvolvedores na fase de organização, limpeza e montagem inicial dos datasets de perguntas e respostas.

5.4. Exemplo de Arquivo JSON (JavaScript Object Notation)
O formato JSON utiliza uma estrutura hierárquica baseada em chaves e valores (chave: valor), permitindo representar objetos complexos, listas e dados aninhados com muita facilidade.

5.5. Aqui está um exemplo prático do formato JSONL (JSON Lines), que é o formato padrão obrigatório exigido para o fine-tuning de modelos baseados em chat (messages):

Dica para explicar aos alunos: Diferente de um arquivo JSON tradicional (que fica dentro de uma única lista [...]), no JSONL cada linha do arquivo é um objeto JSON completamente independente, separado por quebras de linha (\n). Isso permite que ferramentas de IA processem arquivos gigantescos linha por linha de forma muito mais eficiente, sem precisar carregar a estrutura inteira na memória de uma só vez

6. Mostrar aos alunos o arquivo erp.csv, motrar a migração para xlsx. 

7. Instalação da Bliblioteca Pandas, para demonstração conversor_xlsx_jsonl.py
pip install pandas openpyxl

8. Prompt para pedir a IA apoio para gerar o material de Jsonl para realizar fine-tuning de IA

Aqui está o comando reescrito e otimizado para você enviar a uma IA Generativa, adaptado exatamente para a criação de um dataset voltado ao fine-tuning moderno (formato de chat messages com papéis system, user e assistant) baseado na documentação que você enviar:

Você deverá me ajudar a estruturar e transformar uma documentação técnica completa de software em pares de treinamento para fine-tuning de inteligência artificial (utilizando o padrão moderno de chat em formato JSONL, com os papéis system, user e assistant).

Eu vou lhe enviar trechos de documentações, e você deve me devolver o conteúdo processado seguindo exatamente este padrão estruturado:

- system: Defina o papel ou persona técnica que o modelo deve assumir (ex: assistente de suporte sênior, especialista em CRM/ERP, etc.).

- user: Crie uma pergunta ou comando realista que um usuário final ou operador faria sobre aquele trecho da documentação.

- assistant: Elabore a resposta técnica ideal, precisa e completa que o modelo deve aprender a entregar.

Regras importantes para a resposta:

1. Para cada trecho de texto que eu enviar, crie 3 variações diferentes de perguntas (user) mantendo a mesma intenção, mas usando palavras e abordagens distintas, acompanhadas de suas respectivas respostas ideais (assistant).

2. Devolva o conteúdo em formato limpo ou em blocos de texto estruturados, prontos para serem revisados e inseridos em uma planilha ou arquivo de dados.

3. Não inclua conversas desnecessárias ou introduções longas; foque puramente na entrega dos pares de treinamento solicitados.

Responda apenas com "OK" para confirmar que entendeu as diretrizes e aguarde o envio do primeiro texto da documentação.

https://www.totvs.com/blog/inovacoes/fine-tuning/

Documentação Oficial Azure

https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning

# Depois de montar o arquivo manual_python.xlsx - (system,user,assistant)
Explicar o conversor de xlsx para jsonl
Realizar a conversão do arquivo.

# O Papel de uma LLM, Agente de IA e Finetuning

A __LLM__ (O Cérebro): É o motor de linguagem. Ela processa texto, entende contexto e gera respostas. Sozinha, ela apenas "conversa" e responde perguntas com base no que está na tela ou na memória dela.

O __Fine-Tuning__ (A Especialização): É a lapidação desse cérebro. Ele garante que a forma de falar, o tom técnico e as diretrizes estejam rigorosamente alinhados aos manuais e às regras da sua empresa.

O __Agente de IA__ (As Mãos e Ferramentas): É um sistema construído em cima da LLM para dar a ela autonomia e capacidade de ação. Enquanto uma LLM comum apenas responde "Para reiniciar o serviço, digite X", um agente de IA pode receber o problema, decidir qual ferramenta usar, conectar-se via API (como no seu n8n e WAHA), acessar um banco de dados MariaDB, rodar o comando de reinicialização no servidor e verificar se o sistema voltou a funcionar.

