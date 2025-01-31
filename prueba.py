#  Librerias a utilizar
import pandas as pd
import flask
from flask import request

"""
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
#print(df_usuarios) 

#Eliminar usuario
fila_eliminar = 1
df_usuarios = df_usuarios.drop(fila_eliminar)
df_usuarios = df_usuarios.reset_index(drop=True)
df_usuarios.index += 1
#print(df_usuarios)

#Agregar usuario
nuevo_nombre = "Alejandro Aguilar"
nuevo_email = "ale.agui@example.com"
nuevo_rol = "Usuario"
nuevo_usuario = {"name": nuevo_nombre, "email": nuevo_email, "role": nuevo_rol }
df_usuarios.loc[len(df_usuarios)+1] = nuevo_usuario
#print(df_usuarios)

#Editar Usuario
fila_editar = 3
editar_nombre = "Miguel Aguilar"
editar_email = "migue.agui@example.com"
editar_rol = "Usuario"
df_usuarios.loc[fila_editar] = [editar_nombre,editar_email,editar_rol]
#print(df_usuarios) """

usuarios= [   
{"name": "Juan Pérez", "email": "juan.perez@example.com", "role": 
"Administrador" },   
{"name": "María López", "email": "maria.lopez@example.com", "role": 
"Usuario" },   
{"name": "Carlos García", "email": "carlos.garcia@example.com", "role": 
"Usuario" }   
]
df_usuarios = pd.DataFrame(usuarios)
df_usuarios.index += 1
df_usuarios.to_csv('usuarios.csv')


# API
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Esta es la pagina raiz"

@app.route('/mostar_los_usuarios', methods=['GET'])
def mostrar_usuarios():
    df_usuarios = pd.read_csv("usuarios.csv")
    usuarios = df_usuarios.to_dict('records')
    return usuarios

@app.route('/eliminar_usuario', methods=['POST'])
def eliminar_usuario():
    df_usuarios = pd.read_csv("usuarios.csv")
    fila_eliminar = request.json
    fila_eliminar = fila_eliminar["fila_eliminar"]
    df_usuarios = df_usuarios.drop(fila_eliminar)
    df_usuarios = df_usuarios.reset_index(drop=True)
    df_usuarios.index += 1
    df_usuarios.to_csv('usuarios.csv')
    usuarios = df_usuarios.to_dict('records')
    #return jsonify({"received_data": fila_eliminar})
    return usuarios
"""{
  "fila_eliminar": 1
}"""

@app.route('/editar_usuario', methods=['POST'])
def editar_usuario():
    df_usuarios = pd.read_csv("usuarios.csv")
    data =  request.json
    fila_editar = data["fila_editar"]
    editar_nombre = data["editar_nombre"]
    editar_email = data["editar_email"]
    editar_rol = data["editar_rol"]
    df_usuarios.loc[fila_editar] = [editar_nombre,editar_email,editar_rol]
    df_usuarios.to_csv('usuarios.csv')
    usuarios = df_usuarios.to_dict('records')
    return usuarios
"""
{
  "fila_editar":1,
  "editar_nombre": "Uriel Cardenas",
  "editar_email": "u123@gmail.com",
  "editar_rol": "usuario"
}
"""

@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    df_usuarios = pd.read_csv("usuarios.csv")
    data =  request.json
    nuevo_nombre = data["nuevo_nombre"]
    nuevo_email = data["nuevo_email"]
    nuevo_rol = data["nuevo_rol"]
    nuevo_usuario = {"name": nuevo_nombre, "email": nuevo_email, "role": nuevo_rol }
    df_usuarios.loc[len(df_usuarios)+1] = nuevo_usuario
    df_usuarios.to_csv('usuarios.csv')
    usuarios = df_usuarios.to_dict('records')
    return usuarios
"""
{
  "nuevo_nombre": "Uriel Cardenas",
  "nuevo_email": "u123@gmail.com",
  "nuevo_rol": "usuario"
}
"""

app.run()


