from flask import Flask, render_template, request
from firebase_admin import db, credentials, initialize_app

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = ""
    if request.form.get("action") == "Starten":
        data = request.form.get("Time")
        if str.isdigit(data) and int(data) > 0 and int(data) <= 30:
            ref = db.reference("/")
            ref.update({"active": True})
            ref.update({"Time": data})
        else:
           data = "keine gültige Eingabe!"
    
    return render_template("index.html", data=data)

@app.route("/cameraView")
def cameraView():
    return render_template("cameraView.html")


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
