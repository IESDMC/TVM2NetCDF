# TVM2NetCDF
This tool combines [emc-tools](https://github.com/iris-edu/emc-tools) to convert TVM models into NetCDF format.

## Usage
### pre-processing
- Install [emc-tools](https://github.com/iris-edu/emc-tools).
- Download TVM models from [link](http://tecdc.earth.sinica.edu.tw/TWtomo/ModelInfo.php).

### process
- Use txt2csv.csh to turn TVM models into GeoCSV.
```
csh txt2csv.csh
```
- Add Header to the GeoCSV.
- Transform into NetCDF
```
python ./src/GeoCSV_2_netCDF_3D.py -i KIM2005.csv -d
```
- Read NetCDF file with python library
```
python readNetCDF.py
```


