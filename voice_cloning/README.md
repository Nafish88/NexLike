[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nafish88/NexLike/blob/main/voice_cloning/voice_clone_colab.ipynb)

# Voice Cloning Setup (Hindi-First, XTTS v2)

This folder now supports **two flows**:
1. **Google Colab notebook** (quickest way)
2. **Local Gradio app** (professional workflow with upload/text/play UI)

---

## 1) Colab Flow (existing)
Use `voice_clone_colab.ipynb` for one-click cloud usage.

## 2) Local Python 3.12 Flow (new)
Use `app.py` for a complete mini studio:
- Voice upload (or record with mic)
- Story text box
- One-click generation
- Output playback
- Auto language detect (Hindi/Urdu/English fallback)
- Basic professional audio quality checks (duration, clipping, low volume, low sample-rate)

---

## Recommended model
For your requirement (Hindi-focused, cloning + natural TTS), best practical option is:

- **Coqui XTTS v2** (`tts_models/multilingual/multi-dataset/xtts_v2`)

Why:
- strong multilingual support
- stable one-shot cloning
- works with short clean reference clips
- good community support and docs

---

## Python 3.12 Setup

### Step 1: Create environment
```bash
cd voice_cloning
python3.12 -m venv .venv
source .venv/bin/activate
```

### Step 2: Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Run app
```bash
python app.py
```
Open browser at `http://localhost:7860`.

---

## Best-practice input guide
- Use **clean mono voice** sample
- Duration: **6–20 seconds** ideal
- Background noise minimal
- Normal speaking pace
- Avoid music + heavy reverb

---

## Feature checklist vs your plan
- ✅ Voice upload
- ✅ Story text box
- ✅ Generate button
- ✅ Play output voice
- ✅ Auto language detect function
- ✅ Professional quality warning checks
- ✅ Python 3.12 friendly dependency set

---

## Notes
- First run may take time because model weights download.
- If GPU is available, generation speed improves significantly.
- Long scripts should be generated in chunks for best stability.
