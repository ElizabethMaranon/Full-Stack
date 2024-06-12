![Logo Mielma](/Logo/Logo_Encabezado.png)

# <center><b><font color="#556CEE">CheckPoint 7 - ¿Qué es la palabra clave "this" en JS?</font></b>

## <b><font color="#006cb5">¿Qué es la palabra clave "this" en JS?[🔗](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/this)</font></b>
La palabra clave this de una función se comporta un poco diferente en Javascript en comparación con otros lenguajes. Además tiene algunas diferencias entre el modo estricto y el modo no estricto.

En general, el valor de this está determinado por cómo se invoca a la función. No puede ser establecida mediante una asignación en tiempo de ejecución, y puede ser diferente cada vez que la función es invocada.

## <b><font color="#006cb5">Forma más común</font></b>

Una de las formas más comunes de usar `this` es dentro de un objeto.

Podemos llamar a un método indicando a qué objeto this se referirá la palabra clave. 

Necesitamos decir `this.` porque necesita saber la instancia exacta a la que nos referimos.

Pero cuando decimos `this.`, sabe que estamos haciendo referencia a estos objetos visibles para usar o al método, esa es la clave. Estamos haciendo referencia a esta instancia específica de este objeto porque, en un tipo de aplicación tradicional, lo que normalmente sucederá es que tendrás cientos o miles de estas instancias de guía. Si acaba de llamar a una forma genérica al método, no sabrá a cuál está haciendo referencia, debemos decirle que estamos haciendo referencia a este para este caso. 

Puedes usar this tanto para métodos como para datos.

```js
var música = { // Crear objeto 
  artista: 'Saurom', // Pares clave-valor,
  álbum: "El pájaro fantasma", // Pares clave-valor,
  visible: function (vistaRolUsuario) { // Método para verificar si está registrado
    if (vistaRolUsuario === 'Registrado') { // Argumento
      return true;
    } else {
      return false;
    }
  },
  ofrecerContenido: function(rolUsuario) { // Método para presentar el contenido.
    if (this.visible(rolUsuario)) { // Argumento: this.visible porque necesita saber la instancia exacta
      console.log(this.artista + " - " + this.álbum);
    } else {
      this.content = "";
      console.log(this.artista + " - " + this.álbum);
    }
  }
}

Mielma = {role: 'Registrado'};
Eli = {role: 'otro rol cualquiera'};

música.ofrecerContenido(Mielma.role); // "Saurom - El pájaro fantasma"
música.ofrecerContenido(Eli.role); // "Saurom - "
```

# <center><b><font color="#556CEE">🔗Links🔗</font></b>

[DevCamp Exclusivo Usuarios](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-use-the-this-keyword-javascript-programs)  

[Código DevCamp](https://github.com/rails-camp/javascript-programming/blob/master/section_d_09_this_keyword.js)

[Código Mielma](https://codepen.io/ElizabethMaranon/pen/YzbxOaK)

