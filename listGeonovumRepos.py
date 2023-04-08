#!/usr/bin/python3
#
# https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html
#
from github import Github
import os;

f = open('docs/index.md', 'w')

f.write('''
Op dit dashboard zie je in één oogopslag alle openbare Github repositories van Geonovum.

| Naam | Omschrijving | laatste wijziging| zichtbaarheid | archief |heeft_pages|releases|views(2w)|
|------|-------------|-----------|----|----|---|---|----|
''')

#
# Het script maakt gebruik van de GitHub API hiervoor heb je een access token nodig.
# Dit script gaat ervan uit dat deze in een environment variable staat.
#
git = Github(os.environ['GITHUBSECRET'])
org = git.get_organization('Geonovum')

#
# Itereer over alle repositories van Geonovum.
#
for repo in org.get_repos():
    #
    # Sla private repos over.
    #
    if repo.private:
        continue

    releases = ""
    for release in repo.get_releases():
        releases = releases + " " + release.tag_name

    description = repo.description
    if description is not None:
        description = description.replace('|',' ')
    else:
        description = ""

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

    views = repo.get_views_traffic('week')

    f.write("| [{}]({}) | {} | {} | {} | {} | {} | {} | {} |\n".format(
        repo.name,
        repo.html_url,
        description,
        repo.pushed_at.date(),
        zichtbaarheid,
        archief,
        pages,
        releases,
        views['count']))
