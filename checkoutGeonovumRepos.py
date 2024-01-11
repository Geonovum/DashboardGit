#!/usr/bin/python3
#
# author: Wilko Quak (w.quak@geonovum.nl)
#
# Dit script checkt alle Geonovum repositories uit en houdt ze up to date.
# Vereisten:
# - Github client is geinstalleerd: https://cli.github.com/manual
# - Token maken en inloggen met
#
import subprocess
import json
import os
from git import Repo

output = subprocess.check_output('gh repo list Geonovum -L 400 --json name,isEmpty',shell=True)
data = json.loads(output)

#data = json.loads('''
#[
  #{
    #"name": "dso-cimop"
  #},
  #{
    #"name": "DashboardGit"
  #}
#]
#''')

for x in data:
    repo = x['name']
    isEmpty = x['isEmpty']
    
    if isEmpty:
        print('skipping repo {} because empty.'.format(repo))
    elif os.path.isdir(repo):
        print('repo {} exisits updating'.format(repo))
        repo = Repo(os.path.abspath(repo));
        repo.git.pull()
    else:
        print('repo {} does not exist checking out'.format(repo))
        subprocess.check_output('gh repo clone Geonovum/{}'.format(repo),shell=True)
