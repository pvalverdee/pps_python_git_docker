# pps_python_git_docker

Es una práctica para puesta en producción segura


## Para resolver dependencias ejecuta

pip install -r requirements.txt

## Ahora debería funcionar la aplicacion desde la rama MAIN

conectarse a localhost:5000/frotar/$(N)

## Se han corregido errores en el código para compatibilidad con docker

para crear contenedor de docker ejecutar:

   ```bash
   docker build -t nombre_imagen:tag .
```
y luego

 ```bash
    docker run -d -p 5000:5000 nombre_imagen:tag
 ```
