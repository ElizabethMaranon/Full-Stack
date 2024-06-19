![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Introducción a las funciones de flecha (Arrow functions) en JavaScript </font></b>
<!-- ## <b><font color="#006cb5"></font></b>
### <font color="#556CEE"></font>
#### <font color="#006cb5"></font> -->
## <b><font color="#006cb5">Guía DevCamp → Introducción a las funciones de flecha (Arrow functions) en JavaScript</font></b>
En esta parte de la sección, comenzaremos a analizar las funciones de flecha; ahora las funciones de flecha son una de las cosas más importantes para aprender en JavaScript moderno. Los verás por todas partes y, si nunca los has visto antes, si nunca antes has trabajado con ellos, pueden parecer un poco intimidantes.
Se ven completamente diferentes a cualquier otro tipo de declaración de función que haya visto si acaba de usar JavaScript simple. En versiones anteriores. Entonces, a modo de revisión, hablemos de dos formas en que puedes crear una función en javascript.

La primera será una declaración de función normal. Entonces, si digo función y digo nombre completo. Diga fName y lName para obtener un nombre y apellido. Ahora puedo registrar esto en la consola y decir: voy a usar nuestras versiones más modernas de interpolación de cadenas aquí, y diré fname y luego agregaré esto al apellido.
Eso es todo lo que tengo que hacer. Y ahora, si llamo a esto así, si digo el nombre completo, se imprimirán los nombres que le doy, así que pasaré a Mielma y Developer. Si ejecuto este código aquí. Resulta que Mielma Developer no sorprende.
```js
// Declaración de Función
function nombreCompleto(nombre, apellido) {
  console.log(`${nombre}, ${apellido}`);
}
nombreCompleto("Mielma", "Developer"); //"Mielma, Developer"
```
Entonces, si guardo y luego ejecuto esto, obtenemos exactamente el mismo resultado. Entonces la primera es una declaración de función. La segunda es una expresión de función.
```js
nombreCompleto = function (nombre, apellido) {
  console.log(`${nombre}, ${apellido}`);
}
nombreCompleto("Mielma", "Developer"); // "Mielma, Developer"
```
Ahora vamos a hablar de la función de flecha porque es una forma nueva y es increíblemente popular, tan popular de hecho que la verás en tantas aplicaciones diferentes que quería dedicarle una pequeña miniparte completa. el curso solo para funciones de flecha. Eventualmente, vamos a replicar nuestra función de nombre completo como una flecha.

Una cosa que he descubierto que ayuda mucho a los estudiantes cuando se trata de comprender las funciones de flecha es declarar la función de flecha más simple del mundo. Así que la forma en que lo hago es con un Hola mundo. Así que saluda al mundo y configura esto sin parámetros. Voy a recorrer todo esto en un segundo y luego pasaré una flecha. Ese es el nombre de la función de flecha porque tiene un signo igual seguido de un signo mayor que. Y luego pasaremos un bloque de código aquí dentro de llaves. Registro de la consola y luego, dentro de él, saludaré. Y ese es el punto y coma. Y tengo que poner un punto y coma justo después de esto.
Pero luego tengo que llamar a hola mundo de la misma manera que llamaríamos a una función.

Así que ahora puedo decir hola mundo si presiono borrar y luego ejecuto este. Ahora simplemente se imprimirá. Hola tal cual.
```js
// Basic arrow function
saludo = () => { console.log("Hola"); }
saludo();
```
Esta es la función de flecha más básica del mundo. Primero, siempre debe almacenarse dentro de una variable o ejecutarse de inmediato. Todavía no vamos a entrar en las funciones de ejecución inmediata. Podemos preocuparnos por eso más tarde.

Por ahora, piense que las funciones de flecha son como funciones anónimas, por lo que son muy similares a las expresiones de funciones como las que tenemos aquí. Pero en lugar de agregar el nombre de la función, solo tenemos estos pares seguidos de una flecha seguida de lo que queremos ejecutar.

Ahora, lo primero en lo que quiero centrarme con esto es, en primer lugar, no solo en la sintaxis, sino también en que no te intimides cuando los veas porque es exactamente lo mismo que estamos haciendo aquí.

Solo hay algunas diferencias sutiles en los cambios, y veremos los momentos en los que desea usar una función de flecha y los momentos en los que desea usar otra cosa.

Por ahora sólo quiero mostrarte las similitudes para que te acostumbres a este tipo de sintaxis. Así que aquí está nuestro ejemplo base de hola mundo. Solo para reiterar, lo almacena en una variable que establece igual a los pares, y si tiene argumentos, ahí es donde irían los pares. Luego tenemos una flecha y luego tenemos el proceso que queremos ejecutar.

Ahora que todo esto está en su lugar, hablemos de ir un paso más allá. Ahora lo siguiente que voy a hacer es la forma en que puedes implementar una función de flecha si solo tienes un argumento.

Entonces aquí puedo decir nombre y este será el nombre de la función. Y luego pasaré un único argumento que será fname y luego le daré la función de flecha y luego copiaré el registro de mi consola aquí.

Entonces, dentro de esto, simplemente pasaré el argumento que es fname y luego también llamaré una función, para que puedas ver que puedes hacer eso.

Así que voy a decir mayúsculas, lo que hará que todo esté en mayúscula y es una función. Así que lo paso así.

Ahora puedo llamar al nombre y pasar el valor, y ahora, si borro y ejecuto, esto se imprimirá. Entonces imprimirá el nombre. Y también ejecutó esta función en él.
```js
// Función de flecha con argumento de función abreviada para argumentos únicos
nombre = (nombre) => {
  console.log(nombre.toUpperCase());
};
nombre("Mielma");
```
Lo convirtió a mayúsculas, por lo que esta es exactamente la forma en que puedes hacerlo cuando solo tienes un argumento. Ahora bien, si recuerdas que antes dije que los pares son donde pones tus argumentos y si tienes más de uno, entonces sí necesitas tener pares, pero como un atajo y verás ambas sintaxis. Si solo tiene un argumento, entonces no necesita los pares a su alrededor.

Ahora si quieres. No va a tener ningún efecto. Puedo haberlo ejecutado y todo funciona exactamente igual, depende de ti si quieres usarlos o no. Y los guardaré así en caso de que quieras recordar la sintaxis.

Ahora, el siguiente del que vamos a hablar es qué quieres hacer si tienes múltiples argumentos, aquí es donde vamos a replicar estas funciones aquí arriba.




## <center><b><font color="#006cb5">Coding Exercise</font></b>
```js
```
Resultado:
```js
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios]()  

[Código DevCamp]()

[Código Mielma]()

<!-- Ordenar enlaces -->