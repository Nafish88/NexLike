[![Open In Colab (OpenVoice V2)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nafish88/NexLike/blob/main/voice_cloning/voice_clone_openvoice.ipynb)

# Hindi Voice Cloning TTS for Google Colab

This folder contains beginner-friendly Colab notebooks for Hindi voice cloning.

## Included files
- `voice_clone_openvoice.ipynb` — OpenVoice V2 (MIT licensed) Hindi voice-cloning notebook
- `voice_clone_colab.ipynb` — XTTS v2 Hindi voice-cloning notebook
- `requirements.txt` — helper Python packages used in the OpenVoice notebook

## OpenVoice V2 notebook features
The `voice_clone_openvoice.ipynb` notebook:
1. Installs PyTorch CUDA 11.8 wheels (`torch`, `torchvision`, `torchaudio`) in Colab
2. Clones the official OpenVoice GitHub repo
3. Installs repository dependencies from `OpenVoice/requirements.txt`
4. Downloads OpenVoice V2 checkpoints from public sources (Hugging Face with S3 fallback)
5. Detects GPU automatically and loads models
6. Provides an `ipywidgets` UI with:
   - `.wav` upload
   - Hindi text box
   - Generate button
   - Status messages
   - Audio playback
   - Download link for `output.wav`

## Quick start (Google Colab)
1. Open `voice_clone_openvoice.ipynb` in Colab.
2. Set **Runtime → Change runtime type → GPU**.
3. Run cells top-to-bottom.
4. Upload a clean `.wav` sample (5–20 seconds recommended).
5. Enter Hindi text and click **Generate output.wav**.

## Tips for better cloning quality
- Use a clean, noise-free reference clip.
- Keep reference voice in one speaker and one language/accent style.
- Use short-to-medium sentences for first tests.
