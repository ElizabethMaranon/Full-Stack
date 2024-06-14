![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Eliminar el primer y último elemento de una matriz de JavaScript</font></b>

## <b><font color="#006cb5">¿Qué es const[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/const)?</font></b>

Las variables constantes presentan un ámbito de bloque (block scope) tal y como lo hacen las variables definidas usando la instrucción let, con la particularidad de que el valor de una constante no puede cambiarse a través de la reasignación. Las constantes no se pueden redeclarar.

## <b><font color="#006cb5">Crear una función de recorte para matrices</font></b>
```js
const eliminasPrimerUltimo = lista => { // Crear función nombre = lista
  if (lista.length >= 3) { // Condición -> lista mayor o igual que 3
    return lista.slice(1, -1); // Condición verdadero, elimina primero y último
  } else { // Condición = Falso -> Nota de aviso
    throw "You need at least three elements in the array"; // 
  }
};

console.log(eliminasPrimerUltimo([1, 2, 3, 4]));
// [object Array] (2)
// [2,3]
console.log(eliminasPrimerUltimo(["<h1>", "Some content", "</h1>"]));
// [object Array] (1)
// ["Some content"]
console.log(eliminasPrimerUltimo(["Some content", "</h1>"]));
// Uncaught You need at least three elements in the array 
//  at https://cdpn.io/cpe/boomboom/pen.js?key=pen.js-fc3c2ede-28fd-ddc6-2af3-d3a3e4910917:5
```


### <font color="#556CEE">Ejercicio</font>



<!-- ## <center><b><font color="#006cb5">Coding Exercise</font></b>
```js
```
Resultado:
```js
``` -->

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/remove-first-last-element-javascript-array)  

[Código DevCamp](https://github.com/bottega-code-school/javascript-code-exercises/blob/master/data-structures/remove-first-and-last.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/KKLvGpR)