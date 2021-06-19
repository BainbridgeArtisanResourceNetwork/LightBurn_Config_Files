#!/usr/bin/env bash

LB='Little Blue cut lib.clb'
BR='big red cut lib.clb'

head -n -1 "$LB" | sed 's/Material name=\"/&LB-/' > part1.txt &&
sed 's/Material name=\"/&BR-/' "$BR" | tail +3 > part2.txt &&
cat part1.txt part2.txt > combined-lib.xml &&
rm part1.txt && rm part2.txt


