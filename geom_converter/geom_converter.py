import os.path
import shapefile

from pyteltools.geom import conversion, geometry, Shapefile


# Write polylines shapefile
lines = [geometry.Polyline([(0, 0, 0), (10, 20, 30)], attributes=[0], m_array=[[0], [100]])]
Shapefile.write_shp_lines('from_scratch/polyline.shp', shapefile.POLYLINE, lines, 'LineID')
Shapefile.write_shp_lines('from_scratch/polylinez.shp', shapefile.POLYLINEZ, lines, 'LineID')
Shapefile.write_shp_lines('from_scratch/polylinem.shp', shapefile.POLYLINEM,  lines, 'LineID')

# Write polygons shapefile
lines = [geometry.Polyline([(0, 0, 0), (10, 20, 30), (10, 40, 30), (0, 0, 0)],
                           attributes=[0], m_array=[[0], [100], [200], [300]])]
Shapefile.write_shp_lines('from_scratch/polygon.shp', shapefile.POLYGON, lines, 'PolyID')
Shapefile.write_shp_lines('from_scratch/polygonz.shp', shapefile.POLYGONZ, lines, 'PolyID')
Shapefile.write_shp_lines('from_scratch/polygonm.shp', shapefile.POLYGONM,  lines, 'PolyID')

# Open files just written
for file_path in ['polyline.shp', 'polylinez.shp', 'polylinem.shp']:
    print(list(Shapefile.get_open_polylines(os.path.join('from_scratch', file_path))))
for file_path in ['polygon.shp', 'polygonz.shp', 'polygonm.shp']:
    print(list(Shapefile.get_polygons(os.path.join('from_scratch', file_path))))

# Convert from POINTZM shapefile
conv = conversion.ShpPointConverter('../data/shp/Point/POINTZM_dalle_lidar_simple.shp')
conv.read()
conv.write('xyz', 'from_shp_points/POINTZM_to_xyz.xyz', ('Z', '0'))
conv.write('csv', 'from_shp_points/POINTZM_to_csv.csv', ('Z', 'M'))
conv.write('shp Point', 'from_shp_points/POINTZM_to_POINT.shp', ('0', '0'))
conv.write('shp PointZ', 'from_shp_points/POINTZM_to_POINTZM.shp', ('Z', 'M'))
conv.write('shp PointM', 'from_shp_points/POINTZM_to_POINTM.csv', ('0', '0'))

# Convert from POINTZM shapefile
conv = conversion.ShpMultiPointConverter('../data/shp/Point/MULTIPOINTZM_from_las.shp')
conv.read()
conv.write('xyz', 'from_shp_multipoints/MULTIPOINTZM_to_xyz.xyz', ('Z', '0'))
conv.write('csv', 'from_shp_multipoints/MULTIPOINTZM_to_csv.csv', ('Z', 'M'))
conv.write('shp Point', 'from_shp_multipoints/MULTIPOINTZM_to_POINT.shp', ('Z', 'M'))
conv.write('shp PointZ', 'from_shp_multipoints/MULTIPOINTZM_to_POINTZM.shp', ('Z', 'M'))
conv.write('shp PointM', 'from_shp_multipoints/MULTIPOINTZM_to_POINTM.csv', ('0', '0'))
conv.write('shp MultiPoint', 'from_shp_multipoints/MULTIPOINTZM_to_MULTIPOINT.shp', ('Z', 'M'))
conv.write('shp MultiPointZ', 'from_shp_multipoints/MULTIPOINTZM_to_MULTIPOINTZM.shp', ('Z', 'M'))
conv.write('shp MultiPointM', 'from_shp_multipoints/MULTIPOINTZM_to_MULTIPOINTM.csv', ('0', '0'))

# Convert from XYZ file
conv = conversion.XYZConverter('from_shp_points/POINTZM_to_xyz.xyz')
conv.read()
conv.write('xyz', 'from_xyz/XYZ_to_xyz.xyz', ('Z', '0'))
conv.write('csv', 'from_xyz/XYZ_to_csv.csv', ('Z', 'M'))
conv.write('shp PointZ', 'from_xyz/XYZ_to_POINTZM.shp', ('Z', 'M'))

# Convert from i2s file
conv = conversion.BKLineConverter('../data/pildepon/sections.i2s')
conv.read()
conv.write('csv', 'from_i2s/i2s_to_csv.csv', ('', False))
conv.write('i2s', 'from_i2s/i2s_to_i2s.i2s', ('', False))
conv.write('i3s', 'from_i2s/i2s_to_i3s.i3s', ('', False))
conv.write('shp Polyline', 'from_i2s/i2s_to_POLYLINE.shp', ('ColName', False))
conv.write('shp PolylineZ', 'from_i2s/i2s_to_POLYLINEZ.shp', ('ColName', False))  # value is not taken

conv = conversion.BKLineConverter('../data/bk/polygons.i2s')
conv.read()
conv.write('csv', 'from_i2s/i2s_POLYGON_to_csv.csv', ('', False))
conv.write('i2s', 'from_i2s/i2s_POLYGON_to_i2s.i2s', ('', False))
conv.write('shp Polygon', 'from_i2s/i2s_POLYGON_to_POLYGON.shp', ('ColName', False))

# Convert from i3s file
conv = conversion.BKLineConverter('../data/bk/EMG_Bathy_point_asLines.i3s')
conv.read()
conv.write('csv', 'from_i3s/i3s_to_csv.csv', ('', False))
conv.write('i2s', 'from_i3s/i3s_to_i2s.i2s', ('', False))
conv.write('i3s', 'from_i3s/i3s_to_i3s.i3s', ('', False))
conv.write('shp Polyline', 'from_i3s/i3s_to_POLYLINE.shp', ('value', False))
conv.write('shp PolylineZ', 'from_i3s/i3s_to_POLYLINEZ.shp', ('value', False))

conv = conversion.BKLineConverter('../data/bk/polygons_withZ.i3s')
conv.read()
conv.write('csv', 'from_i3s/i3s_POLYGON_to_POLYGON.csv', ('', False))
conv.write('i3s', 'from_i3s/i3s_POLYGON_to_POLYGON.i3s', ('', False))
conv.write('shp Polygon', 'from_i3s/i3s_POLYGON_to_POLYGON.shp', ('value', False))

# Convert from POLYLINEZM shapefile
conv = conversion.ShpLineConverter('from_i2s/i2s_to_POLYLINEZ.shp')
conv.read()
conv.write('shp Polyline', 'from_shp_polyline/POLYLINEZ_to_POLYLINE.shp', ('Z', 'Z', False))
conv.write('shp PolylineZ', 'from_shp_polyline/POLYLINEZ_to_POLYLINEZ.shp', ('Z', 'Z', False))
conv.write('shp PolylineM', 'from_shp_polyline/POLYLINEZ_to_POLYLINEZM.shp', ('M', 'Z', False))
conv.write('i2s', 'from_shp_polyline/POLYLINEZ_to_i2s.i2s', ('Iteration', False))
conv.write('i3s', 'from_shp_polyline/POLYLINEZ_to_i3s.i3s', ('0', 'Iteration', False))
