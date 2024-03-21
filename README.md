# Instalación
En tu consola ejecuta:
```pip install -r .\requirements.txt```

# Ejecución
Abre una consola, puedes definir variables de entorno (opcinal). En caso de no definirlos se usarán los valores por defecto.
Puedes definir las variables `port` y `host`.
Pycharm usa powerShell:
```
$env:port = "8001"
Write-Host $env:port
```
Finalmente ejecuta desde consola como cualquier script normal de python (desde la carpeta raiz).
```python ./src/main.py```

En caso de ejecutarlo desde Pycharm, configura el work directory justo fuera de `\src` (carpeta raiz)

# Endpoints
Para añadir nuevos endpoints sigue estos pasos en orden:

1. Crea un nuevo objeto`schema`: donde definas los campos del json de respuesta
2. Crea una nueva clase `DAO` (Data Access Object): donde definas los métodos CRUD del objeto anterior.
3. Crea un nuevo `router`: donde expongas las urls con sus métodos (GET, POST...). Cada endpoint llamará a un método CRUD de la clase DAO.
4. Finalmente incluye el router al main.py

__Nota1__: 
Cuando crees archivos dentro de un módulo, recuerda importarlo dentro de `__init__.py`

Un módulo se comporta como un archivo, concretamente lo que haya en el archivo `__init__.py` (ignora el resto de archivos la carpeta)

__Nota2__: 
Python es orientado a objetos, `self` equivale a `this` (usados en otros lenguajes de programación como C# o Java).

__Nota3__: 
Recuerda usar el modo depuración para ver como funciona paso a paso.