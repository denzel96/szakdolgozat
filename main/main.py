from github import Github

pw = '|)aneeka:)XD11'
g = Github('denzel96', pw)

codeBase = [
    'https://github.com/Microsoft/pyright',
    'https://github.com/achael/eht-imaging',
    'https://github.com/tensorflow/models',
    'https://github.com/TheAlgorithms/Python'
]


def get_commits():
    current_repo = g.get_repo('Microsoft/pyright')
    cList = current_repo.get_commits()
    print('asd', cList)

    for p in cList:
        comm = p.get_comments()
        print('asd')
        for c in comm:
            print(c)
        # print(p.get_message())


get_commits()

# repoList = g.get_repos()
#
# print(g.get_repos())
# for repo in repoList:
#     commits = repo.get_commits()
#
#     i = 0
#     for commit in commits:
#         pages = commit.get_page(i)
#         i = i+1
#
#         print(pages)
#

# for repo in repoList:
#     c = repo.get_commits()
#     print(len(c.get_page(2)))

# for i in range(0, len(a)):
#     print(c)
#     print(c.get_page(i))
# print(c.get_page(0)[0])
# print(c.get_page(0)[0].commit)
# print(c.get_page(0)[0].commit.message)
