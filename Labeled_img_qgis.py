from PyQt5.QtCore import QTimer
''' CHANGE THE FILENAME PATH, AND THE  TIMERS '''

# exported is a prefix for the file names
fileName = 'E:\\Kanishka\\FullData_queens_CT\\'
#boundaryLayer = QgsProject.instance().mapLayersByName('Cooling_Tower')[0]
#QgsProject.instance().layerTreeRoot().findLayer(boundaryLayer.id()).setItemVisibilityChecked(True)
print('started')
otherLayers = []
for layer in QgsProject.instance().mapLayers().values():
    if layer.name().startswith("q_"):
        otherLayers.append(layer.name())
        print('In for loop')

count = 0


def prepareMap():  # Arrange layers
    for layer in QgsProject.instance().mapLayers().values():
        if layer.name().startswith("b_"):
            QgsProject.instance().layerTreeRoot().findLayer(
                layer).setItemVisibilityChecked(False)
    for layer in QgsProject.instance().mapLayers().values():
        try:
            if layer.name().startswith(otherLayers[count]):
            
                QgsProject.instance().layerTreeRoot().findLayer(
                    layer).setItemVisibilityChecked(True)
                qgis.utils.iface.setActiveLayer(layer)
                qgis.utils.iface.zoomToActiveLayer()
                qgis.utils.iface.mapCanvas().refresh()

                project = QgsProject.instance()
                manager = project.layoutManager()
                layoutName = 'Layout'
                layouts_list = manager.printLayouts()
                # remove any duplicate layouts
                for layout in layouts_list:
                    if layout.name() == layoutName:
                        manager.removeLayout(layout)
                layout = QgsPrintLayout(project)
                layout.initializeDefaults()
                layout.setName(layoutName)
                manager.addLayout(layout)

                page_size = QgsLayoutSize(
                    5000, 5000, QgsUnitTypes.LayoutPixels)
                pc = layout.pageCollection()
                page = pc.pages()[0]
                page.setPageSize(page_size)

                # create map item in the layout
                map = QgsLayoutItemMap(layout)
                map.setRect(20, 20, 20, 20)

                # set the map extent
                #ms = QgsMapSettings()
                #ms.setLayers([layer, boundaryLayer]) # set layers to be mapped
                rect = QgsRectangle(layer.extent())
                #ms.setExtent(rect)
                map.setExtent(rect)
                #map.setBackgroundColor(QColor(255, 255, 255, 0))
                layout.addLayoutItem(map)

                #map.attemptMove(QgsLayoutPoint(0, 0, QgsUnitTypes.LayoutMillimeters))
                map.attemptResize(QgsLayoutSize(423.333, 423.333,
                                                QgsUnitTypes.LayoutMillimeters))

                layout = manager.layoutByName(layoutName)
                exporter = QgsLayoutExporter(layout)

                fn = fileName + layer.name() + '.png'
                exporter.exportToImage(
                    fn, QgsLayoutExporter.ImageExportSettings())

                # Wait a second and export the map
                QTimer.singleShot(2000, exportMap)
        except:
            pass


def exportMap():  # Save the map as a PNG
    try:
        global count  # We need this because we'll modify its value
        if count < len(otherLayers):
            QTimer.singleShot(2000, prepareMap)
        count += 1
        print('Done')
        print(count)
    except:
        pass


prepareMap()  # Let's start the fun
