//Crear Usuario Admin
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
// Crear base de datos
use lovemetal

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

// Crear Colección
db.createCollection('nombre_colección') 

//Eliminar colección
db.nombre_colección.drop() 

// Insertar documento
db.música.insertOne({ 
  "nombre": "Saurom", 
  "publishedDate": new Date(),
  "canciones": [
      {"nombre": "Fuego"},
      {"nombre": "Pájaro fantasma"}
  ]
})

// Insertar muchos documentos
db.música.insertMany([
  {
      "nombre": "Saurom",
      "publishedDate": new Date(),
      "canciones": [
          {"nombre": "Pájaro fantasma"}
      ]
  },
  {
      "nombre": "Sylvania",
      "publishedDate": new Date(),
      "canciones": [
          {"nombre": "Purgatorium"}
      ]
  },
  {
      "nombre": "Lepoka",
      "publishedDate": new Date(),
      "Canciones": [
          {"nombre": "Un año más"}
      ]
  }
])

// Consultar documentos
db.música.find()
db.música.find().pretty()

// Consultar documento en concreto
db.música.find({nombre: "Sylvania"})
db.música.find({nombre: "Sylvania"}).pretty()


// Consultar Proyección
db.música.find(
  {
      nombre: "Lepoka"
  },
  {
      nombre: 1,
      canciones: 1
  }
).pretty()