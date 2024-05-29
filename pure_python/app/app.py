from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    pokemons = []
    return render_template("search.html", **{"pokemons": pokemons})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
