import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class _PlaceholderMarkItDown:
    def __init__(self, llm_client=None):
        self.llm_client = llm_client

    def convert_stream(self, stream, file_extension):
        raise NotImplementedError


stub_module = types.ModuleType("markitdown")
stub_module.MarkItDown = _PlaceholderMarkItDown
sys.modules.setdefault("markitdown", stub_module)
