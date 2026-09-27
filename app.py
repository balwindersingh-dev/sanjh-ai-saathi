"""
Sanjh - Your Offline AI Saathi
Prototype scaffold for the Snapdragon AI Lab Build & Present Challenge.

Pipeline: Speech In -> Understand & Respond -> Speech Out
All three stages are meant to run fully on-device via the Snapdragon NPU,
using models from Qualcomm AI Hub (https://aihub.qualcomm.com).

This file is a starting skeleton, not a finished product -- each stage
below is a stub with a TODO for the real on-device model call.
"""


def listen_and_transcribe() -> str:
    """Capture audio from the mic and transcribe it (Punjabi/Hindi).

    TODO: replace with a quantized Whisper-tiny model run on the
    Snapdragon NPU via Qualcomm AI Hub.
    """
    raise NotImplementedError("Wire up on-device ASR here")


def generate_response(user_text: str) -> str:
    """Generate a spoken-style reply using a small local LLM.

    TODO: replace with a quantized Phi-3-mini / Llama-3.2-1B model,
    prompted to respond warmly in Punjabi/Hindi, and to recognize
    three intents: casual check-in, government scheme questions,
    and potential scam messages the user wants checked.
    """
    raise NotImplementedError("Wire up on-device LLM here")


def speak(text: str) -> None:
    """Convert text back to speech and play it.

    TODO: replace with an on-device TTS model in Punjabi/Hindi.
    """
    raise NotImplementedError("Wire up on-device TTS here")


def run_once() -> None:
    user_text = listen_and_transcribe()
    reply = generate_response(user_text)
    speak(reply)


if __name__ == "__main__":
    run_once()