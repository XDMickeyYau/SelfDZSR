#!/bin/bash
echo "Start to test the model.... (metric only)"

dataroot="./"
name="camerafusion_l1" # You can replace 'camerafusion_l1' with 'camerafusion_l1sw' when testing the model trained by SW loss.
scale='2'
data='cam'
cam='True'
device="0"
iter="401"

python metrics.py  --device $device --name $name --load_iter $iter  --cam $cam  --dataroot $dataroot
