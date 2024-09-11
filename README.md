# Progress-Website
A website used to track your daily programming progress.

# Table of contents
* [Contributing Guide](https://github.com/z1ppyyy/Progress-Website?tab=readme-ov-file#contributing)
* [Release Date](https://github.com/z1ppyyy/Progress-Website?tab=readme-ov-file#contributing)
* [Made By](https://github.com/z1ppyyy/Progress-Website?tab=readme-ov-file#contributing)

# Contributing
To contribute to the project, you need to follow these instructions.

## Collaborators
If you are a collaborator of the Progress-Website repository, here's how you should implement new features:

### Part 1
#### 1.1 Make sure you're on the correct branch (master):
  ```shell
  git checkout master
  ```

#### 1.2 Update your branch:
  ```shell
  git pull origin master
  ```

#### 1.3 Create a new branch for your feature:
  ```shell
  git checkout -b feature-branch-name
  ```
  Replace feature-branch-name with a descriptive name for your feature.

#### 1.4 Push the new branch to the remote repository:
  ```shell
  git push -u origin feature-branch-name
  ```
  Now, you have a new branch where you can start working on your feature independently of the main branch.

Once you've finished the first part and your feature is ready, you can proceed to the next part

### Part 2
#### 2.1 Create a Pull Request (PR):
* Go to your repository on GitHub.
* You’ll see an option to create a Pull Request for your feature branch.
* Select the branch you want to merge into (master).
* Add a description of the changes, and submit the PR.

#### 2.2 Once the PR is submitted, your team can review the code and provide feedback.

#### 2.3 Wait till the PR is merged with the master branch, or merge it yourself if you have the right to.

#### 2.4 Delete the feature branch (optional but recommended):
  ```shell
  git branch -d feature-branch-name
  git push origin --delete feature-branch-name
  ```
  This keeps the branches organized

## Non-Collaborators
If you are not marked as collaborator of this project, here are the steps for you:

### Part 1: Fork the Repository and Create a Feature Branch

#### 1.1 Fork the repository:
- Go to the **Progress-Website** repository on GitHub.
- Click the "Fork" button at the top right to create your own copy of the repository.

#### 1.2 Clone your forked repository:
  ```shell
  git clone https://github.com/your-username/Progress-Website.git
  ```
Replace your-username with your GitHub username. This will download your forked copy to your local machine.

#### 1.3 Navigate to the cloned repository:
  ```shell
  cd Progress-Website
  ```

#### 1.4 Make sure you're on the master branch:
  ```shell
  git checkout master
  ```
#### 1.5 Create a new branch for your feature:
  ```shell
  git checkout -b feature-branch-name
  ```
Replace feature-branch-name with a descriptive name for your new feature.

#### 1.6 Push your new branch to your fork:
  ```shell
  git push -u origin feature-branch-name
  ```
Now, you can start making changes to your feature branch.

### Part 2: Submit a Pull Request (PR)

#### 2.1 Create a Pull Request:
* Go to your forked repository on GitHub.
* Click on the "Pull Request" button.
* Set the base repository to the original Progress-Website repository and the base branch to master.
* Add a description of the changes you've made, and submit the PR.

#### 2.2 Wait for review:
Once the PR is submitted, the repository maintainers will review your code and may provide feedback or request changes.

#### 2.3 After PR approval:
Once your PR is approved and merged into the master branch of the original repository, your changes will become part of the project.

### Part 3: Sync Your Fork (Optional but Recommended)
To keep your fork up-to-date with the original repository, follow these steps:

#### 3.1 Add the original repository as an upstream remote:
  ```shell
  git remote add upstream https://github.com/z1ppyyy/Progress-Website.git
  ```
Replace original-owner with the GitHub username of the repository owner.

#### 3.2 Fetch the latest changes from the upstream repository:
  ```shell
  git fetch upstream
  ```
#### 3.3 Checkout your local master branch:
  ```shell
  git checkout master
  ```
#### 3.4 Merge changes from upstream/master into your local master branch:
  ```shell
  git merge upstream/master
  ```
This will sync your local master branch with the latest changes from the original repository.

# Release Date
The release is expected by the end of September 🏆

# Made By
Made by [@pinkozz](https://github.com/pinkozz) and [@z1ppyyy](https://github.com/z1ppyyy)