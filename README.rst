===============================
AlienVaultPyEx2
===============================

+---------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| **Travis CI** (Linux Build and Integration Tests) | .. image:: https://travis-ci.org/TheFantasyClub/AlienVaultPyEx2.svg?branch=master                   |
|                                                   |  :alt: Travis Support :target: https://travis-ci.org/TheFantasyClub/AlienVaultPyEx2                 |
|                                                   |  :target: https://travis-ci.org/TheFantasyClub/AlienVaultPyEx2                                      |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| **Coveralls coverage support**                    | .. image:: https://coveralls.io/repos/github/TheFantasyClub/AlienVaultPyEx2/badge.svg?branch=master |
|                                                   |  :alt: Coveralls coverage support                                                                   |
|                                                   |  :target: https://coveralls.io/github/TheFantasyClub/AlienVaultPyEx2?branch=master                  |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| **Documentation Status**                          | .. image:: https://readthedocs.org/projects/alienvaultpyex2/badge/?version=latest                   |
|                                                   |  :alt: Documentation Status                                                                         |
|                                                   |  :target: https://alienvaultpyex2.readthedocs.io/en/latest/?badge=latest                            |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------+

----------

+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **SonarCloud**                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| .. image:: https://sonarcloud.io/api/project_badges/measure?project=AlienVaultPyEx2_W&metric=alert_status     | .. image:: https://sonarcloud.io/api/project_badges/measure?project=AlienVaultPyEx2_W&metric=code_smells     | .. image:: https://sonarcloud.io/api/project_badges/measure?project=AlienVaultPyEx2_W&metric=sqale_index     | .. image:: https://sonarcloud.io/api/project_badges/measure?project=AlienVaultPyEx2_W&metric=coverage    |
|         :alt: Alert Status                                                                                    |         :alt: Code Smells                                                                                    |         :alt: Technical debt                                                                                 |         :alt: Code coverage                                                                              |
|         :target: https://sonarcloud.io/dashboard?id=AlienVaultPyEx2_W                                         |         :target: https://sonarcloud.io/dashboard?id=AlienVaultPyEx2_W                                        |         :target: https://sonarcloud.io/dashboard?id=AlienVaultPyEx2_W                                        |                             :target: https://sonarcloud.io/dashboard?id=AlienVaultPyEx2_W                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+




AlienVault's hiring exercise

* Free software: MIT license
* Documentation: https://AlienVaultPyEx2.readthedocs.org.


First steps into creating the package and use it
------------------------------------------------

This is an example package to give to the AlienVault's Hiring Team.
The code provided could not be safe in industrial environments and this is only a test for hiring purposes.

I'm not responsible in any way if this code eats your homework.

Features
--------

* Package to read Github issues and process them.


TODO GLOBAL
*****************
* ✔️ TDD with Sonarcloud and Coveralls to ensure effective conversion.
* ✔️ Insert the issue dictionary as element into a list.
* ✔️ Create a list to save all issues dates.
* ✔️ Convert all issues dates in isoformat Z or `datetime` into day date with format YYYY-MM-DD from the dates list.
* ❌ Extract all the repository and created at into two lists
* ❌ using the list preiously created, search trough all elements and create a dictionary with the keywords `day` and `ocurrences`

TODO Specific in `if __name__ == '__main__'`
**********************************************
* ❌ prompt for user/pass or token
* ❌ prompt for proxy if needed
* ❌ set a python's list pointing to Github's repos.
* ❌ connect to Github
* ❌ using PyGithub, extract the id, state, title, repository and created at with isoformat Z and create with those data, a dictionary.

Input
*****
.. code-block::

  ["owner1/repository1", "owner2/repository2"]

Restult
*******

.. code-block::

  {
    "issues": [
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
    ],
    "top_day": {
      "day": "2011-04-22",
      "occurrences": {
        "own1/repo1": 2,
        "own2/repo2": 0
      }
    }
  }
