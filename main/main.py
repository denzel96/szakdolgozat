from github import Github

g = Github('81a93fa01e526bacf1f8b1f93706bfc50c14b0cf')

repoList = g.get_repos()
# c = g.get_repos().totalCount
# print('Num of repos: ', c)
for i in range(0, 1000):
    print(i, ' ', len(g.get_repos().get_page(i)))
# for repo in repoList:
#     c = repo.get_commits()
#     print(len(c.get_page(2)))

    # for i in range(0, len(a)):
    #     print(c)
    #     print(c.get_page(i))
        # print(c.get_page(0)[0])
        # print(c.get_page(0)[0].commit)
        # print(c.get_page(0)[0].commit.message)
