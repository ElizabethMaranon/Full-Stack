![Logo Mielma](logo/Logo%20Encabezado.png)

# <b><font color="#556CEE">Trabajar con funciones de cadena - Parte 2</font></b>

## <b><font color="#006cb5">¿Qué son expresiones regulares[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_expressions)?</font></b>

Las expresiones regulares son patrones que se utilizan para hacer coincidir combinaciones de caracteres en cadenas. En JavaScript, las expresiones regulares también son objetos.

## <b><font color="#006cb5">Funciones de datos</font></b>

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
¡[Funciones String .indexOf()](image/Funciones_String_.indexOf().png)

### <font color="#556CEE">Función lastIndexOf()[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/lastIndexOf)</font>
El método lastIndexOf() devuelve la posición (indice) en la que se encuentra el valor, dentro del objeto String que realiza la llamada, de la última ocurrencia del valor especificado; o -1 si no se halla.
![Funciones String lastIndexOf()](image/Funciones_String_.lastIndexOf().png)

## <b><font color="#006cb5">Coding Exercise</font></b>
For this submission, replace dog with cat, find the index of over, and find the last index of never.
~~~
stringOne = "The dog meows"  

replacedString =  // replace the word dog with cat

stringTwo = "The cow jumped over the moon"

indexOfOver =  // get the index of over

stringThree = "Never gonna give you up never gonna let you down"

lastIndex = // get the last index of never 
~~~
~~~
stringOne = "The dog meows"

replacedString = stringOne.replace("dog", "cat") // replace the word dog with cat

stringTwo = "The cow jumped over the moon"

indexOfOver =  stringTwo.indexOf("over")// get the index of over

stringThree = "Never gonna give you up never gonna let you down"

lastIndex = stringThree.lastIndexOf("never") // get the last index of never 
~~~


# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/working-with-string-functions-part-2)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_b_13_string_functions.js)

[Lista completa de funciones de cadena](https://www.w3schools.com/jsref/jsref_obj_string.asp)