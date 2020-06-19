# Minimal repro of env_info pollution of build dependencies in cross-compilation.

## To reproduce:

**WARNING: THIS WILL OVERWRITE YOUR EXISTING SETTINGS.YML**

* `conan config install .`
* `conan export ./MyInstaller test/test`
* `conan export ./MyTool test/test`
* `conan create ./MyLib test/test --profile:build ./build --profile:host ./host --build`

### In conan 1.26.0, observe the following result:

```
ERROR: MyTool/1.0@test/test: Error in build() method, line 17
        raise tools.ConanException("MyInstaller requirement is being applied to %s in profile %s" % (self.name, self.settings.context))
        ConanException: MyInstaller requirement is being applied to MyTool in profile 'build'
```