cadastros = [
    {
        "id":1042,
        "perfil":
        {
            "nome":"Mariana",
            "email":"mariana@gmail.com,"
        }
    },
    {
    "id":1043,
    "perfil": 
    {    
        "nome":"Luís",
        "email":"luis@gmail.com"
    }
    }
]

for item in cadastros:
    id_formulario = item.get("id")
    perfil_extraido = item.get("perfil")
    nome_usuario = perfil_extraido.get("nome")
    telefone_usuario = perfil_extraido.get("telefone")

print(f"ID:{id_formulario} | Usuário: {nome_usuario} | Telefone: {telefone_usuario}")