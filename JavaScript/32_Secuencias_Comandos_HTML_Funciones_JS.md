![Logo Mielma](Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Introducción a las secuencias de comandos HTML con funciones JavaScript integradas</font></b>

## <b><font color="#006cb5">¿Qué son las secuencias de comandos?</font></b>


Las secuencias de comandos permiten calcular valores, intercambiar datos entre las diversas tareas del proceso y ejecutar operaciones específicas utilizando llamadas SOAP. Las secuencias de comandos son ubicuas en los diagramas de flujo de trabajo: Todas las actividades tienen secuencias de comandos de inicialización.

## <b><font color="#006cb5">Cómo aprovechar las funciones de JavaScript integradas para modificar el contenido de un sitio web</font></b>


Dado que javascript se procesa dentro del navegador, muchas de las funciones que proporciona también funcionan con el propio navegador.

### <font color="#556CEE">Ejercicio</font>

Inspeccionar página, desde allí se puede ver los datos que tiene el documento y acceder a la consola y tener acceso a todo el código.

`document` consulta todo el código
```js
#document (https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/introduction-html-scripting-built-javascript-functions)<!DOCTYPE html><html>​<head>​…​</head>​<body>​…​</body>​</html>​
```

`document.getElementsByClassName('item-title')` Consulta el código con clase 'item-title' y te devuelve un objeto y en el se pueden ver toda clase de atributos
```js
HTMLCollection [div.item-title]
0: div.item-title
length: 1
[[Prototype]]: HTMLCollection
```
`document.getElementsByClassName('item-title')[0]` El número selecciona el primero, ya que empieza a contar desde 0
```js
<div class="item-title">Introducción a las secuencias de comandos HTML con funciones JavaScript integradas</div>
```
`document.getElementsByClassName('item-title')[0].innerHTML = "Mielma Full Stack Developer"` Con inner HTML cambiamos la variable temporalmente
```
'Mielma Full Stack Developer'
```
![Cambiar datos HTML](image/Cambias_Datos_HTML.png)


Es muy útil cuando creamos programas que necesitan cambiar su contenido sobre la marcha.




## <center><b><font color="#006cb5">Coding Exercise</font></b>
Grab the below paragraph tag by its class name and change the inner HTML of the tag to Wizards don't jump they float.
```js
var weirdSentence = //Write your code here!
```
Resultado:
```js
var weirdSentence = document.getElementsByClassName("p > grabThis")
weirdSentence.innerHTML = "Wizards don't jump they float";

console.log(weirdSentence.innerHTML);
```


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/introduction-html-scripting-built-javascript-functions)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_97_built_in_functions.js)

<!-- [Código Mielma]() -->
[Cómo cambiar texto html con javascript, seleccionado una clase y cambiando la etiqueta adentro](https://es.stackoverflow.com/questions/339708/c%C3%B3mo-cambiar-texto-html-con-javascript-seleccionado-una-clase-y-cambiando-la-et)
