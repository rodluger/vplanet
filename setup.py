"""vplanet install script."""
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess
import os
__version__ = '0.1.0'


class CustomInstall(install):
    """Custom handler for the 'install' command."""

    def run(self):
        """Run the install."""
        try:
            super(CustomInstall, self).run()
        except TypeError:
            install.run(self)
        subprocess.check_call("make", cwd=".", shell=True)
        os.symlink(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'vplanet'),
            os.path.join(self.script_dir, 'vplanet'))


class CustomDevelop(develop):
    """Custom handler for the 'develop' command."""

    def run(self):
        """Run the install."""
        try:
            try:
                super(CustomDevelop, self).run()
            except TypeError:
                develop.run(self)
            if os.path.exists("vplot"):
                os.rmdir("vplot")
            subprocess.check_call("make test", cwd=".", shell=True)
            if os.path.exists(os.path.join(self.script_dir, 'vplanet')):
                os.remove(os.path.join(self.script_dir, 'vplanet'))
            os.symlink(os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'vplanet'),
                os.path.join(self.script_dir, 'vplanet'))
            subprocess.check_call("tests/certificate --pass", cwd=".",
                                  shell=True)
        except subprocess.CalledProcessError:
            subprocess.check_call("tests/certificate --fail", cwd=".",
                                  shell=True)


setup(name='vplanet',
      version=__version__,
      author='Virtual Planet Laboratory',
      url='https://github.com/uwvpl/',
      description='Virtual planet simulator',
      install_requires=['vplot>=0.3.1',
                        'pytest'],
      cmdclass={'install': CustomInstall,
                'develop': CustomDevelop})
