# Git Conventions

### 0.0 General Information

- Its good to think about git as a tool for version control.
- Github is a platform that allows for code to be uploaded to something similar to the cloud and then able to be brought to your local machine where you manage it and then you can upload changes back to the cloud.

#### What is our main flow?

- Currently you've likely been using

```
git add .
git commit -m "message"
git push
```
- then you see all your code reflected in github. 

### 1.0 General Commands

```
Cloning Repo: git clone <repo-url>
```

#### Make sure you are up to date with the develop branch.

```
git checkout develop
git pull origin develop
```

#### You can also pull from main to get the latest working version. 

```
git checkout main
git pull origin main
```

#### If you are working on a feature branch, you can pull from develop to get the latest changes.

```
git checkout feature/[feature-name] - The branch exists so we switch to it 
git pull origin develop - this updates the changes from develop into your feature branch.
```

### 1.1 Feature Branches

#### What are feature branches?
- Git branches start from origin. this includes main, which is a starting branch.
- When you say something like git push origin main it means bring all my remote code from the main branch to the main remote branch.

#### Demonstration below on how to create a feature branch locally and then push it to our remote repository. 

- **Feature branches:** `feature/[feature-name]`
- Please pull and push so we don't have duplicates.

#### Create a new feature branch.
```
git checkout -b feature/[feature-name]
```
#### Push the branch to the remote repository.
```
git push origin feature/[feature-name]
```

#### Switching between branches

```
git checkout [branch-name]
```

#### Checking what branches you have locally

```
git branch
```

#### Checking what branches you have remotely

```
git branch -r
```

- Note: We push to origin, as when you create your repo main is configured to origin, thats why you can do git push
- But the new branch you created isn't automatically known to be configed to origin, so you need to explicitly state that you want to bring your remote branch code to origin.

### 1.2 Commit Message Guidelines.

Follow this format:
```
[type]: [Short Summary]

[Optional Detailed Explanation]
```
Example:
```
feat: Implement user authentication

- Added JWT-based authentication
- Implemented login/logout functionality
```

### 1.3 Commit Types

| Type      | Description |
|-----------|------------|
| feat      | A new feature |
| fix       | A bug fix |
| docs      | Documentation changes |
| style     | Code formatting, no logic changes |
| refactor  | Code refactoring without changing functionality |
| perf      | Performance improvements |
| test      | Adding or modifying tests |
| chore     | Minor changes, dependencies, scripts |

### 1.4 Branching Strategy

#### Main Branches
- `main` - Production-ready code only.
- `develop` - Development branch, for code sprints. 

#### 1.5 Pull Request Guidelines

Open a Pull Request (PR) to develop
Go to your repository on GitHub.
Open a PR from feature/[feature-name] → develop.
Request at least one peer review.
Address any requested changes.

#### 1.6 Merge Conflicts.
- Merge conflicts will open happen when you try to merge two branches using a PR.
- You will need to resolve the conflicts manually. by deciding which code to keep.
- Go to PR on github > and then click on the two branches you want to compare > Build pull request

#### 1.7 Deleting branches 
- You can delete a branch on github first, this will delete it in the remote repository
- After that you can perform 
```
git branch -D [branch-name] 
```
- This will delete it locally on your computer. 

#### 1.8 Common Branch Mistake
- When you work on a feature branch you push your changes to your repo, but you dont have all the changes locally first
```
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

- This is because you dont have the latest changes from the remote repository.

- To solve this issue 
```
git pull --rebase origin [branch-name]
```