//use lovemetal
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

db.createCollection('música')


//Eliminar colección
db.nombreCollection.drop() 