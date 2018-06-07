#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_AlienVaultPyEx2
----------------------------------

Tests for `AlienVaultPyEx2` module.
"""

import unittest
import json
import AlienVaultPyEx2

from AlienVaultPyEx2.DictIssuesComposer import ListComposer


class TestDictIssuesComposer(unittest.TestCase):

    def setUp(self):
        self.id = 38
        self.state = "open"
        self.title = "Found a bug"
        self.repository = "own1/repo1"
        self.created_at = "2011-04-22T13:33:48Z"
        pass

    def test_creation(self):
        a = ListComposer(
                         self.id, self.state, self.title,
                         self.repository, self.created_at)
        out_a = json.dumps(a.GetListComposer())
        assert(out_a == '{"id": 38, "state": "open", "title": "Found a bug", '
                        + '"repository": "own1/repo1", "created_at":'
                        + ' "2011-04-22T13:33:48Z"}')

    def tearDown(self):
        pass


class TestAlienvaultpyex2(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(AlienVaultPyEx2.__version__)

    def tearDown(self):
        pass
