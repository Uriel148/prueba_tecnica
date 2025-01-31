Para ejecutar este programa se creo un ambiente virtual en python3, de esta manera evitamos cualquier posible conflinco con la compatibilidad de las librerias
1. Lo primero es tener algun editor como visual studio code y tener cualquier version Python, pues las librerias usadas son compatibles con toda las versiones.
2. Con este comando es posible ejecutar el entorno virtual ```python -m venv prueba_tecnica``` y poder empezar a ejecutar el codigo.
3. En caso de que no funcione el entorno virtual hay que instalar ```pip install pandas``` y ```pip install flask``` para tener las librerias necesarias.
4. El codgo esta en el archivo prueba.py al ejecutar el archivo se genera el documento usuarios.csv que actuara como la "base de datos"
5. Dentro del documento se generaron varios metodos 2 GET (/,/mostar_los_usuarios) y 3 POST (/eliminar_usuario,/editar_usuario,/agregar_usuario)


Consideraciones: Se pudieron usar metodos como DELETE o PUT, pero como el archivo csv funciona como nuestra base de datos se opto por usar solo metodos post y get.
Dentro del archivo prueba.py aparece un ejemplo de como llamar a cada uno de los metodos de manera comentada
