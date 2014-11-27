#!/usr/bin/env python
#
# Juho Juopperi <jkj@kapsi.fi>, +358405422321
# Public Domain
#

import sys, re, socket, struct

cidr_re = re.compile(r"(\d+\.\d+\.\d+\.\d+(?:[/m ](?:\d+\.\d+\.\d+\.\d+|\d+)){0,1})")

def parse_addr(addr):
    parts = re.split('[/m ]', addr) # IP/MASK, IPmMASK, IP MASK
    ip = struct.unpack('>I', socket.inet_aton(parts[0]))[0]
    prefix = None

    if len(parts) > 1 and '.' in parts[1]:
        try:
            mask = struct.unpack('>I', socket.inet_aton(parts[1]))[0]
            prefix = 32
            while (mask & 1) == 0:
                mask >>= 1;
                prefix -= 1;
        except:
            pass
    elif len(parts) > 1:
        try:
            prefix = int(parts[1])
        except:
            pass
    else:
        prefix = 32

    #print (addr, ip, prefix)
    return (ip, prefix)

def check_ip(a, b):
    (a_ip, a_prefix) = parse_addr(a)
    (b_ip, b_prefix) = parse_addr(b)
    roll = 32 - min(a_prefix, b_prefix)
    a_ip >>= roll
    b_ip >>= roll
    if a_ip == b_ip:
        return True
    return False

def grep(pattern, files):
    for filename in files:
        with open(filename) as fd:
            for line in fd:
                matches = False
        
                match = cidr_re.search(line)
                if match:
                    for ip in match.groups():
                        try:
                            parse_addr(ip)
                            if check_ip(pattern, ip):
                                matches = True
                        except:
                            pass
                if matches:
                    if len(sys.argv) > 3:
                        print("%s: %s" % (filename, line.rstrip("\n")))
                    else:
                        print(line.rstrip("\n"))

def main():
    if len(sys.argv) < 3:
        print("%s <cidr> <file> [file...]" % sys.argv[0])
        sys.exit(0)
    grep(pattern=sys.argv[1], files=sys.argv[2:])

if __name__ == '__main__':
    main()

