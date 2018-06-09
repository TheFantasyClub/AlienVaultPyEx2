# -*- coding: utf-8 -*-
import json
from github import Github
from AlienVaultPyEx2.OcurrencesComposer import OcurrencesComposer
from AlienVaultPyEx2.DictIssuesComposer import DictIssuesComposer
from AlienVaultPyEx2.IssueListComposer import IssueListComposer
from AlienVaultPyEx2.DateRelatedFunctions import DateConverterPyGithub


def Exercise():
    uses_token = False
    uses_user_pass = False
    tokenval = input("Insert Token ")

    if tokenval != "":
        print("Received token " + tokenval)
        uses_token = True

    if uses_token is False:
        user_in = input("Insert your Github account's user")
        pass_in = input("Insert Password (Is visible!)")
        uses_user_pass = True

    if uses_token is False and uses_user_pass is False:
        print("Program fail. Exiting")
        exit()
    elif uses_token and not uses_user_pass:
        g = Github(tokenval)
    elif not uses_token and uses_user_pass:
        g = Github(user_in, pass_in)

    issue_list = IssueListComposer()
    dict_issues = DictIssuesComposer()

    for reponame in glist:
        for repo in g.get_repo(reponame).get_issues():

            dict_issues = DictIssuesComposer(
             repo.id, repo.state, repo.title,
             reponame, DateConverterPyGithub(repo.created_at))

            if len(issue_list.GetIssueList()) == 0:
                issue_list = IssueListComposer(dict_issues.GetDictIssues())
            else:
                issue_list.append(dict_issues.GetDictIssues())
            # print("id " + str(repo.id))
            # print("state " + repo.state)
            # print("title " + repo.title)
            # print("repository " + reponame)
            # print("created_at " + DateConverterPyGithub(repo.created_at))
    occurrences = OcurrencesComposer(issue_list.GetIssueList())

    print(occurrences.OutputData())

    occurrences.Process()

    outdic = occurrences.OutputData()

    with open('dataoutput.txt', 'w') as outfile:
        json.dump(outdic, outfile)


if __name__ == '__main__':
    glist = ["moewe-io/embed-google-fonts",
             "UW-Hydro/bmorph",
             "sjinks/qt_eventdispatcher_libevent",
             "inProgress-team/react-native-meteor",
             "aperezdc/synpurge",
             "ErikTillberg/Project-Schwarma",
             "shirorndcode/atelier_remap",
             "hyenaspots/yampatch"]
    Exercise()
