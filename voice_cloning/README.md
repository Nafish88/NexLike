[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nafish88/NexLike/blob/main/voice_cloning/voice_clone_colab.ipynb)

# Hindi Voice Cloning TTS (XTTS v2) for Google Colab

A beginner-friendly, professional Google Colab notebook for **Hindi voice cloning** using **Coqui XTTS v2**.

## Included Files
- `voice_clone_colab.ipynb` — ready-to-run Colab notebook
- `requirements.txt` — minimal Python dependencies (`TTS`, `soundfile`)

## What the notebook does
1. Installs PyTorch CUDA 11.8 wheels (T4-friendly) and minimal dependencies
2. Detects GPU automatically and loads `tts_models/multilingual/multi-dataset/xtts_v2`
3. Provides a simple UI with:
   - `.wav` voice upload
   - Hindi text input
   - Generate button
   - Progress/status messages
   - Audio playback
   - Download button for `output.wav`

## Quick Start (Colab)
1. Open the notebook in Google Colab.
2. Enable GPU: **Runtime → Change runtime type → Hardware accelerator → GPU**.
3. Run all cells from top to bottom.
4. Upload a clean `.wav` sample (5–20 seconds recommended).
5. Enter Hindi text and click **Generate output.wav**.

Default language is set to `hi`.
