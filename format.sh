#----------------------------#
# A script for formatting csv#
#----------------------------#

#!/bin/bash

data_dir = "/SodaFountain/data"
csv_dir = "/SodaFountain/data/csv" 

cd $data_dir 
i=1

for filename in /data/*.mid; do 
    midicsv $filename ${filename%.*} #converts to csv
    midicsv $filename | perl exchannel.pl
    $i+1
    echo $i
    echo
done 

