# tests/test_embed.py（修正版）

import json
from pathlib import Path

def test_embedding_cache_exists():
    """埋め込みキャッシュファイルが存在し、正しいJSON形式で読み込めることを確認"""
    path = Path("data/embedding_cache.json")
    assert path.exists(), "embedding_cache.json が存在しません"

    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list), "埋め込みキャッシュはリスト型である必要があります"
    assert len(data) > 0, "埋め込みキャッシュが空です"
    assert isinstance(data[0], dict), "埋め込みキャッシュの各要素は辞書型である必要があります"
    assert "embedding" in data[0], "各要素に 'embedding' キーが必要です"
