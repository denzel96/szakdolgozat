from github import Github


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


def get_diffs(repo, commit):
    size = len(commit.parents)
    for i in range(size):
        return repo.compare(commit.commit.sha,
                            commit.parents[i].sha).diff_url


##########

pw = '|)aneeka:)XD11'
g = Github('denzel96', pw)

codeBase = [
    'TucoBenedictoPacificoJuanMariaRamirez/fotav'
    # ,
    # 'Microsoft/pyright'
    # ,
    # 'achael/eht-imaging',
    # 'tensorflow/models',
    # 'TheAlgorithms/Python'
]

changes = []
for link in codeBase:
    current_repo = g.get_repo(link)
    commits = get_related_commits(link)
    i=9
    msg = get_message(commits[i])
    print(msg)
    print(get_diffs(current_repo, commits[i]))
