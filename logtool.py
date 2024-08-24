#!/usr/bin/env python3

# Correlate multiple lines from a log file based on PID within a 
# time window or number of lines.


import re



def process_file(filename: str):

    with open(filename, 'rt') as logfile:
        while True:
            line = logfile.readline().strip()
            if not line:
                break

            
            print(line)

            

    

def main():
    process_file('/home/jared/tmp/secure')



if __name__ == "__main__":
    main()



