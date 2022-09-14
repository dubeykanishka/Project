# Project - "Automated detection of Cooling Towers applying Deep Learning to Orthophotos Images"
The project aims to build a deep learning
model for the automatic detection of air conditioning cooling towers in
New York region using a time series database of orthophotos and a training
data set provided with geolocated annotated features.
The project will use a set of orthophotos downloaded from 'http://gis.ny.gov/gateway/mg/nysdop_download.cfm?v=1' provided by NYC
DoITT. The plan began in 1996 and aims to capture aerial orthophotos
covering New York city. Since 2004, the aerial images has been captured
with a fixed update period, currently two years during summer/spring
months and computerised procedures were utilised to rectify the images
by eliminating distortions brought on by shifts in altitude and camera orientation. The resolution of orthophotos has also been changing over time,
and since 2001, the resolution reached to 6 inches covering the New York
city with color and infrared bands.
For detection of Cooling Towers in an image, YOLOv5 is the model that
has been chosen in the project and the dataset has been optimized based
on the chosen model. It can be seen that YOLOv5s6 with the optimized
dataset greatly improves the detection accuracy.

Code: https://github.com/dubeykanishka/Project/blob/main/coolingtowerdetectionusingyolo.ipynb
#RANDBEE CONSULTANTS
