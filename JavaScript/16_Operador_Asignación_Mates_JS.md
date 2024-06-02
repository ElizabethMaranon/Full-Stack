![Logo Mielma](logo/Logo%20Encabezado.png)

# <b><font color="#556CEE">Guía de operadores de asignación compuestos en JavaScript</font></b>

## <b><font color="#006cb5">¿Qué es un [operador de asignación🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_Operators#asignacion)?</font></b>
Un operador de asignación asigna un valor a su operando izquierdo basándose en el valor de su operando derecho. El operador de asignación simple es igual ( = ), que asigna el valor de su operando derecho a su operando izquierdo. Es decir, x = y asigna el valor de y a x.

## <b><font color="#006cb5">¿Qué son los operadores de asignación compuestos[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_Operators#asignacion)?</font></b>
 Los operadores de asignación compuestos en JavaScript son un tipo de operador que, como su nombre indica, une el operador de asignación con otro operador. Es decir, son una forma de abreviar dos operaciones.

## <b><font color="#006cb5">¿Qué son los operadores bitwise[🔗](https://es.wikipedia.org/wiki/Operador_a_nivel_de_bits#:~:text=Una%20operaci%C3%B3n%20bit%20a%20bit,soportada%20directamente%20por%20los%20procesadores.)?</font></b>
Una operación bit a bit o bitwise opera sobre números binarios a nivel de sus bits individuales. Es una acción primitiva rápida, soportada directamente por los procesadores.
 

 ### <font color="#556CEE">Operador asignación compuesto +=</font>
Sumar elementos que están asignados, cambia el valor de la variable, con el resultado de la suma.

Si tuviéramos 100 números, simplemente podríamos agregarlos así.

Básicamente, esto equivale a una abreviatura de decir algo como <font color="#006cb5">suma = suma + lo que sea que diga el siguiente</font>, que tuviéramos un grado tres, sería lo mismo que hacer eso. Entonces está realizando una tarea, pero también está realizando una operación. Esa es la razón por la que se llama operador de asignación compuesta..
![Operadores Asignación Compuesta +=](image/
Operadores_Asignación_Compuesta_+=.png)
Ahora, además de tener la posibilidad de resumir elementos, también puedes hacer lo mismo con los demás operadores. De hecho, literalmente, cada uno de los operadores que acabamos de ver puede usarlos para realizar esta tarea compuesta. 
```js
suma *= ochenta; // 14400
```



## <b><font color="#006cb5">Coding Exercise</font></b>
You need 250 lemons and 36 limes for your lemonade. Whats your total number of fruit?
```js
//Use Compound Assignment Operators to solve the above problem

function mathTest() {
    //please do not delete this
    var sum = 0;
    
    //Delete this and assign your variables, then do some math
    
    //please do not delete this
    return sum;
}

mathTest();
```

```js
//Use Compound Assignment Operators to solve the above problem

function mathTest() {
    //please do not delete this
    var sum = 0;
    var lemons = 250;
    var limes = 36;
    sum +=lemons;
    sum +=limes;
    
    //please do not delete this
    return sum;
}

mathTest();
```

# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-compound-assignment-operators-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_b_17_compound_assignment_operators.js)

[Documentación para operadores de asignación compuesta](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)