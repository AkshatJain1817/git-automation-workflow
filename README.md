# 🚀 Git & GitHub Workflow Project

This is my **second project** in my journey through **Linux, Networking, and Git/GitHub**.
The focus of this project is to build a **strong, practical workflow around Git and GitHub**, emphasizing code quality, collaboration, and disciplined development practices.

---

## 🎯 Project Objective

The goal of this project is to simulate a **real-world development workflow** by implementing:

* Local safeguards (before code is committed or pushed)
* Standardized commit history
* Structured pull request process
* Protected main branch with enforced rules

---

## 🧩 Features Implemented

### 🧼 Pre-commit Hook

* Checks Python files before committing
* Prevents:

  * Syntax errors
  * Debug `print` statements
* Ensures only clean code is committed

---

### 🚧 Pre-push Hook

* Runs deeper checks before pushing code
* Includes:

  * Syntax validation
  * Debug print detection
  * Test execution (if available)
* Prevents broken or untested code from being shared

---

### 📝 Commit Message Validation

* Enforces a structured commit format:

```bash
type(scope): message
```

Examples:

```bash
feat(auth): add login feature
fix(api): handle null response
```

* Ensures clean, readable commit history

---

### 📄 PR (Pull Request) Template

* Provides a structured format for pull requests

* Includes:

  * Description of changes
  * Reason for changes
  * Testing details
  * Checklist

* Improves code review clarity and consistency

---

### 🛡️ GitHub Branch Protection

Configured rules for the `main` branch:

* Require pull request before merging
* Require at least 1 approval
* Dismiss stale approvals on new commits
* Require review from code owners
* Require status checks (ready for CI integration)

👉 This ensures:

* No direct pushes to `main`
* All changes are reviewed before merging

---

### 🧪 Test File (`test.py`)

* Created to validate:

  * Pre-commit hook behavior
  * Pre-push hook behavior

Used to simulate:

* Syntax errors
* Debug prints
* Successful commits

---

## 🔄 Workflow Overview

1. Developer writes code ✍️
2. **Pre-commit hook** runs → blocks bad commits
3. Commit message is validated 📝
4. Code is pushed → **pre-push hook** runs 🚧
5. Pull request is created → **PR template auto-loads** 📄
6. Review is required → **branch protection enforced** 🛡️
7. Approved PR → merged into `main` ✅

---

## 🧠 Key Learnings

* Importance of **local validation before sharing code**
* How **Git hooks** improve code quality
* Writing **meaningful commit messages**
* Structuring **professional pull requests**
* Enforcing rules using **GitHub branch protection**
* Understanding real-world **team workflows**

---

## 📌 Future Improvements

* Add CI/CD pipeline using GitHub Actions
* Automate version tagging
* Integrate linting and formatting tools
* Add CODEOWNERS for automatic reviewer assignment

---

## 🎬 Conclusion

This project focuses on building a **clean, disciplined, and professional Git workflow**.
It reflects how modern teams ensure code quality, maintainability, and collaboration.

---

✨ *This is a foundational step toward mastering real-world DevOps and software development practices.*

