# Sanjh — Your Offline AI Saathi

An offline, voice-first AI companion built for Snapdragon-powered PCs, designed
for elderly users in Punjab who face isolation, inaccessible government
schemes, and financial scams.

## Why offline / on-device

Sanjh runs entirely on the Snapdragon NPU — no internet connection and no
cloud calls at any point. That matters here for three reasons:

- Works in low-connectivity rural areas
- Sensitive data (health, financial, personal conversations) never leaves the device
- Consistent, low-latency response regardless of network quality

## Pipeline

```
Speech In  ->  Understand & Respond  ->  Speech Out
(ASR)          (small local LLM)         (TTS)
```

- **ASR:** quantized Whisper-tiny (Qualcomm AI Hub build)
- **LLM:** quantized Phi-3-mini / Llama-3.2-1B, prompted for Punjabi–Hindi conversation
- **TTS:** on-device text-to-speech

## Current prototype scope (honest status)

- **Working right now:** `intent_engine.py` — a pure-Python, rule-based
  intent classifier + response generator, no external dependencies. Covered
  by `tests/test_intent_engine.py`. Run `python app.py --demo` for a
  text-only interactive demo of the full conversation loop with no mic,
  speakers, or extra installs needed.
- **Written, not yet hardware-tested:** `listen_and_transcribe()` (faster-whisper)
  and `speak()` (pyttsx3) in `app.py`. They need `pip install -r requirements.txt`
  and a real mic/speaker to run — not yet verified on physical hardware.
- **Not yet built (Phase 2, needs real Snapdragon hardware):** replacing the
  rule-based intent engine with a quantized on-device LLM (Phi-3-mini /
  Llama-3.2-1B) run via Qualcomm AI Hub on the Snapdragon NPU, plus
  streaming transcription and voice-activity detection.

## Roadmap

- [ ] Phase 1: ASR + LLM prototype validated for Punjabi/Hindi conversation
- [ ] Phase 2: offline government scheme eligibility lookup
- [ ] Phase 3: scam-pattern detector for calls/messages

## Status

Early prototype — built for the Snapdragon AI Lab Build & Present Challenge.

## Author

Balwinder Singh — B.Tech IT, Guru Nanak Dev Engineering College, Ludhiana