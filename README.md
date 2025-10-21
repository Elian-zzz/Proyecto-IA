# Proyecto ceilab

Un proyecto de ***inteligencia artificial*** en el cual hacemos un chatbot para la consulta de horarios en la semana.

***

### Comandos para ejecutar el proyecto (por primera vez)

1. *Dirigirse a la raíz del poryecto `C:\Users\56591552\Desktop\proyecto_chat\proyecto_chat`*
2. *Ejecutar `.\venv\Scripts\activate` en la en la consola de comandos para crear el entrono de desarrollo python.* 
3. *Luego que aparezca `(venv)` en el principio de la línea de comandos ejecutar `.\venv\Scripts\python.exe -m pip install python-dotenv` para instalar **dotnev** en el entorno de desarrollo.*
4. *Ejecutar `py app.py` para ejecutar la aplicación python.*

### Comandos para ejecutar el proyecto (ya instalado)
1. *Seguir los pasos 1 y 2*
2. *Luego ejecutar `py app.py` en la consola para ejecutar la aplicación* 

***

## Tecnologías

Tecnologías utilizadas en el proyecto:

#### **FrontEnd**  
***Stack:*** | _HTML_ | _CSS_ | _JavaScript_ |

***Bibliotecas:***  | _Bootstrap_ |

#### **BackEnd**  
***Stack:*** | _Python_ |
***Bibliotecas:*** | _Flask_ | 

***
### EndPoint 
`/consulta` :
Consulta al servidor _app.py_ el mensaje ingresado por el cliente, ejemplo de ingreso:
`que tengo los martes?` ó `cuando es el examen de ADA?`

***

### API Consulta

*FrontEnd __JavaScript__*
``` javascript
    // Enviar al servidor
  fetch("/consulta", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensaje }),
  })
    .then(...)
```

*BackEnd __Pyhon__*

El servidor está oriendado a dirigir las consultas en dos tipos: `horarios` y `examenes`

Funciónes de cargar horarios:

``` python
    # Funciones para cargar archivos
def cargar_horarios():
    horarios = {}
    with open("horarios.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): 
                continue
            dia, clase = line.strip().split("|", 1)
            dia = dia.lower()
            horarios.setdefault(dia, []).append(clase)
    return horarios
```

Funciónes de cargar examenes:

``` python
    def cargar_examenes():
    examenes = {}
    with open("examenes.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): 
                continue
            materia, fecha = line.strip().split("|", 1)
            examenes[materia.lower()] = fecha
    return examenes
```


***
### Integrantes del grupo MKIA
- Elian Gutierrez
- Javier Leiva
- Mateo Lalin
- Ignacio del Rio
- Rodrigo Alvez
- Kevin Mir
***
_Todos los derechos reservados ©2025 MKIA_
