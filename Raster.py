import os

myDir = 'E:\\Kanishka\\Full_Data\\'
project = QgsProject().instance()
layers = [layer for layer in QgsProject.instance().mapLayers().values() if layer.dataProvider().name() == 'gdal']
pipe = QgsRasterPipe()
count = 0
for layer in layers:
    pipe.set(layer.dataProvider().clone())
    #Returns the data provider interface
    pipe.set(layer.renderer().clone())
    #Returns the raster renderer interface, applies color to the raster.
    output_path = os.path.join(myDir, '{}.png'.format(layer.name()))
    file_writer = QgsRasterFileWriter(output_path)
    #The raster file writer allows to save a raster to a new file.
    file_writer.writeRaster(pipe, layer.width(), layer.height(), layer.extent(), layer.crs(), project.transformContext())

#Reference: https://gis.stackexchange.com/questions/371586/batch-export-rasters-as-rendered-images
