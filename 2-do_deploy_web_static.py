#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
from os.path import exists

env.hosts = ['34.73.186.220', '35.237.108.29']

def do_pack():
    """function that pack archives"""
    local('mkdir -p versions')
    date = datetime.now()
    tgz_file: local('tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz web_static'
                   .format(date.year, date.month, date.day,
                           date.hour, date.minute, date.second), capture=True)

    if tgz_file.succeeded:
        return tgz_file
    return None