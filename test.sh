#!/bin/sh

./ipgrep 1.2.3.5/24 test.txt

./ipgrep 1.2.3.5/24 test.txt test2.txt

echo 4.3.2.1/24
./ipgrep 4.3.2.1/24 test.txt test2.txt

echo 1.2.3.4
./ipgrep 1.2.3.4 test.txt test2.txt