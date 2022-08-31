import os

myDir = 'E:\\Kanishka\\Full_Data\\'
project = QgsProject().instance()
layers = [layer for layer in QgsProject.instance().mapLayers().values() if layer.dataProvider().name() == 'gdal']
pipe = QgsRasterPipe()
count = 0
for layer in layers:
    #idx = layer.dataProvider().handlePostCloneOperations(source=QgsVectorDataProvider)
    pipe.set(layer.dataProvider().clone())
    pipe.set(layer.renderer().clone())
    output_path = os.path.join(myDir, '{}.png'.format(layer.name()))
    file_writer = QgsRasterFileWriter(output_path)
    file_writer.writeRaster(pipe, layer.width(), layer.height(), layer.extent(), layer.crs(), project.transformContext())