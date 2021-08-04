import json
from  app import app
from tests.BaseCase import BaseCase


class SignUpTest(BaseCase):
    def test_successful_signup(self):
        payload = json.dumps({
            "email": "awedaoluwanifemi@gmail.com",
            "password": "Adenifesim1"
        })

        response = self.app.post("/api/auth/signup", headers={"content-type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json["id"]))
        self.assertEqual(200, response.status_code)