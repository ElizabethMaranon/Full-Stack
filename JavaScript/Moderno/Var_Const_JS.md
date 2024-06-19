![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Usando el tipo de variable constante en JavaScript</font></b>

## <b><font color="#006cb5">Variable Const[🔗][Variable const]</font></b>
Las variables constantes presentan un ámbito de bloque (block scope) tal y como lo hacen las variables definidas usando la instrucción let, con la particularidad de que el valor de una constante no puede cambiarse a través de la reasignación. Las constantes no se pueden redeclarar.
```
⚠️ Advertencia: La re-declaración de la misma variable bajo un mismo ámbito léxico terminaría en un error de tipo SyntaxError. Esto también es extensible si usamos var dentro del ámbito léxico. Esto nos salvaguarda de redeclarar una variable accidentalmente y que no era posible solo con var.
```
### <font color="#556CEE">Sintaxis</font>
```js
const varname1 = value1 [, varname2 = value2 [, varname3 = value3 [, ... [, varnameN = valueN]]]];
```
#### <font color="#006cb5">Parámetros</font>
`varnameN`
Nombre de la constante. Puede ser un identificador legal.

`valueN`
Valor de la constante. Puede ser cualquier expresión legal.

### <font color="#556CEE">Descripción</font>
Esta declaración crea una constante cuyo alcance puede ser **global o local para el bloque en el que se declara**. Es necesario **inicializar** la constante, es decir, se debe especificar su valor en la misma sentencia en la que se declara, lo que tiene sentido, dado que no se puede cambiar posteriormente.

La declaración de una constante crea una referencia de sólo lectura. No significa que el valor que tiene sea inmutable, sino que el identificador de variable no puede ser reasignado, por lo tanto, en el caso de que la asignación a la constante sea un objeto, el objeto sí que puede ser alterado.

Una constante **no puede compartir su nombre** con una función o variable en el mismo ámbito.

Todas las consideraciones acerca de la `" zona muerta temporal "` se aplican tanto a `let` y `const`.

### <font color="#556CEE">Ejemplos</font>
El siguiente ejemplo produce una salida `"a es 7."`
```js
const a = 7;
document.writeln("a es " + a + ".");
```
Las siguientes instrucciones demuestra como se comporta `const`
```
⚠️ Advertencia: Las instrucciones deberán ser ordenadas correctamente para conseguir la salida esperada a los ejemplos
```
```js
// NOTA: Las constantes pueden ser declaradas en mayusculas o minusculaas,
//pero por convencion para distinguirlas del resto de variables se escribe todo en mayusculas

// definimos MY_FAV como constante y le damos un valor de 7
const MY_FAV = 7;

// lanzara un error: Unkeught TypeError: Asignación a variable constante.
MY_FAV = 20;

// imprimira 7
console.log('my favorite number is: ' + MY_FAV);

// lanzara un error: SyntaxError: tratando de redeclarar una constante. El identificador 'MY_FAV' ya ha sido declarado
const MY_FAV = 20;

// el nombre MY_FAV esta reservado para la constante anterior, también fallara y lanzara un SyntaxError por la redeclaración
var MY_FAV = 20;

// el nombre MY_FAV esta reservado para la variable anterior, esto también lanzara un SyntaxError por la redeclaración
let MY_FAV = 20;

// es importante tener en cuenta como funciona el alcance de bloque
if (MY_FAV === 7) {
    // esto esta bien y crea una variable MY_FAV de alcance/ambito de bloque
    // (funciona igual de bien con let para declarar un alcance de bloque/ambito de variable no-constante)
    const MY_FAV = 20;

    // MY_FAV ahora es 20
    console.log('my favorite number is ' + MY_FAV);

    // aquín también lanzara un SyntaxError por la redeclaración
    var MY_FAV = 20;
}

// MY_FAV todavia es 7
console.log('my favorite number is ' + MY_FAV);

// lanza error, falta el inicializador en la declaracion de const
const FOO;

// const tambien funciona en objetos
const MY_OBJECT = {'key': 'value'};

// Intentando sobrescribir el objeto nos lanza un error
MY_OBJECT = {'OTHER_KEY': 'value'};

// Sin embargo, los object keys no estan protegidas,
// por lo que la siguiente sentencia se ejecutara sin problema
MY_OBJECT.key = 'otherValue'; // Use Object.freeze() para hacer un objeto inmutable

// Lo mismo se aplica a los arrays
const MY_ARRAY = [];
// es posible empujar elementos en el array
MY_ARRAY.push('A'); // ["A"]
// Sin embargo, asignar un nuevo array a la variable lanza error
MY_ARRAY = ['B']
```

## <b><font color="#006cb5">Guía DevCamp Variable Const</font></b>
Durante años y años, siempre que deseaba crear una variable en Javascript, usaba la palabra clave VAR..
```js
var city = ‘Scottsdale';console.log(city)
```
Era más limitado si lo creabas o lo agregabas a una función, entonces solo estaría disponible en esa función. No tendrías otros momentos en los que esté disponible. No voy a entrar en las diferencias entre var y let en esta guía porque ya lo hicimos en el curso introductorio.

Lo que voy a hacer es hablar sobre el miembro más nuevo de la familia de variables en javascript y ese es constante, por lo que const es una de las formas de declarar variables ahora.
De hecho, si observa las prácticas de desarrollo modernas en las que se centra este curso, verá que const es en realidad el tipo de variable que se elige sobre todas las demás. En la mayoría de las aplicaciones, trabajo en: o declaro const o declaro let cuando tengo que hacerlo.

La mejor regla general es que en los programas modernos, especialmente si está compilando en reaccionar o en angular o cualquiera de estos marcos, siempre intente usar const de inmediato, que debería ser su opción predeterminada para escribir una variable. Si es demasiado específico entonces, y te mostraré cuándo este es el caso, entonces usa let.
Es muy raro que utilices var en las prácticas modernas. Todavía es importante saberlo. Esa es la razón por la que lo enseñamos. Verás los tres en diferentes aplicaciones y hay muchas ocasiones en las que necesitarás crear una variable global..
Para una especie de día a día, usted es una variable común y corriente, intentará usar const tanto como sea posible. Esto se debe a que const nos brinda una pequeña herramienta muy útil.
```js
let lugar = 'let lugar';
console.log(lugar); // "let lugar"

lugar = 'lugar';
console.log(lugar); // "lugar"
```
```js
const lekua = 'const lekua';
console.log(lekua); "const lekua"

lekua = 'lekua';
console.log(lekua); //Uncaught TypeError: Assignment to constant variable. //at https://cdpn.io/cpe/boomboom/pen.js?key=pen.js-62c5b7e7-ec00-0325-2ce7-74aec77aa12b:10
```
![Variable Const image][Variable Const image]

Ahora, si pruebo este error de tipo no detectado y esto es lo que estaba sucediendo, pero se oculta en el código Penn, por eso es genial usar herramientas como esta, pero a veces también tienes que cambiar y usar otros sistemas, como solo la consola pura.

Entonces, ¿qué es este error? Dice Error de tipo no detectado: Asignación a variable constante. Así que aquí es donde está el problema y es muy bueno detectarlo. No queremos tener siempre la capacidad de redefinir nuestras variables. Así que voy a salir de aquí. Entonces, con solo mirar este código, quiero que te acostumbres a escribir el tipo de variable const porque cuando comiences a revisar la documentación de React y Angular, y todos estos otros tipos de marcos, verás const usado mucho por todas partes.


## <center><b><font color="#006cb5">Coding Exercise</font></b>
Using the const variable type, make a variable called "wins" and set it to any number above 5. (When assigning a number to a variable, you cannot use quotes, "5")

Resultado:
```js
const wins = 7;
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/using-the-const-variable-type-in-javascript)  


[Código Mielma Variable Const](https://codepen.io/ElizabethMaranon/pen/zYQRMJg)

<!-- Ordenar enlaces -->

[Variable Const image]: image/Var_Const_Modern_JS.png
[Variable const]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/const