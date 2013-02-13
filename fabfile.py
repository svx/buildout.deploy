import os
import os.path
from fabric.api import env, cd, run, roles

env.roledefs = {
    'testing': ['testing.foobar.com'],
    'staging': ['staging.foobar,com'],
    'production': ['production.foobar.com']
}

#env.deploy_user = 'zopeuser'
env.user = 'zopeuser'
#env.directory = '/home/%s/sites/foobar.com/buildout' % env.deploy_user
env.directory = '/home/%s/sites/foobar.com/buildout' % env.user

def stop():
    """
    Stop the instance and zeo
    """
    with cd (env.directory):
        #run('./bin/supervisorctl shutdown all', user=env.deploy_user)
        run('./bin/supervisorctl shutdown all')

def start():
    """
    Start the instance and zeo
    """
    with cd (env.directory):
       #run('./bin/supervisord', user=env.deploy_user)
       run('./bin/supervisord')

def pull():
     """
     Do a git pull
     """
     with cd (env.directory):
        #run('nice git pull --rebase')
        run('touch foobar')

def update():
    """
    Update code on the server and restart all
    """
    #stop()
    pull()
    #start()

@roles('testing')
def deploy_testing():
    """
    Update testing
    """
    update()

@roles('staging')
def deploy_staging():
    """
    Update staging
    """
    update()

@roles('production')
def deploy_production():
    """
    Update production
    """
    update()