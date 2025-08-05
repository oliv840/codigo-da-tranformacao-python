import json

def gerenciar_notas_clientes(nome_arquivo):
    """
    Permite adicionar notas de clientes, salvá-las em um arquivo JSON,
    e depois carregar e exibir os dados.
    """
    notas_clientes = {}

    # Tenta carregar dados existentes, se houver
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            notas_clientes = json.load(arquivo)
            print("Dados existentes carregados.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo não encontrado ou vazio. Começando com um novo dicionário.")

    # Adicionar novas notas
    print("\n--- Adicionar novas notas de clientes ---")
    while True:
        cliente = input("Digite o nome do cliente (ou 'parar' para salvar): ")
        if cliente.lower() == 'parar':
            break
        try:
            nota = float(input(f"Digite a nota para '{cliente}': "))
            notas_clientes[cliente] = nota
        except ValueError:
            print("Por favor, digite um número válido para a nota.")

    # Salvar os dados atualizados
    print(f"\n--- Salvando dados em '{nome_arquivo}' ---")
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(notas_clientes, arquivo, indent=4)
    print("Dados salvos com sucesso.")

    # Exibir os dados finais
    print("\n--- Exibindo todas as notas de clientes ---")
    if notas_clientes:
        for cliente, nota in notas_clientes.items():
            print(f"- {cliente}: {nota}")
    else:
        print("Nenhuma nota de cliente para exibir.")

# Exemplo de uso
gerenciar_notas_clientes("notas_clientes_interativo.json")
