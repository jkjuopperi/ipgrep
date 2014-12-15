#!/bin/sh

ipgrep 1.2.3.5/24 sample_files/test.txt

ipgrep 1.2.3.5/24 sample_files/test.txt sample_files/test2.txt

echo 4.3.2.1/24
ipgrep 4.3.2.1/24 sample_files/test.txt sample_files/test2.txt

echo 1.2.3.4
ipgrep 1.2.3.4 sample_files/test.txt sample_files/test2.txt
