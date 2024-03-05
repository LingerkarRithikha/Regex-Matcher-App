from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        test_string = request.form["test_string"]
        regex_pattern = request.form["regex_pattern"]
        matches = re.findall(regex_pattern, test_string)
        return render_template("index.html", matches=matches)
    return render_template("index.html", matches=None)

@app.route("/email", methods=["POST"])
def mail():
    return render_template("email_valid.html", valid=None)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})

    return render_template("email_valid.html")

if __name__ == "__main__":
    app.run(debug=True)
