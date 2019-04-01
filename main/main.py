from github import Github

g = Github('aa15a84cfcb39f88f09c847c760d7c3d19814028')
print("hello")

for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo.full_name)

print("hello")