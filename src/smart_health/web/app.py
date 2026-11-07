from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/find-hospital", methods=["GET", "POST"])
def find_hospital():
    result = None
    if request.method == "POST":
        pass  # TODO: call smart_health.ai.hospital_search.recommend_hospital
    return render_template("find_hospital.html", result=result)


@app.route("/blood-donation", methods=["GET", "POST"])
def blood_donation():
    donors = None
    if request.method == "POST":
        pass  # TODO: call smart_health.ai.donor_search.rank_donors
    return render_template("blood_donation.html", donors=donors)


@app.route("/methodology")
def methodology():
    return render_template("methodology.html")


if __name__ == "__main__":
    app.run(debug=True)
