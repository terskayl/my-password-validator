import flask


# TODO: change this to your academic email
AUTHOR = "aajiang@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")


    # Length >= 8, 1 upper case, 1 digit, 1 special character
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "too short"}), 501 
    if len([c for c in list(pw) if c in "!@#$%^&*"]) < 1:
        return flask.jsonify({"valid": False, "reason": "no special characters"}), 501 
    if len([c for c in list(pw) if c.isupper()]) < 1:
        return flask.jsonify({"valid": False, "reason": "no uppercase letters"}), 501 
    if len([c for c in list(pw) if c.isdigit()]) < 1:
        return flask.jsonify({"valid": False, "reason": "no digits"}), 501 


    return flask.jsonify({"valid": True, "reason": "Valid Password"}), 501
