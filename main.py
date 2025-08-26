# main.py

# 🚀 Módulo 01 - Bora começar!
def show_intro():
    print("Olá! Este é o módulo de introdução 🚀")


# 🤔 Módulo 02 - Testando umas lógicas
def basic_logic():
    x, y = 5, 3
    print(f"{x} + {y} = {x + y}")
    print(f"{x} > {y}? {x > y}")


# 🍎 Módulo 03 - Brincando com listas
def show_list_example():
    fruits = ["apple", "banana", "orange"]
    print("Lista de frutas:", fruits)
    print("Primeira fruta:", fruits[0])


# 🎬 Aqui é onde tudo acontece
def main():
    print("=== Projeto Código da Transformação em Python ===")

    print("\n👉 [Modulo 01] Introdução:")
    show_intro()

    print("\n👉 [Modulo 02] Lógica:")
    basic_logic()

    print("\n👉 [Modulo 03] Estruturas de Dados:")
    show_list_example()


if __name__ == "__main__":
    main()
