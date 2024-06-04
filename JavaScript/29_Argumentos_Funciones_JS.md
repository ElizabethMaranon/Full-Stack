![Logo Mielma](logo/Logo%20Encabezado.png)

# <center><b><font color="#556CEE">Cómo trabajar con argumentos de funciones en JavaScript</font></b>

## <b><font color="#006cb5">¿Qué son los argumentos en Javascript?</font></b>
<p style="text-align: justify;">
Una función puede tener cero o más parámetros. Así, los parámetros son los nombres que aparecen en la definición de una función. Por su parte, los argumentos son los valores que le pasamos (y que, por tanto, recibe) una función.
<p style="text-align: justify;">
El término parámetro, se usa a menudo para referirse a la variable en la declaración del método, mientras que argumento, se refiere al valor que se envía. Para evitar confusiones, es común ver a un parámetro como una variable y un argumento como un valor.

Declaración de función con dos argumentos
```js
// function nombre_función(argumento1, argumento2)
function Función(arg1, arg2) {
  // concatenar con ","
  return arg1.toUpperCase() + "," + arg2.toUpperCase();
}
//console.log(nombre_función('parámetro1', 'parámetro2'))
console.log(Función('parámetro1', 'parámetro2'))

//Console: "PARÁMETRO1,PARÁMETRO2"
```
```js
function Ejemplo(arg1, arg2) {
console.log(arg1);
console.log(arg2);
}
Ejemplo();

// Console: undefined
//          undefined
```




<!-- ## <center><b><font color="#006cb5">Coding Exercise</font></b>
```js
```
Resultado:
```js
``` -->


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-work-function-arguments-javascript)  

<!-- [Código DevCamp]() -->

<!-- [Código Mielma]() -->