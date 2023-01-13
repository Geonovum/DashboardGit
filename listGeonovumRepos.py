#!/usr/bin/python3
from github import Github
import os;

f = open('index.md', 'w')

f.write('''
# Dashboard met Geonovum repos

Dit is het begin van een dashboard waarop je in één oogopslag een aantal gegevens van de Github repos van Geonovum kunt zien.
''')

# using an access token
#
# Een github access should be provided via the environment.
#
git = Github(os.environ['GITHUBSECRET'])
org = git.get_organization('Geonovum')

#
for repo in org.get_repos():
    releases = ""
    for release in repo.get_releases():
        releases = releases + " " + release.tag_name


    if not repo.private:
        f.write("## " + repo.name + "\n" )
        f.write("\n")
        f.write("|Property|Value|\n")
        f.write("|--------|-----|\n")
        f.write("|description|" + str(repo.description) + "|\n")
        f.write("|last push|" + str(repo.pushed_at) + "|\n")
        if releases != "":
            f.write("|releases|" + releases + "|\n")
        f.write("\n")
