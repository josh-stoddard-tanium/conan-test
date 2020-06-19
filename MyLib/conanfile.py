#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class MyLib(ConanFile):
    name = "MyLib"
    version = "1.0"
    settings = "context"

    def build_requirements(self):
        self.build_requires("MyTool/1.0@test/test")

    def build(self):
        if self.settings.context == "host":
            if ("MyInstaller" not in self.deps_env_info.deps) or (not self.deps_env_info["MyInstaller"].HOST_CONTEXT):
                raise tools.ConanException("MyInstaller requirement is not being applied to %s in profile '%s'" % (self.name, self.settings.context))
        else:
            raise tools.ConanException("%s built using profile %s incorrectly" % (self.name, self.settings.context))
        self.output.info("%s built using profile %s as expected" % (self.name, self.settings.context))
