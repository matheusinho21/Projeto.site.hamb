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
        # Adicionando hambúrgueres iniciais com preços atualizados
        self.cadastrar_produto("X Bacon", 23.90)
        self.cadastrar_produto("X Salada", 16.90)

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
        pagamento = input("Deseja realizar o pagamento? (s/n): ")
        if pagamento.lower() == 's':
            print("Pagamento realizado com sucesso!")
        else:
            print("Pedido não finalizado.")

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
