#!/usr/bin/env python3

import sys
import cmd

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()
    ret = cmd.exec(sys.argv[1:])
    exit(ret)

