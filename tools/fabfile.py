from fabric.api import env, run, sudo, cd, get, put

env.user = 'ubuntu'
env.hosts = ["ec2-54-251-162-124.ap-southeast-1.compute.amazonaws.com"]
env.key_filename = '/home/shabi/Desktop/doc/serv/myubuntu.pem'

def install_git():
    sudo("apt-get install git")
    
def checkout_git(git_ssh_path):
    with cd("/home/proj"):
        sudo("git clone %s" % git_ssh_path)
    
def install_mongodb():
    sudo('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10')
    sudo('echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list')
    sudo('apt-get update')
    sudo('apt-get install -y mongodb-org')
    
def install_nginx():
    sudo('apt-get install nginx')
    
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
    sudo("service supervisord restart")
    
def set_up():
    install_mongodb()
    install_nginx()
