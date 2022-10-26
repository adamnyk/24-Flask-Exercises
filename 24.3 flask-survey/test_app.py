from app import app, session
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class SurveyTestCase(TestCase):
    def test_start_page(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            # Testing successful get request
            self.assertEqual(res.status_code, 200)

            # Testing root directory contains start button
            self.assertIn("<button>Start the survey</button>", html)

    def test_start_redirect(self):
        with app.test_client() as client:
            res = client.post("/reset_session")

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "questions/0")

# not working right now -POST TEST-
    def test_submit_answer(self):
        with app.test_client() as client:
            res = client.post("/answer", data={"answer", "Yes"})
            responses = session["responses"]

            self.assertEqual(res.status_code, 200)
            self.assertEqual(responses[0], "Yes")
