class OcurrencesComposer(object):
    """
    Receives a list of issues and extract the dates into a list
    """

    def __init__(self, issue_list=None):
        self.dictocurrences = dict()
        if issue_list is not None:
            self.dictocurrences = {issue_list}

    def OutputData(self):
        return self.dictocurrences
