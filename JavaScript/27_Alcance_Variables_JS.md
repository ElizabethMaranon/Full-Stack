![Logo Mielma](/Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Cómo funciona el alcance variable en JavaScript</font></b>

Es muy importante comprender exactamente cómo funciona el alcance variable en JavaScript para que podamos utilizarlo correctamente, podamos organizar nuestro código de la manera correcta y también para no encontrarnos con un comportamiento extraño en el que tenemos un valor que es disponible y podría ser llamado accidentalmente o incluso anulado más adelante en un programa.

## <b><font color="#006cb5">¿Qué es el alcance de una variable?</font></b>

El alcance define en que partes del código se puede acceder o utilizar una variable, ya que mientras algunas variables pueden ser accedidas en cualquier parte del programa, otras solo pueden ser utilizadas en ciertas partes del código.

## <b><font color="#006cb5">¿Qué es Scope[🔗](https://developer.mozilla.org/es/docs/Glossary/Scope)?</font></b>

El contexto actual de ejecución. El contexto en el que los valores y las expresiones son "visibles" o pueden ser referenciados. Si una variable u otra expresión no está "en el Scope- alcance actual", entonces no está disponible para su uso. Los Scope también se pueden superponer en una jerarquía, de modo que los Scope secundarios tengan acceso a los ámbitos primarios, pero no al revés.

Una función sirve como un cierre en JavaScript y, por lo tanto, crea un ámbito, de modo que (por ejemplo) no se puede acceder a una variable definida exclusivamente dentro de la función desde fuera de la función o dentro de otras funciones.

### <font color="#556CEE">Ejercicio</font>
#### <font color="#006cb5">Alcance global</font>
La función recibe el valor de la variable
```js
// Crear usuario
var usuario = { 
email: 'mielma@devcamp.com',
nombre: 'Acceso global'
}
// Crear función saludo
function saludo(){ 
//concat uniría string con el nombre de usuario
console.log("Hola, ".concat(usuario.nombre));
}
// LLamar a la función
saludo(); // "Hola, acceso global"
```
#### <font color="#006cb5">Alcance local</font>
La función anularía la variable creada fuera de la función, lo haría solamente dentro de la función, ya que el valor de la variable creada fuera de la función no cambiaría.

La variable local solamente funcionaría dentro de la función desde la que se le crea.

Al llamar al objeto, devuelve el valor de la variable global.

<b><font color="red">⚠️Si no se pusiera var o let delante de la variable ya no sería local, 

⚠️ Usar siempre var o let al crear la variable dentro de la función</b></font>
```js
// Crear la función
function saludo() {
  // Variable dentro de función
  var usuario = {
    email: 'mielma@devcamp.com',
    nombre: 'Acceso local'
  }
//concat uniría string con el nombre de usuario  
console.log("Hola, ".concat(usuario.nombre));
}
// LLamar a la función
saludo(); // "Hola, Acceso local"
```
#### <font color="#006cb5">Llamar a la variable</font>
```js
console.log(usuario.nombre) // "Acceso global"
```
<!-- ## <b><font color="#006cb5">Coding Exercise</font></b>
```js
```
Resultado:
```js
``` -->


# <center><b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios]()  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_02_variable_scope.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/gOJWMMV)