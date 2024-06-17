![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Guía de bucles[🔗][bucle e iteración] For Loops en JavaScript</font></b>

Los bucles ofrecen una forma rápida y sencilla de hacer algo repetidamente. Diferentes declaraciones de iteración disponibles para JavaScript.

Puedes pensar en un bucle como una versión computarizada del juego en la que le dices a alguien que dé X pasos en una dirección y luego Y pasos en otra. Por ejemplo, la idea "Ve cinco pasos hacia el este" se podría expresar de esta manera como un bucle:
```js
for (let pasos = 0; pasos < 5; pasos++) {
  // Se ejecuta 5 veces, con valores del paso 0 al 4.
  console.log("Camina un paso hacia el este");
}
```
Hay muchos diferentes tipos de bucles, pero esencialmente, todos hacen lo mismo: repiten una acción varias veces. (¡Ten en cuenta que es posible que ese número sea cero!).

Los diversos mecanismos de bucle ofrecen diferentes formas de determinar los puntos de inicio y terminación del bucle. Hay varias situaciones que son fácilmente atendidas por un tipo de bucle que por otros.

Las declaraciones para bucles proporcionadas en JavaScript son:
+ for Declaración
+ Declaración do...while
+ Declaración while
+ Declaración labeled
+ Declaración break
+ Declaración continue
+ for Declaración...in
+ for Declaración...of   


## <b><font color="#006cb5">for Declaración loops[🔗][for Declaración]</font></b>
Un ciclo `for` se repite hasta que una condición especificada se evalúe como `false`.

Crea un bucle que consiste en tres expresiones opcionales, encerradas en paréntesis y separadas por puntos y comas, seguidas de una sentencia ejecutada en un bucle.

### <font color="#556CEE">Sintaxis for loops</font>
```js
for ([expresiónInicial]; [expresiónCondicional]; [expresiónDeActualización])
  instrucción
```
#### <font color="#006cb5">Parámetros for</font>
`expresión-inicial`
Una expresión (incluyendo las expresiones de asignación) o la declaración de variable. Típicamente se utiliza para usarse como variable contador. Esta expresión puede opcionalmente declarar nuevas variables con la palabra clave `var`. Estas variables no son locales del bucle, es decir, están en el mismo alcance en el que está el bucle `for`. El resultado de esta expresión es descartado.

`condición`
Una expresión para ser evaluada antes de cada iteración del bucle. Si esta expresión se evalúa como verdadera, se ejecuta `sentencia`. Esta comprobación condicional es opcional. Si se omite, la condición siempre se evalúa como verdadera. Si la expresión se evalúa como falsa, la ejecución salta a la primera expresión que sigue al constructor de `for`.

`expresión-final`
Una expresión para ser evaluada al final de cada iteración del bucle. Esto ocurre antes de la siguiente evaluación de la `condición`. Generalmente se usa para actualizar o incrementar la variable contador.

`sentencia`
Una sentencia que se ejecuta mientras la condición se evalúa como verdadera. Para ejecutar múltiples sentencias dentro del bucle, utilice una sentencia `block` `({ ... })` para agrupar aquellas sentencias.

### <font color="#556CEE">Descripción for loops</font>
Cuando se ejecuta un bucle for, ocurre lo siguiente:
1. Se ejecuta la expresión de iniciación `expresiónInicial`, si existe. Esta expresión normalmente inicia uno o más contadores de bucle, pero la sintaxis permite una expresión de cualquier grado de complejidad. Esta expresión también puede declarar variables.
2. Se evalúa la expresión `expresiónCondicional`. Si el valor de `expresiónCondicional` es verdadero, se ejecutan las instrucciones del bucle. Si el valor de `condición` es falso, el bucle for termina. (Si la expresión `condición` se omite por completo, se supone que la `condición` es verdadera).
3. Se ejecuta la `instrucción`. Para ejecutar varias instrucciones, usa una declaración de bloque `({ ... })` para agrupar esas declaraciones.
4. Si está presente, se ejecuta la expresión de actualización `expresiónDeActualización`.
5. El control regresa al paso 2.

### <font color="#556CEE">bucle ejercicio incrementador</font>
La siguiente sentencia for comienza mediante la declaración de la variable `índice` y se inicializa a 0. Comprueba que `índice` es menor que `length`, realiza las dos sentencias con éxito e incrementa `índice` en 1 (++)después de cada pase del bucle.
```js
//Crear matriz string
var matriz_string = ["Mielma", "Full Stack", "Developer", "Eli"];
// var indice = 0 (Declarar variable)
// indice< matriz_string.length (Declarar condición hasta que no se cumpla) indice menor a length
// indice++ (Incrementador)
for (var indice = 0; indice< matriz_string.length; indice++) {
  console.log(matriz_string[indice])
}
```
console:
```js
"Mielma"
"Full Stack"
"Developer"
"Eli"
```
![bucle ejercicio][bucle ejercicio]

### <font color="#556CEE">Ejercicio for Loops</font>
De una lista de 4 elementos que repita hasta que se acabe la lista
```js
//Crear matriz en plural
var listas = ["Mielma", "Full Stack", "Developer", "Eli"]; 
// lista representa indice 
for (lista in listas) { // Repetir hasta que se acaben los elementos
  console.log(lista); // index
  console.log(listas[lista]); // elemento pertenece al indeX
}
```
console:
```js
"0"
"Mielma"
"1"
"Full Stack"
"2"
"Developer"
"3"
"Eli"
```
![Bucle For Loops][Bucle For Loops]

## <b><font color="#006cb5">ForEach Declaración[🔗][ForEach Declaración]</font></b>
El método forEach() ejecuta la función indicada una vez por cada elemento del array.

### <font color="#556CEE">Sintaxis forEach </font> 
matriz.forEach(function callback(currentValue, index, matriz) {
    // tu iterador
}[, thisArg]);


#### <font color="#006cb5">Parámetros forEach</font>
+ `callback`
Función a ejecutar por cada elemento, que recibe tres argumentos:
  + `currentValue`  
  El elemento actual siendo procesado en el array.
  + `index` Opcional  
  El índice del elemento actual siendo procesado en el array.
  + `array` Opcional  
  El vector en el que forEach() esta siendo aplicado.

+ `thisArg` Opcional  
  Valor que se usará como `this` cuando se ejecute el `callback`.

#### <font color="#006cb5">Valor de retorno forEach</font>
`undefined`.

### <font color="#556CEE">Descripción forEach()()</font>
`forEach()` ejecuta la función `callback` una vez por cada elemento presente en el `array` en orden ascendente. No es invocada para índices que han sido eliminados o que no hayan sido inicializados (Ej. sobre arrays `sparse`)

`callback` es invocada con tres argumentos:
1. el valor del elemento
2. el índice del elemento
3. el array que está siendo recorrido

Si un parámetro `thisArg` es proporcionado a `forEach`, será usado como el valor `this` para cada invocación de `callback` como si se llamara a `callback.call(thisArg, element, index, array)`. Si `thisArg` es `undefined` o `null`, el valor th`is dentro de la función depende si la función está o no en modo estricto (valor pasado si está en modo estricto, objeto global si está en modo no-estricto).

El rango de elementos procesados por `forEach()` se establece antes de la primera invocación del `callback`. Los elementos que sean añadidos al vector después de que inicie la llamada a `forEach` no serán visitados por `callback`. Si los valores de los elementos existentes en el vector son modificados, el valor pasado al `callback` será el valor al momento de que `forEach` los visite; no se evaluarán los elementos borrados antes de ser visitados por `forEach`.

`forEach()` ejecuta la función `callback` una vez por cada elemento del array; a diferencia de `map()` o `reduce()` este siempre devuelve el valor `undefined` y no es encadenable. El típico uso es ejecutar los efectos secundarios al final de la cadena.

`forEach()` no muta/modifica el array desde el que es llamado (aunque `callback`, si se invoca, podría hacerlo).

### <font color="#556CEE">Ejemplo forEach()</font>
De una lista de 4 elementos que repita hasta que se acabe la lista
```js
//Crear matriz 
var listas = ["Mielma", "Full Stack", "Developer", "Eli"]; 
//matriz.forEach(function(argumento){console.log(argumento)});
listas.forEach(function(gente) {
  console.log(gente);
});
```
Console:

```js
"Mielma"
"Full Stack"
"Developer"
"Eli"
```
![ForEach Imagen][ForEach Imagen]


## <center><b><font color="#006cb5">Coding Exercise</font></b>
Create an array called "members" with 5 elements. Write a traditional for loop that uses an iterator and iterates through the array and console logs each member
```js
```
Resultado:
```js
var members = ['mielma', 'full stack', 'developer', 'Eli', 'Marañón'];

for (var i = 0; i < members.length; i++) {
  console.log(members[i]);
  
}
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-for-loops-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_f_01_for_loops.js)

<!-- [Código Mielma]() -->

<!-- Ordenar enlaces -->
[bucle e iteración]: https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Loops_and_iteration

[for Declaración]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/for

[bucle ejercicio]: image/Ejercicio_Bucle.png

[Bucle For Loops]: image/Bucle_For_Loops.png

[ForEach Declaración]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach

[ForEach Imagen]: image/Bucle_ForEach_Loops.png

