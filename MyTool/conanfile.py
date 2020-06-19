#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class MyTool(ConanFile):
    name = "MyTool"
    version = "1.0"
    settings = "context"

    def build(self):
        if self.settings.context == "host":
            raise tools.ConanException("%s built using profile %s incorrectly" % (self.name, self.settings.context))
        else:
            if "MyInstaller" in self.deps_env_info.deps:
                raise tools.ConanException("MyInstaller requirement is being applied to %s in profile '%s'" % (self.name, self.settings.context))
        self.output.info("%s built using profile %s as expected" % (self.name, self.settings.context))