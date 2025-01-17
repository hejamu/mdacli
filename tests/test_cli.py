#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2021 Authors and contributors
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later
"""Test mdacli cli."""

import subprocess

import pytest


def test_required_args():
    """Test that there is a module given."""
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(['mda'])


def test_wrong_module():
    """Test for a non existent module."""
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(['mda', 'foo'])


@pytest.mark.parametrize('args', ("version", "debug", "help"))
def test_extra_options(args):
    """Test for a ab extra option."""
    subprocess.check_call(['mda', '--' + args])


@pytest.mark.parametrize('args', ("RMSF", "rmsf"))
def test_case_insensitive(args):
    """Test for beeing case insensitive."""
    subprocess.check_call(['mda', args, "-h"])
