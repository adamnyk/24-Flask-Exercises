from unittest import TestCase
from app import app
from flask import session, jsonify
from boggle import Boggle

# Do these need to be an a setup function or are they ok here?
app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_home(self):
        with app.test_client() as client:

            response = client.get("/")
            html = response.get_data(as_text=True)

            self.assertIn("board", session)
            self.assertIsNone(session.get("highscore"))
            self.assertIsNone(session.get("nplays"))
            self.assertIn("Highscore:", html)
            self.assertIn("Score:", html)
            self.assertIn("Time remaining: 60", html)

    def test_valid_word(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess["board"] = [
                    ["A", "P", "P", "L", "E"],
                    ["A", "P", "P", "L", "E"],
                    ["A", "P", "P", "L", "E"],
                    ["A", "P", "P", "L", "E"],
                    ["A", "P", "P", "L", "E"],
                ]

            response = client.get("/check_word?word=apple")
            self.assertEqual(response.json["result"], "ok")

    def test_invalid_word(self):
        with app.test_client() as client:
            # why this line? - to get session data from setting the board in the last test?
            client.get("/")
            response = client.get("/check_word?word=pear")
            self.assertEqual(response.json["result"], "not-on-board")

    def test_not_english_word(self):
        with app.test_client() as client:
            # why this line?
            client.get("/")
            response = client.get("/check_word?word=zzzzzzzz")
            self.assertEqual(response.json["result"], "not-word")

    def test_post_score(self):
        with app.test_client() as client:

            # client.get("/")
            # self.assertIsNone(session.get("highscore"))
            response = client.post("/post_score", data={"score": 5})

            # self.assertEqual(session.get("nplays"), 1)
            # self.assertEqual(session.get("highscore"), 5)
            # self.assertTrue(response.json["brokeRecord"], True)
            self.assertEqual(response.status_code, 200)
