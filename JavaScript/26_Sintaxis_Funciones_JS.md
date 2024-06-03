![Logo Mielma](logo/Logo%20Encabezado.png)

# <b><font color="#556CEE">Sintaxis básica para crear funciones en JavaScript</font></b>

## <b><font color="#006cb5">Diferencia retur e imprimir</font></b>
<p style="text-align: justify;">
print: imprime lo que tenga dentro de los paréntesis () puede ser una variable o un valor. nota: esto se puede hacer en cualquier parte de la funcion.  
<p style="text-align: justify;">
return: esto finaliza la funcion y retorna lo que tengas a la derecha; puede ser una variable, objeto o un valor.


<p style="text-align: justify;">
Una definición de función, también denominada declaración de función o expresión de función consta de la palabra clave `function`, seguida de:

+ El nombre de la función.
+ Una lista de parámetros de la función, entre paréntesis y separados por comas.
+ Las declaraciones de JavaScript que definen la función, encerradas entre llaves, { ... }.

<p style="text-align: justify;">
Nuestra función aquí en realidad no devolvió nada. Todo lo que hizo fue imprimirlo en la consola. Hola. Eso está muy bien. Sin embargo, hay muy pocas ocasiones en las que creará una función que no devuelva nada en absoluto. Y el nombre para eso se llama función nula.

<p style="text-align: justify;">
Lo que eso significa es que esta función se ejecutará pero no devolverá nada. Eso sería algo así como cuando estás ejecutando un proceso. Pero el proceso no devuelve nada parecido al inicio. Quizás una parte de un servidor o algo así. Y por ahora no tienes que preocuparte por qué está haciendo exactamente aquí. Entonces, cuando digo la función "Hola", el registro de la consola lo único que sucede es que se imprime en la consola..

```js
function fun_basic_console(){
  console.log('Console.log imprime, Return devuelve para usar posteriormente, ')
}
fun_basic_console() // Imprime

function fun_basic_return(){
  return('Return devuelve para usar posteriormente, Console.log imprime')
}
fun_basic_return() // Devuelve
```
Crear variables con las funciones
```js

var imprimir = fun_basic_console(); // Imprime

imprimir; // undefined

var devolver = fun_basic_return();

devolver; // devuelve

```



<!-- ## <b><font color="#006cb5">Coding Exercise</font></b>
```js
```
Resultado:
```js
``` -->


# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/section-introduction-introduction-javascript-functions)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_01_function_syntax.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/bGyqzPN)