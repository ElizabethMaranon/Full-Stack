![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">CheckPoint 7 - ¿Cuál es la diferencia entre una declaración de función y una expresión de función? </font></b>

Las funciones son uno de los bloques de construcción fundamentales en JavaScript. Una función en JavaScript es similar a un procedimiento — un conjunto de instrucciones que realiza una tarea o calcula un valor, pero para que un procedimiento califique como función, debe tomar alguna entrada y devolver una salida donde hay alguna relación obvia entre la entrada y la salida. Para usar una función, debes definirla en algún lugar del ámbito desde el que deseas llamarla.

Una definición de función (también denominada declaración de función o expresión de función) consta de la palabra clave function, seguida de:  

+ El nombre de la función.
+ Una lista de parámetros de la función, entre paréntesis y separados por `;` .
+ Las declaraciones de JavaScript que definen la función, encerradas entre llaves, { ... }.

Las funciones se pueden definir de dos maneras

+ Declaración de función
+ Expresiones function



## <b><font color="#006cb5">Declaraciones[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions#declaraci%C3%B3n_de_funci%C3%B3n) de funciones</font></b>
+ function
+ Nombre
+ Parámetros, (separados por comas)
+ {Declaraciones};
```js
function declaración(){
return "declaración → function nombre(parámetros) {dec1; dec2; dec3;}";
}
console.log(declaración());
```

## <b><font color="#006cb5">Expresiones[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions#expresiones_function) de funciones</font></b>

Una función que se almacena dentro de una variable.

No olvidar `;`

+ var nombre `=` 
+ function
+ (Parámetros, separados por `,`)
+ {Declaraciones separadas por `;` }`;`
  
```js
var expresión = function () {
return 'expresión → expresión = function (parámetros) {dec1; dec2; dec3;}"';
};

console.log(expresión())
```

### <font color="#556CEE">Ejercicio</font>
```js
var edad = 3; // Menú Infantil

if (edad <= 10) {
  var menu = function () {
    return "Menú Infantil";
  };
  function menu2 () {
    return "Otro menú infantil";
  }
}

console.log(menu()); // Menú infantil
console.log(menu2()); // Otro menú infantil
```

Ahora tenemos un error que dice que las declaraciones de funciones no deben colocarse en bloques. Y cuando se refieren a bloques, se refieren a dentro de llaves en cosas como un bloque condicional o try-catch o algo así. Y eso es exactamente lo que estamos tratando de hacer: estamos tratando de generar una función sobre la marcha y eso no es lo que pretendían hacer las declaraciones de función, para eso estaba destinada una expresión de función..

Entonces dice que no se debe colocar en bloques, usarlo e incluso nos dice aquí lo cual es bueno. Utilice una expresión de función o mueva la declaración a la parte superior de la función externa. Entonces esto es algo muy importante y esto va a comenzar a cerrarse. Esto está empezando a acercarnos a la creación de aplicaciones de tipo dinámico porque en muchas ocasiones será necesario crear funciones sobre la marcha. Es posible que desee almacenar una función dentro de un objeto y todas esas cosas no son lo que haría con un tipo estándar de declaración de función. Esto es lo que usaría para funciones listas para usar, mientras que las expresiones de funciones son más modulares.

Esa es la forma más fácil de intentar recordar esto si tienes algo que necesitas poder mover o una función que necesitas poder crear en cualquier momento dado. Para eso están las expresiones de función, mientras que una declaración como esta es solo cuando la tienes fuera de ese bloque. Entonces tendrías algo como esto y luego funcionaría exactamente de la manera para la que fue diseñado, pero no en la forma en que intentamos hacerlo aquí. Así es como puedes trabajar con expresiones de función o funciones anónimas en javascript tal como lo tenemos aquí y también un tutorial sobre la diferencia entre expresiones de función y declaraciones de función.



# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/differences-between-function-expressions-function-declarations)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_03_function_expression.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/GRamjQm)

