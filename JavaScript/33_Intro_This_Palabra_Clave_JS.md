![Logo Mielma](Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Introducción a la palabra clave 'this' en JavaScript</font></b>

## <b><font color="#006cb5">¿Qué significa palabra clave "this"[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/this)?</font></b>
<p style="text-align: justify;">
This en JavaScript es una palabra clave muy utilizada dentro de funciones y clases, pues tiene un valor flexible. This significa esto en español y, como su nombre indica, hace referencia al objeto en cuestión.
<p style="text-align: justify;">
La palabra clave this de una función se comporta un poco diferente en Javascript en comparación con otros lenguajes. Además tiene algunas diferencias entre el modo estricto y el modo no estricto.
<p style="text-align: justify;">
En general, el valor de this está determinado por cómo se invoca a la función. No puede ser establecida mediante una asignación en tiempo de ejecución, y puede ser diferente cada vez que la función es invocada.

```js
console.log(this.document === document); // true

// En los navegadores web, el objeto window también es un objeto global:
console.log(this === window); // true

this.a = 37;
console.log(window.a); // 37
```

'this' es una palabra muy especial en JavaScript.

### <font color="#556CEE">Ejercicio</font>
Escribir 'Jquery', esto hará que no se abra el enlace aunque hagas click
```js
$('.track-title').click(function(event) {
    event.preventDefault();
    console.log($(this));
});
```
Devuelve lo que hay en track-title
```js
E.fn.init {0: div.track-title, 1: div.track-title, 2: div.track-title, length: 3, prevObject: E.fn.init}.
0: div.track-title
1: div.track-title
2: div.track-title
length: 3
prevObject: E.fn.init {0: document, length: 1}
[[Prototype]]: Object
```


## <center><b><font color="#006cb5">Coding Exercise</font></b>
Follow the instructions below to utilize the this keyword to create a new person with the name of Jordan
```js
class Person {
  constructor(name){
    this.name = name;
  }
}

const yourPerson = new Person('enterTheNameInHere');
```
Resultado:
```js
class Person {
  constructor(name){
    this.name = name;
  }
}

const yourPerson = new Person('Jordan')
```


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/introduction-this-keyword-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_08_introduction_this.js)

<!-- [Código Mielma]() -->