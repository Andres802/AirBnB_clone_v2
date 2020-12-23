#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive
 from the contents of the web_static folder of
 your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import *
from os.path import exists


env.hosts = ['34.73.186.220', '35.237.108.29']


def do_deploy(archive_path):
    """Distributes an archive to your web servers
    """

    if not exists(archive_path):
        return False

    try:
        file_nametgz = archive_path.split("/")[-1]
        file_name = file_nametgz.split(".")[0]
        put(archive_path, "/tmp/{}".format(file_nametgz))
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("tar -xzf /tmp/{} -C\
            /data/web_static/releases/{}/".format(file_nametgz, file_name))

        run("rm /tmp/{}".format(file_nametgz))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))

        # Deletes the symbolic link?
        run("rm -rf /data/web_static/current")

        # Creates the symbolic link again
        run("ln -s /data/web_static/releases/{}/\
            /data/web_static/current".format(file_name))
        return True
    except Exception:
        return False
