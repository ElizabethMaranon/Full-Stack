![Logo Mielma](image/Logo_Encabezado.png)

# <b><font color="#556CEE">Condicionales compuestos en JavaScript</font></b>

## <b><font color="#006cb5">¿Qué son los condicionales compuestos[🔗](https://ferreiragomez.wordpress.com/wp-content/uploads/2019/07/3.-guia-3-condicionales_javascript.pdf) en JS?</font></b>
En una estructura condicional compuesta es aquella que contiene más de un condicional (if - else), cuando se usa condicionales compuestos tenemos entradas, salidas, operaciones, tanto por la rama del verdadero como por la rama del falso.

```js
var age = 44;

if (age <= 16) {// Condición: si eres menor de 16
  console.log("El menú infantil es tu opción");// Si se cumple condición
  console.log("No puedes conducir un coche");// Si se cumple condición
  console.log("No puedes alquilar un coche");// Si se cumple condición
} // Si no se cumple condición anterior
else if (age >= 16 && age < 25) {// Condición: entre 16 y 25
  console.log("El menú adulto es tu opción");// Si se cumple condición
  console.log("Puedes conducir un coche");// Si se cumple condición
  console.log("No puedes alquilar un coche");// Si se cumple condición
 } // Si no se cumple condición anterior
else if (age >= 25) {// Condición: mayor que 25
  console.log("El menú adulto es tu opción");// Si se cumple condición
  console.log("Puedes conducir un coche");// Si se cumple condición
  console.log("Puedes alquilar un coche");// Si se cumple condición
}
```
En este caso nos devuelve
```js
"El menú adulto es tu opción"
"Puedes conducir un coche"
"Puedes alquilar un coche"
```

## <b><font color="#006cb5">Coding Exercise</font></b>
Create a condition that allows a 15 year old to get a permit, but can't get a license.
```js
function kid() {
    age = GiveYourKidAnAge;
    
    if (EnterYourConditionsHere) {
        return true;
    }
}
```
Resultado:
```js
function kid() {
    age = 15;
    
    if (age <=15) {
        console.log('Get a permit');
        
        console.log('Can´t get a license')
        return true;
    }
}
```

# <b><font color="#556CEE">Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/compound-conditionals-javascript)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_c_03_compound_conditionals.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/VwOpMQd)