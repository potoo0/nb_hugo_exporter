import unittest
from pathlib import Path

from .context import HugoExporter


class TestHugoExporter(unittest.TestCase):
    def test_export(self):
        resources = Path(__file__).parent / "resources"
        exporter = HugoExporter()
        (body, _) = exporter.from_filename(str(resources / "test.ipynb"))

        expected = (resources / "test.md").read_text(encoding="utf8")
        self.assertEqual(expected, body)


if __name__ == "__main__":
    unittest.main()
