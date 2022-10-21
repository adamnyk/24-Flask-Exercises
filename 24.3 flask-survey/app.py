from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


debug = DebugToolbarExtension(app)


@app.route("/")
def show_homepage():
    """Shows homepage"""
    return render_template("home.html", survey=survey)


@app.route("/reset_session", methods=["POST"])
def reset_session():
    """Post request to create and empty Flask session list of responses."""
    session["responses"] = []

    return redirect("questions/0")


@app.route("/questions/<int:ques_id>")
def show_question(ques_id):
    """Show question with given question id."""

    if len(session["responses"]) == len(survey.questions):
        flash("Submission already recieved.", "success")
        return redirect("/thank_you")

    if ques_id != len(session["responses"]):
        flash("Redirecting you to the next question.", "error")
        return redirect(f"/questions/{len(session['responses'])}")

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

    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses

    if len(responses) == len(survey.questions):
        return redirect("/thank_you")

    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/thank_you")
def show_thank_you():
    """Show thank-you page."""

    return render_template("thank_you.html")
