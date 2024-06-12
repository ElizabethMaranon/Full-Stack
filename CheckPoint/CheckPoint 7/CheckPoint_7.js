// -Cree una función JS que acepte 4 argumentos. Suma los dos primeros argumentos, luego los dos segundos y multiplícalos. Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". Si es más pequeño, la consola registra "¡El número es menor que 50!"

function CheckPoint7(uno, dos, tres, cuatro) {
    var operación = (uno + dos) * (tres + cuatro);
  
    if (operación < 50) {
      console.log('¡El número es menor que 50!');
    }
    if (operación > 50) {
      console.log('¡El número es mayor que 50!');
    }
  }
  
  CheckPoint7(10, 2, 3, 4)