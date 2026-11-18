# 1. Check Git installation
git --version

# 2. Configure Git (use your own name and email)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list

# 3. Create a project folder
mkdir ml-project
cd ml-project

# 4. Create sample project files
New-Item train.py -ItemType File
New-Item requirements.txt -ItemType File
New-Item config.yaml -ItemType File

# 5. Initialize Git repository
git init
git branch -M main

# 6. Add and commit files
git add .
git commit -m "Add initial training script and configuration"

# 7. Create a feature branch
git branch feature-preprocessing
git checkout feature-preprocessing

# 8. Create a preprocessing file
New-Item preprocess.py -ItemType File

# 9. Commit the new file
git add preprocess.py
git commit -m "Add data preprocessing module"

# 10. Switch to main and merge
git checkout main
git merge feature-preprocessing

# 11. Connect your GitHub repository
# Replace the URL with your own GitHub repository URL
git remote add origin https://github.com/username/ml-project.git

# 12. Push project to GitHub
git push -u origin main

# 13. Check repository status and history
git status
git log --oneline --graph --all

# 14. Other useful Git commands
git branch
git diff
git pull
git --help
