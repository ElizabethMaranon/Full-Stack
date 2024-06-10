![Logo Mielma](Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">CheckPoint 7 - ¿Qué es un condicional?</font></b>

## <b><font color="#006cb5">¿Qué son los condicionales[🔗](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)?</font></b>

Los condicionales son uno de los componentes más fundamentales de cualquier tipo de lenguaje de programación.  
La razón de esto es porque conditionals le permite tener un comportamiento dinámico en su aplicación

Las declaraciones condicionales son Declaraciones lógicas o comandos que manejan decisiones basadas en ciertas condiciones. Lo hacen realizando diferentes cálculos o acciones dependiendo de si la condición definida por el desarrollador resulta ser verdadera o falsa.

## <b><font color="#006cb5">Sintaxis básica para usar condicionales en JavaScript</font></b>
Los condicionales nos dan la posibilidad de mirar un par de valores o incluso varios. Tres, cuatro o cinco, dependiendo de lo que necesite comparar y ver cómo se relacionan entre sí. Podemos ver si son iguales entre sí si uno es mayor que el otro..

Podemos verificar si no son explícitamente iguales entre sí y luego también en JavaScript tenemos la capacidad de verificar si también son del mismo tipo. 

### <font color="#556CEE">if[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/if...else)</font>
Ejecuta una sentencia si una condición específica es evaluada como verdadera. Si la condición es evaluada como falsa, otra sentencia puede ser ejecutada.


```js
edad = 12;
edadDos = 15;
// Para saber si son iguales
if (edad == edadDos) {
  console.log("Tenéis la misma edad");
}
//No imprime nada porque las edades son diferentes
```

```js
edad = 12;
edadDos = 12;
// Para saber si son iguales
if (edad === edadDos) {
  console.log("Tenéis la misma edad");
}

// Imprime → "Tenéis la misma edad"
```
|if|Var|Signo|Descripción          
|-|-|:-:|-
|if|Var|==| Mala práctica para igual
|if|Var|===| Igual
|if|Var|!==| No igual
|if|Var|<=| Mayor 
|if|Var|>=| Menor 




### <font color="#556CEE">If/Else[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/if...else)</font>

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

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios Condicionales](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/javascript-conditional-section-introduction)

[DevCamp Exclusivo Usuarios If](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/basic-syntax-using-conditionals-javascript)

[DevCamp Exclusivo Usuarios If/Else](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/guide-if-else-conditionals-javascript) 

[Código DevCamp If](https://github.com/rails-camp/javascript-programming/blob/master/section_c_01_comparison_operators.js)

[Código DevCamp If/Else](https://github.com/rails-camp/javascript-programming/blob/master/section_c_02_if_else_conditionals.js)

[Código Mielma Condicionales](https://codepen.io/ElizabethMaranon/pen/KKLWyLo)

[Código Mielma If](https://codepen.io/ElizabethMaranon/pen/MWdJxaO)

[Código Mielma If/Else](https://codepen.io/ElizabethMaranon/pen/rNgyGmM)

[Documentación del operador de comparación](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)

