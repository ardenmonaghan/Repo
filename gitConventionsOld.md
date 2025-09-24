git add .
git commit -m "message"
git push 

# Git Conventions

### 1.0 General Commands

```
Cloning Repo: git clone <repo-url>
```

#### Make sure you are up to date with the main branch.

```
git checkout main
git pull origin main
```

### 1.1 Feature Branches

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

#### 1.5 Pull Request Guidelines

Open a Pull Request (PR) to develop
Go to your repository on GitHub.
Open a PR from feature/[feature-name] → develop.
Request at least one peer review.
Address any requested changes.

### 1.6 Deleting Branches

- You can delete a branch on github first, this will delete it in the remote repository
- After that you can perform git branch -D [branch-name] to delete it locally on your computer. 

### 1.7 Pulling Code.

- Often you will be pulling your production code from the main branch using git pull origin main
- If 2 people are working on a feature branch (not recommended) you can use git pull origin feature/[feature-name]