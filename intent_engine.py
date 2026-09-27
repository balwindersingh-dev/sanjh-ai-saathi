"""
Sanjh - offline intent + response engine.

This is the CURRENTLY WORKING piece of the prototype: a small, pure-Python,
keyword-based classifier that recognizes three intents and returns a
canned, human-sounding reply. It needs no external libraries and no
internet, so it runs identically on any machine, including inside this
sandbox.

Why rule-based right now, not a full LLM:
- A quantized on-device LLM (Phi-3-mini / Llama-3.2-1B) is the real Phase-2
  goal, but that needs actual Snapdragon hardware + Qualcomm AI Hub to run
  and evaluate properly.
- This module is the fallback/demo brain in the meantime, and it's also a
  sane safety net during a live demo if the real model pipeline isn't
  available on the judging machine.

generate_response() in app.py calls straight into this module.
"""

from dataclasses import dataclass


@dataclass
class Intent:
    name: str
    keywords: list


INTENTS = [
    Intent(
        name="scam_check",
        keywords=["fraud", "scam", "otp", "lottery", "prize", "bank account", "kyc", "block", "police case"],
    ),
    Intent(
        name="scheme_query",
        keywords=["pension", "scheme", "yojana", "form", "eligible", "eligibility", "sarkari", "government", "aadhar", "ration"],
    ),
    Intent(
        name="check_in",
        keywords=["hello", "hi", "kaise ho", "sat sri akal", "namaste", "kya haal", "good morning", "good evening"],
    ),
]

RESPONSES = {
    "scam_check": (
        "Ruko, ye message thoda suspicious lagta hai. Koi bhi bank ya sarkari department "
        "kabhi phone ya SMS pe OTP nahi maangta. Ise ignore kar do, aur agar shaq ho to "
        "apne family member se ek baar dikha dena."
    ),
    "scheme_query": (
        "Chalo dekhte hain. Pension aur welfare schemes ke liye apna Aadhar aur ration card "
        "ready rakho. Main tumhe eligibility ke basic sawal poochta hoon, phir bata dunga "
        "konsi scheme apply ho sakti hai."
    ),
    "check_in": (
        "Sat sri akal! Aaj din kaisa raha? Khana kha liya? Main yahin hoon, jab bhi baat "
        "karni ho bol dena."
    ),
    "fallback": (
        "Mujhe thoda aur simple shabdon mein bolo, main samajhne ki koshish karta hoon."
    ),
}


def classify_intent(text: str) -> str:
    """Return the best-matching intent name for a piece of transcribed text."""
    lowered = text.lower()
    for intent in INTENTS:
        if any(keyword in lowered for keyword in intent.keywords):
            return intent.name
    return "fallback"


def generate_response(user_text: str) -> str:
    """Public entry point used by app.py — classify then respond."""
    intent = classify_intent(user_text)
    return RESPONSES[intent]