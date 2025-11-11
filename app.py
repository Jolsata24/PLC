from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variables simuladas
entradas = {"start": False, "stop": False}
salidas = {"motor": False}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    entradas["start"] = data.get("start", False)
    entradas["stop"] = data.get("stop", False)

    # --- Lógica tipo PLC ---
    if entradas["start"] and not entradas["stop"]:
        salidas["motor"] = True
    if entradas["stop"]:
        salidas["motor"] = False

    return jsonify(salidas)

if __name__ == "__main__":
    app.run(debug=True)
