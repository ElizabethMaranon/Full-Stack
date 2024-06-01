![Logo Mielma](logo/Logo%20Encabezado.png)

# <b><font color="#556CEE">Sintaxis básica para usar condicionales en JavaScript</font></b>
Los condicionales nos dan la posibilidad de mirar un par de valores o incluso varios. Tres, cuatro o cinco, dependiendo de lo que necesite comparar y ver cómo se relacionan entre sí. Podemos ver si son iguales entre sí si uno es mayor que el otro..

Podemos verificar si no son explícitamente iguales entre sí y luego también en JavaScript tenemos la capacidad de verificar si también son del mismo tipo. 

## <b><font color="#006cb5">if[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/if...else)</font></b>
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

// Imprime → "Teneis la misma edad"
```
|if|Var|Signo|Descripción          
|-|-|-|-
|if|Var|==| Mala práctica para igual
|if|Var|===| Igual
|if|Var|!==| No igual
|if|Var|<=| Mayor 
|if|Var|>=| Menor 

## <b><font color="#006cb5">Coding Exercise</font></b>
Create a conditional that returns true, using the starting code below.
```js
answer = false;

if (input your conditions here) {
    answer = true;
}
```
Respuesta
```js
answer = false;

if (answer === false) {
    answer = true;
}
```

# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/basic-syntax-using-conditionals-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_c_01_comparison_operators.js)

[Documentación del operador de comparación](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)