#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools

class SigslotConan(ConanFile):
    name = "sigslot"
    version = "1.2.0"
    license = "https://github.com/palacaze/sigslot/blob/master/LICENSE"
    author = "https://github.com/palacaze/sigslot/graphs/contributors"
    url = "https://github.com/palacaze/sigslot.git"
    description = "header-only, thread safe implementation of signal-slots for C++"
	no_copy_source = True
    exports = "*"

    def source(self):
        self.run("git clone %s %s" % (self.source_url, self.name))
        self.run("cd %s && git checkout" % (self.name))

    def package(self):
        self.copy("*.h")


