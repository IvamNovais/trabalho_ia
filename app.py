from flask import Flask, render_template,request
import clasificadores
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    dados = request.form.values()
    dados = dados.gi_frame.f_locals.get("self")
    dadosf=[]
    for coisa in dados:
        dadosf.append(float(dados.get(coisa)))
    saida = clasificadores.getPreticao(dadosf)
    saida = "{:.2f}".format(saida).replace(".",",")
    return render_template("index.html", prediction_text=saida)