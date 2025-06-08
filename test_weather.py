import unittest
from unittest.mock import patch, MagicMock
import weather


dummy_response = {
    "current_weather": {
        "temperature": 20.0,
        "windspeed": 5.0,
        "time": "2021-01-01T00:00"
    }
}


class WeatherTestCase(unittest.TestCase):
    @patch('weather.requests.get')
    def test_fetch_weather(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = dummy_response
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        data = weather.fetch_weather(0, 0)
        self.assertEqual(data, dummy_response)
        mock_get.assert_called_once()

    def test_format_weather(self):
        output = weather.format_weather(dummy_response)
        self.assertIn("Temperature", output)
        self.assertIn("Wind Speed", output)
        self.assertIn("Time", output)


if __name__ == '__main__':
    unittest.main()

