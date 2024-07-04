// Código Codepen: https://codepen.io/ElizabethMaranon/pen/ZENggYy

console.log("-----Bucle For-----");
// Cree un bucle for en JS que imprima cada nombre en esta lista. miLista = “velma”, “exploradora”, “jane”, “john”, “harry”
var miLista = ["velma", "exploradora", "jane", "john", "harry"];
for (var indice = 0; indice < miLista.length; indice++) {
  console.log(miLista[indice]);
}
console.log("-----Bucle While-----");
// Cree un bucle while que recorra la misma lista y también imprima los nombres. Nota: Recuerda crear un contador para que el ciclo no sea infinito.
var miLista = ["velma", "exploradora", "jane", "john", "harry"];
var data = 0;
while (data < miLista.length) {
  console.log(miLista[data]);
  data++;
}
console.log("-----Función Flecha-----");
// Cree una función de flecha que devuelva "Hola mundo".
saludo = () => {
  console.log("Hola mundo");
};
saludo();
