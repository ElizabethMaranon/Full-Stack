![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Cómo recorrer un objeto JavaScript for...in[🔗][for...in Loops]</font></b>

## <b><font color="#006cb5">for-in declaración</font></b>
La instrucción for-in itera sobre todas las propiedades enumerables de un objeto que está codificado por cadenas (ignorando los codificados por Símbolos), incluidas las propiedades enumerables heredadas.

### <font color="#556CEE">Sintaxis</font>
```js
for (variable in objeto)
    instrucción
```

#### <font color="#006cb5">Parámetros </font>
`variable`
Asigna un nombre de propiedad diferente a la variable en cada iteración.

`objeto`
Objeto cuyas propiedades enumerables que no son símbolos se iteran.

### <font color="#556CEE">Descripción </font>
Un bucle `for...in` solo itera sobre propiedades enumerables que no son símbolo. Los objetos creados a partir de constructores integrados como `Array` y `Object` han heredado propiedades no enumerables de `Object.prototype` y `String.prototype`, como el método `indexOf()` de `String` o el método `toString()` de `Object`. El bucle iterará sobre todas las propiedades enumerables del objeto en sí y aquellas que el objeto hereda de su cadena de prototipos (las propiedades de los prototipos más cercanos tienen prioridad sobre las de los prototipos más alejados del objeto en su cadena de prototipos).

#### <font color="#006cb5">Propiedades **deleted**, **added** o **modified** </font>
Un bucle for...in itera sobre las propiedades de un objeto en un orden arbitrario 

Si una propiedad se modifica en una iteración y luego se visita en un momento posterior, su valor en el bucle es su valor en ese momento posterior. Una propiedad que se elimina antes de haber sido visitada no se visitará más tarde. Las propiedades agregadas al objeto sobre el que se está produciendo la iteración se pueden visitar u omitir de la iteración.

En general, es mejor no agregar, modificar o eliminar propiedades del objeto durante la iteración, aparte de la propiedad que se está visitando actualmente. No hay garantía de si se visitará una propiedad agregada, si se visitará una propiedad modificada (distinta de la actual) antes o después de que se modifique, o si se visitará una propiedad eliminada antes de eliminarla.

#### <font color="#006cb5">Iteración en arreglos y `for...in`</font>
```js
⚠️Nota: `for...in` no se debe usar para iterar sobre un `Array` donde el orden del índice es importante.
```
Los índices del arreglo son solo propiedades enumerables con nombres enteros y, por lo demás, son idénticos a las propiedades generales del objeto. No hay garantía de que `for...in` devuelva los índices en un orden en particular. La instrucción de bucle `for...in` devolverá todas las propiedades enumerables, incluidas aquellas con nombres no enteros y aquellas que se heredan.

Debido a que el orden de iteración depende de la implementación, es posible que la iteración sobre un arreglo no visite los elementos en un orden coherente. Por lo tanto, es mejor usar un bucle `for` con un índice numérico (o `Array.prototype.forEach()` o el bucle `for...of`) cuando se itera sobre arreglos donde el orden de acceso es importante.

#### <font color="#006cb5">Iterar solo sobre propiedades directas</font>
Si solo deseas considerar las propiedades adjuntas al objeto en sí mismo, y no sus prototipos, usa `getOwnPropertyNames()` o realiza una `hasOwnProperty()` verificación (`propertyIsEnumerable(`) también se puede utilizar). Alternativamente, si sabes que no habrá ninguna interferencia de código externo, puedes extender los prototipos incorporados con un método de verificación.

### <font color="#556CEE">¿Por qué usar for...in?</font>
Dado que `for...in` está construido para iterar propiedades de objeto, no se recomienda su uso con arreglos y opciones como `Array.prototype.forEach()` y existe `for...of`, ¿cuál podría ser el uso de `for...in`?

Es posible que se utilice de forma más práctica con fines de depuración, ya que es una forma fácil de comprobar las propiedades de un objeto (mediante la salida a la consola o de otro modo). Aunque los arreglos suelen ser más prácticos para almacenar datos, en situaciones en las que se prefiere un par clave-valor para trabajar con datos (con propiedades que actúan como la "clave"), puede haber casos en los que desees comprobar si alguna de esas claves cumple un valor particular.


### <font color="#556CEE">Ejemplo </font>
```js
var estudiante = {
  nombre: 'Mielma',
  edad: 44,
  curso: 'Full Stack'
};

for (var clave in estudiante) {
  console.log("estudiante[clave] => " + clave + " => " + estudiante[clave]);
}

for (var clave in estudiante) {
  console.log("estudiante.clave => " + clave + " => " + estudiante.clave);
}
```
console:
```js
"estudiante[clave] => nombre => Mielma"
"estudiante[clave] => edad => 44"
"estudiante[clave] => curso => Full Stack"
"estudiante.clave => nombre => undefined"
"estudiante.clave => edad => undefined"
"estudiante.clave => curso => undefined"
```
![for...in Loops][for...in Loops Image]


## <center><b><font color="#006cb5">Coding Exercise</font></b>
Create an object called "user". Assign it a username, email, phone and give them values. Console log the data in the same format as the video.
```js
let user = {
  
};
```
Resultado:
```js
let user = {
    username: 'Mielma',
    email: 'mielma@fullsatck.com',
    phone: 777-777-777,
};
for (var key in user) {
  console.log(key + " => " + user[key]);
}
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-loop-javascript-object)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_f_02_looping_over_object.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/KKLZjYE)

<!-- Ordenar enlaces -->

[for...in Loops]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/for...in

[for...in Loops Image]: image/For...in_Loops.png

