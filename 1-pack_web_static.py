#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime
import os


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
