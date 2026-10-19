
import unittest
import json
from app import AppHandler
from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), AppHandler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_home_endpoint(self):
        with urlopen(self.base_url) as response:
            data = json.loads(response.read().decode("utf-8"))
        self.assertEqual(data["status"], "running")
        self.assertIn("Welcome", data["message"])

    def test_health_endpoint(self):
        with urlopen(f"{self.base_url}/health") as response:
            data = json.loads(response.read().decode("utf-8"))
        self.assertEqual(data["status"], "healthy")


if __name__ == "__main__":
    unittest.main()
