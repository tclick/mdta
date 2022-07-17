#  Copyright (C) 2022 by Timothy H. Click <Timothy.Click@briarcliff.edu>
#
#  Permission to use, copy, modify, and/or distribute this software for any purpose
#  with or without fee is hereby granted.
#
#  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
#  REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
#  FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
#  INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
#  OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
#  TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
#  THIS SOFTWARE.
"""Parse a configuration file."""
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, List

import click
import pylibyaml  # noqa: F401
import yaml

from ... import PathLike

logger: logging.Logger = logging.getLogger(__name__)


@dataclass
class Config:
    """Configuration data."""

    def update(self, **kwargs: Any) -> None:
        """Add or update attributes.

        Parameters
        ----------
        kwargs : Any
            Dict of attributes to add
        """
        for key, value in kwargs.items():
            setattr(self, key, value)


def configure(ctx: click.Context, param: List[Any], filename: PathLike) -> None:
    """Read a configuration file and pouplate click.Context.default_map with contents.

    Parameters
    ----------
    ctx : click.Context
        Context object
    param : list
        List of parameters
    filename : PathLike
        configuration file
    """
    if Path(filename).exists():
        logger.debug(f"Using configuration file: {filename}")
        with open(filename) as config_file:
            ctx.default_map = yaml.safe_load(config_file)
