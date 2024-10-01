
clientes = {}
produtos = {}
pedidos = []

def cadastrar_cliente(nome, telefone):
    clientes[nome] = telefone
    print(f"Cliente {nome} cadastrado com sucesso!")

def cadastrar_produto(nome, preco):
    produtos[nome] = preco
    print(f"Produto {nome} cadastrado com sucesso!")

def visualizar_clientes():
    print("Lista de Clientes:")
    for nome, telefone in clientes.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

def visualizar_produtos():
    print("Lista de Produtos:")
    for nome, preco in produtos.items():
        print(f"Produto: {nome}, Preço: R${preco:.2f}")

def fazer_pedido(cliente_nome, produtos_pedidos):
    if cliente_nome not in clientes:
        print("Cliente não encontrado!")
        return
    
    pedido = {
        'cliente': cliente_nome,
        'produtos': produtos_pedidos
    }
    pedidos.append(pedido)
    print(f"Pedido feito com sucesso para {cliente_nome}!")

def visualizar_pedidos():
    print("Lista de Pedidos:")
    for pedido in pedidos:
        print(f"Cliente: {pedido['cliente']}, Produtos: {pedido['produtos']}")


cadastrar_cliente("Cleyton", "1234-5678")
cadastrar_cliente("Kauanne", "9876-5432")
cadastrar_produto("Hamburguer", 29.90)
cadastrar_produto("Refrigerante", 9.00)

visualizar_clientes()
visualizar_produtos()

fazer_pedido("Cleyton", ["Hamburguer", "Refrigerante"])
fazer_pedido("Kauanne", ["Hamburguer"])

visualizar_pedidos()

