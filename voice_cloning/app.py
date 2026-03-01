"""Gradio app for Hindi-first voice cloning with Coqui XTTS v2.

Features:
- Upload reference voice
- Enter story text
- Automatic language detection (Hindi/Urdu/English fallback)
- Basic professional pre-checks on uploaded voice
- Generate and play cloned output
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Tuple

import gradio as gr
import numpy as np
import soundfile as sf
from langdetect import DetectorFactory, LangDetectException, detect
from pydub import AudioSegment
from TTS.api import TTS

DetectorFactory.seed = 0

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
MAX_TEXT_CHARS = 1200
MIN_AUDIO_SEC = 4.0
MAX_AUDIO_SEC = 45.0
TARGET_SR = 24000

# Lazy cache for model instance
_TTS_MODEL: TTS | None = None


LANG_MAP = {
    "hi": "hi",
    "ur": "ur",
    "en": "en",
}


def load_model() -> TTS:
    global _TTS_MODEL
    if _TTS_MODEL is None:
        _TTS_MODEL = TTS(MODEL_NAME)
    return _TTS_MODEL


def detect_language(text: str) -> Tuple[str, str]:
    """Return (xtts_lang_code, human_message)."""
    text = text.strip()
    if not text:
        return "hi", "Defaulted language: Hindi (empty text)."

    try:
        detected = detect(text)
    except LangDetectException:
        return "hi", "Could not detect language confidently, defaulting to Hindi."

    lang = LANG_MAP.get(detected, "hi")
    if detected in LANG_MAP:
        return lang, f"Auto-detected language: {detected}."
    return lang, f"Detected '{detected}', not directly supported in this setup; using Hindi for better stability."


def analyze_reference_audio(audio_path: str) -> str:
    """Basic quality checks for more professional output consistency."""
    audio = AudioSegment.from_file(audio_path)
    duration = len(audio) / 1000.0

    warnings: list[str] = []
    if duration < MIN_AUDIO_SEC:
        warnings.append(f"Voice sample is too short ({duration:.1f}s). Recommended: 6–20s.")
    if duration > MAX_AUDIO_SEC:
        warnings.append(f"Voice sample is long ({duration:.1f}s). Recommended: under 45s for faster + stable cloning.")

    waveform, sr = sf.read(audio_path)
    if waveform.ndim > 1:
        waveform = waveform.mean(axis=1)

    peak = float(np.max(np.abs(waveform))) if waveform.size else 0.0
    rms = float(np.sqrt(np.mean(np.square(waveform)))) if waveform.size else 0.0

    if peak > 0.99:
        warnings.append("Audio appears clipped. Re-record with lower input gain.")
    if rms < 0.01:
        warnings.append("Audio volume is very low. Increase mic/input level.")
    if sr < 16000:
        warnings.append(f"Sample rate is low ({sr} Hz). Use 22.05kHz or higher if possible.")

    if not warnings:
        return "Reference voice check: good quality ✅"
    return "Reference voice check warnings:\n- " + "\n- ".join(warnings)


def clone_voice(reference_audio: str, text: str):
    if not reference_audio:
        raise gr.Error("Please upload a voice sample first.")

    text = (text or "").strip()
    if not text:
        raise gr.Error("Please enter some text/story before generating.")
    if len(text) > MAX_TEXT_CHARS:
        raise gr.Error(f"Text too long. Keep under {MAX_TEXT_CHARS} characters per generation.")

    language, lang_msg = detect_language(text)
    quality_msg = analyze_reference_audio(reference_audio)

    tts = load_model()

    output_file = Path(tempfile.gettempdir()) / "xtts_hindi_clone_output.wav"
    tts.tts_to_file(
        text=text,
        speaker_wav=reference_audio,
        language=language,
        file_path=str(output_file),
    )

    result_msg = (
        "Generation complete ✅\n"
        f"{lang_msg}\n"
        f"{quality_msg}\n"
        f"Model: {MODEL_NAME}"
    )
    return str(output_file), result_msg


with gr.Blocks(title="Hindi Voice Cloning Studio (XTTS v2)") as demo:
    gr.Markdown(
        """
        # 🎙️ Hindi Voice Cloning Studio
        Upload voice sample → paste story text → generate and play cloned voice.

        **Python 3.12 friendly setup** with Coqui XTTS v2.
        """
    )

    with gr.Row():
        reference_audio = gr.Audio(
            label="1) Upload Voice Sample",
            type="filepath",
            sources=["upload", "microphone"],
        )
        text_input = gr.Textbox(
            label="2) Story / Text",
            placeholder="Yahan apni story ya script likho...",
            lines=8,
            max_lines=14,
        )

    generate_btn = gr.Button("3) Generate Cloned Voice", variant="primary")
    output_audio = gr.Audio(label="4) Play Output", type="filepath")
    status_box = gr.Textbox(label="Status + Professional Checks", lines=8)

    generate_btn.click(
        fn=clone_voice,
        inputs=[reference_audio, text_input],
        outputs=[output_audio, status_box],
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
