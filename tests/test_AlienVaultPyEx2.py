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

from AlienVaultPyEx2.DictIssuesComposer import DictIssuesComposer
from AlienVaultPyEx2.IssueListComposer import IssueListComposer

class TestDictIssuesComposer(unittest.TestCase):

    def setUp(self):
        self.id = 38
        self.state = "open"
        self.title = "Found a bug"
        self.repository = "own1/repo1"
        self.created_at = "2011-04-22T13:33:48Z"

    def test_creation_dict(self):
        test_in = DictIssuesComposer(self.id, self.state, self.title,
                                     self.repository, self.created_at)
        out_dump = json.dumps(test_in.GetDictIssues())
        assert(len(test_in.GetDictIssues()) == 5)
        assert(len(out_dump) == 117)
        assert(out_dump == '{"id": 38, "state": "open",'
                         + ' "title": "Found a bug",'
                         + ' "repository": "own1/repo1",'
                         + ' "created_at": "2011-04-22T13:33:48Z"}')

    def tearDown(self):
        pass

class TestIssueListComposer(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation_list_empty(self):
        test_in = IssueListComposer()
        out_list = test_in.GetIssueList()
        assert(len(out_list) == 0)
        assert(out_list == [])

    def test_creation_list(self):
        issue_listed = {"id": 38,
                        "state": "open",
                        "title": "Found a bug",
                        "repository": "own1/repo1",
                        "created_at": "2011-04-22T13:33:48Z"}
        test_in = IssueListComposer(issue_listed)
        out_list = test_in.GetIssueList()
        assert(len(out_list) == 1)
        out_list.append(issue_listed)
        assert(len(out_list) == 2)

    def tearDown(self):
        pass
