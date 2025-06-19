# pypinyin-g2pw-torch

This package provides a seamless bridge to integrate the `g2pw_torch` engine with the popular `pypinyin` library.

Its main purpose is to act as a custom "converter" for `pypinyin`, enabling it to perform high-accuracy, context-aware polyphonic character disambiguation using a PyTorch-based model.

## Features

- **Easy Integration**: Use as a simple `converter` argument in the `pypinyin.pinyin()` function.
- **Leverages `g2pw_torch`**: Brings the full power of the PyTorch-native G2P engine to `pypinyin`.
- **Enables `heteronym` mode**: Provides accurate results for `pypinyin`'s heteronym feature.

## Installation

This package is intended to be installed as part of the `g2pw-torch` workspace. Navigate to the project's root directory (`g2pw_torch_publish`) and run:

```bash
pip install -e .
```

This will install both this package and its core dependency, `g2pw_torch`.

## Quick Start

This library makes using the advanced G2P model extremely simple within your existing `pypinyin` workflow.

```python
from pypinyin import pinyin, Style
from pypinyin_g2pw_torch import G2PWPinyin

# --- Configuration ---
# Path to the directory containing model assets (like config.py)
MODEL_DIR = '../../G2PWModel'
# Path to your PyTorch model checkpoint (.pth file)
CHECKPOINT_PATH = '../../G2PWModel-pth/best_accuracy.pth'

# --- Initialization ---
# 1. Initialize our custom converter
g2pw_converter = G2PWPinyin(
    model_dir=MODEL_DIR,
    checkpoint_path=CHECKPOINT_PATH,
    use_onnx=False  # Tell it to use the PyTorch backend
)

# --- Usage ---
text = "你好，世界。这是一个多音字测试，比如银行和行走。"

# 2. Pass the converter to the pypinyin function
result = pinyin(
    text,
    style=Style.TONE3,
    heteronym=True,  # Enable polyphonic character handling
    converter=g2pw_converter
)

print(f"Original Text: {text}")
print(f"Pinyin Result from pypinyin with g2pw-torch: {result}")

# Example with a single word
word_bank = "银行"
pinyin_bank = pinyin(word_bank, style=Style.TONE3, heteronym=True, converter=g2pw_converter)
print(f"'{word_bank}' -> {pinyin_bank} (Correctly identified as 'yinhang')")
```