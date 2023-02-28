'''
Code projeto visto em vídeos na internet

'''

# passo 1
candidatos = []

# passo 2
while True:
    nome = input("Digite o nome do candidato (ou digite 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    candidatos.append({"nome": nome, "votos": 0})

# passo 3
funcionarios = []

# passo 4
while True:
    nome = input("Digite o nome do funcionário (ou digite 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    setor = input("Digite o setor do funcionário: ")
    funcionarios.append({"nome": nome, "setor": setor})

# passo 5
votos = {}
for funcionario in funcionarios:
    votos[funcionario["nome"]] = None

# passo 6
for funcionario in funcionarios:
    while True:
        print(f"Olá, {funcionario['nome']}! Por favor, vote em um candidato:")
        for i, candidato in enumerate(candidatos):
            print(f"{i + 1}. {candidato['nome']} ({candidato['votos']} votos)")
        voto = input("Digite o número do candidato escolhido: ")
        try:
            voto = int(voto)
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue
        if voto < 1 or voto > len(candidatos):
            print("Valor inválido. Tente novamente.")
            continue
        candidato = candidatos[voto - 1]
        votos[funcionario["nome"]] = candidato["nome"]
        candidato["votos"] += 1
        break

# passo 8
vencedor = max(candidatos, key=lambda candidato: candidato["votos"])
total_votos = sum(candidato["votos"] for candidato in candidatos)

# passo 9
print("Resultado:")
for candidato in candidatos:
    print(f"{candidato['nome']}: {candidato['votos']} votos ({candidato['votos'] / total_votos * 100:.2f}%)")
print(f"Total de votos: {total_votos}")
print(f"Vencedor: {vencedor['nome']} com {vencedor['votos']} votos ({vencedor['votos'] / total_votos * 100:.2f}%)")
