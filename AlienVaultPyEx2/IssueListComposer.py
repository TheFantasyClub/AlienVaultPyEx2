class IssueListComposer(object):
    """ Creates a dictionary with the elements inserted """

    def __init__(self, issue_dict = None):
        self.listissue = []
        if issue_dict is not None:
            self.listissue = issue_dict

    def GetIssueList(self):
        return self.issuedic
