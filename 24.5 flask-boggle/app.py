from boggle import Boggle
from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"

boggle_game = Boggle()


@app.route("/")
def board():
    """Show boggle board."""

    board = boggle_game.make_board()
    session["board"] = board

    return render_template("index.html")


@app.route("/check_word")
def check_guess():
    word = request.args('word')
    result = boggle_game.check_valid_word(session['board'], word)
    return result
