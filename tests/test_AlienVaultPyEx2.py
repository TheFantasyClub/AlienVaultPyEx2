#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_AlienVaultPyEx2
----------------------------------

Tests for `AlienVaultPyEx2` module.
"""

import unittest
import json
import datetime

from AlienVaultPyEx2.DictIssuesComposer import DictIssuesComposer
from AlienVaultPyEx2.IssueListComposer import IssueListComposer
from AlienVaultPyEx2.DateRelatedFunctions import DateDayConverter
from AlienVaultPyEx2.DateRelatedFunctions import PyGithubDateConverter


class TestDictIssuesComposer(unittest.TestCase):

    def setUp(self):
        self.id = 38
        self.state = "open"
        self.title = "Found a bug"
        self.repository = "own1/repo1"
        self.created_at = "2011-04-22T13:33:48Z"
        self.issue_dict = {"id": 38,
                           "state": "open",
                           "title": "Found a bug",
                           "repository": "own1/repo1",
                           "created_at": "2011-04-22T13:33:48Z"}

    def test_creation_dict(self):
        """ Test some kinds of object construction """

        """ Construction without parameters """
        empty_dic = DictIssuesComposer()
        empty_val = empty_dic.GetDictIssues()
        assert(len(empty_val) == 5)
        dump_empty = json.dumps(empty_val)
        assert(dump_empty == json.dumps({"id": None,
                                         "state": None,
                                         "title": None,
                                         "repository": None,
                                         "created_at": None}))

        """ Construction with all parameters """
        test_in = DictIssuesComposer(self.id, self.state, self.title,
                                     self.repository, self.created_at)
        test_val = test_in.GetDictIssues()
        assert(len(test_val) == 5)
        dump_test = json.dumps(test_val)
        assert(dump_test == json.dumps({"id": 38,
                                        "state": "open",
                                        "title": "Found a bug",
                                        "repository": "own1/repo1",
                                        "created_at": "2011-04-22T13:33:48Z"}))

        dict_in = DictIssuesComposer(39, self.state, self.title,
                                     self.repository, self.created_at)
        dict_val = dict_in.GetDictIssues()
        assert(len(dict_val) == 5)
        dump_dict = json.dumps(dict_val)
        assert(dump_dict == json.dumps({"id": 39,
                                        "state": "open",
                                        "title": "Found a bug",
                                        "repository": "own1/repo1",
                                        "created_at": "2011-04-22T13:33:48Z"}))

        """ Check both constructions are not equal (redundant) """
        assert(dump_dict != dump_test)
        assert(test_val["id"] != dict_val["id"])
        assert(test_val["state"] == dict_val["state"])
        assert(test_val["title"] == dict_val["title"])
        assert(test_val["repository"] == dict_val["repository"])
        assert(test_val["created_at"] == dict_val["created_at"])

    def test_copy_dict(self):
        """ Test copy_from function """

        """ To check values """
        test_in = DictIssuesComposer(self.id, self.state, self.title,
                                     self.repository, self.created_at)
        test_val = test_in.GetDictIssues()
        dump_test = json.dumps(test_val)

        """ To test values """
        dict_in = DictIssuesComposer()
        dict_in.CopyFrom(self.issue_dict)
        dict_val = dict_in.GetDictIssues()
        dump_dict = json.dumps(dict_val)

        assert(test_val == dict_val)
        assert(dump_dict == dump_test)

    def tearDown(self):
        pass


class TestIssueListComposer(unittest.TestCase):

    def setUp(self):
        self.issue_list_element = {"id": 38,
                                   "state": "open",
                                   "title": "Found a bug",
                                   "repository": "own1/repo1",
                                   "created_at": "2011-04-22T13:33:48Z"}
        self.issue_list_element_2 = {"id": 40,
                                     "state": "open",
                                     "title": "Found a bug",
                                     "repository": "own2/repo2",
                                     "created_at": "2011-04-23T13:33:48Z"}

    """ Construction without parameters """

    def test_creation_list_empty(self):
        test_in = IssueListComposer()
        out_list = test_in.GetIssueList()
        assert(len(out_list) == 0)
        assert(out_list == [])

    """ Construction and appending more values """

    def test_creation_list(self):
        issue_listed = self.issue_list_element
        test_in = IssueListComposer(issue_listed)
        out_list = test_in.GetIssueList()
        assert(len(out_list) == 1)
        out_list.append(issue_listed)
        assert(len(out_list) == 2)
        out_list.append(self.issue_list_element_2)
        assert(len(out_list) == 3)
        assert(out_list[2] == self.issue_list_element_2)

    def tearDown(self):
        pass


class test_conversion_date_formats(unittest.TestCase):

    def setUp(self):
        pass

    def test_date_conversion_to_YYYY_MM_HH(self):
        date_test = DateDayConverter("2011-04-22T13:33:48Z")
        assert(date_test == "2011-04-22")

    def test_date_conversion_from_pygithub_format(self):
        dtp = datetime.datetime(2018, 6, 6, 16, 49, 12)
        assert(PyGithubDateConverter(dtp) == '2018-06-06T16:49:12Z')
        pass

    def tearDown(self):
        pass
