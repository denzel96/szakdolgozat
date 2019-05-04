# TODO diff lines starting with 'import {*\n*\n*}' should be ignored
# TODO skip already downloaded diff files
# TODO diff file encoding
#  (UnicodeEncodeError: 'charmap' codec can't encode character '\xaf' in position 3214: character maps to <undefined>)
from github import Github
import requests
from gui import show_app
import time
import math


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


def get_diff_files(repo, commit):
    this = commit.commit
    parent = commit.parents[0]

    cmp = repo.compare(parent.sha, this.sha)
    diff = requests.get(cmp.diff_url)
    diff_text = diff.text

    old = []
    for i in range(0, len(parse_diff_files(diff_text))):
        old.append(parse_diff_files(diff_text)[i][0])

    new = []
    for i in range(0, len(parse_diff_files(diff_text))):
        new.append(parse_diff_files(diff_text)[i][1])

    write_files(old, new, commit.sha)


def parse_diff_files(diff_text):
    body = diff_text.split('@@')
    data = []
    for i in range(2, len(body), 2):
        data.append(process_diff_item(body[i]))
    return data


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
    return [old_text, new_text]


def write_files(old, new, sha):
    old_filename = 'training/' + str(sha) + '.o'
    new_filename = 'training/' + str(sha) + '.n'
    old_file = open(old_filename, 'w+')
    new_file = open(new_filename, 'w+')

    old_str = '\n'.join(old)
    new_str = '\n'.join(new)

    old_file.write(old_str)
    new_file.write(new_str)


##########

pw = '|)aneeka:)XD11'
g = Github('denzel96', pw)

codeBase = [
    'TucoBenedictoPacificoJuanMariaRamirez/fotav'
    ,
    'Microsoft/pyright'
    ,
    'achael/eht-imaging',
    'tensorflow/models',
    'TheAlgorithms/Python'
]

show_app()
start = time.time()
print('Strarttime:' + str(start))
for link in codeBase:
    print(link)
    print('\tDownloading data...')
    current_repo = g.get_repo(link)
    print('\tGathering commits...')
    commits = get_related_commits(link)
    print('\t' + str(len(commits)) + ' commits found')
    print('\tCreating diff files...')

    for commit in commits:
        get_diff_files(current_repo, commit)

    print('\tDiff files are ready')

end = time.time()
print('Endtime: ' + str(end))
print('Duration : ' + str(math.floor(end-start)) + ' seconds')
