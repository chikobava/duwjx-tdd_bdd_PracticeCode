"""
Test Cases for Counter Web Service
"""
from unittest import TestCase
import status
from counter import app


class CounterTest(TestCase):
    """Test Cases for Counter Web Service"""

    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """It should create a counter"""
        result = self.client.post("/counters/foo")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertIn("foo", data)
        self.assertEqual(data["foo"], 0)

    def test_duplicate_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_counter(self):
        """It should update the provided counter"""
        result = self.client.post("/counters/boom")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertIn("boom", data)
        self.assertEqual(data["boom"], 0)
        result = self.client.put("/counters/boom")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertIn("boom", data)
        self.assertEqual(data["boom"], 1)
        result = self.client.put("/counters/boom2")
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

    def test_read_counter(self):
        """It should return the value of the provided counter"""
        result = self.client.post("/counters/new")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertEqual(data["new"], 0)
        result = self.client.put("/counters/new")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["new"], 1)
        result = self.client.get("/counters/new")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["new"], 1)
        result = self.client.get("/counters/super")
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_counter(self):
        """It should delete the provided counter"""
        result = self.client.post("/counters/delete")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertEqual(data["delete"], 0)

        result = self.client.get("/counters/delete")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["delete"], 0)

        result = self.client.delete("/counters/delete")
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

        result = self.client.get("/counters/delete")
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
