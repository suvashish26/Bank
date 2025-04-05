from django.test import TestCase, Client
from django.urls import reverse

class WAFTests(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_xss_blocked(self):
        response = self.client.get("/", {"param": "<script>alert(1)</script>"})
        self.assertEqual(response.status_code, 403)
        
    def test_sqli_blocked(self):
        response = self.client.get("/search?q=SELECT * FROM users")
        self.assertEqual(response.status_code, 403)
        
    def test_path_traversal_blocked(self):
        response = self.client.get("/download?file=../../etc/passwd")
        self.assertEqual(response.status_code, 403)
        
    def test_clean_request_allowed(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)