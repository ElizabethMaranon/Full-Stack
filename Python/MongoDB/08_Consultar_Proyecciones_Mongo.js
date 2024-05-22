db.música.find({nombre: "Lepoka"})


db.música.find(
    {
        nombre: "Lepoka"
    },
    {
        nombre: 1,
        canciones: 1
    }
)
.pretty()
