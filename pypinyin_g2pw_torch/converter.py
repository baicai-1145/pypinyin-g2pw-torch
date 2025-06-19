# -*- coding: utf-8 -*-

from pypinyin.constants import RE_HANS
from pypinyin.core import Pinyin, Style
from pypinyin.seg.simpleseg import simple_seg
from pypinyin.converter import UltimateConverter
from pypinyin.contrib.tone_convert import to_tone
from g2pw.api import G2PWConverter


class G2PWPinyin(Pinyin):
    def __init__(self, model_dir='G2PWModel/', model_source=None,
                 num_workers=None, batch_size=None,
                 turnoff_tqdm=True, enable_non_tradional_chinese=True,
                 v_to_u=False, neutral_tone_with_five=False, tone_sandhi=False,
                 use_onnx=True, checkpoint_path=None, **kwargs):
        self._g2pw = G2PWConverter(
            model_dir=model_dir,
            style='pinyin',
            model_source=model_source,
            num_workers=num_workers,
            batch_size=batch_size,
            turnoff_tqdm=turnoff_tqdm,
            enable_non_tradional_chinese=enable_non_tradional_chinese,
            use_onnx=use_onnx,
            checkpoint_path=checkpoint_path,
        )
        self._converter = Converter(
            self._g2pw, v_to_u=v_to_u,
            neutral_tone_with_five=neutral_tone_with_five,
            tone_sandhi=tone_sandhi,
        ) 