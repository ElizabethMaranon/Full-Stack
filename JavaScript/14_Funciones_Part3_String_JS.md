![Logo Mielma](Logo/Logo_Encabezado.png)

# <b><font color="#556CEE">Trabajar con funciones de cadena - Parte 3</font></b>

## <b><font color="#006cb5">¿Qué es un array[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array) en JS?</font></b>
 Los arrays son objetos similares a una lista cuyo prototipo proporciona métodos para efectuar operaciones de recorrido y de mutación. Tanto la longitud como el tipo de los elementos de un array son variables.

## <b><font color="#006cb5">Funciones de datos</font></b>

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

## <b><font color="#006cb5">Coding Exercise</font></b>
Fill in the return below with some of the string function syntax you just learned!
```js
//We have given you the sentences already, please fill in the returns to make the test pass
// EXAMPLE "return (str.toUpperCase());"

function strings() {
    
    // Use slice to return from the "w" to the end of the sentence
    var str = "The five boxing wizards jump quickly";
    return (  <--Delete-this-and-write-your-string-function-->  );
    
}

strings();
```
```js
//We have given you the sentences already, please fill in the returns to make the test pass
// EXAMPLE "return (str.toUpperCase());"

function strings() {
    
    // Use slice to return from the "w" to the end of the sentence
    var str = "The five boxing wizards jump quickly";
    return (  str.slice(16) );
    
}

strings();
```

# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/working-with-string-functions-part-3)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_b_13_string_functions.js)

[Lista completa de funciones de cadena](https://www.w3schools.com/jsref/jsref_obj_string.asp)