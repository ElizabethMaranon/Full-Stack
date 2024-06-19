![Logo Mielma](image/Logo_Encabezado.png)

# <center><b><font color="#556CEE">Seguimiento automático de cuentas y hashtags en LinkedIn con JavaScript</font></b>
Ahora veamos cómo podemos automatizar tareas en LinkedIn. Ahora bien, esta es una forma muy popular de utilizar JavaScript. Si desea desarrollar su red, esta es una excelente manera de hacerlo de manera muy rápida..

La razón por la que voy a hacer esto es que si lo hiciera para todos: se lo enviaría a un grupo de personas, y no estoy 100% seguro de querer agregar a todas estas personas recomendadas. Sin embargo, sé que hay muchas personas y desarrolladores que están tratando de construir su red y simplemente quieren ejecutar y agregar un montón de conexiones..

Está perfectamente bien, pero te mostraré cómo seguir varios hashtags. El proceso es completamente idéntico. Lo sabía porque hice una pequeña prueba antes de filmar esto y envió el **conectar mensajes** y **conectar invitaciones** para todos.

Entonces esto funcionará para personas, para todos o para hashtags. Voy a pasar a los hashtags y podremos explicar exactamente cómo funciona esto. Así que haga clic derecho en seguir y `inspect`. Ahora, esto me dará el texto real, porque eso es lo que seleccioné, pero necesitamos avanzar un poco más en el `DOM`.

Aquí mismo podéis ver que tenemos el botón. Este elemento de botón es en realidad lo que estamos buscando. Entonces, aquí en el botón, esto será relativamente sencillo, porque tenemos una clase que podemos tomar.

Todo lo que tengo que hacer es agarrar esto. `button`. Es un bonito nombre largo. Presiona copiar y luego ve a la consola. Permitirme aclarar cualquier error que hayamos tenido. Aquí mismo hagamos una prueba y asegurémonos de que tenemos acceso a todo lo que creemos que tenemos acceso. Entonces voy a decir:
```js
let hashtagBtns = document.querySelectorAll('.mn-discovery-hashtag-card__action-btn')


```
Ahora lo que puedo hacer es simplemente ejecutar el selector, y ahora si busco un `hashtagBtns ` Puedes ver que muestra todos los botones de seguimiento específicos que tenemos aquí. Si quisiera comprobar el largo. puedo ver que tengo 83 de aquellos.

```js
hashtagBtns
```

Ahora lo que podemos hacer es automatizar el proceso de seguir todos esos hashtags. Así que aquí puedo decir: botonUnirse.forEach(). Para cada uno en JavaScript se necesita una función. Entonces solo voy a decir:
```js
hashtagBtns.forEach(btn => btn.click())
```
Este es el click function que está disponible en JavaScript. Ahora, si ejecuto eso, puedes ver que fue y siguió cada uno de esos hashtags. Entonces, si hago clic en Actualizar en esta página, pueden ver que ahora estoy siguiendo cada uno de los hashtags. Así que ahora sigo a cada uno de los que estaban allí..

Ahora podrías hacer exactamente lo mismo aquí, y yo lo haré. Quiero mostrarte ambos lados, así que te mostré cómo puedes hacerlo por siguiente.

Ahora, si quieres dejar de seguir, di todos estos elementos diferentes. Veamos si podemos hacer eso. Así que voy a hacer clic `inspect` aquí, y ahora tienes esto `actor_follow_toggle`. Este es un nombre de control. Entonces el `class`, tienes `follows-recommendation-card__follow-btn`. Esto es lo que estamos buscando, esta clase aquí.

Voy a copiar esto y vamos a hacer lo mismo. Entonces voy a decir, esta vez no importa si usas `const`, `let`, o `var` para la variable. No voy a cambiarlo, así que voy a decir:

```js
const followingBtns = document.querySelectorAll('.follows-recommendation-card__follow-btn')
```
Ejecute eso y ahora, si verifico todos los siguientes botones, podrá verlos allí mismo. Ahora puede ejecutar exactamente el mismo proceso, así que puedo decir:
```js
followingBtns.forEach(followbtn => followbtn.click())
```
Ahora puedes ver que dejó de seguir cada uno de esos hashtags.

Entonces, con solo escribir una sola línea de código, podemos seguir todos esos hashtags en la página y luego escribir otra línea de código muy similar para ingresar y dejar de seguirlos. Si eso es algo que estás buscando hacer, donde estás tratando de construir tu red o en eso específico de LinkedIn, pero estos procesos que simplemente pasan por esto podrían aplicarse a cualquier tipo de página..

Puedes hacer esto para Instagram, puedes hacerlo para Facebook, puedes hacerlo para cualquier cosa que quieras automatizar. Lo que me dio esta idea fue que el director ejecutivo de Bottega Code School me preguntó si podía ayudarlo a crear un guión porque estaba tratando de automatizar el proceso de ir y seguir a un grupo de personas en algunos de estos grupos de LinkedIn..

Eso fue lo que me dio la idea de hacer eso porque asumo que si él lo pedía, otras personas buscaban automatizar el mismo proceso. Ahora ya sabes cómo hacerlo y, como puedes ver, es relativamente sencillo..

Recuerde, cualquier tipo de script como este tiene dos pasos principales. primero tiene el `query step`. Ahí es donde vas y encuentras el nombre de clase que estás buscando, luego lo consultas y almacenas ese valor en una variable..

Luego a partir de ahí, el segundo paso es `perform the process`. En este caso el proceso fue simplemente hacer clic en el botón. El proceso podría ser cualquier otro. Podría implicar otros pasos si necesita decir completar los elementos del formulario y luego hacer clic o lo que sea que necesite hacer..

Siempre y cuando tengas ese elemento seleccionado cuando tengas `forEach` y tienes un método como este, lo que puedes hacer es tratar cada elemento como si fueras tú quien estuviera haciendo clic o estuvieras completando un formulario o cualquier proceso que estés buscando hacer. Simplemente puedes hacer que el código lo haga..

De eso se trata, de poder automatizar todo el proceso usando JavaScript. Gran trabajo. Ahora sabes cómo automatizar completamente cualquier tipo de proceso que necesites realizar dentro de un navegador..


## <center><b><font color="#006cb5">Coding Exercise</font></b>
6 Snakes have made themselves at home in your boot. Use the query selector all to locate all of the snakes!
```html
<div id="boot">
  <div class="snake"></div>
  <div class="snake"></div>
  <div class="snake"></div>
  <div class="snake"></div>
  <div class="snake"></div>
  <div class="snake"></div>
</div>
```
const nodeList = write-Your-Code-Here-to-select-the-snakes
```js
```
Resultado:
```js
const nodeList = document.querySelectorAll('.snake')
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/auto-following-accounts-hashtags-linkedin-javascript)  

