"""
Sanjh - Your Offline AI Saathi
Prototype for the Snapdragon AI Lab Build & Present Challenge.

Pipeline: Speech In -> Understand & Respond -> Speech Out

CURRENT STATE (honest scope):
- generate_response() is REAL and working right now: a pure-Python,
  rule-based intent engine (see intent_engine.py) with no external
  dependencies. Covered by tests/test_intent_engine.py.
- listen_and_transcribe() and speak() are wired to real, commonly used
  offline libraries (faster-whisper, pyttsx3). They need `pip install -r
  requirements.txt` to run, and a working microphone/speaker on your
  machine -- they have NOT been executed in this dev environment, only
  written and reviewed against the libraries' documented APIs.
- Run with `python app.py --demo` to exercise the full pipeline via typed
  text instead of a microphone -- useful for testing, and as a safety net
  if audio hardware isn't available during a live demo.

ROADMAP (not yet built, needs real Snapdragon hardware to do properly):
- Replace intent_engine's rule-based logic with a quantized on-device LLM
  (Phi-3-mini / Llama-3.2-1B) run via Qualcomm AI Hub on the Snapdragon NPU.
- Replace faster-whisper's default model with the Qualcomm AI Hub-optimized
  Whisper build for on-device NPU inference.
- Add streaming transcription + voice-activity detection instead of
  record-then-transcribe.
"""

import argparse

from intent_engine import generate_response


def listen_and_transcribe() -> str:
    """Record a short clip from the mic and transcribe it (Punjabi/Hindi).

    Uses faster-whisper (CPU/GPU) as an offline ASR baseline. Swap the
    model for the Qualcomm AI Hub-optimized Whisper build once running on
    actual Snapdragon hardware, for NPU-accelerated inference.
    """
    import sounddevice as sd
    import numpy as np
    from faster_whisper import WhisperModel

    sample_rate = 16000
    duration_seconds = 5

    print(f"Listening for {duration_seconds}s...")
    recording = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=1, dtype="float32")
    sd.wait()
    audio = np.squeeze(recording)

    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio, language=None)
    text = " ".join(segment.text for segment in segments).strip()
    return text


def speak(text: str) -> None:
    """Convert text to speech and play it, fully offline via pyttsx3."""
    import pyttsx3

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def run_once() -> None:
    user_text = listen_and_transcribe()
    print(f"Heard: {user_text}")
    reply = generate_response(user_text)
    print(f"Sanjh: {reply}")
    speak(reply)


def run_demo() -> None:
    """Text-only loop -- exercises the real, working part of the pipeline
    (intent_engine) without needing a mic, speakers, or the ASR/TTS
    libraries installed. Good for quick testing and for judging demos
    where audio hardware isn't guaranteed to work.
    """
    print("Sanjh demo mode -- type a message (Hindi/Punjabi/English), or 'quit' to exit.\n")
    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in {"quit", "exit"}:
            break
        reply = generate_response(user_text)
        print(f"Sanjh: {reply}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sanjh - Your Offline AI Saathi")
    parser.add_argument("--demo", action="store_true", help="Run the text-only demo loop (no mic/speaker needed)")
    args = parser.parse_args()

    if args.demo:
        run_demo()
    else:
        run_once()