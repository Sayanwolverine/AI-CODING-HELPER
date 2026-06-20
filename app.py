from flask import Flask, request, jsonify
from flask_cors import CORS
from fixer import fix_code

app = Flask(__name__)
CORS(app)

@app.route("/fix", methods=["POST"])
def fix():
    data = request.get_json()

    code = data.get("code")
    language = data.get("language")

    result = fix_code(code, language)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)