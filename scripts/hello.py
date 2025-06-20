#!/usr/bin/env python3
"""
A simple script that prints the current date & time
in ASCII art using pyfiglet.
"""

import datetime
from pyfiglet import Figlet

def main():
    # get now
    now = datetime.datetime.now()
    date_str = now.strftime('%A, %B %d, %Y %H:%M:%S')
    
    # render in ASCII art
    f = Figlet(font='slant')
    art = f.renderText(date_str)
    
    print(art)

if __name__ == '__main__':
    main()
