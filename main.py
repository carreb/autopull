from importlib.resources import contents
from github import Github
from time import sleep
from datetime import datetime
import git
import os
import configparser


#var
config = configparser.ConfigParser()
config.read('config.ini')
info = config['info']
repo_name = info['repo-name']
owner_username = info['owner-username']
token = info['token']
git_dir = "./" + repo_name
git = git.cmd.Git(git_dir)
g = Github(token)
repo = g.get_repo(owner_username+"/"+repo_name)
filename = info['filename']
sleepamount = int(info['sleep-amount'])

def startup():
    global updatefile
    global doneworking
    doneworking = False
    try:
        updatefile = repo.get_contents(filename)
        print("Updatefile found!")
        doneworking = True
    except:
        print("Updatefile not found... Creating one")
        doneworking = False
        try:
          repo.create_file(filename, "[AUTOMATED] Create updatefile", "hello world", branch="main")
          print("Successfully created updatefile!")
          doneworking = True
        except:
           print("Failed to create updatefile!")
           exit()
startup()


def check():
    while True:
        os.system("cls")
        now = str(datetime.now())
        contents = repo.get_contents("")
        try:
          updatefile = repo.get_contents(filename)
        except:
            print("[" + now + "] There are no updates!")
        print("[" + now + "] Checking for updates...")
        for ContentFile in contents:
            if ContentFile.name == filename:
                os.system('cls')
                print("[" + now + "] Update file found!")
                print("[" + now + "] Removing update file...")
                try:
                    repo.delete_file(updatefile.path, "[AUTOMATED] Removed update file", updatefile.sha, branch="main")
                    print("[" + now + "] Update file removed!")
                    print("[" + now + "] Attempting to pull repo...")
                    try:
                        git.pull()
                        print("[" + now + "] Repo pulled!")
                    except:
                        print("[" + now + "]" " Failed to pull repo! Recreating update file to try again...")
                        repo.create_file(filename, "[AUTOMATED] Error occurred while pulling.", "hello world", branch="main")
                except:
                    print("[" + now + "] Error occurred while removing update file!")
        sleep(sleepamount)
sleep(5)
if doneworking == True:
    check()
