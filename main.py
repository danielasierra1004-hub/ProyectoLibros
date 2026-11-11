
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API de Libros",
    description="API para administrar una colección de libros",
    version="1.0"
)

# Modelo para registrar libros
class Libro(BaseModel):
    titulo: str
    autor: str
    anio: int

# Lista temporal de libros
libros = [
    {
        "id": 1,
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupery",
        "anio": 1943
    },
    {
        "id": 2,
        "titulo": "Don Quijote",
        "autor": "Miguel de Cervantes",
        "anio": 1605
    }
]

# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Libros"}

# GET: Mostrar todos los libros
@app.get("/libros")
def obtener_libros():
    return libros

# GET: Buscar un libro por ID
@app.get("/libros/{libro_id}")
def buscar_libro(libro_id: int):
    for libro in libros:
        if libro["id"] == libro_id:
            return libro

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )

# POST: Agregar un libro
@app.post("/libros", status_code=201)
def agregar_libro(libro: Libro):
    nuevo_id = max(
        [l["id"] for l in libros],
        default=0
    ) + 1

    nuevo_libro = {
        "id": nuevo_id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "anio": libro.anio
    }

    libros.append(nuevo_libro)

    return {
        "mensaje": "Libro agregado correctamente",
        "libro": nuevo_libro
    }
