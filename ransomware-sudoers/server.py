import cgi
from http.server import BaseHTTPRequestHandler
import io
import sqlite3
import datetime
from datetime import date
from datetime import datetime
now = datetime.now()
con = sqlite3.connect('example.db')
cur = con.cursor()


class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        # Begin the response
        self.send_response(200)

        print(self.client_address)

        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )
        out.write('1')
        out.write('3')
        print('---')
        print(form)
        print('---')
        # COMPRUEBA SI EXISTE UNA TABLA PARA EL EQUIPO Y LA CREA DE NO SER ASÍ
        string_a_comprobar = form['id'].value
        consultacomprobar = "SELECT * FROM equipos WHEre id = '{}'".format(
            string_a_comprobar)
        cur.execute(consultacomprobar)
        data = cur.fetchall()
        print("owo")
        print(data)
        print("owo")
        format = now.strftime('%Y%m%d%H%M%S00')
        if len(data) == 0:
            consultacrear = "INSERT INTO equipos (id,ultima_fecha,primera_fecha) VALUES ('" + \
                form['id'].value+"',"+format+","+format+");"
            cur.execute(consultacrear)
            cur.execute('INSERT INTO equipos (id,ip,so,nombre,puertos,root) VALUES (' +
                        form['id'].value+','+form['ip'].value+','+form['so'].value+','+form['nombre'].value+','+form['puertos'].value+','+form['root'].value+');')
            # print ('hola'+form['id'].value+'mundo'+)
            print('No existe')
        else:
            consultaactualizar = "UPDATE equipos SET ultima_fecha = (" + \
                format+") where id = '"+form['id'].value+"';"
            cur.execute(consultaactualizar)
            print('Existe')
        print(form)
        if 'ls' not in form:
            print('LS No existe')
            #consultaactualizar = "UPDATE equipos SET {} = '{}' WHERE id='{}';".format(field, form[field].value, form['id'].value)
            # cur.execute(consultaactualizar) # !!!
            # cur.execute()
            # print(a)
        else:
            print('LS Existe')
            consultacomandos = "SELECT pendiente FROM COMANDOS WHERE id_equipo = '" + \
                form['id'].value+"';"
            print(consultacomandos)
            cur.execute(consultacomandos)
            datacomando = cur.fetchall()
            print(datacomando)
            if len(datacomando) == 0:
                consultacrear = "INSERT INTO comandos (id_equipo) VALUES ('" + \
                    form['id'].value+"');"
                cur.execute(consultacrear)
                #cur.execute('INSERT INTO equipos (id,ip,so,nombre,puertos,root) VALUES ('+form['id'].value+','+form['ip'].value+','+form['so'].value+','+form['nombre'].value+','+form['puertos'].value+','+form['root'].value+');')
            # print ('hola'+form['id'].value+'mundo'+)
                print('No existe tabla ls')
            else:
                print('Existe tabla ls')
                consultacrear = "UPDATE comandos SET ls = '{}' WHERE id_equipo='{}';".format(
                    form['ls'].value, form['id'].value)
                print(consultacrear)
        if 'arp' not in form:
            print('ARP No existe')
            #consultaactualizar = "UPDATE equipos SET {} = '{}' WHERE id='{}';".format(field, form[field].value, form['id'].value)
            # cur.execute(consultaactualizar) # !!!
            # cur.execute()
            # print(a)
        else:
            print('ARP Existe')
            consultacomandos = "SELECT pendiente FROM COMANDOS WHERE id_equipo = '" + \
                form['id'].value+"';"
            print(consultacomandos)
            cur.execute(consultacomandos)
            datacomando = cur.fetchall()
            print(datacomando)
            if len(datacomando) == 0:
                consultacrear = "INSERT INTO comandos (id_equipo) VALUES ('" + \
                    form['id'].value+"');"
                cur.execute(consultacrear)
                #cur.execute('INSERT INTO equipos (id,ip,so,nombre,puertos,root) VALUES ('+form['id'].value+','+form['ip'].value+','+form['so'].value+','+form['nombre'].value+','+form['puertos'].value+','+form['root'].value+');')
            # print ('hola'+form['id'].value+'mundo'+)
                print('No existe tabla ls')
            else:
                print('Existe tabla ls')
                consultacrear = "UPDATE comandos SET arp = '{}' WHERE id_equipo='{}';".format(
                    form['arp'].value, form['id'].value)
                print(consultacrear)

        # Echo back information about what was posted in the form
        for field in form.keys():

            field_item = form[field]
            a = (' {}={} '.format(field, form[field].value))
            # AÑADE O ACTUALIZA LOS CAMBOS A LA FILA DEL EQUIPO
            # IGNORA LOS CAMPOS DE COMANDOS
            if field != ('ls' or 'arp'):
                consultaactualizar = "UPDATE equipos SET {} = '{}' WHERE id='{}';".format(
                    field, form[field].value, form['id'].value)
                cur.execute(consultaactualizar)  # !!!
                # cur.execute()
                # print(a)
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
        con.commit()

        # Disconnect our encoding wrapper from the underlying
        # buffer so that deleting the wrapper doesn't close
        # the socket, which is still being used by the server.
        # out.write('1')
        out.detach()
        # PRUEBA DE ENVIO DE ORDEN


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('127.0.0.1', 80), PostHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
