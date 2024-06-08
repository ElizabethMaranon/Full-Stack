![Logo Mielma](Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Cómo trabajar con argumentos de funciones en JavaScript</font></b>

## <b><font color="#006cb5">¿Qué son los argumentos en Javascript?</font></b>
<p style="text-align: justify;">
Una función puede tener cero o más parámetros. Así, los parámetros son los nombres que aparecen en la definición de una función. Por su parte, los argumentos son los valores que le pasamos (y que, por tanto, recibe) una función.
<p style="text-align: justify;">
El término parámetro, se usa a menudo para referirse a la variable en la declaración del método, mientras que argumento, se refiere al valor que se envía. Para evitar confusiones, es común ver a un parámetro como una variable y un argumento como un valor.

### <font color="#556CEE">Declaración de función con dos argumentos</font>

```js
// function nombre_función(argumento1, argumento2)
function Función(arg1, arg2) {
  // concatenar con ","
  return arg1.toUpperCase() + "," + arg2.toUpperCase();
}
//console.log(nombre_función('parámetro1', 'parámetro2'))
console.log(Función('parámetro1', 'parámetro2'))

// Console: "PARÁMETRO1,PARÁMETRO2"
```
### <font color="#556CEE">Declaración de función con argumentos sin parámetros</font>

```js
// function nombre_función(argumento1, argumento2)
function Ejemplo(arg1, arg2) {
console.log(arg1);
console.log(arg2);
}
Ejemplo();

// Console: undefined
//          undefined
```
### <font color="#556CEE">Declaración de función con argumento opcional no definido</font>
```js
// function nombre_función(argumento1, argumento2, opcional)
function Opcional(arg1, arg2, opc) {
  // concatenar con ","
  return arg1.toUpperCase() + "," + arg2.toUpperCase() + " - " + opc;
}
//console.log(nombre_función('parámetro1', 'parámetro2'))
console.log(Opcional('para', 'para2')) // "PARA,PARA2 - undefined"
```

### <font color="#556CEE">Declaración de función con argumento opcional definido</font>

```js
// function nombre_función(argumento1, argumento2, opcional)
function OpcionalDefecto(arg1, arg2, opc) {
  // Variable será el parámetro || En su defecto aparecerá esto
    var opc = opc || 'Por Defecto';
  // concatenar con ","
  return arg1.toUpperCase() + "," + arg2.toUpperCase() + " - " + opc;
}
//console.log(nombre_función('parámetro1', 'parámetro2'))
console.log(OpcionalDefecto('para', 'para2')) // "PARA,PARA2 - Por Defecto"
console.log(OpcionalDefecto('para', 'para2', 'para3')) // "PARA,PARA2 - para3"
```


## <center><b><font color="#006cb5">Coding Exercise</font></b>
Create a function called sum that adds two arguments together and returns the sum of the two numbers.
```js
var uno = 10;
var dos = 20;

function sum (uno, dos) {
    return uno + dos;
}
```


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-work-function-arguments-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_04_function_arguments.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/eYaWLaw)