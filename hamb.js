
let clientes = {};
let produtos = {};
let pedidos = [];


function cadastrarCliente(nome, telefone) {
    clientes[nome] = telefone;
    console.log(`Cliente ${nome} cadastrado com sucesso!`);
}


function cadastrarProduto(nome, preco) {
    produtos[nome] = preco;
    console.log(`Produto ${nome} cadastrado com sucesso!`);
}


function visualizarClientes() {
    console.log("Lista de Clientes:");
    for (let nome in clientes) {
        console.log(`Nome: ${nome}, Telefone: ${clientes[nome]}`);
    }
}


function visualizarProdutos() {
    console.log("Lista de Produtos:");
    for (let nome in produtos) {
        console.log(`Produto: ${nome}, Preço: R$${produtos[nome].toFixed(2)}`);
    }
}


function fazerPedido(clienteNome, produtosPedidos) {
    if (!clientes[clienteNome]) {
        console.log("Cliente não encontrado!");
        return;
    }
    
    let pedido = {
        cliente: clienteNome,
        produtos: produtosPedidos
    };
    pedidos.push(pedido);
    console.log(`Pedido feito com sucesso para ${clienteNome}!`);
}


function visualizarPedidos() {
    console.log("Lista de Pedidos:");
    for (let pedido of pedidos) {
        console.log(`Cliente: ${pedido.cliente}, Produtos: ${pedido.produtos.join(", ")}`);
    }
}


cadastrarCliente("Rafael", "1234-5678");
cadastrarCliente("Bruna", "9876-5432");
cadastrarProduto("Hamburguer", 29.90);
cadastrarProduto("Refrigerante", 10.00);

visualizarClientes();
visualizarProdutos();

fazerPedido("Rafael", ["Hamburguer", "Refrigerante"]);
fazerPedido("Bruna", ["Hamburguer"]);

visualizarPedidos();

