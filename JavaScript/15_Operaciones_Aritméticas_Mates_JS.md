![Logo Mielma](Logo/Logo_Encabezado.png)

# <b><font color="#556CEE">Operadores aritméticos de JavaScript</font></b>

## <b><font color="#006cb5">¿Qué son los operadores aritméticos[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_Operators#operadores_aritm%C3%A9ticos)?</font></b>
Los operadores aritméticos, como su propio nombre indica, permiten realizar operaciones matemáticas aritméticas, es decir, las operaciones básicas: suma, resta, multiplicación y división.

Un operador aritmético toma valores numéricos (ya sean literales o variables) como sus operandos y devuelve un solo valor numérico. Los operadores aritméticos estándar son suma (+), resta (-), multiplicación (*) y división (/). Estos operadores funcionan como lo hacen en la mayoría de los otros lenguajes de programación cuando se usan con números de punto flotante (en particular, ten en cuenta que la división entre cero produce Infinity). 

### <font color="#556CEE">Operadores básicos[🔗](https://developer.mozilla.org/es/docs/Learn/JavaScript/First_steps/Math)</font>
```js
2 + 2; // 4 → Suma
2 - 3; // -1 → Resta
6 / 2; // 3 → División
2 * 5; // 10 → Multiplicación
2 ** 5; // 1024 → Exponencial
7 % 2; // 1 → Resto
6 % 2; // 0 → Entre 2 resto 0 = par
```

### <font color="#556CEE">Increment[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/Increment)</font>
El operador de incremento (++) incrementa (agrega uno a) su operando y retorna el valor antes o después del incremento, dependiendo de dónde está posicionado el operador.

Si se usa <font color="#006cb5">postfijo</font> con el operador después del operando (por ejemplo, x++), el operador de incremento incrementa y devuelve el valor antes de incrementar.  
Advertencia, hay que llamarle con variable, sino error.
```js
var num = 5; // undefined

num++; // 5 → Incrementa, devuelve antes de incrementar

num++; // 6 → Incrementa, devuelve antes de incrementar

num → 7 // Devuelve valor variable
```
Si se usa <font color="#006cb5">prefijo</font> con un operador antes del operando (por ejemplo, ++x), el operador de incremento incrementa y devuelve el valor después del incremento.
```js
var num = 5; // undefined
++num; // 6 → Incrementa, devuelve después de incrementar
++num; // 7 → Incrementa, devuelve después de incrementar
num → 7 // Devuelve valor variable
```

### <font color="#556CEE">Decrement[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/Increment)</font>
El operador de decremento (--) incrementa (resta uno a) su operando y retorna el valor antes o después del decremento, dependiendo de dónde está posicionado el operador.  
Advertencia, hay que llamarle con variable, sino error.


Si se usa <font color="#006cb5">postfijo</font> con el operador después del operando (por ejemplo, x--), el operador de decremento decrementa y devuelve el valor antes de decrementar.
```js
var num = 5; // undefined

num--; // 5 → Decrementa, devuelve antes de decrementar

num--; // 4 → Decrementa, devuelve antes de decrementar

num → 3 // Devuelve valor variable
```
Si se usa <font color="#006cb5">prefijo</font> con un operador antes del operando (por ejemplo, --x), el operador de decremento decrementa y devuelve el valor después del decremento.
```js
var num = 5; // undefined
--num; // 4 → Decrementa, devuelve antes de decrementar
--num; // 3 → Decrementa, devuelve antes de decrementar
num → 3 // Devuelve valor variable
```

### <font color="#556CEE">Invertir valores</font>
Invertir valores para obtener negativo si es positivo y positivo y si es negativo
```js
var pos = 7; // undefined

var pos_neg = -pos; // -7 → Positivo en negativo

var pos_neg_pos = -pos_neg // 7 → Negativo en positivo
```

### <font color="#556CEE">Convertir string en número</font>
Convertir string a número en JavaScript con el operador +

El operador unario u operador + es otro elemento que permite transformar una cadena o string. El + precede al operando y, por consiguiente, se evalúa como su operando, para convertirlo en un número.
```js
var string = '100';

var convertir = +string; // 100 → pasa de string a número

convertir; // 100 

```

## <b><font color="#006cb5">Coding Exercise</font></b>
Add the correct arithmetic operators to make variable equal the number in the comment.
```js
numOne = 5 10 // add the right Arithmetic Operators to have it equal 15

numTwo = 90 3 // add the right Arithmetic Operators to have it equal 30

numThree = 50 25 // add the right Arithmetic Operators to have it equal 25

numFour =  20 5 // add the right Arithmetic Operators to have it equal 100
```
```js
numOne = 5 + 10 // add the right Arithmetic Operators to have it equal 15

numTwo = 90 / 3 // add the right Arithmetic Operators to have it equal 30

numThree = 50 - 25 // add the right Arithmetic Operators to have it equal 25

numFour =  20 * 5 // add the right Arithmetic Operators to have it equal 100
```

# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/javascript-arithmetic-operators)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_b_16_arithmetic_operators.js)

<!-- [Código Mielma]() -->