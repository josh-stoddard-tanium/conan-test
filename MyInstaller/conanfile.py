#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile


class MyInstaller(ConanFile):
    name = "MyInstaller"
    version = "1.0"

    def package_info(self):
        self.env_info.HOST_CONTEXT = "True"