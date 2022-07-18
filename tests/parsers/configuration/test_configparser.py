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
"""Test ConfigParser class."""
from dataclasses import is_dataclass

import click
import pytest

from mdta.parsers.configuration.configparser import Config, configure

from ...datafile import TRAJFILES


class TestConfig:
    """Test Config class."""

    @pytest.fixture
    def context(self) -> Config:
        """Create an mock click.Context object.

        Returns
        -------
        Config
            a mock click.Context object
        """
        config = Config()
        config.analysis = "coordinates"
        return config

    def test_config(self, context: Config) -> None:
        """Test the Config class.

        GIVEN a Config class
        WHEN the class is initialized
        THEN the object should be of type `dataclass`

        Parameters
        ----------
        context: Config
            mock object
        """
        assert is_dataclass(context)
        assert hasattr(context, "analysis")
        assert context.analysis == "coordinates"

    def test_update(self, context: Config) -> None:
        """Test functionality of update method.

        GIVEN a Config object
        WHEN a dict is included in the update method
        THEN the object should add the new attribute

        Parameters
        ----------
        context: Config
            mock object
        """
        kwargs = dict(debug=True, startres=1)
        context.update(**kwargs)

        assert hasattr(context, "analysis")
        assert hasattr(context, "debug")
        assert hasattr(context, "startres")
        assert context.debug
        assert context.startres == 1


class TestConfigParser:
    """Test ConfigParser class."""

    @pytest.fixture
    def ctx(self) -> click.Context:
        """Create a mock click.Context object.

        Returns
        -------
        Context
            a mock click.Context object
        """
        ctx = click.Context(click.Command("mock"))
        ctx.default_map = {}
        return ctx

    def test_configure(self, ctx: click.Context) -> None:
        """Test the configure function.

        GIVEN a click.Context and a filename
        WHEN the configure function is called
        THEN context.default_map is populated with the YAML configuration

        Parameters
        ----------
        ctx: click.Context
            mock object
        """
        configure(ctx, [], TRAJFILES)

        assert len(ctx.default_map) > 0  # type: ignore
        assert "trajfiles" in ctx.default_map  # type: ignore
        assert ctx.default_map["trajfiles"] is not None  # type: ignore
