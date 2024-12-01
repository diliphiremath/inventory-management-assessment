from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class SaveInventoryTest(TestCase):
    def setUp(self):
        # Initialize the APIClient for making requests
        self.client = APIClient()
        self.url = "/inventory/save/" 

    def test_save_inventory_success(self):
        """Test creating a inventory with valid data"""
        data = {
    "batch_id": "71a8a97591894dda9ea1a372c89b7987",
    "objects": [
        {
        "object_id": "d6f983a8905e48f29ad480d3f5969b52",
        "data": [
            {
            "key": "type",
            "value": "shoe"
            },
            {
            "key": "color",
            "value": "purple"
            }
        ]
        },
        {
        "object_id": "1125528d300d4538a33069a9456df4e8",
        "data": [
            {
            "key": "fizz",
            "value": "buzz"
            }
        ]
        }
    ]
    }
        
        response = self.client.post(self.url, data, format='json')

        # Check the response status code is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["batch_id"], data["batch_id"])
        self.assertEqual(len(response.data["items"]), len(data["objects"]))

    def test_save_inventory_invalid_data(self):
        """Test creating a batch with invalid data (e.g., missing batch_id)"""
        # Prepare invalid data (missing "batch_id")
        invalid_data = {
            "objects": [
                {
                    "object_id": "d6f983a8905e48f29ad480d3f5969b52",
                    "data": [
                        {"key": "color", "value": "purple"}
                    ]
                }
            ]
        }

        response = self.client.post(self.url, invalid_data, format='json')

        # Check the response status code is 400 (bad request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Ensure that the error message contains information about the missing "batch_id"
        self.assertIn('batch_id', response.data)
