# tests/test_chatgpt.py

import os
import sys
import pytest

# プロジェクトルートをimportパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.call_chatgpt import call_chatgpt

@pytest.mark.skipif("OPENAI_API_KEY" not in os.environ, reason="APIキーが未設定のためスキップ")
def test_chatgpt_response_format():
    prompt = "住民票を取得するにはどうすればいいですか？"
    response = call_chatgpt(prompt)
    assert isinstance(response, str)
    assert len(response) > 10
