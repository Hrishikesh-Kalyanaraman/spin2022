#!/usr/bin/env python3
import pygit2;

repo = pygit2.Repository('.git')

print(""""<html>
<body>
<p>Hello, Roland!<p/>""")

print("""
<p>Git log is:
<pre>
TODO: add git log here
</pre>
</p>
""")

# check the last log (git log -1)
"""commit = repo[repo.head.target]
print(commit.message) """

# command for git log
last = repo[repo.head.target]
for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    print(commit.message)

print("""
</body>
</html>""")
