from flask import Flask, render_template, request
from firebase_admin import db, credentials, initialize_app

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    i = False
    if request.form.get("action") == "Senden":
        data = request.form.get("Time")
        ref = db.reference("/")
        ref.update({"active": i})
        ref.update({"Time": int(data)})

    return render_template("index.html")


if __name__ == "__main__":
    cred_obj = credentials.Certificate(
        "esp32-uvhaerter-firebase-adminsdk-ao16c-90b83e6e37.json"
    )
    default_app = initialize_app(
        cred_obj,
        {
            "databaseURL": "https://esp32-uvhaerter-default-rtdb.europe-west1.firebasedatabase.app/"
        },
    )
    app.run(debug=True)
