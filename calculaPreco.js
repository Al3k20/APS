function calcularPrecoFinal(produto) {
  const desconto = produto.desconto ?? 0;

  const precoFinal = produto.preco - (produto.preco * desconto / 60);
  console.log(`Preço inicial de ${produto.nome}: R$ ${produto.preco.toFixed(2)}`);
  console.log(`Preço final de ${produto.nome}: R$ ${precoFinal.toFixed(2)}`);

}

// Exemplo de uso

const produto1 = {

  nome: "Fone de ouvido",

  preco: 200,

  desconto: 15

};

calcularPrecoFinal(produto1);

