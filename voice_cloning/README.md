[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nafish88/NexLike/blob/main/voice_cloning/voice_clone_colab.ipynb)

# Voice Cloning (Coqui XTTS v2) for Google Colab

This folder contains a beginner-friendly Google Colab notebook for cloning a voice with **Coqui TTS (XTTS v2)** and generating `output.wav`.

## Files
- `voice_clone_colab.ipynb` — main Colab notebook
- `requirements.txt` — Python dependencies used by the notebook

## How to run in Google Colab
1. Open `voice_clone_colab.ipynb` in Google Colab.
2. In Colab, enable GPU:
   - **Runtime → Change runtime type → Hardware accelerator → GPU**
3. Run all cells from top to bottom.
4. Upload a clean voice sample (recommended: `.wav`, 5–20 seconds).
5. Edit `text_to_speak` and `language_code`.
6. Run the generation cell.
7. The notebook saves cloned audio as **`output.wav`** and offers download.

## Notes for stable free Colab usage
- The notebook checks that GPU is enabled before generating speech.
- The first model load can take a few minutes because XTTS v2 weights are downloaded.
- Keep input text short-to-medium during early tests for faster generation.
- Use clear voice samples with minimal background noise for better results.

## Dependency notes (Colab Latest / Python 3.12)
- The notebook installs **PyTorch CUDA 11.8** wheels (`cu118`) for good T4 compatibility.
- Dependency installation avoids strict `numpy` pinning to reduce resolver conflicts on Colab Latest.
- XTTS v2 dependencies are installed with a simple, beginner-friendly setup flow in the notebook.

## If you want this setup in a NEW GitHub repo (not NexLike)

If this was added in the wrong repo by mistake, you can safely move it.

### What to copy to the new repo
- `voice_cloning/voice_clone_colab.ipynb`
- `voice_cloning/requirements.txt`
- `voice_cloning/README.md` (optional, for instructions)

### Update the Colab badge link in the new repo
The current badge in this file points to the notebook inside **NexLike**. In a new repo, change owner/repo/path in the badge URL to your target repo so it opens directly from GitHub to Colab.

Badge format:

```md
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<OWNER>/<REPO>/blob/<BRANCH>/<NOTEBOOK_PATH>)
```

Example:

```md
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/myname/hindi-voice-clone/blob/main/voice_clone_colab.ipynb)
```

### Will it run on Colab?
Yes—this notebook is written for Colab flow (GPU check + install + upload + inference). Make sure GPU is enabled and run cells top-to-bottom.


---

## Hindi Voice Cloning (Python 3.12) — Recommended Professional Setup Plan

Aapka plan **strong** hai, aur is repo ke XTTS v2 base par easily build ho sakta hai.

### Suggested core stack
- **Model**: Coqui **XTTS v2** (best practical balance of quality + multilingual support, including Hindi).
- **Backend API**: **FastAPI** (upload, inference, playback endpoint).
- **Frontend UI**: **Gradio** (quick launch) ya Streamlit (agar app-like UX chahiye).
- **Audio tools**: `ffmpeg`, `pydub`, `librosa`, `soundfile`.

### Features (as requested)
1. **Voice upload**
   - Accepted formats: wav/mp3/m4a
   - Auto-convert to 24k mono wav
   - Duration + SNR checks before inference

2. **Text box for story/script**
   - Hindi text input
   - Optional auto-splitting for long paragraphs
   - Punctuation cleanup for better prosody

3. **Generate + Play button**
   - "Generate" button triggers TTS
   - Inline audio player for immediate playback
   - Download output wav/mp3

4. **Professional automatic detection functions**
   - Silence detection
   - Background-noise estimate
   - Clipping detection
   - Min/max duration guardrails
   - Language-script heuristics (Devanagari presence)

### Python 3.12 compatibility notes
- XTTS pipeline Python 3.12 par possible hai, lekin dependency versions carefully lock karne honge.
- Recommend pinning torch + torchaudio + coqui-tts compatible versions and testing on GPU first.
- Production ke liye Docker image with fixed versions best rahega.

### High-level workflow
1. Upload reference voice.
2. Auto quality checks + preprocessing.
3. Hindi text normalize/split.
4. XTTS inference.
5. Output post-process (normalize, optional denoise).
6. Play + download.

### Extra must-have items
- Request queue (concurrent users ke liye)
- Error logs + retries
- GPU/CPU fallback behavior
- Rate limit + file size limit
- Consent + voice-cloning policy acknowledgement

### Verdict on your plan
**Plan bahut accha hai**. Agar chaho to next step me main iske liye ready-to-run:
- `app.py` (Gradio UI)
- `backend.py` (FastAPI endpoints)
- `requirements-312.txt`
- sample `.env` + run instructions
bana sakta hoon.
