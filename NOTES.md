# Notes - Git + Python Practice Lab

This file documents all the steps I performed, the commands I used, and the errors/learnings I encountered during the Git practice.

## Section A: Basic Setup

**Steps:**
1. Created a new GitHub repository named `python-git-lab`.
2. Cloned it locally and initialized with a `README.md`.

**Commands:**
- echo "# fwdevedefv" >> README.md
- git init
- git add README.md
- git commit -m "first commit - added README.md"
- git branch -M main
- git remote add origin https://github.com/hrishi-2407/python-git-lab.git
- git push -u origin main

## Section B: Python Basics + Git Tracking

**Steps:**

1. Created calculator.py with add(a, b) function.
2. Staged & committed file.
3. Pushed to main.

**Commands:**
- git add calculator.py
- git commit -m "Added calculator.py with add function"
- git push origin main

## Section C: Branching & PR

**Steps:**

1. Created branch feature/subtraction.
2. Added subtract(a, b) in calculator.py.
3. Committed & pushed.
4. Opened PR from GitHub UI.

**Commands:**
- git checkout -b feature/subtraction
- ## edited calculator.py
- git add calculator.py
- git commit -m "Added subtract function"
- git push origin feature/subtraction

## Section D: Stash & Reuse

**Steps:**

1. Began writing multiply(a, b) but left incomplete.
2. Stashed unfinished work with a message.
3. Switched to main.
4. Created new branch feature/multiplication.
5. Applied stash and completed multiply(a, b).
6. Committed & pushed.

**Commands:**
- ## unfinished multiply work
- git stash push -m "WIP multiply function"
- git checkout main
- git checkout -b feature/multiplication
- git stash list
- git stash pop
- git add calculator.py
- git commit -m "Add multiply function"
- git push origin feature/multiplication

## Section E: Reverting & Resetting

**Steps:**

1. Merged subtraction PR into main on GitHub.
2. Pulled latest changes.
3. Reverted commit for subtract().
4. Added a mistake commit (print("oops")).
5. Removed it using reset.

**Commands:**
- git pull origin main
- git log --oneline
- git revert <commit_hash_of_subtract>
- git add calculator.py
- git commit -m "Added unnecessary print"
- git reset --hard HEAD~1

## Section F: Merge Conflicts

**Steps:***

1. Created branch feature/conflict-A, added conflict.py with "Hello from A".
2. Committed & pushed.
3. Created branch feature/conflict-B from main, added "Hello from B".
4. Committed & pushed.
5. Merged feature/conflict-A into main.
6. Tried merging feature/conflict-B into main → conflict.
7. Resolved conflict locally, chose correct version, committed.

**Commands:**
- git checkout -b feature/conflict-A
- git add conflict.py
- git commit -m "Add conflict.py from A"
- git push origin feature/conflict-A

- git checkout main
- git checkout -b feature/conflict-B
- git add conflict.py
- git commit -m "Add conflict.py from B"
- git push origin feature/conflict-B

- ## merge steps
- git checkout main
- git merge feature/conflict-A
- git push origin main

- git merge feature/conflict-B
- ## resolved conflict manually in conflict.py
- git add conflict.py
- git commit -m "Resolve merge conflict between A and B"
- git push origin main

## Final Learnings

- Practiced full Git workflow: branch, PR, stash, revert, reset, merge conflicts.
- Understood difference between temporary stashes vs permanent commits.
- Learned that reset rewrites history, revert preserves history.
- Gained confidence in handling merge conflicts in real scenarios
