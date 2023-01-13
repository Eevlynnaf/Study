let valor     //nao inicializada
console.log(valor)

valor = null  //definida, mas declara ausência de valor
console.log(valor)
//console.log(valor.toString())   // Erro, nao se pode acessar uma variavel com valor nulo

const produto = {}
console.log(produto.preco)
console.log(produto)

produto.preco = 3.50
console.log(produto)

produto.preco = undefined     //evitar atribuir undefined
console.log(!!produto.preco)
console.log(produto)

produto.preco = null        // sem preco
