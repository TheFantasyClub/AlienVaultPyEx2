class ListComposer(object):
    """ Creates a dictionary with the elements inserted """

    def __init__(self, issue_id, issue_state, issue_title,
                 issue_repository, issue_created_at):
        self.issuedic = {"id": issue_id,
                         "state": issue_state,
                         "title": issue_title,
                         "repository": issue_repository,
                         "created_at": issue_created_at
                         }

    def GetListComposer(self):
        return self.issuedic
