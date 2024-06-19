![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Guía para la interpolación de cadenas Backtick (Backtick string interpolation) en Javascript</font></b>
<!-- ## <b><font color="#006cb5"></font></b>
### <font color="#556CEE"></font>
#### <font color="#006cb5"></font> -->
## <b><font color="#006cb5">Guía DevCamp → Backtick string interpolation</font></b>
Esta lección tratará sobre enfoques modernos para usar la interpolación de cadenas.
Ahora, una revisión rápida de la antigua forma de usar la interpolación de cadenas fue algo como esto. Tenemos nuestra constante de letras como variable aquí., `const lyrics = 'Never gonna give you up'`; Y si quiero agregarle algo, entonces si quiero un registro de la consola, diga: "Y luego tendré que agregar un espacio aquí en lugar de un plus"..
`console.log("I'm " + lyrics)`;
Y luego puedo llamar letras. Ahora, si guardo y luego ejecuto esto, todo funcionará.
```js
const backtick = 'String interpolation'
console.log("Mielma " + backtick); //"Mielma String interpolation"
```
![Backtick String Interpolation][Backtick String Interpolation]

Esto está bien, pero las versiones más modernas de JavaScript nos brindan una manera mucho mejor de hacerlo y utilizan comillas invertidas. Ahora, si nunca has usado la parte posterior antes, hay un pequeño botón justo encima del botón de pestaña en tu teclado..
Entonces, en lugar de estas comillas dobles, usaré esta comilla invertida. Ahora, cuando miras la documentación, puedes confundirte y pensar que esto es solo un apóstrofo normal.

No lo es. Es una comilla invertida. Así que voy a hacer una comilla invertida aquí mismo. Ahora esto se considera una cadena normal y voy a aclararlo. Y sólo para demostrártelo voy a ejecutarlo de nuevo. Y si lo ejecuta, podrá ver que lo ha convertido en una cadena normal.
```js
const backtick = 'String interpolation'
console.log(`Mielma  ${backtick}`); //"Mielma String interpolation"
```
![Backtick String Interpolation Moderno][Backtick String Interpolation Moderno]

Muchas veces veo estudiantes que ven esta sintaxis y solo ven un ejemplo como este, y piensan que solo puedes colocar una única variable dentro de allí. Pero en realidad puede ser cualquier cosa que desees dentro de ese lugar y lo ejecutará como Javascript puro..
Esa es la forma moderna de usar la interpolación de cadenas en javascript.
```js
const backtick = 'String interpolation'
console.log(`Mielma  ${backtick}`); // "Mielma String interpolation"
console.log(`Mielma ${2 + 2}`); // "Mielma 4"
console.log(`Mielma ${backtick + " escribe lo que quieras " + backtick}`); // "Mielma String interpolation escribe lo que quieras String interpolation"
```
![Backtick String Interpolation Moderno Varias][Backtick String Interpolation Moderno Varias]




## <center><b><font color="#006cb5">Coding Exercise</font></b>
Inside the below function, write a variable and give it a string that says "It's a trap!" Then on the `return` use string interpolation to finish the movie line
```js
function movieLine() {
    // Set your variable here
    
    return (`replace-this-with-something-clever ${}`)
}
```
Resultado:
```js
function movieLine() {
    const trap = "It's a trap!"
    
    return (`Es una trampa! ${trap}`)
}
console.log(movieLine())
```
![Backtick String Interpolation Moderno Coding Exercise][Backtick String Interpolation Moderno Coding Exercise]

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-backtick-string-interpolation-javascript)  



[Código Mielma Backtick](https://codepen.io/ElizabethMaranon/pen/wvbyRGE)

[Código Mielma Backtick Moderno](https://codepen.io/ElizabethMaranon/pen/vYwdvgW)

[Código Mielma Backtick Moderno Coding Exercise](https://codepen.io/ElizabethMaranon/pen/NWVyeym)



<!-- Ordenar enlaces -->

[Backtick String Interpolation]: image/Backtick_string_interpolation.png
[Backtick String Interpolation Moderno]: image/Backtick_string_interpolation_moderno.png
[Backtick String Interpolation Moderno Varias]: image/Backtick_string_interpolation_moderno_varias.png
[Backtick String Interpolation Moderno Coding Exercise]: image/Backtick_String_Interpolation_Moderno_Coding_Exercise.png