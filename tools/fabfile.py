from fabric.api import env, run, sudo, cd

env.user = 'ubuntu'
env.hosts = [] # specify host
env.key_filename = '' # specify aws pem file


def install_git():
    sudo("apt-get install git")


def checkout_git(git_ssh_path):
    with cd("/home/proj"):
        sudo("git clone %s" % git_ssh_path)


def setup_mongodb():
    sudo('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10')
    sudo('echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list')
    sudo('apt-get update')
    sudo('apt-get install -y mongodb-org')

    
def setup_nginx():
    sudo('apt-get install nginx')
    sudo("cp /home/proj/directory/tools/app_nginx /etc/nginx/sites-available/")
    sudo("service nginx restart")

    
def install_requirements(req_path):
    sudo('apt-get update')
    sudo("apt-get install memcached")
    sudo("apt-get install python-dev")
    sudo("sudo apt-get install zlib1g-dev")
    sudo("apt-get install libmemcached-dev")
    sudo("pip install -r %s" % req_path)

    
def setup_supervisor():
    sudo("apt-get install supervisor")
    sudo("cp /home/proj/directory/tools/gunicorn.conf /etc/supervisor/conf.d/")
    sudo("service supervisor restart")
    
    
def set_up():
    """
    Install requirements and setup application
    """
    
    install_git()
    checkout_git()
    setup_mongodb()
    install_requirements()
    setup_supervisor()
    setup_nginx()


def app_update():
    """
    It will pull records on server and restart servers
    """
    
    with cd("/home/proj/directory"):
        sudo("git pull origin master")
    
    sudo("service supervisor restart")
    sudo("service nginx restart")
