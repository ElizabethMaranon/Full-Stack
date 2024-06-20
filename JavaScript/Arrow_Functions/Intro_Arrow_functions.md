![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Introducción a las funciones de flecha (Arrow functions) en JavaScript </font></b>

## <b><font color="#006cb5">Funciones Flecha[🔗][Arrow Funcions Link]</font></b>
Una expresión de función flecha es una alternativa compacta a una expresión de función tradicional, pero es limitada y no se puede utilizar en todas las situaciones.

**Diferencias y limitaciones:**

+ No tiene sus propios enlaces a this o super y no se debe usar como métodos.
+ No tiene argumentos o palabras clave new.target.
+ No apta para los métodos call, apply y bind, que generalmente se basan en establecer un ámbito o alcance
+ No se puede utilizar como constructor.
+ No se puede utilizar yield dentro de su cuerpo.
#### <font color="#006cb5">Comparación de funciones tradicionales con funciones flecha</font>
Observa, paso a paso, la descomposición de una "función tradicional" hasta la "función flecha" más simple: **Nota**: Cada paso a lo largo del camino es una "función flecha" válida
```js
// Función tradicional
function (a){
  return a + 100;
}

// Desglose de la función flecha

// 1. Elimina la palabra "function" y coloca la flecha entre el argumento y el corchete de apertura.
(a) => {
  return a + 100;
}

// 2. Quita los corchetes del cuerpo y la palabra "return" — el return está implícito.
(a) => a + 100;

// 3. Suprime los paréntesis de los argumentos
a => a + 100;
```
```js
🗒️Nota: Como se muestra arriba, los { corchetes }, ( paréntesis ) y "return" son opcionales, pero pueden ser obligatorios.
```
Por ejemplo, si tienes **varios argumentos** o **ningún argumento**, deberás volver a introducir paréntesis alrededor de los argumentos:
```js
// Función tradicional
function (a, b){
  return a + b + 100;
}

// Función flecha
(a, b) => a + b + 100;

// Función tradicional (sin argumentos)
let a = 4;
let b = 2;
function (){
  return a + b + 100;
}

// Función flecha (sin argumentos)
let a = 4;
let b = 2;
() => a + b + 100;
```
Del mismo modo, si el cuerpo requiere **líneas de procesamiento adicionales**, deberás volver a introducir los corchetes **Más el "return"** (las funciones flecha no adivinan mágicamente qué o cuándo quieres "volver"):
```js
/ Función tradicional
function (a, b){
  let chuck = 42;
  return a + b + chuck;
}

// Función flecha
(a, b) => {
  let chuck = 42;
  return a + b + chuck;
}
```
Y finalmente, en las funciones con nombre tratamos las expresiones de flecha como variables
```js
// Función tradicional
function bob(a) {
  return a + 100;
}

// Función flecha
let bob = (a) => a + 100;
```
### <font color="#556CEE">Sintaxis</font>
Un parámetro. Con una expresión simple no se necesita `return`:
```js
param => expression;
(param) => expression;
```
Varios parámetros requieren paréntesis. Con una expresión simple no se necesita `return`:
```js
(param1, paramN) => expression;
```
Las declaraciones de varias líneas requieren corchetes y return:
```js
(param) => {
  let a = 1;
  return a + b;
};
```
Varios parámetros requieren paréntesis. Las declaraciones de varias líneas requieren corchetes y `return`:
```js
(param1, paramN) => {
  let a = 1;
  return a + b;
};
```



### <font color="#556CEE"></font>
#### <font color="#006cb5"></font>



## <b><font color="#006cb5">Guía DevCamp → Introducción a las funciones de flecha (Arrow functions) en JavaScript</font></b>
En esta parte de la sección, comenzaremos a analizar las funciones de flecha; ahora las funciones de flecha son una de las cosas más importantes para aprender en JavaScript moderno. Los verás por todas partes y, si nunca los has visto antes, si nunca antes has trabajado con ellos, pueden parecer un poco intimidantes.
Se ven completamente diferentes a cualquier otro tipo de declaración de función que haya visto si acaba de usar JavaScript simple. En versiones anteriores. Entonces, a modo de revisión, hablemos de dos formas en que puedes crear una función en javascript.

La primera será una declaración de función normal. Entonces, si digo función y digo nombre completo. Diga fName y lName para obtener un nombre y apellido. Ahora puedo registrar esto en la consola y decir: voy a usar nuestras versiones más modernas de interpolación de cadenas aquí, y diré fname y luego agregaré esto al apellido.
Eso es todo lo que tengo que hacer. Y ahora, si llamo a esto así, si digo el nombre completo, se imprimirán los nombres que le doy, así que pasaré a Mielma y Developer. Si ejecuto este código aquí. Resulta que Mielma Developer no sorprende.
```js
// Declaración de Función
function nombreCompleto(nombre, apellido) {
  console.log(`${nombre}, ${apellido}`);
}
nombreCompleto("Mielma", "Developer"); //"Mielma, Developer"
```
Entonces, si guardo y luego ejecuto esto, obtenemos exactamente el mismo resultado. Entonces la primera es una declaración de función. La segunda es una expresión de función.
```js
nombreCompleto = function (nombre, apellido) {
  console.log(`${nombre}, ${apellido}`);
}
nombreCompleto("Mielma", "Developer"); // "Mielma, Developer"
```
Ahora vamos a hablar de la función de flecha porque es una forma nueva y es increíblemente popular, tan popular de hecho que la verás en tantas aplicaciones diferentes que quería dedicarle una pequeña miniparte completa. el curso solo para funciones de flecha. Eventualmente, vamos a replicar nuestra función de nombre completo como una flecha.

Una cosa que he descubierto que ayuda mucho a los estudiantes cuando se trata de comprender las funciones de flecha es declarar la función de flecha más simple del mundo. Así que la forma en que lo hago es con un Hola mundo. Así que saluda al mundo y configura esto sin parámetros. Voy a recorrer todo esto en un segundo y luego pasaré una flecha. Ese es el nombre de la función de flecha porque tiene un signo igual seguido de un signo mayor que. Y luego pasaremos un bloque de código aquí dentro de llaves. Registro de la consola y luego, dentro de él, saludaré. Y ese es el punto y coma. Y tengo que poner un punto y coma justo después de esto.
Pero luego tengo que llamar a hola mundo de la misma manera que llamaríamos a una función.

Así que ahora puedo decir hola mundo si presiono borrar y luego ejecuto este. Ahora simplemente se imprimirá. Hola tal cual.
```js
// Basic arrow function
saludo = () => { console.log("Hola"); }
saludo();
```
Esta es la función de flecha más básica del mundo. Primero, siempre debe almacenarse dentro de una variable o ejecutarse de inmediato. Todavía no vamos a entrar en las funciones de ejecución inmediata. Podemos preocuparnos por eso más tarde.

Por ahora, piense que las funciones de flecha son como funciones anónimas, por lo que son muy similares a las expresiones de funciones como las que tenemos aquí. Pero en lugar de agregar el nombre de la función, solo tenemos estos pares seguidos de una flecha seguida de lo que queremos ejecutar.

Ahora, lo primero en lo que quiero centrarme con esto es, en primer lugar, no solo en la sintaxis, sino también en que no te intimides cuando los veas porque es exactamente lo mismo que estamos haciendo aquí.

Solo hay algunas diferencias sutiles en los cambios, y veremos los momentos en los que desea usar una función de flecha y los momentos en los que desea usar otra cosa.

Por ahora sólo quiero mostrarte las similitudes para que te acostumbres a este tipo de sintaxis. Así que aquí está nuestro ejemplo base de hola mundo. Solo para reiterar, lo almacena en una variable que establece igual a los pares, y si tiene argumentos, ahí es donde irían los pares. Luego tenemos una flecha y luego tenemos el proceso que queremos ejecutar.

Ahora que todo esto está en su lugar, hablemos de ir un paso más allá. Ahora lo siguiente que voy a hacer es la forma en que puedes implementar una función de flecha si solo tienes un argumento.

Entonces aquí puedo decir nombre y este será el nombre de la función. Y luego pasaré un único argumento que será fname y luego le daré la función de flecha y luego copiaré el registro de mi consola aquí.

Entonces, dentro de esto, simplemente pasaré el argumento que es fname y luego también llamaré una función, para que puedas ver que puedes hacer eso.

Así que voy a decir mayúsculas, lo que hará que todo esté en mayúscula y es una función. Así que lo paso así.

Ahora puedo llamar al nombre y pasar el valor, y ahora, si borro y ejecuto, esto se imprimirá. Entonces imprimirá el nombre. Y también ejecutó esta función en él.
```js
// Función de flecha con argumento de función abreviada para argumentos únicos
nombre = (nombre) => {
  console.log(nombre.toUpperCase());
};
nombre("Mielma");
```
Lo convirtió a mayúsculas, por lo que esta es exactamente la forma en que puedes hacerlo cuando solo tienes un argumento. Ahora bien, si recuerdas que antes dije que los pares son donde pones tus argumentos y si tienes más de uno, entonces sí necesitas tener pares, pero como un atajo y verás ambas sintaxis. Si solo tiene un argumento, entonces no necesita los pares a su alrededor.

Ahora si quieres. No va a tener ningún efecto. Puedo haberlo ejecutado y todo funciona exactamente igual, depende de ti si quieres usarlos o no. Y los guardaré así en caso de que quieras recordar la sintaxis.

Ahora, el siguiente del que vamos a hablar es qué quieres hacer si tienes múltiples argumentos, aquí es donde vamos a replicar estas funciones aquí arriba.

Así que ahora voy a hacer un par de cosas. Voy a simplemente copiar esta sintaxis. Sólo para que podamos tener eso. Excepto que lo cambiaré a nombre completo, y luego, para los argumentos, ahora lo envolveré entre paréntesis, digamos, fname y lname así. Seguido de la flecha y seguido de nuestra expresión de cuál es el proceso que realmente queremos ejecutar.
```js
// Función de flecha con múltiples argumentos
nombreCompleto = (nombre, apellido) => { console.log(`${nombre}, ${apellido}`); }
nombreCompleto('Mielma', 'Developer');
```
Entonces, una cosa importante que quiero que aprendas de esta guía es que una función de flecha es solo otra forma de definir una función, es otra forma de configurar algún proceso que deseas concluir, encapsular y luego deseas para llamarlo más tarde, que es en su caso más básico, es exactamente lo que es una función.

Es simplemente una forma un poco más limpia de hacerlo. Y si estás pensando que esto es completamente inútil porque ya has pasado mucho tiempo aprendiendo cómo recordar la función seguida del nombre seguido de los argumentos e incluso la forma anónima de hacerlo y crees que esto no tiene sentido, no es del todo.
Y en la siguiente guía, analizaremos las diferencias sutiles sobre cuándo desea usar una función de flecha y cuándo no desea hacerlo, todo se basa en cómo funciona dentro de otras funciones. Y más adelante, dentro de las clases, ahí es donde entrarás en la siguiente guía.


Resumen de los códigos
```js
// Declaración de función
function nombreCompleto(nombre, apellido) {
  console.log(`${nombre}, ${apellido}`);
}
nombreCompleto("Mielma", "Developer"); // "Mielma, Developer"
// Expresión de función`;
nombreCompleto = function (nombre, apellido) {
  console.log(`${nombre}, ${apellido}`);
};
nombreCompleto("Mielma", "Developer"); // "Mielma, Developer"
// Función flecha
saludo = () => {
  console.log("Hola");
};
saludo();
// Función de flecha con argumento de función abreviada para argumentos únicos
nombre = (nombre) => {
  console.log(nombre.toUpperCase());
};
nombre("Mielma"); // "MIELMA"
// Función de flecha con múltiples argumentos
nombreCompleto = (nombre, apellido) => { console.log(`${nombre}, ${apellido}`); }
nombreCompleto('Mielma', 'Developer');"Mielma, Developer"
```
![Arrow Function][Arrow Function]




## <center><b><font color="#006cb5">Coding Exercise</font></b>
Use a function expression called userInfo with three arguments for city, state, and zip. It must return Lehi, UT 84043.

Resultado:
```js
userInfo=(city, state, zip) => { return(`${city}, ${state} ${zip}`);}
userInfo("Lehi", "UT", "84043");
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/introduction-arrow-functions-javascript)  

<!-- [Código DevCamp]() -->

[Código Mielma Arrow Function](https://codepen.io/ElizabethMaranon/pen/PovQgYE)

<!-- Ordenar enlaces -->

[Arrow Function]: image/Arrow_Function.png
[Arrow Funcions Link]: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Functions/Arrow_functions