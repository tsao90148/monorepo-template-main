import unittest
import json

# Import the classes and functions from the code you want to test
from jsonapi import BetterEncoder, BetterDecoder, dumps, loads

class TestBetterEncoder(unittest.TestCase):
    def test_encode_complex(self):
        encoder = BetterEncoder()
        complex_number = complex(3.0, 4.0)
        encoded = encoder.encode(complex_number)
        expected = {"real": 3.0, "imag": 4.0, "__extended_json_type__": "complex"}
        self.assertEqual(encoded, json.dumps(expected))

    def test_encode_range(self):
        encoder = BetterEncoder()
        r = range(1, 10, 2)
        encoded = encoder.encode(r)
        expected = {"start": 1, "stop": 10, "step": 2, "__extended_json_type__": "range"}
        self.assertEqual(encoded, json.dumps(expected))

class TestBetterDecoder(unittest.TestCase):
    def test_decode_complex(self):
        decoder = BetterDecoder()
        encoded = '{"real": 3.0, "imag": 4.0, "__extended_json_type__": "complex"}'
        decoded = decoder.decode(encoded)
        expected = complex(3.0, 4.0)
        self.assertEqual(decoded, expected)

    def test_decode_range(self):
        decoder = BetterDecoder()
        encoded = '{"start": 1, "stop": 10, "step": 2, "__extended_json_type__": "range"}'
        decoded = decoder.decode(encoded)
        expected = range(1, 10, 2)
        self.assertEqual(list(decoded), list(expected))

class TestDumpsAndLoads(unittest.TestCase):
    def test_dumps_and_loads(self):
        data = {
            "complex": complex(3.0, 4.0),
            "range": range(1, 10, 2)
        }
        dumped = dumps(data)
        loaded = loads(dumped)
        self.assertEqual(data, loaded)

if __name__ == '__main__':
    unittest.main()
