#!/usr/bin/python3
from github import Github
import os;

f = open('index.md', 'w')

f.write('''
# Dashboard met Geonovum repos

Dit is het begin van een dashboard waarop je in één oogopslag een aantal gegevens van de Github repos van Geonovum kunt zien.

| Naam | Omschrijving | laatste wijziging| zichtbaarheid | archief |html-url|
|------|-------------|-----------|----|----|---|
''')

# using an access token
#
# Een github access should be provided via the environment.
#
git = Github(os.environ['GITHUBSECRET'])
org = git.get_organization('Geonovum')

#
# Itereer over alle publieke repos van Geonovum.
#
for repo in org.get_repos():
    releases = ""
    for release in repo.get_releases():
        releases = releases + " " + release.tag_name

    if not repo.archived:
        archief = "actief";
    else:
        archief = "archived";

    if not repo.private:
        zichtbaarheid = "publiek";
    else:
        zichtbaarheid = "prive";

    #
    # Only public repos should be on the dashboard.
    #
    if not repo.private:
        f.write("| {} | {} | {} | {} | {}|{}|\n".format(repo.name,repo.description,repo.pushed_at,zichtbaarheid,archief,repo.html_url))
    #if releases != "":
    #f.write("|releases|" + releases + "|\n")

