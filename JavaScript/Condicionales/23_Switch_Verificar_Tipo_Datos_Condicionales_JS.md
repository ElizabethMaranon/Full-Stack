![Logo Mielma](image/Logo_Encabezado.png)

# <b><font color="#556CEE">Cómo crear una declaración de cambio en JavaScript para verificar tipos de datos (switch)</font></b>

## <b><font color="#006cb5">¿Qué es switch[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/switch)?</font></b>
La declaración `switch` evalúa una expresión, comparando el valor de esa expresión con una instancia `case`  , y ejecuta declaraciones asociadas a ese `case`  , así como las declaraciones en los `case`  que siguen.

## <b><font color="#006cb5">¿Qué es expresión[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/switch#expresi%C3%B3n)?</font></b>
Es una expresión que es comparada con el valor de cada instancia `case` .

## <b><font color="#006cb5">¿Qué es case valorN[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/switch#case_valorn)?</font></b>
Una instancia `case`  valorN es usada para ser comparada con la expresión. Si la expresión coincide con el valorN, las declaraciones dentro de la instancia `case`  se ejecutan hasta que se encuentre el final de la declaración `switch` o hasta encontrar una interrupción `break`.

## <b><font color="#006cb5">¿Qué es default[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/switch#default)?</font></b>
Una instancia `default`, cuando es declarada, es ejecutada si el valor de la expresión no coincide con cualquiera de las otras instancias `case` valorN.

## <b><font color="#006cb5">Descripción</font></b>


Si ocurre una coincidencia, el programa ejecuta las declaraciones asociadas correspondientes. Si la expresión coincide con múltiples entradas, la primera será la seleccionada, incluso si las mayúsculas son tenidas en cuenta.

El programa primero busca la primer instancia `case`  cuya expresión se evalúa con el mismo valor de la expresión de entrada (usando comparación estricta, ===[🔗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)) y luego transfiere el control a esa cláusula, ejecutando las declaraciones asociadas. Si no se encuentra una cláusula de `case`  coincidente, el programa busca la cláusula `default` opcional, y si se encuentra, transfiere el control a esa instancia, ejecutando las declaraciones asociadas. Si no se encuentra una instancia `default` el programa continúa la ejecución en la instrucción siguiente al final del `switch`. Por convención, la instancia `default` es la última cláusula, pero no tiene que ser así.

La declaración `break` es opcional y está asociada con cada etiqueta de `case` y asegura que el programa salga del `switch` una vez que se ejecute la instrucción coincidente y continúe la ejecución en la instrucción siguiente. Si se omite el `break` el programa continúa la ejecución en la siguiente instrucción en la declaración de `switch`.

## <b><font color="#006cb5">Ejercicio</font></b>

```js
// var Datos = 5; // Number
// var Datos = "String"; // String
// var Datos = true; // Boolean
var Datos = {}; // No Matches

switch (typeof Datos) { // Tipo de datos
  case "string": // En caso de ser
    console.log("Es una string"); // Return
    break; // Si no lo es, siguiente case
  case "number": // En caso de ser
    console.log("Es un número"); // Return
    break; // Si no lo es, siguiente case
  case "boolean": // En caso de ser
    console.log("Es un boolean"); // Return
    break; // Si no lo es, siguiente case
  default: // En caso de ser
    console.log('No matches'); // Return
}
```


## <b><font color="#006cb5">Coding Exercise</font></b>
Write a switch statement that always returns: "number"
```js
function switchStatement() {
    
    //Write your switch statement within this function
    
}

switchStatement();
```
Resultado:
```js
function switchStatement() {
    
    return 'number'//Write your switch statement within this function
    
}

switchStatement();
```


# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-build-switch-statement-javascript-check-data-types)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_c_04_case_statement.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/eYavemG)