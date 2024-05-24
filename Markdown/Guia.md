<!-- Colores
<font color="#006cb5">Círculo #006cb5</font>  
<font color="#000000">Ratón #000000</font>  
<font color="#556CEE">Logo #556CEE</font>   -->
<!-- h1, h2, h3, h4
# <b><font color="#556CEE">h1</font></b>
## <b><font color="#006cb5">h2</font></b>
### <font color="#556CEE">h3</font>
#### <font color="#006cb5">h4</font> -->
# Sintaxis Markdown

En el lenguaje Markdown encontrarás tres tipos de elementos básicos que a su vez engloban el resto de la sintaxis.

## Elementos de bloque

### Párrafos `<p>` y saltos de línea `<br>`

Para generar un nuevo párrafo en Markdown simplemente separa el texto mediante una línea en blanco (pulsando dos veces intro)

Al igual que sucede con HTML, Markdown no soporta dobles líneas en blanco, así que si intentas generarlas estas se convertirán en una sola al procesarse.

Para realizar un salto de línea y empezar una frase en una línea siguiente dentro del mismo párrafo, tendrás que pulsar dos veces la barra espaciadora antes de pulsar una vez intro.

### Encabezados`<h1>` `<h2>`

Las # almohadillas son uno de los métodos utilizados en Markdown para crear encabezados.   
Debes usarlos añadiendo uno por cada nivel, tantos niveles como sean necesarios

~~~
# H1 
## H2 
### h3 
#### Tantos # tanto nivel
~~~


#### Encabezados subrayados `<u>`
== Para el nivel 1  
-- Para el nivel 2

### Citas `<q>`
Las citas se generar utilizando el carácter mayor que > al comienzo del bloque de texto.  
Si la cita en cuestión se compone de varios párrafos, deberás añadir el mismo símbolo > al comienzo de cada uno de ellos.  
Incluso puedes concatenar varios >> para crear citas anidadas.  
Recuerda separar los saltos de línea con >, o >> si te encuentras dentro de la cita anidada; para crear párrafos dentro del mismo bloque de cita.

### Listas `<ol>`

#### Listas desordenadas `<ul>` 

Para crear listas desordenadas utiliza * asteriscos, - guiones, o + símbolo de suma.  
Para generar listas anidadas dentro de otras, simplemente tendrás que añadir **cuatro espacios en blanco antes del siguiente *, - o +.

- Elemento de lista 1
  - Elemento de lista 2
* Elemento de lista 3
  * Elemento de lista 4
+ Elemento de lista 5
  + Elemento de lista 6

#### Listas ordenadas `<li>`

Para crear listas ordenadas debes utilizar la sintaxis de tipo: «número.» 1.. Al igual que ocurre con las listas desordenadas, también podrás anidar o combinar.

### Códigos de bloque
Si quieres crear un bloque entero que contenga código. Lo único que tienes que hacer es encerrar dicho párrafo entre dos líneas formadas por tres ~ virgulillas.
~~~
Al empezar ~~~
texto deseado
y lineas necesarias
al terminar ~~~
~~~

### Reglas horizontales
Las reglas horizontales se utilizan para separar secciones de una manera visual. Las estás viendo constantemente en este artículo ya que las estoy utilizando para separar los diferentes elementos de sintaxis de Markdown.

Para crearlas, en una línea en blanco deberás incluir tres de los siguientes elementos: asteriscos, guiones, o guiones bajos.  
~~~
*** o --- o ___
~~~
Obtienes:
***
## Elementos de línea 
Markdown utiliza asteriscos o guiones bajos para enfatizar.

### Énfasis (negritas`<strong>` o `<b>` y cursivas `<i>`)

Markdown utiliza asteriscos o guiones bajos para enfatizar.

Simplemente tendrás que envolver palabras o textos en éstos símbolos para conseguir  
_cursivas_, __negritas__, ___negrita-cursiva___.
~~~
_cursiva_ __negrita__ ___negrita-cursiva___
*cursiva* **negrita** ***negrita-cursiva***
~~~

### Links o enlaces `<a>`

Añadir enlaces a una publicación, más que común, hoy en día es algo casi obligatorio. Con Markdown tendrás varias formas de hacerlo.

#### Links o enlaces en línea
Son los enlaces de toda la vida. Como su nombre indica, se encuentran en línea con el texto.

