#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ['34.74.39.127', '35.196.159.36']


def do_pack():
    """Function do_pack
    """
    dtime = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(dtime)
    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(archive_path))
    if os.path.exists(archive_path):
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """Function do_deploy
    """
    if os.path.exists(archive_path):
        filename = archive_path[9:-4]
        dest = '/data/web_static/releases/{}'.format(filename)
        put(archive_path, '/tmp')
        run("mkdir -p {}".format(dest))
        run("tar -xzf /tmp/{}.tgz -C {}".format(filename, dest))
        run("rm /tmp/{}.tgz".format(filename))
        run("mv {}/web_static/* {}".format(dest, dest))
        run("rm -rf {}/web_static".format(dest))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest))
        print("New version deployed!")
        return True
    else:
        return False
