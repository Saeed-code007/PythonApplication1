from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load models
coord_model = joblib.load("coord_system_model.pkl")


@app.route("/", methods=["GET", "POST"])
def interface():
    prediction = None
    confidence_scores = {}
    show_enter_again = False

    # Check if this is a return from results page
    if request.args.get('enter_again') == 'true':
        show_enter_again = True

    if request.method == "POST":
        question = request.form["question"]
        prediction = coord_model.predict([question])[0]
        probs = coord_model.predict_proba([question])[0]
        confidence_scores = dict(zip(coord_model.classes_, probs))

    return render_template("interface.html",
                           prediction=prediction,
                           confidence_scores=confidence_scores,
                           show_enter_again=show_enter_again)
