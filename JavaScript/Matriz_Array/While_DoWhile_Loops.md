![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Guía para bucles While y Do/While en JavaScript</font></b>

## <b><font color="#006cb5">while[🔗][while]</font></b>
Crea un bucle que ejecuta una sentencia especificada mientras cierta condición se evalúe como verdadera. Dicha condición es evaluada antes de ejecutar la sentencia
### <font color="#556CEE">Sintaxis while</font>
```js
while(condición)
    sentencia
```

#### <font color="#006cb5">Parámetros while </font>
`condición` Una expresión que se evalúa antes de cada paso del bucle. Si esta condición se evalúa como verdadera, se ejecuta `sentencia`. Cuando la condición se evalúa como false, la ejecución continúa con la `sentencia` posterior al bucle `while`.

`sentencia` Una sentencia que se ejecuta mientras la condición se evalúa como verdadera. Para ejecutar múltiples sentencias dentro de un bucle, utiliza una sentencia `block ({ ... })` para agrupar esas sentencias.

### <font color="#556CEE">Ejemplo  while</font>
El siguiente bucle `while` itera mientras `n` es menor que tres.

```js
n = 0;
x = 0;
while (n < 3) { // Mientras n sea menor a 3
  console.log("n = " + n++); // Incrementar en 1 n
  console.log(" x = " + (x += n)); // Sumar x y n
}
```
Cada iteración, el bucle incrementa `n` y la añade a `x`. Por lo tanto, `x` y `n` toman los siguientes valores:
```js
"n = 0"
" x = 1"
"n = 1"
" x = 3"
"n = 2"
" x = 6"
```
Después de completar el tercer pase, la condición `n` < 3 no será verdadera más tiempo, por lo que el bucle terminará.
![while image][while image]

## <b><font color="#006cb5">Ejercicio while</font></b>
Mientras index jugadores sea inferior a la longitud de la lista, mostrar jugadores
```js
var jugadores = ["Mielma", "Full Stack", "Developer", "Eli"];
var i = 0;
while (i< jugadores.length) {
  console.log(jugadores[i]);
  i++;
}
```
console:
```js
"Mielma"
"Full Stack"
"Developer"
"Eli"
```
![while ejercicio image][while ejercicio image]

## <b><font color="#006cb5">do...while</font></b>
La sentencia (hacer mientras) crea un bucle que ejecuta una sentencia especificada, hasta que la condición de comprobación se evalúa como falsa. La condición se evalúa después de ejecutar la sentencia, dando como resultado que la sentencia especificada se ejecute al menos una vez.
### <font color="#556CEE">Sintaxis do...while</font>
```js
do
  sentencia
while (condición);
```

#### <font color="#006cb5">Parámetros do...while</font>
`sentencia`
Una `sentencia` que se ejecuta al menos una vez y es re-ejecutada cada vez que la condición se evalúa a verdadera. Para ejecutar múltiples `sentencias` dentro de un bucle, utilice la sentencia `block ({ ... })` para agrupar aquellas `sentencias`.

`condición`
Una expresión se evalúa después de cada pase del bucle. Si `condición` se evalúa como verdadera, la `sentencia` se re-ejecuta. Cuando `condición` se evalúa como falsa, el control pasa a la siguiente `sentencia` hacer mientras.

### <font color="#556CEE">Ejemplo do...while</font>
En el siguiente ejemplo, el bucle hacer mientras itera al menos una vez y se reitera hasta que i ya no sea menor que 5.
```js
var i = 0;
do {
  console.log(i += 1);
  document.write(i);
} while (i < 5);
```
console:
```js
1
2
3
4
5
```
![doWhile][doWhile]

## <b><font color="#006cb5">Ejercicio do...while</font></b>
```js
var jugadores = ["Mielma", "Full Stack", "Developer", "Eli"];

var i = 0;
do {
  console.log(jugadores[i]);
  i++;
} while (i < jugadores.length)
```
console:
```js
"Mielma"
"Full Stack"
"Developer"
"Eli"
```
![doWhile ejercicio image][doWhile ejercicio image]


## <center><b><font color="#006cb5">Coding Exercise</font></b>
In the below starter code, place 4 dog names (elements) of your choice. Write a while loop that iterates through the dogHouse array. The iterator variable must be named "data".
```js
//Please leave the below starter code but fill in the array with 4 elements
var dogHouse = [];
```
Resultado:
```js
//Please leave the below starter code but fill in the array with 4 elements
var dogHouse = ["Mielma", "Full Stack", "Developer", "Eli"];

var data = 0;
while (data < dogHouse.length) {
  console.log(dogHouse[data]);
  data++;
}
```


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-while-do-while-loops-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_f_03_while_loops.js)



<!-- Ordenar enlaces -->

[while]:https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/while

[while image]: image/while_loops.png

[while ejercicio image]:image/while_loops_ejercicio.png

[doWhile]: image/doWhile_Loops.png

[doWhile ejercicio image]: image/doWhile_loops_ejercicio.png