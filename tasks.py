# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright © 2019 Damien Flament
# This file is part of pytest-notimplemented.

"""Usefull tasks to `invoke` when developing."""

from pathlib import Path

import pdoc
from invoke import task

import pytest_notimplemented

DIR = Path(__file__).parent
README_TARGET = DIR / "README.md"


def get_module_doc():
    """Gives the module documentation object."""
    context = pdoc.Context()
    module = pdoc.Module(pytest_notimplemented, context=context)
    pdoc.link_inheritance(context=context)

    return module


@task
def lint(c):
    """Lint the source code"""
    c.run("flake8", hide="out")


@task
def check(c):
    """Checks the plugin"""
    c.run("pytest", hide="out")


@task
def readme(c):
    """Generates the readme"""
    module = get_module_doc()
    title = "pytest-notimplemented"

    README_TARGET.touch()
    README_TARGET.write_text("\n".join([title, "=" * len(title), module.docstring]))


@task(lint, check, readme, name="pre-commit")
def pre_commit(c):
    """Run tasks required for commiting"""
    c.run(f"git add {README_TARGET}")
