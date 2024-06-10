![Logo Mielma](Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">CheckPoint 7 - ¿Cuáles son las tres funciones de String en JS?</font></b>

## <b><font color="#006cb5">¿Qué es una función[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions) en JavaScript?</font></b>

Una función en JavaScript es similar a un procedimiento — un conjunto de instrucciones que realiza una tarea o calcula un valor, pero para que un procedimiento califique como función, debe tomar alguna entrada y devolver una salida donde hay alguna relación obvia entre la entrada y la salida.

Básicamente, una función le permite encapsular el comportamiento. En este caso, no somos nosotros quienes realmente creamos las funciones, éstas se proporcionan en la biblioteca principal de JavaScript, por lo que simplemente podemos llamarlas. Más adelante veremos cómo podemos crear nuestras propias funciones. Pero esto debería darles una pequeña introducción porque, esencialmente, lo que vamos a poder hacer es tener un objeto y luego cambiarlo o realizar ciertos tipos de consultas de valor sobre él, todo tipo de cosas.

Se necesitaría mucho código si tuviéramos que escribirlo todo a mano. Y la otra cosa buena que nos permiten hacer las funciones es realizar una tarea una y otra vez sin tener que repetir ningún código. Esa es una visión de alto nivel de lo que son las funciones.

## <b><font color="#006cb5">¿Qué es index[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf#descripci%C3%B3n) o índice en JS?</font></b>

Los caracteres de una cadena se indexan de izquierda a derecha. El índice del primer carácter es 0, y el índice del último carácter es - 1.

## <b><font color="#006cb5">¿Qué son expresiones regulares[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_expressions)?</font></b>

Las expresiones regulares son patrones que se utilizan para hacer coincidir combinaciones de caracteres en cadenas. En JavaScript, las expresiones regulares también son objetos.

## <b><font color="#006cb5">¿Qué es un array[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array) en JS?</font></b>
 Los arrays son objetos similares a una lista cuyo prototipo proporciona métodos para efectuar operaciones de recorrido y de mutación. Tanto la longitud como el tipo de los elementos de un array son variables.

## <b><font color="#006cb5">Funciones de datos</font></b>

### <font color="#556CEE">Atributo lenght[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/length)</font>

La propiedad length de un objeto String representa la longitud de una cadena, en unidades de código UTF-16.
![Funciones String .lenght](image/Funciones_String_.length.png)

Ahora, la razón por la que sé que esto es un atributo y no una función es porque si intentara poner paréntesis al final, que es lo que haría si fuera una función, llame y presione regresar, obtendrá un error. Incluso te dice que .length no es una función.

### <font color="#556CEE">Función .charAt()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)</font>

El método charAt(`index`) de String devuelve en un nuevo String el carácter UTF-16 de una cadena.  
El valor del índice de cadena comienza desde 0 y sube hasta la longitud de la cadena menos 1 (n-1).
![Funciones String .charAt()](image/Funciones_String_.charAt().png)

### <font color="#556CEE">Función .concat()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/concat)</font>

La función concat() concatena los argumentos de tipo texto con la cadena de sobre la que se llama a la función y devuelve una nueva cadena de texto. Los cambios en la cadena original o la cadena devuelta no afectan al otro.  

<font color="#006cb5">¿Qué significa concatenar?</font>

Unir o enlazar dos o más cosas. Usado también como pronominal.  
Añade string nuevo al final del  var string, pero no lo modifica  
Crear una nueva variable con concat si quieres guardar los cambios
![Funciones String Concat()](image/Funciones_String_.concat().png)

### <font color="#556CEE">Función .includes()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)</font>

El método includes() determina si una matriz incluye un determinado elemento, devuelve true o false según corresponda.

Determina si una cadena de texto puede ser encontrada dentro de otra cadena de texto, devolviendo true o false según corresponda.

<b>Diferencia mayúsculas y minúsculas</b>
![ Funciones String .includes()](image/Funciones_String_.includes().png)

### <font color="#556CEE">Función .startsWith()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith)</font>

El método startsWith() indica si una cadena de texto comienza con los caracteres de una cadena de texto concreta, devolviendo true o false según corresponda.

<b>Diferencia mayúsculas y minúsculas</b>
![Funciones String .startsWith()](image/Funciones_String_.startsWith().png)


### <font color="#556CEE">Función .endsWith()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)</font>

El método endsWith() determina si una cadena de texto termina con los caracteres de una cadena indicada, devolviendo true o false según corresponda. (caracteres, no palabra)  
<b>Diferencia mayúsculas y minúsculas</b>
![Funciones String .endsWith()](image/Funciones_String_.endsWith().png)

### <font color="#556CEE">Función repeat()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)</font>

El método repeat() construye y devuelve una nueva cadena que contiene el número especificado de copias de la cadena en la cual fue llamada, concatenados.  
![Funciones String Repeat()](image/Funciones_String_.repeat().png)

### <font color="#556CEE">Función match()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/match)</font>

El método match() devuelve todas las ocurrencias de una expresión regular dentro de una cadena.
![Funciones String Match()Tel](image/Funciones_String_.match()tel.png)

### <font color="#556CEE">Función Replace()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/replace)</font>
El método replace() devuelve una nueva cadena con una, algunas, o todas las coincidencias de un patrón , siendo cada una de estas coincidencias reemplazadas por un reemplazo . El patrón puede ser una cadena o un objeto RegExp , y el reemplazo puede ser una cadena o una función que será llamada para cada coincidencia.
El primer argumento es lo que estás buscando y el segundo argumento separado por una coma es con lo que quieres reemplazarlo.
No cambia la variable
![Funciones String .replace()](image/Funciones_String_.replace().png)

### <font color="#556CEE">Función Search()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/search)</font>
El método search() ejecuta una búsqueda que encaje entre una expresión regular y el objeto String desde el que se llama.
![Funciones String .search()](image/Funciones_String_.search()tel.png)

### <font color="#556CEE">Función indexOf()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)</font>
El método indexOf() devuelve el índice, dentro del objeto String que realiza la llamada, de la primera ocurrencia del valor especificado, comenzando la búsqueda desde indiceDesde ; o -1 si no se encuentra dicho valor.
![Funciones String .indexOf()](image/Funciones_String_.indexOf().png)

### <font color="#556CEE">Función lastIndexOf()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/lastIndexOf)</font>

El método lastIndexOf() devuelve la posición (indice) en la que se encuentra el valor, dentro del objeto String que realiza la llamada, de la última ocurrencia del valor especificado; o -1 si no se halla.
![Funciones String lastIndexOf()](image/Funciones_String_.lastIndexOf().png)

### <font color="#556CEE">Función slice()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)</font>
El método slice() devuelve una copia de una parte del array dentro de un nuevo array empezando por inicio hasta fin (fin no incluido). El array original no se modificará.
Corta desde index hasta index. Si sólo se especifica un index, corta desde index hasta final.
![Funciones String .slice()](image/Funciones_String_.slice().png) 

### <font color="#556CEE">Función trim()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/trim)</font>

El método trim( ) elimina los espacios en blanco en ambos extremos del string. Los espacios en blanco en este contexto, son todos los caracteres sin contenido (espacio, tabulation, etc.) y todos los caracteres de nuevas lineas (LF,CR,etc.).
![Funciones String .trim()](image/Funciones_String_.trim().png)

### <font color="#556CEE">Función toUpperCase()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)</font>
El toUpperCase() método devuelve el valor convertido en mayúsculas de la cadena que realiza la llamada.
![Funciones String .toUpperCase](image/Funciones_String_.toUpperCase().png)

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios Parte 1](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/working-string-functions-part-1)

[DevCamp Exclusivo Usuarios Parte 2](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/working-with-string-functions-part-2) 

[DevCamp Exclusivo Usuarios Parte 3](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/working-with-string-functions-part-3)

[Código DevCamp Parte 1](https://github.com/rails-camp/javascript-programming/blob/master/section_b_13_string_functions.js)

[Código DevCamp Parte 2](https://github.com/rails-camp/javascript-programming/blob/master/section_b_13_string_functions.js)

[Código DevCamp Parte 3](https://github.com/rails-camp/javascript-programming/blob/master/section_b_13_string_functions.js)
 

[Lista completa de funciones de cadena](https://www.w3schools.com/jsref/jsref_obj_string.asp)

[The quick brown fox jumps over the lazy dog](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog)