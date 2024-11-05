r"""The hugoexporter module.

This module exports a single class:

    HugoExporter: An `nbconvert` `MarkdownExporter` for exporting notebooks
        to a Markdown format compatible with [Hugo](https://gohugo.io)

"""

import os.path

import toml
from nbconvert.exporters.markdown import MarkdownExporter
from traitlets import default

from .hugopreprocessor import HugoPreprocessor


class HugoExporter(MarkdownExporter):
    r"""The HugoExporter class.

    This class overrides the `MarkdownExporter` of `nbconvert` to use a custom
    template and preprocessor. It is registered as an `entry_point` in
    `setup.py` as follows
    ```
        'nbconvert.exporters': [
            'hugo = nbhugoexporter.hugoexporter:HugoExporter',
        ]
    ```
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_preprocessor(HugoPreprocessor, enabled=True)
        self.register_filter('toml_dumps', toml.dumps)

    @default("template_paths")
    def _template_paths(self) -> list[str]:
        """Extend the template_path to include this library's directory."""
        return super()._template_paths() + [
            os.path.join(os.path.dirname(__file__), "templates")
        ]

    @default("template_file")
    def _template_file_default(self):
        """Override and return the traitlet template_file."""
        return "hugo.j2"

    # def _init_resources(self, resources):
    #     """Extend resources dictionary initialization.

    #     - Make sure the primary output filename is `index.md`
    #     - Do not create a subdirectory for output files, use the `output-dir`
    #       directory.
    #     """
    #     resources = super()._init_resources(resources)
    #     resources["unique_key"] = "index"
    #     resources["output_files_dir"] = "."
    #     return resources
