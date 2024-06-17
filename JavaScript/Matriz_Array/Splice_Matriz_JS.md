![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Cómo utilizar la función de splice() en JavaScript para eliminar elementos de matriz específicos</font></b>

## <b><font color="#006cb5">splice()[🔗][splice]</font></b>
El método `splice()` cambia el contenido de un array eliminando elementos existentes y/o agregando nuevos elementos.

### <font color="#556CEE">Sintaxis splice()</font>
```js
matriz.splice(start[, deleteCount[, item1[, item2[, ...]]]])
```
#### <font color="#006cb5">Parámetros splice()</font>
`start`
    Índice donde se comenzará a cambiar el array (con 0 como origen). Si es mayor que la longitud del array, el punto inicial será la longitud del array. Si es negativo, empezará esa cantidad de elementos contando desde el final.

`deleteCount` Opcional
    Un entero indicando el número de elementos a eliminar del array antiguo.

    Si `deleteCount` se omite, o si su valor es mayor que `arr.length - start` (esto significa, si es mayor que el número de elementos restantes del array, comenzando desde `start`), entonces todos los elementos desde `start` hasta el final del array serán eliminados.

    Si `deleteCount` es igual a 0 o negativo, no se eliminará ningún elemento. En este caso, se debe especificar al menos un nuevo elemento (ver más abajo).

`item1, item2,` ... Opcional
    Los elementos que se agregarán al array, empezando en el índice `start`. Si no se especifica ningún elemento, `splice()` solamente eliminará elementos del array.

#### <font color="#006cb5">Valor devuelto splice()</font>
Un array que contiene los elementos eliminados. Si sólo se ha eliminado un elemento, devuelve un array con un solo elemento. Si no se ha eliminado ningún elemento, devuelve un array vacío.

### <font color="#556CEE">Descripción splice()</font>
Si especifica un número diferente de elementos a agregar que los que se eliminarán, el array tendrá un tamaño diferente al original una vez finalizada la llamada.


### <font color="#556CEE">Ejemplo splice()</font>
Eliminar 0 elementos desde el índice 2 e insertar 1
```js
var matriz = ["Mielma", "Full Stack", "Developer", "Eli", "Marañón"] // [object Array] (5)
var eliminar0_index2_insert1 = matriz.splice(2,0, "bat")
console.log(matriz); // [object Array] (6) ["Mielma","Full Stack","bat","Developer","Eli","Marañón"]
console.log(eliminar0_index2_insert1); // [object Array] (0) []
```
Eliminar 1 elemento desde indice 3 e insertar 0
```js
var matriz = ["Mielma", "Full Stack", "Developer", "Eli", "Marañón"] // [object Array] (5)
var eliminar1_index3_insert0 = matriz.splice(3, 1);
console.log(matriz); // [object Array] (4) ["Mielma","Full Stack","Developer","Marañón"]
console.log(eliminar1_index3_insert0); // [object Array] (1) ["Eli"]
```
Eliminar 1 elemento desde indice 2 e insertar 1
```js
var matriz = ["Mielma", "Full Stack", "Developer", "Eli", "Marañón"] // [object Array] (5)
var eliminar1_index2_insert1 = matriz.splice(2, 1, "bat")
console.log(matriz); // [object Array] (5) ["Mielma","Full Stack","bat","Eli","Marañón"]
console.log(eliminar1_index2_insert1); // [object Array] (1) ["Developer"]
```
Eliminar 2 elementos desde indice 0 e insertar 3
```js
var matriz = ["Mielma", "Full Stack", "Developer", "Eli", "Marañón"] // [object Array] (5)
var eliminar2_index0_insert3 = matriz.splice(0,2, "uno", "dos", "tres")
console.log(matriz); // [object Array] (6) ["uno","dos","tres","Developer","Eli","Marañón"]
console.log(eliminar2_index0_insert3); // [object Array] (2) ["Mielma","Full Stack"]
```
Eliminar 2 elementos desde indice 2 e insertar 0
```js
var matriz = ["Mielma", "Full Stack", "Developer", "Eli", "Marañón"] // [object Array] (5)
var eliminar2_index2_insert0 = matriz.splice(2,2);
console.log(matriz); // [object Array] (3) ["Mielma","Full Stack","Marañón"]
console.log(eliminar2_index2_insert0); // [object Array] (2) ["Developer","Eli"]
```
Eliminar 1 elemento desde indice -1 e insertar 0
```js
var matriz = ["Mielma", "Full Stack", "Developer", "Eli", "Marañón"] // [object Array] (5)
var eliminar1_index_1_insert0 = matriz.splice(-1,1);
console.log(matriz); // [object Array] (4) ["Mielma","Full Stack","Developer","Eli"]
console.log(eliminar1_index_1_insert0); // [object Array] (1) ["Marañón"]
```
Eliminar todos elementos desde indice 2 e insertar 0
```js
var matriz = ["Mielma", "Full Stack", "Developer", "Eli", "Marañón"] // [object Array] (5)
var eliminartodos_index2_insert0 = matriz.splice(2);
console.log(matriz); // [object Array] (2) ["Mielma","Full Stack"]
console.log(eliminartodos_index2_insert0); // [object Array] (3)
["Developer","Eli","Marañón"]
```
![splice Código][splice Código]
![splice Código][splice Console]

## <b><font color="#006cb5">Ejercicio</font></b>
```js
var matriz = ['Mielma', 'Full Stack', 'Developer', 'Eli'];

var indice = matriz.indexOf('Eli'); // variable index de elemento

console.log(indice); // 3 (devuelve index)

console.log(matriz.splice(indice, 1)); // [object Array] (1) ["Eli"]

console.log(matriz); // [object Array] (3) ["Mielma","Full Stack","Developer"]

console.log(matriz.splice(1, 2)); // [object Array] (2) ["Full Stack","Developer"]

console.log(matriz); // [object Array] (1) ["Mielma"]
```
![splice ejercicio][splice ejercicio]
## <center><b><font color="#006cb5">Coding Exercise</font></b>
Use the method splice on the array to leave the first 3 values in the array, and have the splice return "Springer".
```js
var array = ['Altuve', 'Bregman', 'Correa', 'Springer'];
```
Resultado:
```js
var array = ['Altuve', 'Bregman', 'Correa', 'Springer'];
array.splice(3,1);
array;
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios]()  

[Código DevCamp]()

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/eYayodJ)

<!-- Ordenar enlaces -->
[splice]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/splice
[splice Código]:image/Splice_Añadir_Eliminar_Elemento_Matriz_Código.png
[splice Console]:image/Splice_Añadir_Eliminar_Elemento_Matriz_Console.png
[splice ejercicio]: image/Splice_Ejercicio.png