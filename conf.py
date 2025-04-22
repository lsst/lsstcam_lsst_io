# See the documenteer.toml for overrides of the Rubin user guide presets

from pathlib import Path

from documenteer.conf.guide import *  # noqa: F401, F403

# Configure bibliography with the bib cache
documenteer_bibfile_cache_dir = "_build/.bibfiles"
documenteer_bibfile_github_repos = [
    {
        "repo": "lsst/lsst-texmf",
        "ref": "main",
        "bibfiles": [
            "texmf/bibtex/bib/lsst.bib",
            "texmf/bibtex/bib/lsst-dm.bib",
            "texmf/bibtex/bib/refs_ads.bib",
            "texmf/bibtex/bib/refs.bib",
            "texmf/bibtex/bib/books.bib",
        ],
    }
]
# Set up bibtex_bibfiles
# Automatically load local bibfiles in the root directory.
bibtex_bibfiles = [str(p) for p in Path.cwd().glob("*.bib")]

bibtex_default_style = "lsst_aa"
bibtex_reference_style = "author_year"
