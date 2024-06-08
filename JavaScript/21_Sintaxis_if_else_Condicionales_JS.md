![Logo Mielma](logo/Logo_Encabezado.png)

# <b><font color="#556CEE">Guía de condicionales If/Else en JavaScript</font></b>

## <b><font color="#006cb5">If/Else[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/if...else)</font></b>

Ejecuta una sentencia si una condición específica es evaluada como verdadera. Si la condición es evaluada como falsa, otra sentencia puede ser ejecutada.
```js
if (condición) sentencia1 [else sentencia2]
```
`Condición`
Una expresión que puede ser evaluada como verdadera o falsa.

`sentencia1`
Sentencia que se ejecutará si condición es evaluada como verdadera. Puede ser cualquier sentencia, incluyendo otras sentencias if anidadas. Para ejecutar múltiples sentencias, use una sentencia block ({ ... }) para agruparlas.

`sentencia2`
Sentencia que se ejecutará si condición se evalúa como falsa, y exista una cláusula else. Puede ser cualquier sentencia, incluyendo sentencias block y otras sentencias if anidadas.

`Descripción`
Multiples sentencias if...else pueden ser anidadas para crear una cláusula else if:
```js
if (condición1)
   sentencia1
else if (condición2)
   sentencia2
else if (condición3)
   sentencia3
...
else
   sentenciaN
```
Para entender como esto funciona, así es como se vería si el anidamiento hubiera sido indentado correctamente:
```js
if (condición1)
   sentencia1
else
   if (condición2)
      sentencia2
   else
      if (condición3)
      ...
```
---
Una declaración if no es muy útil sin tener también la capacidad de dar otra opción. La capacidad de tener un si o un otro, me encanta la forma en que se describen porque puedes leerlo casi como un lenguaje sencillo. Donde se puede decir si tal o cual es cierto. Si se cumple esta condición, quiero que ejecute todo dentro de esta sección. De lo contrario, si no, quiero que muestres todo o ejecutes todo en esta otra sección.
```js
var edad = 44;

if (edad <= 10) {// Condición
  console.log('El menú infantil es tu opción'); // Si se cumple condición
} // Si no se cumple condición
else { // Condición
  console.log('El menú adulto es tu opción'); // si se cumple condición
}
```
Devuelve → El menú adulto es tu opción


## <b><font color="#006cb5">Coding Exercise</font></b>
Write a condition that returns true if you have more than 50 watermelons.
```js
function watermelonParty() {
    
    watermelons = EnterYourNumberHere;
    
    if (WriteYourConditionsHere) {
        return true;
    }
}

watermelonParty();
```
Resultado:
```js
function watermelonParty() {
    
    watermelons = 100;
    
    if (watermelons >= 50) {
        return true;
    }
}

watermelonParty();
```

# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-if-else-conditionals-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_c_02_if_else_conditionals.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/rNgyGmM)