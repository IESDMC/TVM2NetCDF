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

### results
<table>
   <tr>
      <td> <img src="https://github.com/IESDMC/TVM2NetCDF/blob/main/docs/KIM2005_Vs31.jpeg?raw=true" width="100%"></td>
   </tr>
   <tr>
      <td align="center">
         <div>Velocity Model in NetCDF format</div>
         <div>Kim, K.H., J.M. Chiu, J. Pujol, K.C. Chen, B.S. Huang, Y. Yeh, and P. Shen (2005). Three-dimensional Vp and Vs structural models associated with the active subduction and collision tectonics in the Taiwan region, Geophysical Journal International, 162, 204-220.
            <a href="http://dx.doi.org/10.1111/j.1365-246X.2005.02657.x">10.1111/j.1365-246X.2005.02657.x</a></div>
      </td>
   </tr>
</table>

