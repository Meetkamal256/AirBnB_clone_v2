#!/usr/bin/python3
#!/usr/bin/env bash
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import


env.hosts = ['54.164.209.159', '34.224.94.217']
env.user = ubuntu

def do_pack():
    """function do_pack!"""

    path = f"versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

    local("makdir -p versions")
    r = local(f"tar -cvzf {path} web_static")

    if r.failed:
        return path
    return None


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the functio do_deploy
    """

    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/')

    p = archive_path.replace('.tgz',  '')
    run("mkdir -p /data/web_static/releases/{}".format(p)
    run("tar -xvf {} -C {}".format(archive_path,))

    run("rm /tmp/{}".format(archive_path))
    run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/.format(p)
