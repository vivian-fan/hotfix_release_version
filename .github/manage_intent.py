# This script is delete intent into intent_management_file
import os
import sys
import shutil
import yaml
import git
import json

def get_remote():
    username = "vivian-fan"
    password = sys.argv[1]
    remote = f"https://{username}:{password}@github.com/vivian-fan/hotfix_release_version.git"
    return remote


def get_clone_repo(remote, path, branch):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    clone_repo = git.Repo.clone_from(remote, path, branch=branch)
    return clone_repo

def get_intents(path):
    with open(path + "/.github/intent.yml", "r") as intent_mgmt_file:
        intent_mgmt_content = yaml.safe_load(intent_mgmt_file)
    return intent_mgmt_content

remote = get_remote()
# Clone master branch
# Read intent_list from /.github/intent.yml as master_intents
# master_intents = ???
# delete the intent in the released_intents from master_intents
# Push back to master
master_path = "./master"
clone_repo_master = get_clone_repo(remote, master_path, "master")
master_intents = get_intents(master_path)

# Clone develop branch
# Read intent_list from /.github/intent.yml as dev_intents
# dev_intents = ???
# delete the intent in the released_intents from dev_intents
# Push back to develop
dev_path = "./develop"
clone_repo_master = get_clone_repo(remote, dev_path, "develop")
dev_intents = get_intents(dev_path)

# Clone latest_release branch
# Read intent_list from /.github/intent.yml as released_intents
# released_intents = ???
release_path = "./release"
release_branches = []
for branch in clone_repo_master.refs:
    if branch.__str__().startswith("origin/production_release"):
        release_branches.append(branch.__str__())
release_branches.sort()
latest_release_branch = release_branches[-1].replace("origin/", "")
clone_repo_release = get_clone_repo(remote, release_path, latest_release_branch)
released_intents = get_intents(release_path)

print(
    "Before: ",
    "master:", master_intents, "develop:", dev_intents, "released: ", released_intents
)

# Delete released_intents from master_intents
for file in released_intents['intent']:
    for intent_dic in released_intents['intent'][file]:
        if (file in dev_intents and intent_dic in master_intents[file]):
            master_intents[file].remove(intent_dic)
        
    

# Delete released_intents from dev_intents
for file in released_intents['intent']:
    for intent_dic in released_intents['intent'][file]:
        if (file in dev_intents and intent_dic in dev_intents[file]):
            dev_intents[file].remove(intent_dic)

print(
    "After: ",
    "master:", master_intents, "develop:", dev_intents, "released: ", released_intents
)
