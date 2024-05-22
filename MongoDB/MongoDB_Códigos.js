// 01. Crear base de datos
"use lovemetal"

// Crear Usuario Admin
db.createUser({ // Crear función y argumentos en pares clave-valor
    user: 'Eli', // Argumento Usuario 
    pwd: 'Contraseña', // Argumento Contraseña
    fecha: { startDate: new Date() }, // Argumento fecha de inicio
    roles: [ // Añadir roles 
        // ClusterAdmin: Mayor acceso gestión cluster
        //db: 'admin': Usuario admin tiene la capacidad de funcionar como administrador 
        //readAnyDatabase: Leer y modificar colecciones non-system
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
})

// Crear usuario
db.createUser({//base datos
    user: 'Mielma',
    pwd: 'Contraseña',
    fecha: { startDate: new Date() },
    roles: [
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
})

// Eliminar usuario
db.dropUser('usuario a eliminar')

// Ver usuarios base de datos
db.getUsers()

// 03. Crear Colección
db.createCollection('nombre_colección')

//Eliminar colección
db.nombre_colección.drop()

// 04. Insertar documento
db.cantantes.insertOne({
    "nombre": "Saurom",
    "publishedDate": new Date(),
    "canciones": [
        { "nombre": "Fuego" },
        { "nombre": "Pájaro fantasma" }
    ]
})

// 05. Insertar muchos documentos
db.música.insertMany([
    {
        "nombre": "Saurom",
        "publishedDate": new Date(),
        "canciones": [
            { "nombre": "Pájaro fantasma" }
        ]
    },
    {
        "nombre": "Sylvania",
        "publishedDate": new Date(),
        "canciones": [
            { "nombre": "Purgatorium" }
        ]
    },
    {
        "nombre": "Lepoka",
        "publishedDate": new Date(),
        "Canciones": [
            { "nombre": "Un año más" }
        ]
    }
])

// 06. Consultar documentos
db.música.find()
db.música.find().pretty()

// 07. Consultar documento en concreto
db.música.find({ nombre: "Sylvania" })
db.música.find({ nombre: "Sylvania" }).pretty()


// 08. Consultar Proyección
db.música.find(
    {
        nombre: "Lepoka"
    },
    {
        nombre: 1,
        canciones: 1
    }
).pretty()

// 09. Consultar parte elemento {$Slice: num} 1 primero; 2 dos primeros; -1 último; ....
db.cantantes.find(
    {
        nombre: "Saurom"
    },
    {
        fecha: 1,
        nombre: 1,
        canciones: { $slice: 1 }
    }
)

// 10. Eliminar documentos
db.música.remove({ nombre: "Saurom" }, 1)

db.música.remove({ nombre: "Lepoka" }, 1)

// 11. Consultar Campos Anidados
db.música.insertOne({
    "nombre": "Saurom",
    "fecha": new Date(),
    "canciones": [
        { "nombre": "Pájaro Fantasma", "active": "True" },
        { "nombre": "Fuego", "active": "True" }
    ]
})

db.música.find(
    {
        nombre: "Saurom"
    },
    {
        nombre: 1,
        fecha: 1,
        "canciones.nombre": 1
    }
).pretty()

// Consultar un sólo elemento, aunque haya más
db.música.findOne({nombre: "Saurom"})

