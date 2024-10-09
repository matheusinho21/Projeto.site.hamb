import json

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def to_dict(self):
        return {"nome": self.nome, "preco": self.preco}

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Sabor:
    def __init__(self, nome):
        self.nome = nome

class Cliente:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador

class Pagamento:
    def __init__(self, metodo, valor_pago):
        self.metodo = metodo
        self.valor_pago = valor_pago

class Pedido:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)

class Hamburgueria:
    def __init__(self):
        self.produtos = []
        self.sabores = []
        self.pedidos = []
        self.clientes = []
        self.adicionar_produtos_iniciais()  # Adicionando produtos iniciais
    
    def adicionar_produtos_iniciais(self):
        self.cadastrar_produto("X Bacon", 23.90)
        self.cadastrar_produto("X Salada", 16.90)
        self.cadastrar_produto("X Frango", 19.90)
        self.cadastrar_produto("Coca-Cola 2L", 9.90)
        self.cadastrar_produto("Fanta Lata", 6.00)
        self.cadastrar_produto("Sprite 2L", 7.90)

    def cadastrar_produto(self, nome, preco):
        novo_produto = Produto(nome, preco)
        self.produtos.append(novo_produto)
        print(f'Produto {nome} cadastrado com sucesso!')

    def cadastrar_sabor(self, nome):
        novo_sabor = Sabor(nome)
        self.sabores.append(novo_sabor)
        print(f'Sabor {nome} cadastrado com sucesso!')

    def cadastrar_cliente(self, nome, identificador):
        novo_cliente = Cliente(nome, identificador)
        self.clientes.append(novo_cliente)
        print(f'Cliente {nome} cadastrado com sucesso!')

    def listar_produtos(self):
        print("Produtos disponíveis:")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto.nome} - R${produto.preco:.2f}")

    def listar_sabores(self):
        print("Sabores disponíveis:")
        for i, sabor in enumerate(self.sabores, start=1):
            print(f"{i}. {sabor.nome}")

    def fazer_pedido(self, cliente):
        print(f"Cliente: {cliente.nome} fazendo pedido.")
        pedido = Pedido()
        
        while True:
            self.listar_produtos()
            escolha_produto = input("Escolha o número do produto para adicionar ao pedido (ou '0' para finalizar): ")
            if escolha_produto == '0':
                break
            try:
                indice_produto = int(escolha_produto) - 1
                if 0 <= indice_produto < len(self.produtos):
                    pedido.adicionar_produto(self.produtos[indice_produto])
                    print(f"{self.produtos[indice_produto].nome} adicionado ao pedido.")
                else:
                    print("Produto inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")

        total = pedido.calcular_total()
        print(f'Total do pedido: R${total:.2f}')
        
        # Seleção de forma de pagamento
        print("Escolha a forma de pagamento:")
        print("1. Cartão de Crédito")
        print("2. Dinheiro")
        metodo_pagamento = input("Escolha uma opção: ")
        
        valor_pago = float(input("Digite o valor pago: R$"))
        
        if metodo_pagamento == '1':
            pagamento = Pagamento("Cartão de Crédito", valor_pago)
        elif metodo_pagamento == '2':
            pagamento = Pagamento("Dinheiro", valor_pago)
        else:
            print("Forma de pagamento inválida.")
            return

        print(f"Forma de pagamento escolhida: {pagamento.metodo}")
        print(f"Valor total do pedido: R${total:.2f}")
        print(f"Valor pago: R${pagamento.valor_pago:.2f}")

        if valor_pago >= total:
            troco = valor_pago - total
            print(f"Pagamento realizado com sucesso! Troco: R${troco:.2f}")
        else:
            falta = total - valor_pago
            print(f"Pagamento não realizado. Faltam R${falta:.2f}.")

def main():
    hamburgueria = Hamburgueria()

    while True:
        print("\n1. Cadastrar Produto")
        print("2. Cadastrar Sabor")
        print("3. Cadastrar Cliente")
        print("4. Fazer Pedido")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$"))
            hamburgueria.cadastrar_produto(nome, preco)
        elif opcao == '2':
            nome = input("Nome do sabor: ")
            hamburgueria.cadastrar_sabor(nome)
        elif opcao == '3':
            nome = input("Nome do cliente: ")
            identificador = input("Identificador (CPF ou e-mail): ")
            hamburgueria.cadastrar_cliente(nome, identificador)
        elif opcao == '4':
            if not hamburgueria.clientes:
                print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
                continue
            nome_cliente = input("Nome do cliente: ")
            cliente = next((c for c in hamburgueria.clientes if c.nome == nome_cliente), None)
            if cliente:
                hamburgueria.fazer_pedido(cliente)
            else:
                print("Cliente não encontrado.")
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
