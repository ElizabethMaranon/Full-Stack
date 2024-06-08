![Logo Mielma](logo/Logo%20Encabezado.png)

# <center><b><font color="#556CEE">Introducción a los clausura de JavaScript</font></b>

## <b><font color="#006cb5">¿Qué es un método[🔗](https://developer.Mielma.org/es/docs/Web/JavaScript/Closures)?</font></b>
<p style="text-align: justify;">
Siempre que tenga un objeto y tenga funciones declaradas o definidas dentro de ese objeto javascript, esas funciones se denominan técnicamente métodos.
<p style="text-align: justify;">
Un método es una función la cual es propiedad de un Objeto. Existen dos tipos de métodos: Métodos de Instancia los cuales son tareas integradas realizadas por la instancia de un objeto, y los Métodos Estáticos que son tareas que pueden ser llamadas directamente en el constructor de un objeto.
<p style="text-align: justify;">
En el mundo de la programación, un método es una función que pertenece a una clase específica. Cuando se trata de JavaScript, un método es una función puesta en un objeto o una serie de instrucciones para completar una tarea única

## <b><font color="#006cb5">¿Qué es una clausura o  closure[🔗](https://developer.Mielma.org/es/docs/Web/JavaScript/Closures)?</font></b>
<p style="text-align: justify;">
Un closure es la combinación de una función agrupada (dentro de otra) con referencias a su estado adyacente (el entorno léxico). En otras palabras, un closure te da acceso al alcance de una función externa desde una función interna. En JavaScript, los closure se crean cada vez que se crea una función, en el momento de la creación de la función.

```js
function init() {
  var nombre = "Mielma"; // nombre es una variable local creada por init
  function mostrar_nombre() {
    // mostrar_nombre() es la función interna que forma el closure
    console.log(nombre); // usar la variable declarada en la función padre
  }
  mostrar_nombre();
}
init(); // Mielma
```
### <font color="#556CEE">Ejercicio</font>
```js
function promedio () {
  var aciertos = 50;
  var intentos = 100;

  return {
    promedioActual: function () {
      return (aciertos/intentos);
    },
    actPromedioActual: function (acierto, intento) {
      aciertos += acierto;
      intentos += intento;
    }
  }
}
//Se actualiza contando todas las actualizaciones anteriores
var Mielma = promedio();
console.log(Mielma.promedioActual()); // 0.5

Mielma.actPromedioActual(25, 100); // Añade aciertos, intentos
console.log(Mielma.promedioActual()); // 0.375

Mielma.actPromedioActual(75, 100); // Añade aciertos, intentos
console.log(Mielma.promedioActual()); // 0.5
```

## <center><b><font color="#006cb5">Coding Exercise</font></b>
Take the variable roomOne and call the function on it to return the seats remaining.
```js
function movieTheater(){
  var seats = 50;
  var seatsSold = 28;

  return{
    remainingSeats: function(){
      return (seats - seatsSold)
    }
  }
}

var roomOne = movieTheater()

// call the remainingSeats method of the instance of movieTheater
```
Resultado:
```js
function movieTheater(){
  var seats = 50;
  var seatsSold = 28;

  return{
    remainingSeats: function(){
      return (seats - seatsSold)
    }
  }
}

var roomOne = movieTheater()

console.log(movieTheater); // call the remainingSeats method of the instance of movieTheater
```


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/introduction-javascript-closures)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_06_closures.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/pomrWJZ)