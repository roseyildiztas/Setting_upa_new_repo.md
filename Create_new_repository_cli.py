## Setting up a new Git Repo
## Create a new repository on the command line

touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:username/<reponame>.git
git push -u origin master


##Push an existing repository from the command line

git remote add origin git@github.com:username/<reponame>.git
git push -u origin master

git remote -v
origin https://github.com/your_username/repo_name (fetch)
origin https://github.com/your_username/repo_name (push)
  
Quick start with GitHub and   https://docs.github.com/en/get-started/quickstart/hello-world#making-and-committing-changes

