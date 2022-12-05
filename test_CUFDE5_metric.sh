#!/bin/bash
echo "Start to test the model....(metric only)"

dataroot="./CUFDE5"
name="nikon_l1" # You can replace 'nikon_l1' with 'nikon_l1sw' when testing the model trained by SW loss.
scale='4'
data='dsr'
cam='False'
device="0"
iter="401"

python metrics.py  --device $device --name $name --load_iter $iter  --cam $cam  --dataroot $dataroot
