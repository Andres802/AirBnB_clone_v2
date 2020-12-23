#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive
 from the contents of the web_static folder of
 your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import run, put, env
from datetime import datetime
from os.path import exists

env.hosts = ['34.73.186.220', '35.237.108.29']


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    file_1 = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if file_1.failed:
        return None
    return file_1


def do_deploy(archive_path):
    """[summary]"""
    if exists(archive_path):
        file_path = archive_path.split("/")[1]
        serv_path = "/data/web_static/releases/{}".format(
            file_path.replace(".tgz", ""))
        put('{}'.format(archive_path), '/tmp/')
        run('mkdir -p {}'.format(serv_path))
        run('tar -xzf /tmp/{} -C {}/'.format(
            file_path,
            serv_path))
        run('rm /tmp/{}'.format(file_path))
        run('mv -f {}/web_static/* {}/'.format(serv_path, serv_path))
        run('rm -rf {}/web_static'.format(
            serv_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(
            serv_path))
        return True
    else:
        return False
