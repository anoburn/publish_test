import json
from urllib.request import urlopen
from distutils.version import StrictVersion

with open("version.txt", "r") as f:
	version = f.readline()

def test_version_unique():
	url = "https://test.pypi.org/pypi/example-pkg-sschaum-2/json"
	data = json.load(urlopen(url))
	versions = list(data["releases"].keys())

	assert version not in versions

def test_release_version():
	with open("github_version.txt", "r") as f:
		github_version = f.readline()
	
	assert version == github_version
