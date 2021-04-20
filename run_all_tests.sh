#!/bin/bash

echo "Test 00"
cat testcases/input/input00.txt | python solution.py | diff testcases/output/output00.txt -

echo "Test 01"
cat testcases/input/input01.txt | python solution.py | diff testcases/output/output01.txt -

echo "Test 02"
cat testcases/input/input02.txt | python solution.py | diff testcases/output/output02.txt -

echo "Test 03"
cat testcases/input/input03.txt | python solution.py | diff testcases/output/output03.txt -

echo "Test 04"
cat testcases/input/input04.txt | python solution.py | diff testcases/output/output04.txt -

echo "Test 05"
cat testcases/input/input05.txt | python solution.py | diff testcases/output/output05.txt -

echo "Test 06"
cat testcases/input/input06.txt | python solution.py | diff testcases/output/output06.txt -

echo "Test 07"
cat testcases/input/input07.txt | python solution.py | diff testcases/output/output07.txt -

echo "Test 08"
cat testcases/input/input08.txt | python solution.py | diff testcases/output/output08.txt -

echo "Test 09"
cat testcases/input/input09.txt | python solution.py | diff testcases/output/output09.txt -

echo "Test 10"
cat testcases/input/input10.txt | python solution.py | diff testcases/output/output10.txt -

echo "Test 11"
cat testcases/input/input11.txt | python solution.py | diff testcases/output/output11.txt -

echo "Test 12"
cat testcases/input/input12.txt | python solution.py | diff testcases/output/output12.txt -

echo "Test 13"
cat testcases/input/input13.txt | python solution.py | diff testcases/output/output13.txt -

echo "Test 14"
cat testcases/input/input14.txt | python solution.py | diff testcases/output/output14.txt -

echo "Test 15"
cat testcases/input/input15.txt | python solution.py | diff testcases/output/output15.txt -

echo "Test 16"
cat testcases/input/input16.txt | python solution.py | diff testcases/output/output16.txt -
