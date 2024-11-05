r"""Preprocessor Module for Hugo.

This module exports a single class.

    HugoPreprocessor: An `nbconvert` `Preprocessor` for exporting notebooks
        to a Markdown format compatible with [Hugo](https://gohugo.io)

"""

import os.path
from datetime import date

from nbconvert.preprocessors import Preprocessor


class HugoPreprocessor(Preprocessor):
    r"""Preprocessor class for Hugo.

    This class overrides the `preprocess` methods of
    the `nbcovert` `Preprocessor` class, to accomplish the following tasks:

    1.  Set default values for metadata (date, title, and draft).
    """

    def preprocess(self, nb: dict, resources: dict):
        """
        Set metadata defaults, process underscores, and set output file paths.

        Args: See the `nbconvert.preprocessors.Preprocessor` documentation.

        Returns: (nb, resources) where these have been fully processed.
        """
        if nb["metadata"].get("hugo") is None:
            nb["metadata"]["hugo"] = {}
        hugo = nb["metadata"]["hugo"]

        # Set metadata if missing
        hugo["title"] = hugo.get("title") or self._hugo_title(resources)
        hugo["date"] = self._hugo_date(hugo.get("date"), resources)
        hugo["draft"] = hugo.get("draft") or False

        return super().preprocess(nb, resources)

    def preprocess_cell(self, cell, resources, index):
        """Do nothing."""
        return cell, resources

    def _hugo_date(self, datestr: str, resources: dict) -> date:
        """Return a date."""
        if datestr:
            return date.fromisoformat(datestr)
        return date.fromtimestamp(os.path.getmtime(self._filepath(resources)))

    def _hugo_title(self, resources: dict):
        return " ".join(
            word.capitalize() for word in resources["metadata"]["name"].split("_")
        )

    @staticmethod
    def _filepath(resources: dict) -> str:
        path: str = resources["metadata"]["path"]
        name: str = resources["metadata"]["name"]
        return os.path.join(path, name + ".ipynb")
