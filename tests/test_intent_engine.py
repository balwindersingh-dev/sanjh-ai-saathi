import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from intent_engine import classify_intent, generate_response


class TestIntentEngine(unittest.TestCase):
    def test_scam_intent(self):
        self.assertEqual(classify_intent("mujhe ek OTP wala fraud call aaya"), "scam_check")

    def test_scheme_intent(self):
        self.assertEqual(classify_intent("pension yojana ke liye kya karna hai"), "scheme_query")

    def test_check_in_intent(self):
        self.assertEqual(classify_intent("sat sri akal, kaise ho"), "check_in")

    def test_fallback_intent(self):
        self.assertEqual(classify_intent("random unrelated sentence"), "fallback")

    def test_generate_response_returns_nonempty_string(self):
        reply = generate_response("hello")
        self.assertIsInstance(reply, str)
        self.assertGreater(len(reply), 0)

    def test_generate_response_matches_intent(self):
        from intent_engine import RESPONSES
        self.assertEqual(generate_response("scam otp fraud"), RESPONSES["scam_check"])


if __name__ == "__main__":
    unittest.main()