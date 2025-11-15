from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

#Inicializacion con firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
coleccion = db.collection("registros")

#Rutas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar", methods=["POST"])
def registrar():

    # Extraemos los datos enviados desde el form HTML
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    edad = request.form.get("edad")

    coleccion.add({
        "nombre": nombre,
        "correo": correo,
        "edad": edad
    })

    return render_template("succes.html")



# Ejecutar localmente
if __name__ == "__main__":
    app.run(debug=True)
