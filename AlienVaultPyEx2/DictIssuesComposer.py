# -*- coding: utf-8 -*-


class DictIssuesComposer(object):
    """ Creates a dictionary with the elements inserted
        The elements are not being type-tested. Use with caution
    """

    def __init__(self, issue_id=None, issue_state=None, issue_title=None,
                 issue_repository=None, issue_created_at=None):
        self.issuedic = {"id": issue_id,
                         "state": issue_state,
                         "title": issue_title,
                         "repository": issue_repository,
                         "created_at": issue_created_at
                         }

    def CopyFrom(self, dict_issue_object):
        self.issuedic = {"id": dict_issue_object["id"],
                         "state": dict_issue_object["state"],
                         "title": dict_issue_object["title"],
                         "repository": dict_issue_object["repository"],
                         "created_at": dict_issue_object["created_at"]
                         }

    def GetDictIssues(self):
        return self.issuedic
