# -*- coding: utf-8 -*-


from AlienVaultPyEx2.DateRelatedFunctions import DateDayConverter


def gen_dict_extract(key, var):
    """ https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-python-dictionaries-and-lists """
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def DictionaryExtractorMultipleGen(keys, var):
    """
    Variant of gen_dict_extract with multiple keys into a datatype contains
    items as attribute
    """
    for key in keys:
        if hasattr(var, 'items'):
            for k, v in var.items():
                if k == key:
                    yield {key: v}
                if isinstance(v, dict):
                    for result in gen_dict_extract(key, v):
                        yield result
                elif isinstance(v, list):
                    for d in v:
                        for result in gen_dict_extract(key, d):
                            yield result


def SplitAListGen(l, n):
    """Yield successive n-sized chunks from l."""
    """https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks"""
    for i in range(0, len(l), n):
        yield l[i:i + n]


class OcurrencesComposer(object):
    """
    Creates a dictionary with only one element:
    the last and most issues ocurrence counter
    """

    def __init__(self, issue_list=None):
        self.dictocurrences = dict()
        if issue_list is not None:
            self.dictocurrences = {"issues": issue_list}

    def CreateOcurrencesDict(self):
        ExtractionOcurrencesList = list(DictionaryExtractorMultipleGen(
                                         ["created_at", "repository"],
                                         self.AVTestValues))
        OcurrencesSplitted = list(SplitAListGen(ExtractionOcurrencesList,
                                                len(ExtractionOcurrencesList)
                                                // 2))

        for i in range(0, len(OcurrencesSplitted[0])):
            OcurrencesSplitted[0][i] = DateDayConverter(
             OcurrencesSplitted[0][i])
        """
        Uses OcurrencesSplitted[1] directly because we know the size
        but can happen the size can be 0 or 1. This is not tested yet
        """
        self.ocurrencesdict = dict(zip(OcurrencesSplitted[0],
                                       OcurrencesSplitted[1]))

    def OutputData(self):
        return self.dictocurrences
