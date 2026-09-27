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

`app.py` is a starting scaffold — the three pipeline stages are stubbed out
with clear TODOs for wiring in the actual Qualcomm AI Hub models.

## Roadmap

- [ ] Phase 1: ASR + LLM prototype validated for Punjabi/Hindi conversation
- [ ] Phase 2: offline government scheme eligibility lookup
- [ ] Phase 3: scam-pattern detector for calls/messages

## Status

Early prototype — built for the Snapdragon AI Lab Build & Present Challenge.

## Author

Balwinder Singh — B.Tech IT, Guru Nanak Dev Engineering College, Ludhiana