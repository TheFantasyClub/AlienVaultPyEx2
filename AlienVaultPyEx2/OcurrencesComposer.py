class OcurrencesComposer(object):
    """
    Creates a dictionary with only one element:
    the last and most issues ocurrence counter
    """

    def __init__(self, issue_list=None):
        self.dictocurrences = dict()
        if issue_list is not None:
            self.dictocurrences = {issue_list}

    def OutputData(self):
        return self.dictocurrences


def find(key, value):
    for k, v in value.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result


def gen_dict_extract(key, var):
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


if __name__ == '__main__':
    vt = {'temparature': '50',
          'logging': {
            'handlers': {
              'console': {
                'formatter': 'simple',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
                'level': 'DEBUG'
              }
            },
            'loggers': {
              'simpleExample': {
                'handlers': ['console'],
                'propagate': 'no',
                'level': 'INFO'
              },
              'root': {
               'handlers': ['console'],
               'level': 'DEBUG'
              }
            },
            'version': '1',
            'formatters': {
             'simple': {
               'datefmt': "'%Y-%m-%d %H:%M:%S'",
               'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
             }
            }
           },
          'treatment': {'second': 5, 'last': 4, 'first': 4},
          'treatment_plan': [[4, 5, 4], [4, 5, 4], [5, 5, 5]]
          }
    d = {"id": "abcde",
         "key1": "blah",
         "key2": "blah blah",
         "nestedlist": [
          {"id": "qwerty",
           "nestednestedlist": [
            {"id": "xyz", "keyA": "blah blah blah"},
            {"id": "fghi", "keyZ": "blah blah blah"}],
           "anothernestednestedlist": [
            {"id": "asdf", "keyQ": "blah blah"},
            {"id": "yuiop", "keyW": "blah"}]
           }]
         }
    AVTestValues = {"issues": [
                               {
                                 "id": 38,
                                 "state": "open",
                                 "title": "Found a bug",
                                 "repository": "own1/repo1",
                                 "created_at": "2011-04-22T13:33:48Z"
                                },
                               {
                                 "id": 23,
                                 "state": "open",
                                 "title": "Found a bug 2",
                                 "repository": "own1/repo1",
                                 "created_at": "2011-04-22T18:24:32Z"
                                },
                               {
                                 "id": 24,
                                 "state": "closed",
                                 "title": "Feature request",
                                 "repository": "own2/repo2",
                                 "created_at": "2011-05-08T09:15:20Z"
                                }
                              ]
                    }
    list(find("id", d))

    list(gen_dict_extract("id", d))

    list(gen_dict_extract("datefmt", vt))

    [x for x in gen_dict_extract('id', d)]

    list(gen_dict_extract("created_at", AVTestValues))
