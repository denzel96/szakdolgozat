# TODO diff lines starting with 'import' should be ignored
from github import Github
import requests


def get_related_commits(repo_path):
    current_repo = g.get_repo(repo_path)
    cList = current_repo.get_commits()
    tuple = []

    for commit in cList:
        msg = get_message(commit)
        if 'fix' in msg \
                or 'bug' in msg \
                or 'bugfix' in msg \
                or 'patch' in msg:
            tuple.append(commit)

    return tuple


def get_message(commit):
    if commit.commit is not None:
        return commit.commit.message


def get_diff(repo, commit):
    this = commit.commit
    parent = commit.parents[0]

    cmp = repo.compare(parent.sha, this.sha)
    diff = requests.get(cmp.diff_url)
    diff_text = diff.text
    parse_diff(diff_text)


def parse_diff(diff_text):
    body = diff_text.split('@@', 1)
    infos = body[0]
    versions = process_diff_item(body[1].split('@@')[1])
    print('uj verzio:')
    print(versions[0])
    print('/////////////////////////////////')
    print('regi verzio:')
    print(versions[1])


def process_diff_item(item):
    lines = item.split('\n')
    new_version = []
    old_version = []

    for line in lines:
        if line.startswith('-'):
            old_version.append(line.split('-')[1])
        elif line.startswith('+'):
            new_version.append(line.split('+')[1])
        else:
            old_version.append(line[1:])
            new_version.append(line[1:])

    new_text = '\n'.join(new_version)
    old_text = '\n'.join(old_version)
    return [new_text, old_text]


##########

pw = '|)aneeka:)XD11'
g = Github('denzel96', pw)

codeBase = [
    # 'TucoBenedictoPacificoJuanMariaRamirez/fotav'
    # ,
    'Microsoft/pyright'
    # ,
    # 'achael/eht-imaging',
    # 'tensorflow/models',
    # 'TheAlgorithms/Python'
]

changes = []
for link in codeBase:
    # print('Loading commits for ' + link)
    current_repo = g.get_repo(link)
    commits = get_related_commits(link)
    # print('Commits loaded\n\n\n')

    # print('Message: ' + get_message(commits[0]))
    # print('end msg')
    get_diff(current_repo, commits[0])
