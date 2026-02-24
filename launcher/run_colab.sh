#!/bin/bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install xformers --no-build-isolation
pip install -r requirements.txt
python main.py --listen 0.0.0.0 --port 8188 --force-fp16
