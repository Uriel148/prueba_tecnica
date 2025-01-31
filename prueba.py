import tkinter as tk
import pandas as pd
import numpy as np
from fastapi import FastAPI

usuarios= [   
{"name": "Juan Pérez", "email": "juan.perez@example.com", "role": 
"Administrador" },   
{"name": "María López", "email": "maria.lopez@example.com", "role": 
"Usuario" },   
{"name": "Carlos García", "email": "carlos.garcia@example.com", "role": 
"Usuario" }   
]

#Mostar los usuarios
df_usuarios = pd.DataFrame(usuarios)
df_usuarios.index += 1
print(df_usuarios)

#Eliminar usuario
fila_eliminar = 1
df_usuarios = df_usuarios.drop(fila_eliminar)
df_usuarios = df_usuarios.reset_index(drop=True)
df_usuarios.index += 1
print(df_usuarios)

#Agregar usuario
nuevo_nombre = "Alejandro Aguilar"
nuevo_email = "ale.agui@example.com"
nuevo_rol = "Usuario"
nuevo_usuario = {"name": nuevo_nombre, "email": nuevo_email, "role": nuevo_rol }
df_usuarios.loc[len(df_usuarios)+1] = nuevo_usuario
print(df_usuarios)

#Editar Usuario
fila_editar = 3
editar_nombre = "Miguel Aguilar"
editar_email = "migue.agui@example.com"
editar_rol = "Usuario"
df_usuarios.loc[fila_editar] = [editar_nombre,editar_email,editar_rol]
print(df_usuarios)




app = FastAPI()

@app.get("/my-first-api")
def hello():
  return {"Hello world!"}