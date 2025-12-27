from flask import Flask, render_template, request, jsonify
from service import evaluate_decision

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/qdt", methods=["POST"])
def qdt_api():
    try:
        data = request.json
        result = evaluate_decision(data)
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
