---
layout: post
title: Git 基本使用－2
categories:
  - git
tags:
  - git
image: 18.jpg
date: 2016-04-22T02:31:11.000Z
---

# GIT 基本使用

- git log -p
- git diff
- git add
- git diff HEAD
- git commit -m "Add something"
- git branch
- git checkout -b feature-A
- git branch
- git merge --no-ff feature-A
- git log --graph
- git reset
- git reflog
- git merge --no-ff fix-b
- git rebase -i HEAD-2
- git remote add
- git push
- git push -u origin feature-D
- git fetch -all
- git fetch origin refspeec

## GIT Flow

### git-flow-cheatsheet

A cheatsheet on the usage of git flow, visit <http://danielkummer.github.com/git-flow-cheatsheet/>

### GIT FLOW

Git extensions to provide high-level repository operations for Vincent Driessen's branching model. [Read more](http://nvie.com/posts/a-successful-git-branching-model/)

INIT:

```
$ git flow init
```

### TRACK DEVELOP REMOTELY ON GITHUB:

```
$ git push origin develop
```

**FEATURES:**

Use to develop new features starting from the develop branch. Merge back into develop branch waiting for a reasonable amount of features to be there before declaring it a release.

```
$ git flow feature
$ git flow feature start <name>
$ git flow feature finish <name>
```

```
usage: git flow feature [list] [-v]
       git flow feature start [-F] <name> [<base>]
       git flow feature finish [-rFk] <name|nameprefix>
       git flow feature publish <name>
       git flow feature track <name>
       git flow feature diff [<name|nameprefix>]
       git flow feature rebase [-i] [<name|nameprefix>]
       git flow feature checkout [<name|nameprefix>]
       git flow feature pull <remote> [<name>]
```

**RELEASES:**

Use to group together latest development (features) add a few finishing touches if necessary and send to production. All last changes will merge back to master and develop so new features will start from current release.

```
$ git flow release
$ git flow release start <release> [<base>]
$ git flow release finish <release>
```

```
usage: git flow release [list] [-v]
       git flow release start [-F] <version>
       git flow release finish [-Fsumpk] <version>
       git flow release publish <name>
       git flow release track <name>
```

**HOTFIXES:**

Similar to releases but the hotfix branch starts off master to avoid unvoluntary send to production of unwanted features that my be present in branches. The quick fix must be used when an important bug arises in production which must be fixed and can't wait for other features to be ready. It merges back to master and develop.

```
$ git flow hotfix
$ git flow hotfix start <release> [<base>]
$ git flow hotfix finish <release>
```

```
usage: git flow hotfix [list] [-v]
       git flow hotfix start [-F] <version> [<base>]
       git flow hotfix finish [-Fsumpk] <version>
```
