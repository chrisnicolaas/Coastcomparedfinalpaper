import os
import geopandas as gpd

def convert_to_geopackage(source_geojson="aruba.geojson", target_gpkg="aruba_osm_highres.gpkg", layer_name="aruba_boundary"):
    """
    Reads a GeoJSON file and exports it to a GeoPackage (.gpkg) file layer.
    """
    if not os.path.exists(source_geojson):
        raise FileNotFoundError(f"Source GeoJSON file '{source_geojson}' not found in the workspace.")
        
    print(f"1. Loading '{source_geojson}' into GeoPandas GeoDataFrame...")
    gdf = gpd.read_file(source_geojson)
    
    # Print database schema details
    print(f"   - Geometry Type: {gdf.geom_type.unique()}")
    print(f"   - Coordinate Reference System (CRS): {gdf.crs}")
    
    print(f"2. Exporting to GeoPackage: '{target_gpkg}' (layer: '{layer_name}')...")
    # to_file with driver="GPKG" writes out a SQLite-based GeoPackage
    gdf.to_file(target_gpkg, driver="GPKG", layer=layer_name)
    
    if os.path.exists(target_gpkg):
        file_size_kb = os.path.getsize(target_gpkg) / 1024
        print(f"SUCCESS: Created GeoPackage '{target_gpkg}' ({file_size_kb:.1f} KB).")
        
        # Verify we can read it back
        print("3. Verification: Reading back layer from GeoPackage...")
        gdf_check = gpd.read_file(target_gpkg, layer=layer_name)
        print(f"   - Verification Success: Loaded {len(gdf_check)} features.")
    else:
        print("ERROR: Failed to create GeoPackage.")

if __name__ == "__main__":
    convert_to_geopackage()
