#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf vivaldi-beta_%s-4_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
    for i in ["16", "22", "24", "32", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "product_logo_%s.png" % i, "vivaldi-beta.png")
    
