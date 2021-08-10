#!/bin/csh

set model = 'KIM2005.txt.data'
set lon = `awk '{print $1}' $model`
set lat = `awk '{print $2}' $model`
set dep = `awk '{print $3}' $model`
set vp = `awk '{print $4}' $model`
set vs = `awk '{print $5}' $model`
set vpvs = `awk '{print $6}' $model`
set output = $model.csv

set i = 1
foreach line ( $lon )
  echo $lat[$i]'|'$lon[$i]'|'$dep[$i]'|'$vs[$i]'|'$vp[$i]'|'$vpvs[$i] >> $output
  @ i = $i + 1
end
echo 'done'
