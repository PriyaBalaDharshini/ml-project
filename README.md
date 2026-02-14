GIT AND GITHUB WORKFLOW FOR ML PROJECT (WINDOWS CMD)

Project Files:
train.py – model training script
predict.py – prediction script
utils.py – helper functions
README.md – documentation

STAGE 1: BASIC SETUP (FOUNDATION)

Step 1: Create project folder and move into it

Command:
mkdir ml-project
cd ml-project

Explanation:
Creates a new folder named ml-project and moves into it.

Step 2: Initialize Git repository

Command:
git init

Explanation:
Initializes an empty Git repository in the project folder.

Step 3: Create project files (Windows CMD)

Commands:
type nul > train.py
type nul > predict.py
type nul > utils.py
type nul > README.md

Explanation:
Creates empty project files inside the folder.

Step 4: Check repository status

Command:
git status

Explanation:
Displays current state of the repository and shows untracked files.

STAGE 2: VERSION CONTROL WORKFLOW (APPLICATION)

Assume code has been added to train.py and utils.py.

Step 1: Stage only specific files

Command:
git add train.py utils.py

Explanation:
Stages only the modified files train.py and utils.py.

Step 2: Commit the changes

Command:
git commit -m "Add training script and utilities"

Explanation:
Creates a snapshot of staged changes with a meaningful message.

Step 3: Rename branch to main

Command:
git branch -M main

Explanation:
Renames the current branch to main.

Step 4: Create repository on GitHub

Manual Steps:

Go to GitHub

Click New Repository

Name it ml-project

Do NOT initialize with README

Step 5: Link local repository to GitHub

Command:
https://github.com/PriyaBalaDharshini/ml-project

Explanation:
Connects the local repository to the remote GitHub repository.

Step 6: Push to GitHub

Command:
git push -u origin main

Explanation:
Pushes commits to GitHub and sets upstream tracking branch.

STAGE 3: COLLABORATIVE WORKFLOW (TEAM ENVIRONMENT)

Scenario:
Remote repository has updated predict.py and README.md.
Local repository has modified utils.py and new config.py (uncommitted).

Step 1: Check current status

Command:
git status

Explanation:
Shows modified and untracked files.

Step 2: Stage local changes

Command:
git add utils.py config.py

Explanation:
Stages modified and new files.

Step 3: Commit local work

Command:
git commit -m "Update utils and add config file"

Explanation:
Saves local work before pulling remote changes.
Best practice: Always commit before pulling.

Step 4: Pull latest changes from GitHub

Command:
git pull origin main

Explanation:
Fetches and merges teammate’s updates from GitHub.

Step 5: Push updated project to GitHub

Command:
git push origin main

Explanation:
Uploads combined changes (local + remote) to GitHub.

POTENTIAL ISSUES AND SOLUTIONS

Uncommitted changes error

If you try to pull without committing, Git may show:
"Your local changes would be overwritten"

Solution:
git add .
git commit -m "Save changes before pull"
git pull origin main

Merge conflict

If both developers modify the same file:

Open conflicted file

Manually resolve conflict

Then run:
git add filename
git commit

BEST PRACTICES FOR COLLABORATION

Pull latest changes before starting new work.

Commit frequently with meaningful messages.

Avoid force push in shared branches.

Keep commits small and focused.

Always check git status before committing.
