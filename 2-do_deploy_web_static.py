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


def do_deploy(archive_path):
    """create function of deploy"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        pathfix = archive_path.split("/")[-1]
        whithouttgz = pathfix.split(".")[0]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(pathfix))
        run("sudo mkdir -p {}/{}/" .format(path, whithouttgz))
        run("sudo tar -xzf /tmp/{} -C {}/{}/" .format(pathfix,
                                                      path, whithouttgz))
        run("sudo rm /tmp/{}".format(pathfix))
        run("sudo mv {}/{}/web_static/* {}/{}/".format(path,
                                                       whithouttgz,
                                                       path, whithouttgz))
        run("sudo rm -rf {}/{}/web_static" .format(path, whithouttgz))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{}/ /data/web_static/current" .format(path,
                                                                  whithouttgz))
        print("New version deployed!")
        return True
    except Exception:
        return False
