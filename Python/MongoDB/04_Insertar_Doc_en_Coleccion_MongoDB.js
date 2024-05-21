db.música.insertOne({ 
    "nombre": "Saurom", 
    "publishedDate": new Date(),
    "canciones": [
        {"nombre": "Fuego"},
        {"nombre": "Pájaro fantasma"}
    ]
  })
//Eliminar una canción
db.música.insertOne({ 
    "nombre": "Saurom", 
    "publishedDate": new Date(),
    "canciones": [
        {"nombre": "Pájaro fantasma"}
    ]
  })

//Cambiar published date
db.música.insertOne({ 
    "nombre": "Saurom", 
    "startDate": new Date(),
    "canciones": [
        {"nombre": "Pájaro fantasma"}
    ]
  })

//mostrar documentos de una colección
db.música.find({})