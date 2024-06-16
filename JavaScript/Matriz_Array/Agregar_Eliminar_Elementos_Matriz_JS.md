![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Guía para agregar y eliminar elementos de matriz en JavaScript</font></b>

## <b><font color="#006cb5">pop()[🔗][pop]</font></b>
El método pop() elimina el último elemento de un array y lo devuelve. Este método cambia la longitud del array.

### <font color="#556CEE">Sintaxis pop()</font>
```js
matriz.pop()
```
#### <font color="#006cb5">Valor devuelto pop()</font>
El elemento que ha sido eliminado del array; `undefined` si el array está vacío.

### <font color="#556CEE">Descripción pop()</font>
El método `pop()` elimina el último elemento de un array y devuelve su valor al método que lo llamó.

`pop()` es intencionadamente genérico; este método puede ser `call()` o `apply()` en objectos similares a un array. En objetos que no contengan una propiedad `length`, que refleje su forma en una serie de propiedades numéricas consecutivas en base cero, puede no comportarse de manera significativa.

Si se llama a `pop()` en un array vacío, devuelve `undefined`.

### <font color="#556CEE">Ejemplo pop()</font>
```js
var matriz = ['Mielma', 'Developer', 'Full Stack', 'Eli'] // Crear Matriz Longitud 4
console.log(matriz.pop()); // "Eli" (Devuelve y elimina el último elemento)
console.log(matriz); // [object Array] (3) ["Mielma","Developer","Full Stack"]
```
![Pop_Eliminar_Elemento_-01_Matriz][pop image]

## <b><font color="#006cb5">push()[🔗][push]</font></b>
El método `push()` añade uno o más elementos al final de un array y devuelve la nueva longitud del array.

### <font color="#556CEE">Sintaxis push()</font>
```js
matriz.push("elemento a añadir")
```

#### <font color="#006cb5">Valor devuelto push()</font>
La nueva propiedad `length` del objeto sobre el cual se efectuó la llamada.

### <font color="#556CEE">Descripción push()</font>
El método `push()` es muy práctico para añadir valores a un array.

`push()` es genérico intencionadamente. Este método puede ser `call()` o `apply()` a objetos que representen arrays. El método `push()` depende de la propiedad `length` para decidir donde empezar a insertar los valores dados. Si el valor de la propiedad `length` no puede ser convertido en numérico, el índice 0 es usado. Esto permite la posibilidad de que la propiedad `length` sea inexistente, y en este caso `length` será creado.

Los únicos objetos nativos que se asemejen al array son `strings` objetos, aunque estos no se puedan usar en la aplicación de este método ya que son inmutables.



### <font color="#556CEE">Ejemplo push()</font>

```js 
var matriz = ['Mielma', 'Developer', 'Full Stack', 'Eli'] // Crear Matriz
console.log(matriz.push('Marañón')); // 5 (devuelve length)
console.log(matriz);// [object Array] (5) ["Mielma","Developer","Full Stack","Eli"]
```
![Push_Añadir_Elemento_-01_Matriz][Push image]

## <b><font color="#006cb5">shift()[🔗][shift]</font></b>
El método `shift()` elimina el primer elemento del array y lo retorna. Este método modifica la longitud del array.

### <font color="#556CEE">Sintaxis shift()</font>
```js
matriz.shift()
```

#### <font color="#006cb5">Valor devuelto shift()</font>
El elemento que ha sido eliminado del array; undefined si el array está vacío.

### <font color="#556CEE">Descripción shift()</font>
El método `shift()` elimina el elemento en el índice cero y desplaza los valores consecutivos hacia abajo, devolviendo el valor eliminado. Si la propiedad `length` es 0, devuelve undefined.

`shift()` es genérico; este método puede utilizarse con `call()` o `apply()` a objetos similares a arrays. Los objetos que no tengan una propiedad `length` que refleje el último elemento de una serie consecutiva de propiedades numéricas con índice base cero pueden no comportarse de manera significativa.

### <font color="#556CEE">Ejemplo shift()</font>
```js
var matriz = ['Mielma', 'Developer', 'Full Stack', 'Eli'] // Crear Matriz
console.log(matriz.shift()) // "Mielma" (Devuelve y elimina el primer elemento)
console.log(matriz) // [object Array] (3) ["Developer","Full Stack","Eli"]
```
![Shift_Eliminar_Elemento_0_Matriz][shift image]

## <b><font color="#006cb5">unshift()[🔗][unshift]</font></b>
El método `unshift()` agrega uno o más elementos al inicio del array, y devuelve la nueva `length` del array.

### <font color="#556CEE">Sintaxis unshift(</font>
```js
matriz.unshift("elemento a añadir")
```

#### <font color="#006cb5">Valor devuelto</font>
La nueva propiedad `length` del objeto sobre el cual se efectuó la llamada.


### <font color="#556CEE">Descripción</font>
El método `unshift()` inserta los valores proporcionados al inicio de un objeto del tipo array.

`unshift()` es intencionalmente genérico; este método puede ser `call()` o `apply()` a objetos similares a arrays. Objetos que no contengan una propiedad `length` reflejando una serie de propiedades numéricas consecutivas, comenzada a partir del cero, pueden no comportarse de una manera comprensible.

### <font color="#556CEE">Ejemplo</font>
```js
var matriz = ['Mielma', 'Developer', 'Full Stack', 'Eli'] // Crear Matriz
console.log(matriz.push('Marañón')); // 5 (devuelve length)
console.log(matriz);// [object Array] (5) ["Mielma","Developer","Full Stack","Eli"]
```
![Unshift_Añadir_Elemento_0_Matriz][unshift image]






<!-- ## <b><font color="#006cb5">Ejercicio</font></b> -->
<!-- ### <font color="#556CEE">H3</font> -->
<!-- #### <font color="#006cb5">H4</font> -->
<!-- ## <center><b><font color="#006cb5">Coding Exercise</font></b>
```js
```
Resultado:
```js
``` -->


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios]()  

<!-- [Código DevCamp]() -->

<!-- [Código Mielma]() -->

<!-- Ordenar enlaces -->
[pop]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/pop#descripci%C3%B3n
[pop image]: image/Pop_Eliminar_Elemento_-01_Matriz.png

[push]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/push
[push image]: image/Push_Añadir_Elemento_-01_Matriz.png

[shift]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/shift
[shift image]: image/Shift_Eliminar_Elemento_0_Matriz.png

[unshift]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift
[unshift image]: image/Unshift_Añadir_Elemento_0_Matriz.png