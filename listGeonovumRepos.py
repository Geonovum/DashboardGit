#!/usr/bin/python3
#
# https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html
#
from github import Github
import os;

f = open('index.md', 'w')

f.write('''
# Dashboard met Geonovum repos

Dit is het begin van een dashboard waarop je in één oogopslag een aantal gegevens van de Github repos van Geonovum kunt zien.

| Naam | Omschrijving | laatste wijziging| zichtbaarheid | archief |heeft_pages|
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

    html_url = repo.html_url

    description = repo.description
    if description is not None:
        description = description.replace('|',' ')

    if repo.has_pages:
        pages = "[pages](https://geonovum.github.io/{}/)".format(repo.name)
    else:
        pages = "";
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
        f.write("| [{}]({}) | {} | {} | {} | {} | {} |\n".format(repo.name,html_url,description,repo.pushed_at,zichtbaarheid,archief,pages))
    #if releases != "":
    #f.write("|releases|" + releases + "|\n")

