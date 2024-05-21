db.createUser({ // Crear función y argumentos en pares clave-valor
        user: 'Eli', // Argumento Usuario 
        pwd: 'Contraseña', // Argumento Contraseña
        customData: { startDate: new Date() }, // Argumento fecha de inicio
        roles: [ // Añadir roles 
          // ClusterAdmin: Mayor acceso gestión cluster
          //db: 'admin': Usuario admin tiene la capacidad de funcionar como administrador 
          //readAnyDatabase: Leer y modificar colecciones non-system
          { role: 'clusterAdmin', db: 'admin' },
          { role: 'readAnyDatabase', db: 'admin' }, 
          'readWrite'
        ]
      })
      
db.getUsers() // Ver usuarios base de datos
db.dropUser('jon') // Eliminar usuario

db.createUser({
  user: 'Mielma', 
  pwd: 'Contraseña',
  customData: { startDate: new Date() },
  roles: [
    { role: 'clusterAdmin', db: 'admin' },
    { role: 'readAnyDatabase', db: 'admin' }, 
    'readWrite'
  ]
})


use admin
db.createUser(
  {
    user: "Mielma",
    pwd: "contraseña",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, 
    "readWriteAnyDatabase" ]
  }
)

      