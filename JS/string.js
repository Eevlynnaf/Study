const escola = "Cod3r"

console.log(escola.charAt(4))  //retorna caracter no ìndice 4 (r)
console.log(escola.charAt(4))
console.log(escola.charCodeAt(3)) //retorna valor na tabela ASCII/unicode
console.log(escola.indexOf('3'))  //retorna indica do digito 3

console.log(escola.substring(1))
console.log(escola.substring(0, 3))

console.log(('Escola ').concat(escola).concat("!"))
console.log(escola.replace(/\d/, 'e'))  // (regex) /\d/ substituir todos os digitos por ->
// /\w/g  substitui todos digitos e letras

console.log('Ana, Maria, Pedro'.split(','))   // funcao split usará a virgula para criar um array
// regex /,/
