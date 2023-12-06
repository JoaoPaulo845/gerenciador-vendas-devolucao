#RECOMENDADO USAR GOOGLE COLLAB OU JUPYTER
#1
import os
import pandas as pd

# Estrutura inicial do DataFrame
colunas = ['ID', 'Produto', 'Quantidade', 'Preço', 'Tipo']  # 'Venda' ou 'Devolução'
df = pd.DataFrame(columns=colunas)

def adicionar_registro(produto, quantidade, preco, tipo):
    global df
    novo_id = len(df) + 1
    df.loc[novo_id] = [novo_id, produto, quantidade, preco, tipo]

def visualizar_registros():
    global df
    print(df)

def salvar_dados():
    global df
    if not os.path.exists('dados'):
        os.makedirs('dados')
    df.to_csv('dados/registros.csv', index=False)

def carregar_dados():
    global df
    if os.path.exists('dados/registros.csv'):
        df = pd.read_csv('dados/registros.csv')

# Interface de usuário no terminal
def menu():
    while True:
        print("\nGerenciador de Vendas e Devoluções")
        print("1. Adicionar venda/devolução")
        print("2. Visualizar registros")
        print("3. Salvar dados")
        print("4. Carregar dados")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            produto = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            tipo = input("Tipo ('Venda' ou 'Devolução'): ")
            adicionar_registro(produto, quantidade, preco, tipo)
        elif escolha == '2':
            visualizar_registros()
        elif escolha == '3':
            salvar_dados()
        elif escolha == '4':
            carregar_dados()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu()

#2 visualizar dataframe

df
