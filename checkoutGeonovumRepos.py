#!/usr/bin/python3
#
# author: Wilko Quak (w.quak@geonovum.nl)
#
import subprocess
import json
import os
from git import Repo

output = subprocess.check_output('gh repo list Geonovum -L 3 --json name')
data = json.loads(output)

data = json.loads('''
[
  {
    "name": "dso-cimop"
  },
  {
    "name": "DashboardGit"
  }
]
''')

for x in data:
    repo = x['name']
    if os.path.isdir(repo):
        print('repo {} exisits updating'.format(repo))
        repo = Repo(os.path.abspath(repo));
        repo.git.pull()

    else:
        print('repo {} does not exist checking out'.format(repo))
        co = subprocess.check_output('gh repo clone Geonovum/{}'.format(repo))
        print('co={}'.format(co))
