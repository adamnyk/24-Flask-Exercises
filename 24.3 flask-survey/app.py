from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


debug = DebugToolbarExtension(app)

responses = []


@app.route("/")
def show_homepage():
    """Shows homepage"""
    return render_template("home.html", survey=survey)


@app.route("/questions/<int:ques_id>")
def show_question(ques_id):
    """Show question with given question id."""

    if len(responses) == len(survey.questions):
        flash("Submission already recieved.")
        return redirect("/thank_you")

    if ques_id != len(responses):
        flash("Redirecting you to the next question.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[ques_id]

    return render_template(
        "questions.html",
        question=question,
        ques_id=ques_id,
    )


@app.route("/answer", methods=["POST"])
def post_answer():
    """Post request to submit answer to questions."""

    answer = request.form["answer"]
    responses.append(answer)

    if len(responses) == len(survey.questions):
        return redirect("/thank_you")

    if len(responses) != len(survey.questions):
        return redirect(f"/questions/{len(responses)}")


@app.route("/thank_you")
def show_thank_you():
    """Show thank-you page."""

    return render_template("thank_you.html", responses=responses)
