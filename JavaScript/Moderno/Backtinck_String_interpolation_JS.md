![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Guía para la interpolación de cadenas Backtick (Backtick string interpolation) en Javascript</font></b>
## <b><font color="#006cb5">Backtick → Literales de plantilla[🔗][Bactick Literales de plantilla] (cadenas de plantilla) </font></b>
Literales de plantilla son literales delimitados con comilla invertida ```(`)``` personajes, permitiendo *cadenas de varias líneas*, *interpolación de cadenas* con expresiones incrustadas y construcciones especiales llamadas *plantillas etiquetadas*.

Los literales de plantilla a veces se denominan informalmente cadenas de plantilla, porque se utilizan más comúnmente para *interpolación de cadenas* (para crear cadenas mediante la sustitución de marcadores de posición). Sin embargo, es posible que un literal de plantilla etiquetado no dé como resultado una cadena; se puede utilizar con un personalizado *función de etiqueta* para realizar cualquier operación que desee en las diferentes partes del literal de plantilla.

### <font color="#556CEE">Sintaxis</font>
```js
`string text`

`string text line 1
 string text line 2`

`string text ${expression} string text`

tagFunction`string text ${expression} string text`
```

#### <font color="#006cb5">Parámetros</font>
`string text`
El texto de cadena que pasará a formar parte del literal de plantilla. Casi todos los caracteres están permitidos literalmente, incluidos *saltos de línea* y otra *caracteres de espacio en blanco*. Sin embargo, las secuencias de escape no válidas provocarán un error de sintaxis, a menos que se *función de etiqueta* se utiliza.

`expression`
Una expresión que se insertará en la posición actual, cuyo valor se convierte en una cadena o se pasa a `tagFunction`.

`tagFunction`
Si se especifica, se llamará con la matriz de cadenas de plantilla y las expresiones de sustitución, y el valor de retorno se convierte en el valor del literal de plantilla.

### <font color="#556CEE">Descripción</font>
Los literales de plantilla están encerrados entre comillas invertidas. ```(`)``` caracteres en lugar de comillas dobles o simples.

Además de tener cadenas normales, los literales de plantilla también pueden contener otras partes llamadas *marcadores de posición*, que son expresiones incrustadas delimitadas por un signo de dólar y llaves: `${expression}`. Las cadenas y los marcadores de posición se pasan a una función, ya sea una función predeterminada o una función que usted proporciona. La función predeterminada (cuando no proporciona la suya propia) simplemente realiza hacer la sustitución de los marcadores de posición y luego concatenar las partes en una sola cadena.

Para proporcionar una función propia, preceda el literal de plantilla con un nombre de función; el resultado se llama ***plantilla etiquetada***. En ese caso, el literal de plantilla se pasa a su función de etiqueta, donde luego puede realizar las operaciones que desee en las diferentes partes del literal de plantilla.

`\`

```js
`\`` === "`"; // true

`\${1}` === "${1}"; // true

```
#### <font color="#006cb5">Cadenas de varias líneas</font>

Cualquier carácter de nueva línea insertado en la fuente es parte del literal de la plantilla.

Usando cadenas normales, tendría que usar la siguiente sintaxis para obtener cadenas de varias líneas:
```js
console.log("string text line 1\n" + "string text line 2");
// "string text line 1
// string text line 2"
```
Usando literales de plantilla, puedes hacer lo mismo con esto:

```js
console.log(`string text line 1
string text line 2`);
// "string text line 1
// string text line 2"
```
#### <font color="#006cb5">Interpolación de cadenas</font>
Sin literales de plantilla, cuando desee combinar resultados de expresiones con cadenas, deberá concatenarlos Utilizando el operador de suma +:
```js
const a = 5;
const b = 10;
console.log("Fifteen is " + (a + b) + " and\nnot " + (2 * a + b) + ".");
// "Fifteen is 15 and
// not 20."
```
Puede ser difícil de leer, especialmente cuando tienes varias expresiones.
`${expression}`
```js
const a = 5;
const b = 10;
console.log(`Fifteen is ${a + b} and
not ${2 * a + b}.`);
// "Fifteen is 15 and
// not 20."
```
Tenga en cuenta que existe una ligera diferencia entre las dos sintaxis. Literales de plantilla coaccionar sus expresiones directamente a cadenas, mientras que la suma fuerza sus operandos a primitivos primero. Para obtener más información, consulte la página de referencia del + operador.


## <b><font color="#006cb5">Guía DevCamp → Backtick string interpolation</font></b>
Esta lección tratará sobre enfoques modernos para usar la interpolación de cadenas.
Ahora, una revisión rápida de la antigua forma de usar la interpolación de cadenas fue algo como esto. Tenemos nuestra constante de letras como variable aquí., `const lyrics = 'Never gonna give you up'`; Y si quiero agregarle algo, entonces si quiero un registro de la consola, diga: "Y luego tendré que agregar un espacio aquí en lugar de un plus".
`console.log("I'm " + lyrics)`;
Y luego puedo llamar letras. Ahora, si guardo y luego ejecuto esto, todo funcionará.
```js
const backtick = 'String interpolation'
console.log("Mielma " + backtick); //"Mielma String interpolation"
```
![Backtick String Interpolation][Backtick String Interpolation]

Esto está bien, pero las versiones más modernas de JavaScript nos brindan una manera mucho mejor de hacerlo y utilizan comillas invertidas. Ahora, si nunca has usado la parte posterior antes, hay un pequeño botón justo encima del botón de pestaña en tu teclado.
Entonces, en lugar de estas comillas dobles, usaré esta comilla invertida. Ahora, cuando miras la documentación, puedes confundirte y pensar que esto es solo un apóstrofo normal.

No lo es. Es una comilla invertida. Así que voy a hacer una comilla invertida aquí mismo. Ahora esto se considera una cadena normal y voy a aclararlo. Y sólo para demostrártelo voy a ejecutarlo de nuevo. Y si lo ejecuta, podrá ver que lo ha convertido en una cadena normal.
```js
const backtick = 'String interpolation'
console.log(`Mielma  ${backtick}`); //"Mielma String interpolation"
```
![Backtick String Interpolation Moderno][Backtick String Interpolation Moderno]

Muchas veces veo estudiantes que ven esta sintaxis y solo ven un ejemplo como este, y piensan que solo puedes colocar una única variable dentro de allí. Pero en realidad puede ser cualquier cosa que desees dentro de ese lugar y lo ejecutará como Javascript puro.
Esa es la forma moderna de usar la interpolación de cadenas en javascript.
```js
const backtick = 'String interpolation'
console.log(`Mielma  ${backtick}`); // "Mielma String interpolation"
console.log(`Mielma ${2 + 2}`); // "Mielma 4"
console.log(`Mielma ${backtick + " escribe lo que quieras " + backtick}`); // "Mielma String interpolation escribe lo que quieras String interpolation"
```
![Backtick String Interpolation Moderno Varias][Backtick String Interpolation Moderno Varias]




## <center><b><font color="#006cb5">Coding Exercise</font></b>
Inside the below function, write a variable and give it a string that says "It's a trap!" Then on the `return` use string interpolation to finish the movie line
```js
function movieLine() {
    // Set your variable here
    
    return (`replace-this-with-something-clever ${}`)
}
```
Resultado:
```js
function movieLine() {
    const trap = "It's a trap!"
    
    return (`Es una trampa! ${trap}`)
}
console.log(movieLine())
```
![Backtick String Interpolation Moderno Coding Exercise][Backtick String Interpolation Moderno Coding Exercise]

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-backtick-string-interpolation-javascript)  



[Código Mielma Backtick](https://codepen.io/ElizabethMaranon/pen/wvbyRGE)

[Código Mielma Backtick Moderno](https://codepen.io/ElizabethMaranon/pen/vYwdvgW)

[Código Mielma Backtick Moderno Coding Exercise](https://codepen.io/ElizabethMaranon/pen/NWVyeym)



<!-- Ordenar enlaces -->

[Backtick String Interpolation]: image/Backtick_string_interpolation.png

[Backtick String Interpolation Moderno]: image/Backtick_string_interpolation_moderno.png

[Backtick String Interpolation Moderno Varias]: image/Backtick_string_interpolation_moderno_varias.png

[Backtick String Interpolation Moderno Coding Exercise]: image/Backtick_String_Interpolation_Moderno_Coding_Exercise.png

[Bactick Literales de plantilla]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#syntax