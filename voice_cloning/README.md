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
