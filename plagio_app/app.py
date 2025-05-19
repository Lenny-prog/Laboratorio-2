from flask import Flask, render_template, request
from utils.analisisplagio import extraer_texto, comparar_por_parrafo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/informe", methods=["POST"])
def informe():
    archivo1 = request.files.get("archivo1")
    archivo2 = request.files.get("archivo2")

    if not archivo1 or not archivo2:
        return "Faltan archivos PDF", 400

    try:
        texto1 = extraer_texto(archivo1)
        texto2 = extraer_texto(archivo2)
    except Exception as e:
        return f"Error al procesar los archivos: {str(e)}", 500

    if not texto1.strip() or not texto2.strip():
        return "Uno de los archivos está vacío o no contiene texto legible", 400

    resultados = comparar_por_parrafo(texto1, texto2)

    alto = sum(1 for r in resultados if r["score"] > 75)
    bajo = len(resultados) - alto

    return render_template("informe.html", resultados=resultados, alto=alto, bajo=bajo)

if __name__ == "__main__":
    app.run(debug=True)