Se crean escribiendo la palabra o texto enlazada entre [ ] corchetes, y el link en cuestión entre ( ) paréntesis.
~~~
[enlace en línea](http://www.limni.net)
~~~
[enlace en línea](http://www.limni.net)

#### Links y enlaces como referencia
La desventaja del método anterior, es que si utilizas links demasiado complejos o largos pueden dificultarte la lectura de tu texto.

Para solucionarlo y crear tu contenido de una manera más ordenada puedes generar enlaces de referencia.

Esto quiere decir que en tu texto enlazarás palabras o códigos concretos (formados por letras y/o números), que en otro lugar más apartado de tu documento tendrás definidos como determinadas URL.
~~~
[nombre para mostrar][nombre referencia]
~~~
[nombre para mostrar][nombre referencia]
~~~
El nombre de referencia y el link puedes añadirlos en cualquier lugar. En los links, por ejemplo, esos no se visualizan
[nombre referencia]: https://github.com/ElizabethMaranon
~~~
[nombre referencia]: https://github.com/ElizabethMaranon

#### Links Automáticos

Estos son necesarios cuando lo que quieres es mostrar una URL completa, y no un enlace enmascarado bajo una palabra o frase como ocurre con los links en línea.

Para generar links automáticos tan solo hay que envolverlos con los símbolos < >
~~~
<https://github.com/ElizabethMaranon>
~~~
devuelve
~~~
https://github.com/ElizabethMaranon
~~~

### Código `code` y `pre`

En según que tipo de publicaciones (sobre todo las de carácter técnico), necesitarás añadir pequeñas secciones donde mostrar código de otro lenguaje, atajos de teclado, o demás contenido que no debería ser tratado como tal.
Para ello tienes disponible dos alternativas.

#### Código puro - Codigo HTML: `code`

La forma más sencilla de escribir código en Markdown es envolver el texto entre dos comillas sencillas. 
~~~
`Code: línea código entre comillas simples`
~~~
Se visualiza:  
~~~
Code: línea código entre comillas simples
~~~
#### Texto pre-formateado - Código HTML: `pre`
La otra manera de añadir código en Markdown es comenzar el párrafo con cuatro espacios en blanco.
~~~
    Pre: línea código entre comillas simples
~~~
Se visualiza:  
~~~
Pre: línea código entre comillas simples
~~~
Ojo, ¡estos espacios deberás incluirlos en cada línea que escribas! Para añadir código en bloque es mejor utilizar la sintaxis que viste anteriormente: códigos de bloque.

### Imágenes `<img>`
Insertar una imagen con Markdown se realiza de una manera prácticamente idéntica a insertar links.  

Solo que en este caso, deberás añadir un símbolo de ! exclamación al principio y el enlace no será otro que la ubicación de la imagen.
El texto alternativo es lo que se mostraría si la carga de la imagen fallase.
También podrás añadir un título alternativo entre comillas al final de la ruta. Esto sería el título mostrado al dejar el cursor del ratón sobre la imagen.
~~~
![Texto si falla imagen](/ruta/a/imagen.*) "Texto si pasas el ratón"
~~~
Ya que al añadir imágenes también estás tratando con URLs, puedes utilizar el método que viste anteriormente para incluir links mediante referencias, solo que en este caso los enlaces de referencia serán aquellos donde se encuentre tu imagen.
~~~
De esta forma podrías insertar una imagen
![nombre de la imagen][img1]
O dos, sin ensuciar tu espacio de escritura.
![nombre de la imagen2][img2] 
[img1]: /ruta/a/la/imagen.jpg "Título alternativo"
[img2]: /ruta/a/la/imagen2.jpg "Título alternativo"
~~~

## Omitir Markdown
Esto es muy sencillo, ya que en este lenguaje existe un elemento estrella para especificar que todo lo que escribas a continuación, no se interprete como Markdown.

Se trata de la barra invertida \ \.

Escribiéndola justo delante de cualquiera de los elementos que verás a continuación, los mismos no tendrán efecto a la hora de convertirse en negritas, cursivas, links…
~~~
\  barra invertida
`  acento invertido
*  asterisco
_  guión bajo
{} llaves
[] corchetes
() paréntesis
#  almohadilla
+  símbolo de suma
-  guión
.  punto
!  exclamación
~~~

## Texto en color
Se puede controlar el color del texto utilizando el elemento `<FONT COLOR="color"` 
~~~
<FONT COLOR="red">ROJO </FONT>
<FONT COLOR="blue">AZUL </FONT>
<FONT COLOR="navy">AZUL MARINO </FONT>
<FONT COLOR="green">VERDE </FONT>
<FONT COLOR="olive">OLIVA </FONT>
<FONT COLOR="yellow">AMARILLO </FONT>
<FONT COLOR="lime">LIMA </FONT>
<FONT COLOR="magenta">MAGENTA </FONT>
<FONT COLOR="purple">PURPURA </FONT>
<FONT COLOR="cyan">CYAN </FONT>
<FONT COLOR="brown">MARRON </FONT>
<FONT COLOR="black">NEGRO </FONT>
<FONT COLOR="gray">GRIS </FONT>
<FONT COLOR="teal">TEAL </FONT>
<FONT COLOR="white">BLANCO </FONT>
~~~
<FONT COLOR="red">ROJO </FONT>
<FONT COLOR="blue">AZUL </FONT>
<FONT COLOR="navy">AZUL MARINO </FONT>
<FONT COLOR="green">VERDE </FONT>
<FONT COLOR="olive">OLIVA </FONT>
<FONT COLOR="yellow">AMARILLO </FONT>
<FONT COLOR="lime">LIMA </FONT>
<FONT COLOR="magenta">MAGENTA </FONT>
<FONT COLOR="purple">PURPURA </FONT>
<FONT COLOR="cyan">CYAN </FONT>
<FONT COLOR="brown">MARRON </FONT>
<FONT COLOR="black">NEGRO </FONT>
<FONT COLOR="gray">GRIS </FONT>
<FONT COLOR="teal">TEAL </FONT>
<FONT COLOR="white">BLANCO </FONT>

### Colores Logotipo
<FONT COLOR="#006cb5">Círculo #006cb5</FONT>  
<font color="#000000">Ratón #000000</FONT>  
<font color="#556CEE">Logo #556CEE</FONT> 

## Comentarios
~~~
<!-- Comentarios que no se visualizan, se ven de otro color en el editor -->
~~~
<!-- Comentarios que no se visualizan -->
# Links Información Añadida

[Github Mielma]

[Markdown.es](https://markdown.es/)


[Github Mielma]: https://github.com/ElizabethMaranon

# Links información por añadir
https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax


