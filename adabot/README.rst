
Adafruit Adabot
============

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

AdaBot is a friendly helper bot that works across the web to make people's
lives better. It focuses on those contributing to Adafruit's variety of
projects including CircuitPython.

Setup
=======

Here are the instructions for one time setup. Its simpler to start once
everything is installed.

Debian/Ubuntu Dependencies
+++++++++++++++++++++++++++

.. code-block:: shell

    sudo apt-get update # make sure you have the latest packages
    sudo apt-get upgrade # make sure already installed packages are latest
    sudo apt-get install git python3 python3-venv python3-pip screen

Adabot
++++++++++

Once the dependencies are installed, now clone the git repo into your home directory.

.. code-block:: shell

    git clone https://github.com/adafruit/adabot.git
    cd adabot

First, set up a virtual environment and install the deps.

.. code-block:: shell

  python3 -m venv .env
  source .env/bin/activate
  pip install -r requirements.txt

Secrets!
+++++++++

Adabot needs a few secrets to do her work. Never, ever check these into source
control!

They are stored as environment variables in ``env.sh``.

So, copy the example ``template-env.sh``, edit it and save it as ``env.sh``.

.. code-block:: shell

    cp template-env.sh env.sh
    nano env.sh

Do CTRL-X to exit and press Y to save the file before exiting.

Git
+++++++++

Adabot can automatically commit information so git must know an email and name
for the author.

.. code-block:: shell

    git config --global user.email "<adabot's email>"
    git config --global user.name "Adafruit Adabot"
    git config --global credential.helper 'store --file ~/.adabot-git-credentials'
    git push

The git push won't actually push anything but it prompt for the bot's username
and password. These will be stored in the ~/.adabot-git-credentials file which
makes this not very secure. Make sure your OAUTH token has only the permissions
it needs in case it ends up in someone else's hands.

Usage Example
=============

To run Adabot we'll use screen to manage all of the individual pieces. Luckily,
we have a screenrc file that manages starting everything up.

.. code-block:: shell

    screen -c adabot.screenrc

This command will return back to your prompt with something like
``[detached from 10866.pts-0.raspberrypi]``. This means that Rosie is now
running within screen session behind the scenes. You can view output of it by
attaching to the screen with:

.. code-block:: shell

    screen -r

Once reattached you can stop everything by CTRL-Cing repeatedly or detach again
with CTRL-A then D. If any errors occur, a sleep command will be run so you can
view the output before screen shuts down.

You can also run adabot without using screen. To run the library statistics and validation script you must be inside this cloned
adabot directory and run the following command:

.. code-block:: shell

    python3 -m adabot.circuitpython_libraries

Ensure you have set BOTH the Github access token and Travis token environment
variables beforehand--see the template-env.sh for the name and where to get tokens.

Applying Patches To All CircuitPython Libraries
================================================
To apply a patch to all CircuitPython libraries (only guaranteed for files shared
among all libraries, such as those included in the cookiecutter (e.g. README.rst, etc),
do the following:

1. Apply your update(s) to any library as normal, using ``git commit``. It is recommended to
give a short, detailed description of the patch. This description will be used by the next
step for both the name of the patchfile and the subsequent patch messages.

2. Create a patch file using `git format-patch <https://git-scm.com/docs/git-format-patch>`_.
There are many techniques to using `git format-patch`; choose the one that makes
sense for your updates. As a general usage example, ``format-patch -n`` will create patches
for ``n`` number of commits starting with the most recent:

.. code-block:: shell

    # creates a patch file based on the last commit
    git format-patch -1

    # creates patch files based on the last 5 commits
    git format-patch -5

    # creates a patch file with zero lines of context (to eliminate any unique
    # text that will cause the patch to not be applicable). must use
    # 'git apply --unidiff-zero' flag to apply the patch.
    git format-patch -1 -U0

3. Place the new patch file into the ``adabot/patches`` directory on a fork of the
adafruit/adabot repository, and ``git commit`` with a description of the patch(es).

4. Submit a Pull Request (PR) to the adafruit/adabot repository from the updated fork.

5. Run the patch update script after the PR has been merged.


To run the patch update script you must be inside this cloned adabot directory and
run the following command:

.. code-block:: shell

    # note: ensure the local clone is current with the github repo that contains the patch(es)
    # by using git pull before running the script.
    python3 -m adabot.circuitpython_library_patches

    # The 'circuitpython_library_patches' script accepts command line arguments. Use
    # the help argument to display usage.
    python3 -m adabot.circuitpython_library_patches -h

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_adabot/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
