funcionarios = {
    101: {
        "nome": "Carlos",
        "cargo": "desenvolvedor",
        "habilidades": ["Python", "C##","Java"]
    },
    102: {
        "nome": "Maria",
        "cargo": "gerente de projetos",
        "habilidades": ["Srcum", "Gestão"]
    }
}

print (funcionarios[101]["cargo"])
print(funcionarios.get(102,{}).get("nome"))
print(funcionarios.get(103,{}).get("nome", "Funcionário não encontrado"))