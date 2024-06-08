![Logo Mielma](logo/Logo_Encabezado.png)

# <b><font color="#556CEE">Descripción general del operador ternario de JavaScript</font></b>

## <b><font color="#006cb5">¿Qué es operador ternario[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/switch#default)?</font></b>
El operador condicional (ternario) es el único operador en JavaScript que tiene tres operandos. Este operador se usa con frecuencia como atajo para la instrucción if.

Si la condición es true, el operador retorna el valor de la expr1; de lo contrario, devuelve el valor de expr2. 

El operador ternario puede ser muy confuso, tiene una sintaxis muy diferente a la del condicional JavaScript normal o incluso a la declaración Switch. 

Lo que un operador ternario te permite hacer es hacer eso, es escribir un condicional completo en una sola línea.

```html
<!-- Si tiene permiso entonces quiero que regrese activo y si no, quiero que regrese deshabilitado. -->
<div Usuario={Permiso ? 'activo' : 'deshabilitado'}>
</div>
```
Entonces, esta es la razón principal por la que es tan importante aprender los operadores ternarios, porque si está creando algún tipo de aplicación front-end del mundo real, lo más probable es que tenga que construir algo como esto en algún momento u otro.

### <font color="#556CEE">Ejercicio</font>
Verificar edad alquiler coche
```js
// Verificar edad if/else
function if_else(edad) {
  if (edad > 25) {
    console.log('Sí, Verificar edad if/else');
  } else {
    console.log("No, Verificar edad if/else");
  }
}
if_else(30); // Sí, Verificar edad if/else
if_else(10); // No, Verificar edad if/else
```
```js
// Verificar edad operador ternario con variable
function ternario_var(edad) {
    //Crear variable si edad mayor 25 ? if si : else (if no)
    let respuesta = edad > 25 ? 'Sí, operador ternario con var' : "No, operador ternario con var"
    console.log(respuesta);
}
ternario_var(30); // Sí, operador ternario con var
ternario_var(10); // No, operador ternario con var
```
<b>La forma correcta de usar operador ternario</b>

```js
// Verificar edad operador ternario sin variable
function ternario(edad) {
    //Si edad mayor 25 ? console.log(if si) : console.log(else (if no)) ;
    //Importante no olvidar ; al acabar la línea
    edad > 25 ? console.log('Sí, operador ternario') : console.log("No, operador ternario");
}
ternario(30); // Sí, operador ternario
ternario(10); // No, operador ternario
```

### <font color="#556CEE">Ejercicio 2</font>
```js

// Ejercicio permiso, registrado, autorizado if/else
function permiso(usuario) {
    if (usuario) { // Si  registrado
        if (usuario.administrador) { // Si registrado
            console.log('Registrado y autorizado');
        } else { // Si registrado, no admin
            console.log('Registrado pero no autorizado');
        }
    } else { // No registrado
        console.log('No estas registrado')
    }
}
let Mielma = {
  nombre : 'Mielma',
  administrador : true
}
let mielma = {
  nombre : 'mielma',
  administrador : false
}
let eli = null

permiso(Mielma) // "Registrado y autorizado"
permiso(mielma) // "Registrado pero no autorizado"
permiso(eli) // "No estas registrado"
```
```js
// Ejercicio permiso, registrado, autorizado operador ternario
function permiso_ternario(usuario) { // Usar paréntesis ayuda a la lectura, pero no es obligatorio
  let respuesta = usuario ? (usuario.administrador ? "Registrado y autorizado, ternario" : "Registrado pero no autorizado, ternario"): "No estas registrado, ternario";
console.log(respuesta);
}
// Let ya están declaradas anteriormente
permiso_ternario(Mielma) // "Registrado y autorizado, ternario"
permiso_ternario(mielma) // "Registrado pero no autorizado, ternario"
permiso_ternario(eli) // "No estas registrado, ternario"
```




<!-- ## <b><font color="#006cb5">Coding Exercise</font></b>
```js
```
Resultado:
```js
``` -->


# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/overview-javascript-ternary-operator)  

<!-- [Código DevCamp]() -->

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/KKLWyLo)