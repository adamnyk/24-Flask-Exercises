from boggle import Boggle
from flask import Flask, request, render_template, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"

debug = DebugToolbarExtension(app)


boggle_game = Boggle()


@app.route("/")
def home():
    """Show boggle board."""

    board = boggle_game.make_board()
    session["board"] = board

    return render_template("index.html")


@app.route("/check_word")
def check_guess():
    """Check if word is in dictionary and on board. Returns JSON"""
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    # return response
    
    # doesnt need to be sent as Json, could be just a string with no k:v pair. See above commented out code. 
    return jsonify({"result": response})


@app.route("/post_score", methods=["POST"])
def post_score():

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session["nplays"] = nplays + 1
    session["highscore"] = max(score, highscore)


    # import pdb
    # pdb.set_trace()

    return jsonify(brokeRecord=score > highscore)
