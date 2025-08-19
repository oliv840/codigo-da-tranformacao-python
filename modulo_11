import sqlite3

# Função para conectar ao banco de dados e criar a tabela
def setup_database(db_name='clientes.db'):
    """Conecta ao banco de dados e cria a tabela Clientes, se ela não existir."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Operação 1: Inserir um novo cliente (Create)
def inserir_cliente(nome, email, db_name='clientes.db'):
    """Insere um novo cliente na tabela."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        print(f"Cliente '{nome}' inserido com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: O e-mail '{email}' já existe no banco de dados.")
    finally:
        if conn:
            conn.close()

# Operação 2: Consultar todos os clientes (Read)
def consultar_clientes(db_name='clientes.db'):
    """Consulta e exibe todos os clientes."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conn.close()
    
    if not clientes:
        print("Nenhum cliente encontrado.")
        return
    
    print("\n--- Lista de Clientes ---")
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, E-mail: {cliente[2]}")
    print("-------------------------")

# Operação 3: Atualizar um cliente (Update)
def atualizar_cliente(cliente_id, novo_nome, novo_email, db_name='clientes.db'):
    """Atualiza o nome e e-mail de um cliente pelo ID."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE Clientes SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, cliente_id))
    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        print(f"Cliente com ID {cliente_id} atualizado com sucesso!")
    else:
        print(f"Erro: Cliente com ID {cliente_id} não encontrado.")

# Operação 4: Deletar um cliente (Delete)
def deletar_cliente(cliente_id, db_name='clientes.db'):
    """Deleta um cliente pelo ID."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        print(f"Cliente com ID {cliente_id} deletado com sucesso!")
    else:
        print(f"Erro: Cliente com ID {cliente_id} não encontrado.")

# Consultas avançadas (Filtro)
def buscar_clientes_por_nome(termo, db_name='clientes.db'):
    """Busca clientes cujo nome começa com um termo específico."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Usando LIKE para busca parcial e % para corresponder a qualquer sequência
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (termo + '%',))
    clientes = cursor.fetchall()
    conn.close()
    
    if not clientes:
        print(f"Nenhum cliente encontrado com nome começando com '{termo}'.")
        return
    
    print(f"\n--- Clientes com nome começando com '{termo}' ---")
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, E-mail: {cliente[2]}")
    print("--------------------------------------------------")

# Exemplo de uso
if __name__ == '__main__':
    # 1. Configurar o banco de dados e a tabela
    setup_database()

    # 2. Inserir clientes
    inserir_cliente("Ana Silva", "ana.silva@email.com")
    inserir_cliente("Bruno Costa", "bruno.costa@email.com")
    inserir_cliente("Amanda Pereira", "amanda.pereira@email.com")

    # 3. Consultar todos os clientes
    consultar_clientes()

    # 4. Atualizar um cliente
    atualizar_cliente(2, "Bruno Souza", "bruno.souza@email.com")
    consultar_clientes()

    # 5. Consultas SQL para filtrar dados
    buscar_clientes_por_nome("A")

    # 6. Deletar um cliente
    deletar_cliente(1)
    consultar_clientes()
