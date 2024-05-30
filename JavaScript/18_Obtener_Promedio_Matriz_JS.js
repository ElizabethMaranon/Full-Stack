const promedio = lista => {
    // Sumar los valores
    const reducer = (total, valores) => total + valores;
    // Obtener longitud   
    const total = lista.reduce(reducer)
    // Dividir suma entre longitud
    return total / lista.length;
};

const lista = [1, 2, 3, 4, 5, 6]

promedio(lista);

// 3.5