import os
from detect_os import detect_os
from command_runner import command

GITHUB_WORKSPACE = os.environ.get('GITHUB_WORKSPACE')    # path to repo
GITHUB_PATH = os.environ.get('GITHUB_PATH')      # env path
GITHUB_ACTION = os.environ.get('GITHUB_ACTION', '')  # run or .. 
GITHUB_JAVA_HOME = os.environ.get('GITHUB_JAVA_HOME', '') 
GITHUB_RUN_NUMBER = os.environ.get('GITHUB_RUN_NUMBER', '')
RUNNER_NAME = os.environ.get('RUNNER_NAME', '')
GITHUB_REPOSITORY_OWNER_ID = os.environ.get('GITHUB_REPOSITORY_OWNER_ID', '')
GITHUB_TRIGGERING_ACTOR = os.environ.get('GITHUB_TRIGGERING_ACTOR', '')
RUNNER_OS = os.environ.get('RUNNER_OS', '')
GITHUB_EVENT_NAME = os.environ.get('GITHUB_EVENT_NAME', '')
GITHUB_RUN_ID = os.environ.get('GITHUB_RUN_ID', '')
RUNNER_USER = os.environ.get('RUNNER_USER', '')
GITHUB_JOB = os.environ.get('GITHUB_JOB', '')
GITHUB_REF_NAME = os.environ.get('GITHUB_REF_NAME', '')
GITHUB_WORKFLOW_SHA = os.environ.get('GITHUB_WORKFLOW_SHA', '')
GITHUB_ACTOR_ID = os.environ.get('GITHUB_ACTOR_ID', '')
CHROME_BIN = os.environ.get('CHROME_BIN', '')
GITHUB_RETENTION_DAYS = os.environ.get('GITHUB_RETENTION_DAYS', '')
GITHUB_REPOSITORY_OWNER = os.environ.get('GITHUB_REPOSITORY_OWNER', '')
GITHUB_WORKFLOW = os.environ.get('GITHUB_WORKFLOW', '')
ImageOS = os.environ.get('ImageOS', '')
GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY', '')
 
def export_to_github_env(exp_path):
    if detect_os() == "windows":
        path_seprator = ";"
    elif detect_os() == "unix" or detect_os() == "macos":
        path_seprator = ":"
    
    command(f'echo {exp_path} >> $GITHUB_PATH')
    #with open(GITHUB_PATH, 'a') as f:
    #    f.writeLines(f"{exp_path}")