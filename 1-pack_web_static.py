#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""

    path = "versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    local("makdir -p versions")
    r = local(f"tar -cvzf {path} web_static")

    if r.failed:
        return none
    return path
