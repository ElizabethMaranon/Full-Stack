![Logo Mielma](logo/Logo%20Encabezado.png)

# <b><font color="#556CEE">Guía para el Hosting de JavaScript</font></b>

## <b><font color="#006cb5">¿Qué es Hoisting?</font></b>

Una forma muy específica en la que el intérprete de JavaScript lee las variables.

Hoisting es un comportamiento en JavaScript donde las declaraciones de variables y funciones se mueven al principio del ámbito en el que se encuentran, antes de que se ejecuten otras líneas de código en el mismo ámbito.

Hoisting es un término que no encontrará utilizado en ninguna especificación previa a la Especificación del Lenguaje ECMAScript® 2015. El concepto de Hoisting fue pensado como una manera general de referirse a cómo funcionan los contextos de ejecución en JavaScript (específicamente las fases de creación y ejecución)

### <font color="#556CEE">¿Qué caracteriza al hoisting en relación con la palabra clave var?</font>

La principal diferencia entre las variables declaradas con let y var en relación al hoisting es el alcance. Mientras que las variables declaradas con var son elevadas al principio de su ámbito de función, las variables declaradas con let no son elevadas y permanecen en la posición en la que se definen.
~~~
console.log(edad);
var edad = 44
~~~
Imprime indefinido, podría provocar algunos errores extraños, por lo que hay que declarar las variables en la parte de superior.

## <b><font color="#006cb5">Coding Exercise</font></b>
Create a variable called name and its value must be set to "Jordan".
~~~
var name = "Jordan";
~~~

# <b><font color="#556CEE">Links</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-javascript-hoisting)

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/179cd0b3441bc8b69a0770c0bc8c42f102325770/section_b_08_comments.js)