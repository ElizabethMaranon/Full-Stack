![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Integración de condicionales en cadenas de JavaScript con operadores ternarios</font></b>
<!-- ## <b><font color="#006cb5"></font></b>
### <font color="#556CEE"></font>
#### <font color="#006cb5"></font> -->
## <b><font color="#006cb5">Guía DevCamp → Condicionales en cadenacon operadores ternario en JS</font></b>
En la última guía hablamos sobre la interpolación de cadenas y cómo las versiones modernas de JavaScript permiten una sintaxis de retroceso que hace que sea mucho más fácil combinar el desarrollo de JavaScript con las cadenas tradicionales y antiguas.
`${}`

Eso se vería absolutamente horrible, necesitarías tener todas estas líneas diferentes y no querrías poner todo eso dentro de una cadena. Lo que puedes hacer es usar lo que se llama un operador ternario. La mayoría de los lenguajes de programación tienen este tipo de operador y es una forma de comprobar si algo es cierto y luego realizar una acción. Y si no realizar otra acción.

Solo puedes tener un if y un else, no puedes tener múltiples capas, por lo que esto es solo para tipos básicos de condicionales. Sólo puedes tener un tipo de cheque. Entonces, lo que vamos a hacer es un ejemplo bastante práctico aquí donde vamos a cambiar la clase..

Puedes pensar que esto es algo en lo que realizaríamos este tipo de acción dentro de, digamos, un marco como angular donde queremos cambiar la clase de un div o algún tipo de elemento HTML en la página, en función de lo que tipo de página en la que se encuentra.

Entonces, aquí lo que puedo hacer es decir que quiero crear una clase o quiero definir una clase y quiero que sea dinámica en función del valor de esta variable aquí y no la voy a cambiar. . Entonces esto debería ser simplemente una constante y no un let.

Entonces, para una clase aquí, esta es solo tu cadena normal. Esto es lo que encontrarías en el documento HTML. Y voy a usar interpolación de cadenas con nuestras llaves de dólar, y ahora solo voy a escribir un operador ternario.
```js
// const page = 'Mielma'; // "class=Full Stack"
const page = 'Eli'; // "class=Marañón"
console.log(`class=${ page === 'Mielma' ? 'Full Stack' : 'Marañón' }`);
```
![Ternary Operator Condicional 1][Ternary Operator Condicional 1]
![Ternary Operator Condicional 2][Ternary Operator Condicional 2]

Esta es una excelente manera de agregar algo de comportamiento dinámico directamente a su sistema y lo verá mucho en marcos modernos como angular y reaccionar. Así que analicemos lo que estamos pasando aquí..

Un operador ternario se compone de tres componentes. El primero es el condicional. Así que ahí es donde comprobamos si Page es igual a casa. Y luego tienes todo este signo de interrogación y luego el primer componente justo después es qué sucede si esta condición es verdadera, luego tienes dos puntos seguidos de lo que sucede si esta condición no es verdadera..

Así es como se puede crear un turno para el operador. Tiene una condición seguida del resultado si es verdadero, seguida del resultado si no lo es. Es un condicional muy básico pero es bueno porque puedes realizarlo en una sola línea.


## <center><b><font color="#006cb5">Coding Exercise</font></b>
In the below function's return, use a ternary that returns "1 point", when the ship variable is set to "hit". Otherwise, have it return "You lost a point". Then, set the ship variable to "hit" or "miss".
```js
// Fill in the below code with your requirements

var ship = "";

function battleShip() {
  return()
}
```
Resultado:
```js
var ship = "hit";
//var ship = "miss";

function battleShip() {
  return(ship === 'hit' ? '1 point' : 'You lost a point')
}

console.log(battleShip())
```
![Ternary Operators Condicional Coding Exercise][Ternary Operators Condicional Coding Exercise]

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios]()  

[Código DevCamp]()

[Código Mielma]()

<!-- Ordenar enlaces -->

[Ternary Operator Condicional 1]: image/Ternary_Operator_Condicional1.png

[Ternary Operator Condicional 2]: image/Ternary_Operator_Condicional2.png

[Ternary Operators Condicional Coding Exercise]: image/Ternary_Operators_Condicional_Coding_Exercise.png