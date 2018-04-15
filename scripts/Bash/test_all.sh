#!/usr/bin/env bash
cd length
./test_all_length.sh
cd ../area
./test_all_area.sh
cd ../physics/
./test_plank.sh
cd ../standard_atmo/
./test_std_atmo.sh
cd ../nuclear/
./test_all.sh