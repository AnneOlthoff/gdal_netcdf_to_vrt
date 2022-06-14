@ECHO OFF
ECHO Hello World! Your first batch file was printed on the screen successfully.

::findstr C:/Users/anne1/OpenSpacedata/assets/scene/solarsystem/planets/earth/layers/colorlayers/test_ECCO/test2/ "OCEAN_VELOCITY_mon_mean_2016-05_ECCO_V4r4_latlon_0p50deg.ncband_3.tif"
set %counter = 0

md colorfile
md warp
md vrt_evel

for /r %%i in (..\output\*.tif) do (
	
	echo %%i

	gdaldem color-relief "%%~fi" color.txt ".\colorfile\%%~ni.tif" 
	gdalwarp -t_srs "+proj=longlat" ".\colorfile\%%~ni.tif" ".\warp\%%~ni.tif"
	gdalbuildvrt ".\vrt_evel\%%~ni.vrt" -te -180 -90 180 90 -addalpha ".\warp\%%~ni.tif"

)
	



::gdaldem color-relief  OCEAN_VELOCITY_mon_mean_2016-05_ECCO_V4r4_latlon_0p50deg.ncband_3.tif color.txt color7.tif

PAUSE


::for %%A in ("D:\split outputs\raster_compression test\*.tif") do ECHO gdal_translate -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR -co TILED=YES "%%~fA" "D:\split outputs\raster_compression test\%%~nA.tif" -scale -ot Byte