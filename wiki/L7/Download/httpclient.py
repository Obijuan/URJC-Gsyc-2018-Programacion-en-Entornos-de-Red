# -- Ejemplo de cliente web que usa la biblioteca http.client

import http.client

PORT = 8001

# Conectarse con el servidor
conn = http.client.HTTPConnection('localhost', PORT)

# -- Enviar un mensaje de solicitud (Verbo: GET), Recurso: Raiz
conn.request("GET", "/")

# -- Leer el mensaje de respuesta recibido del servidor
r1 = conn.getresponse()

# -- Imprimir la linea de estado de la respuesta
print(r1.status, r1.reason)

# -- Leer el contenido de la respuesta y converirlo a una cadena
data1 = r1.read().decode("utf-8")

# -- Imprimir el fichero html recibido
print(data1)
