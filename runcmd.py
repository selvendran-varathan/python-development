import os
import subprocess
import time
import sys

def run_command(cmd):
    """
    Run a linux command and return the output.

    :Parameters:
        - `cmd` : Command to run

    :Returns:
        contents from the standard out of the command
    """

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True)
    (out, err) = p.communicate()
    return out
