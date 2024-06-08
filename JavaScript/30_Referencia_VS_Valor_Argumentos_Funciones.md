![Logo Mielma](logo/Logo%20Encabezado.png)

# <center><b><font color="#556CEE">Argumentos de función: referencia frente a valor</font></b>
Si le pasamos un objeto,  se comporta de manera muy diferente que si le pasara una variable.

## <b><font color="#006cb5">Valor Vs Referencia</font></b>
### <font color="#556CEE">Valor</font>
Cuando asignamos un valor a una variable, o pasamos un argumento a una función, este proceso siempre se hace “por valor”
```js
var nombre = Mielma
```
### <font color="#556CEE">Referencia</font>
Estrictamente hablando, JavaScript no nos ofrece la opción de pasar o asignar “por referencia” (by reference en inglés), como en otros lenguajes. Lo interesante en nuestro caso, es que cuando una variable hace referencia a un objeto (Object, Array o Function), el “valor” es la referencia en sí.

### <font color="#556CEE">Ejercicio</font>
```js
var usuario  = {
    nombre: 'Mielma'
}
```
El valor de la variable cambia permanentemente

```js
var objeto = {
    nombre: 'Variable Objeto'
}
function formatearObjeto(objeto) {
    return objeto.nombre = 'Variable Objeto Modificada';
}
console.log(formatearObjeto(objeto)); // "Variable Objeto Modificada"
console.log(objeto); // [object Object] {"nombre": "Variable Modificada "}
```
El valor de la variable cambia en la función, pero si se le llama desde fuera, conserva el valor original
```js
function formatearObjeto2(nombreObjeto) {
    return nombreObjeto = 'Variable Objeto Modificada';
}
console.log(objeto.nombre); // "Variable Objeto Modificada"

objeto.nombre = 'Variable Objeto Original2';

console.log(formatearObjeto(objeto.nombre)); // "Variable Objeto Modificada"
console.log(objeto.nombre); // "Variable Objeto Original2"
```
El valor de la variable cambia en la función, pero si se le llama desde fuera, conserva el valor original
```js
var algúnNombre = 'Variable Nombre Original';

function formatearVariable(name) {
    return nombre = 'Variable Nombre Modificada';
}
console.log(formatearVariable(algúnNombre)); // "Variable Nombre Modificada"
console.log(algúnNombre); // "Variable Nombre Original"
```


## <center><b><font color="#006cb5">Coding Exercise</font></b>
Overwrite the someUser.name value so that it says "Jordan" instead of "Blank".
```js
var someUser = {
    name: 'Blank'
};

function changeName(user) {
    return // write the code to overwrite someUser.name
}

changeName(someUser);
```
Resultado:
```js
var someUser = {
    name: 'Blank'
};

function changeName(user) {
    return user.name = 'Jordan';// write the code to overwrite someUser.name
}

changeName(someUser);
```


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios]()  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_05_reference_vs_value.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/vYwZGyJ)