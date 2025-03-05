# Desafio: A Lista de Compras  

# Imagine que um cliente contrata você para criar uma aplicação de lista de compras 
# simples. Essa lista deverá ter uma série de funcionalidades que precisam ser 
# implementadas e que, ao final, deverá permitir que o usuário manipule os produtos na 
# lista. Portanto, você precisará elencar o que será necessário para que a lista seja 
# implementada, de acordo com as necessidades do cliente, utilizando seus conhecimentos
# em programação e implementá-las utilizando Python.

# Objetivo do desafio:Desenvolver um aplicativo que gerencie uma lista de compras que 
# permita adicionar, remover e listar os produtos adicionados nela. 

# Para isso, o seu aplicativo precisa ter as seguintes funcionalidades: 
# Menu de Opções
# Adicionar Produto
# Controle de ID Automático
# Remover Produto
# Pesquisar Produtos por Nome
# Listar Todos os Produtos
# Cabeçalho do Aplicativo
# Feedback de Ação
# Tratamento de Entradas Inválidas
# Encerramento do Programa
import json

ARQUIVO = "lista_de_compras.json"

class Produto:
    _contador_id = 1

    def __init__(self, nome, unidade_medida, quantidade, descricao):
        self.id = Produto._contador_id
        Produto._contador_id += 1

        self.nome = nome.strip().title()
        self.unidade_medida = unidade_medida
        self.quantidade = quantidade
        self.descricao = descricao.strip()

    def __str__(self):
        return (
            f"{self.quantidade}x {self.nome} {self.unidade_medida} (ID:{self.id})\n"
            f"  > Descrição: {self.descricao}"
        )

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "unidade_medida": self.unidade_medida,
            "quantidade": self.quantidade,
            "descricao": self.descricao
        }

    @staticmethod
    def do_dicionario(dicionario):
        produto = Produto(
            dicionario['nome'],
            dicionario['unidade_medida'],
            dicionario['quantidade'],
            dicionario['descricao']
        )
        produto.id = dicionario['id']
        return produto

def carregar_lista():
    """Carrega a lista de compras do arquivo JSON ou cria uma nova se não existir"""
    try:
        with open(ARQUIVO, "r") as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                return []
            
            dados = json.loads(conteudo)
            lista = [Produto.do_dicionario(item) for item in dados]
            
            if lista:
                Produto._contador_id = max(p.id for p in lista) + 1
            return lista
        
    except FileNotFoundError:
        print("\n(!) Arquivo não encontrado. Criando nova lista...")
        return []
    except json.JSONDecodeError:
        print("\n(!) Erro ao ler arquivo. Dados corrompidos. Criando nova lista...")
        return []

def salvar_lista(lista_compras):
    """Salva a lista de compras no arquivo JSON"""
    with open(ARQUIVO, "w") as arquivo:
        json.dump([p.para_dicionario() for p in lista_compras], arquivo, indent=4)

def menu_de_opcoes():
    """Retorna as opções principais do menu"""
    return {
        "A": "Adicionar produto",
        "B": "Remover produto",
        "C": "Pesquisar produtos",
        "D": "Sair do programa"
    }

def menu_de_medidas():
    """Retorna as opções de unidades de medida"""
    return {
        "A": "Quilograma",
        "B": "Grama",
        "C": "Litro",
        "D": "Mililitro",
        "E": "Unidade",
        "F": "Metro",
        "G": "Centímetro"
    }

def criar_produto():
    """Captura os dados do usuário e retorna um novo Produto"""
    medidas = menu_de_medidas()
    
    # Validação do nome
    nome = ""
    while not nome:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("ERRO: O nome não pode ser vazio!")

    # Seleção de unidade
    print("\nUnidades de medida disponíveis:")
    for chave, valor in medidas.items():
        print(f"  {chave}. {valor}")
    
    escolha = input("\nSelecione uma medida: ").upper()
    while escolha not in medidas:
        print("ERRO: Opção inválida!")
        escolha = input("Selecione uma medida (A-G): ").upper()
    
    # Validação da quantidade
    while True:
        quantidade = input("Quantidade: ")
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
            break
        except ValueError:
            print("ERRO: Quantidade deve ser um número inteiro positivo!")

    descricao = input("Descrição (opcional): ").strip()
    return Produto(nome, medidas[escolha], quantidade, descricao)

def adicionar_produto(lista_compras):
    """Adiciona um novo produto à lista"""
    produto = criar_produto()
    lista_compras.append(produto)
    print(f"\n(+) '{produto.nome}' adicionado com sucesso! ID: {produto.id}")

def remover_produto(lista_compras):
    """Remove um produto da lista com base no ID"""
    try:
        id_produto = int(input("ID do produto a remover: "))
    except ValueError:
        print("ERRO: ID deve ser um número!")
        return lista_compras
    
    for i, produto in enumerate(lista_compras):
        if produto.id == id_produto:
            removido = lista_compras.pop(i)
            print(f"\n(-) '{removido.nome}' (ID:{id_produto}) removido!")
            return lista_compras
    
    print(f"\n(!) ID {id_produto} não encontrado!")
    return lista_compras

def pesquisar_produtos(lista_compras):
    """Pesquisa produtos por nome (case-insensitive)"""
    termo = input("Pesquisar por: ").strip().lower()
    resultados = [
        p for p in lista_compras
        if termo in p.nome.lower()
    ]
    
    print(f"\n=== Resultados ({len(resultados)}) ===")
    for produto in resultados:
        print(produto)
    print("="*30)
    
    return resultados

def exibir_cabecalho(lista_compras):
    """Exibe o cabeçalho com informações da lista"""
    print("\n" + "*"*50)
    print(f"___ Lista de Compras Simples | Itens: {len(lista_compras)} ___".center(50))
    print("_"*50)

def main():
    lista_compras = carregar_lista()
    
    while True:
        exibir_cabecalho(lista_compras)
        
        # Exibir lista automaticamente
        if lista_compras:
            print("\nLista atual:")
            for produto in sorted(lista_compras, key=lambda x: x.id):
                print(f"  {produto}")
        else:
            print("\nSua lista está vazia. Adicione itens!")
        
        # Exibir menu
        print("\n" + "*"*50)
        print("Opções:")
        for chave, valor in menu_de_opcoes().items():
            print(f"  {chave}. {valor}")
        
        escolha = input("\nSelecione uma opção: ").upper()
        
        # Processar escolha
        if escolha == "A":
            adicionar_produto(lista_compras)
        elif escolha == "B":
            lista_compras = remover_produto(lista_compras)
        elif escolha == "C":
            pesquisar_produtos(lista_compras)
            input("\nPressione Enter para continuar...")
        elif escolha == "D":
            print("\nObrigado por usar a Lista de Compras Simples! Até mais!")
            break
        else:
            print("ERRO: Opção inválida! Tente novamente.")
        
        salvar_lista(lista_compras)

if __name__ == "__main__":
    main()