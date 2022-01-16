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

NOte: 1-Make sure you install git to your VM
      2- add ssh-public key to GIthub account! 

usuful codes
1- git status

2- git branch -a : 
    git branch List all of the branches in your repo. Add a <branch> argument to
create a new branch with the name <branch>.

3- git merge <branch>:
    Merge <branch> into the current branch. 

4- git log:
    Display the entire commit history using the default format.
For customization see additional options.

5- git init <directory> (-b main)
    Create empty Git repo in specified directory. Run with no
arguments to initialize the current directory as a git repository.
git commit

6- git clone <repo>
    Clone repo located at <repo> onto local machine. Original repo can be
located on the local filesystem or on a remote machine via HTTP or SSH

7- git pull <remote>:
    Fetch the specified remote’s copy of current branch and
immediately merge it into the local copy

8- git push <remote> <branch>:
    Push the branch to <remote>, along with necessary commits and
objects. Creates named branch in the remote repo if it doesn’t exist.

9- git clone ssh LINk from repo/file
    + $ git clone git@github.com:UserName/FileNAme.git (ssh LINk from repo)
    + $ cd FileOrRepoName(jump in folder)
    + $ git pull (for latest changes)

10- Changing Branch amoung the existing branches in CLI
    + $ git checkout BranchNameorMain

11- git checkout -b "BranchName" # (that want to call) creating a new branch CLI
  + $ git add fileName
  + $ git commit-m "Explanation of changes"
  + $ git push -u origin "BranchName" or main 


12- git init:
     Initialize the local directory as a Git repository.
   + $ git init -b main

usufulpage:https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet
