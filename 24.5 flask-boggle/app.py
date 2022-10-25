from boggle import Boggle
from flask import Flask, request, render_template, redirect, session, jsonify

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
    '''Check if word is in dictionary and on board.'''
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)
    

    return response
    # return jsonify({"result": response})
