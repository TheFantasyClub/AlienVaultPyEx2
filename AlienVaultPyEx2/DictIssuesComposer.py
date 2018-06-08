class DictIssuesComposer(object):
    """ Creates a dictionary with the elements inserted
        The elements are not being type-tested. Use with caution
    """

    def __init__(self, issue_id, issue_state, issue_title,
                 issue_repository, issue_created_at):
        self.issuedic = {"id": issue_id,
                         "state": issue_state,
                         "title": issue_title,
                         "repository": issue_repository,
                         "created_at": issue_created_at
                         }

    def GetDictIssues(self):
        return self.issuedic
