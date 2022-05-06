#from crypt import methods
from flask import Flask, request, jsonify #aquí importamos la librería Flask en nuestro archivo.
import json
import os
app = Flask(__name__) #aquí creamos una nueva instancia del servidor Flask.

@app.route("/") #aquí definimos el primer path de la API: GET /
def hello(): #este método se llamará cuando el cliente haga el request
    return "Hello World!" #flask devolverá "Hello World, esto podría ser un string HTML o un string JSON.


@app.route("/helloP") #aquí especificamos la ruta para el endpoint.
def handle_person(): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    return "Hello Person!" #aquí especificamos el string que queremos responder al cliente.

@app.route("/diff", methods=['POST', 'GET']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET.
def route_handler():
  if request.method == 'POST': # podemos entender qué tipo de request estamos manejando usando un condicional
    print("Got info")
    return "Se recibió un POST"
  else:
    person1 = {
        "name" : "Bob"
    }
    print( "Se recibió un GET")
    return jsonify(person1)

@app.route("/error")
def handle_error():
    content = {
      "detalles": "Hubo un error en la solicitud"
    }
    resp = jsonify(content)
    resp.status_code = 400 # aquí cambiamos el código de estado a 400 (código muy común en caso de errores de solicitud)
    return resp

@app.route("/post_ex/<var>", methods={'POST', 'GET'})
def post_test(var):
    if request.method == 'GET':
        return var
    elif request.method == 'POST':
        data=request.form
        return "Updated"
    else:
        return "Try again"


@app.route("/generated")
def handle_json_report():
    filename = os.path.join(app.static_folder, 'out_json.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return data


app.run(host='0.0.0.0', port=4040, debug=True) #finalmente iniciamos el servidor en el localhost.