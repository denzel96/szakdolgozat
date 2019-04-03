from github import Github

g = Github('7d0107588539fb77a9710176f92e55eb70290881')

repo = g.get_repo("denzel96/copper")
c = repo.get_commits()
print(c)
print(c.get_page(0)[0].commit.message)
