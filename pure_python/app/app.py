from flask import Flask, render_template, request
from opensearch_integration import OpenSearchConnector
from opensearchpy.helpers.query import Q

app = Flask(__name__)


@app.route("/")
def pokemons():
    search = request.args.get("search", "")
    connector = OpenSearchConnector()
    query = Q(
        "bool",
        should=[
            Q("query_string", query=f"*{search}*", fields=["name"]),
            Q(
                "nested",
                path="types",
                query=Q("query_string", query=f"*{search}*", fields=["types.name"]),
            ),
            Q(
                "nested",
                path="moves",
                query=Q("query_string", query=f"*{search}*", fields=["moves.name"]),
            ),
            Q(
                "nested",
                path="abilities",
                query=Q("query_string", query=f"*{search}*", fields=["abilities.name"]),
            ),
        ],
        minimum_should_match=1,
    )

    pokemons = connector.search("pokemons", query)
    return render_template("search.html", **{"pokemons": pokemons, "search": search})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
