import base64
import importlib
import logging
import sys
from typing import Any, List

import streamlit as st

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def _reload_module(page):
    """Reloads the specified module/ page
    Arguments:
        page {module} -- A page/ module
    """
    logging.debug(
        """--- Reload of module for live reload to work on deeply imported python modules.
    Cf. https://github.com/streamlit/streamlit/issues/366 ---""")
    logging.debug("2. Module: %s", page)
    logging.debug("3. In sys.modules: %s", page in sys.modules)
    try:
        importlib.import_module(page.__name__)
        importlib.reload(page)
    except ImportError as _:
        logging.debug("4. Writing: %s", page)
        logging.debug("5. In sys.modules: %s", page in sys.modules)


def write_page(page):  # pylint: disable=redefined-outer-name
    """Writes the specified page/module
    Our multipage app is structured into sub-files with a `def write()` function
    Arguments:
        page {module} -- A module with a 'def write():' function
    """
    # _reload_module(page)
    page.write()