.PHONY: repos

all:
	python3 listGeonovumRepos.py

repos:
	(cd repos; python3 ../checkoutGeonovumRepos.py)
