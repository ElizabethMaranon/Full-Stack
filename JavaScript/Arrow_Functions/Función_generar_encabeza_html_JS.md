![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Cree una función de generación de encabezados HTML en JavaScript</font></b>
<!-- ## <b><font color="#006cb5"></font></b>
### <font color="#556CEE"></font>
#### <font color="#006cb5"></font> -->
## <b><font color="#006cb5">Guía DevCamp → Generar encabezado HTML en JS</font></b>
En este ejercicio de codificación de JavaScript, desarrollaremos una función de generación de encabezados HTML. Este será un tipo de ejercicio bastante básico, pero es una buena práctica poder trabajar con interpolación de cadenas.

Lo que quiero que hagas es que puedas construir una función donde puedas pasar dos argumentos. Entonces quiero que puedas construir una función que pase algún tipo de título para el encabezado y luego también quiero que tengas un argumento para el tipo de encabezado. Lo que esto significará es que puedes crear algún tipo de función y podemos decir generador de encabezados y luego pasar algún título como Hola y luego podemos pasar un número, así que quiero que diga 1 y lo que debería generar. Lo que esto debería generar es algo como esto, esto debería darnos HTML de una etiqueta H1 que diga Hola y luego cierre esa etiqueta

Ahora, esto es algo que puede ser un poco básico si tienes mucha experiencia en desarrollo de JavaScript, pero si eres nuevo en programación o en JavaScript, entonces este es definitivamente un buen ejercicio. Así que te recomiendo que ahora mismo pongas en pausa el vídeo y luego vayas y desarrolles esta función

Ahora, la solución que usaría es comenzar creando una función, por lo que diré generador de encabezado constante y haré de esto una función de flecha. Como mencioné, quiero tener un argumento de título y luego un tipo de argumento de encabezado, luego pasaremos nuestra función de flecha y dentro simplemente querré devolver una cadena y usaré la sintaxis de ES6. Voy a tener tics atrás aquí y por eso quiero devolver una cadena y voy a comenzar con un símbolo mayor que porque recuerda cuál es nuestro objetivo y esto puede ayudar a tener un comentario aquí sobre cuál es nuestro objetivo

Quiero poder tener algo como esto donde digas h1 y luego mi título y luego H1 aquí.
```js
// <h1>Title</h1>
```
Ahora, esta parte H1 tiene que ser dinámica, así que no puedo simplemente venir aquí y codificar H1 porque recuerden que necesitamos poder crear una etiqueta h1 y H2, 3, 4 o 5, lo que sea que deseemos. Necesito poder pasar eso. Así que voy a decir solo H y luego, usando los literales de cadena, usaré una llave de signo de dólar y luego adentro, si aquí solo voy a pasar el tipo de rumbo y luego ciérrelo. Luego, dentro de nuestra etiqueta, diré título y luego lo cerraremos, así que diré H y luego el dólar con la llave y luego el tipo de encabezado, finalice y luego queremos cerrar esa etiqueta. y entonces eso es todo lo que tenemos que hacer.
```js
<h${typeOfHeading}>${title}</h${typeOfHeading}>
```
Así que guardaré esto y una vez más lo haré en casi todos los videos que son mi flujo de trabajo normal, pero realmente quiero mostrárselos con Quokka, así que lo renderizaré todo en tiempo real. Voy a decir generador de rumbo. Ahora vamos a pasar nuestro título, así que aquí hagamos del título una cadena y solo digamos saludos y luego el segundo argumento lo convertiremos en una etiqueta h2, así que pasaré h2 y ahora, si llamo a esto, puedes mira que me salen saludos dentro de una etiqueta h2.
Ejemplo
```js
const GeneradorEncabezado = (título, tipoEncabezado) => {
  return `
  <h${tipoEncabezado}>${título}</h${tipoEncabezado}>
  `
}

console.log(GeneradorEncabezado('título', 1));
console.log(GeneradorEncabezado('subtítulo', 2))
```
console:
```js
"
  <h1>título</h1>
  "
"
  <h2>subtítulo</h2>
  "
```
![Generar encabezado HTML](https://github.com/ElizabethMaranon/Full-Stack/blob/main/JavaScript/Arrow_Functions/Funci%C3%B3n_generar_encabeza_html_JS.md)


# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/build-html-heading-generator-function-javascript)  

[Código DevCamp](https://gist.github.com/jordanhudgens/f3c70c323c5ec86b814ee5d04a953be7)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/gOJeaVG)

<!-- Ordenar enlaces -->