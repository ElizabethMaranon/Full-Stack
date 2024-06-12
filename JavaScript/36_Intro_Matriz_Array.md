![Logo Mielma](/Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Introducción a la sección: Introducción a las matrices de JavaScript</font></b>
## <b><font color="#006cb5">¿Qué es una matriz / array[🔗](https://developer.mozilla.org/es/docs/Learn/JavaScript/First_steps/Arrays)?</font></b>

Las matrices — una manera ordenada de almacenar una lista de elementos de datos bajo un solo nombre de variable. 

Las matrices se describen como "objetos tipo lista"; básicamente son objetos individuales que contienen múltiples valores almacenados en una lista. Los objetos de arreglos pueden almacenarse en variables y tratarse de la misma manera que cualquier otro tipo de valor, la diferencia es que podemos acceder individualmente a cada valor dentro de la lista y hacer cosas útiles y eficientes con la lista.

Si no tuviéramos matrices, tendríamos que almacenar cada elemento en una variable separada, luego llamar al código que hace la impresión y agregarlo por separado para cada artículo. Esto sería mucho más largo de escribir, menos eficiente y más propenso a errores.

## <b><font color="#006cb5">¿Qué es operador new[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/new)?</font></b>

El operador new permite a los desarrolladores crear una instancia de un tipo de objeto definido por el usuario o de uno de los tipos de objeto integrados que tiene un función constructora.

### <font color="#556CEE">Sintaxis</font>

```js
new constructor [([arguments])]
```
#### <font color='#006cb5'>Parámetros</font>

`constructor`
Una clase o función que especifica el tipo de instancia del objeto.

`arguments`
Una lista de valores con los que se llamará al constructor

### <font color="#556CEE">Descripción</font>

La palabra clave `new` hace lo siguiente:

1. Crea un objeto JavaScript simple y en blanco;
2. Vincula (establece el constructor de) este objeto a otro objeto;
3. Pasa el objeto recién creado del Paso 1 como el contexto ``this``;
4. Devuelve ``this`` si la función no devuelve un objeto.

La creación de un objeto definido por el usuario requiere dos pasos:

1. Defina el tipo de objeto escribiendo una función.
2. Crea una instancia del objeto con `new`.

Para definir un tipo de objeto, crea una función para el tipo de objeto que especifique su nombre y propiedades. Un objeto puede tener una propiedad que en sí misma es otro objeto. Ve los siguientes ejemplos.

Cuando se ejecuta el código `new Foo(...)`, sucede lo siguiente:

1. Se crea un nuevo objeto, heredado de `Foo`.prototype`.
2. La función constructora `Foo` se llama con los argumentos especificados y con `this` vinculado al objeto recién creado. new `Foo` es equivalente a new `Foo`(), es decir, si no se especifica una lista de argumentos, `Foo` se llama sin argumentos.
3. El objeto (no nulo, `false`, 3.1415 u otros tipos primitivos) devuelto por la función constructora se convierte en el resultado de toda la expresión `new`. Si la función constructora no devuelve explícitamente un objeto, en su lugar se utiliza el objeto creado en el paso 1. (Normalmente, los constructores no devuelven un valor, pero pueden elegir hacerlo si quieren redefinir el proceso normal de creación de objetos).

Siempre puedes agregar una propiedad a un objeto definido previamente. Por ejemplo, la instrucción `car1.color = "black"` agrega una propiedad `color` a `car1` y le asigna un valor de "`black`". Sin embargo, esto no afecta a ningún otro objeto. Para agregar la nueva propiedad a todos los objetos del mismo tipo, debes agregar la propiedad a la definición del tipo de objeto `Car`.

Puedes agregar una propiedad compartida a un tipo de objeto definido previamente mediante la propiedad `Function.prototype`[🔗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype). Esto define una propiedad que comparten todos los objetos creados con esa función, en lugar de solo una instancia del tipo de objeto. El siguiente código agrega una propiedad de color con el valor `"color original"` a todos los objetos de tipo `Car`, y luego redefine ese valor con la cadena "`black`" solo en la instancia `car1` del objeto. Para obtener más información, consulta prototype[🔗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype).

#### <font color='#006cb5'>Ejemplo</font>

```js 
function Car() {}
car1 = new Car();
car2 = new Car();

console.log(car1.color); // undefined

Car.prototype.color = "color original";
console.log(car1.color); // 'color original'

car1.color = "black";
console.log(car1.color); // 'black'

console.log(Object.getPrototypeOf(car1).color); // 'color original'
console.log(Object.getPrototypeOf(car2).color); // 'color original'
console.log(car1.color); // 'black'
console.log(car2.color); // 'color original'
```

```
🗒️ Nota: Si no escribiste el operador new, la función constructor se invocará como cualquier función normal, sin crear un objeto. En este caso, el valor de this también es diferente.
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/introduction-javascript-arrays)  


