![Logo Mielma](image/Logo_Encabezado.png)

# <b><font color="#556CEE">Cómo obtener el promedio de una matriz en JavaScript</font></b>

## <b><font color="#006cb5">Const[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/const)</font></b>
Las variables constantes presentan un ámbito de bloque (block scope) tal y como lo hacen las variables definidas usando la instrucción let, con la particularidad de que el valor de una constante no puede cambiarse a través de la reasignación. Las constantes no se pueden redeclarar.

Esta declaración crea una constante cuyo alcance puede ser global o local para el bloque en el que se declara. Es necesario inicializar la constante, es decir, se debe especificar su valor en la misma sentencia en la que se declara, lo que tiene sentido, dado que no se puede cambiar posteriormente.

La declaración de una constante crea una referencia de sólo lectura. No significa que el valor que tiene sea inmutable, sino que el identificador de variable no puede ser reasignado, por lo tanto, en el caso de que la asignación a la constante sea un objeto, el objeto sí que puede ser alterado.

Una constante no puede compartir su nombre con una función o variable en el mismo ámbito.

Todas las consideraciones acerca de la " zona muerta temporal " se aplican tanto a let y const.

## <b><font color="#006cb5">Obtener promedio de matriz</font></b>

```js
const promedio = lista => {
    // Sumar los valores
    const reducer = (total, valores) => total + valores;
    // Obtener longitud   
    const total = lista.reduce(reducer)
    // Dividir suma entre longitud
    return total / lista.length;
};

const lista = [1, 2, 3, 4, 5, 6]

promedio(lista); // Resultado 3.5
};

const lista = [1, 2, 3, 4, 5, 6]

average(lista);
```


<!-- ## <b><font color="#006cb5">Coding Exercise</font></b> -->

# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-get-average-array-javascript)  

[Código DevCamp](https://github.com/bottega-code-school/javascript-code-exercises/blob/master/data-structures/get-average.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/OJYpOob)

[Referencia de Mozilla sobre reductores de Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)