import arcpy
arcpy.ImportToolbox(r"@\Spatial Statistics Tools.tbx")
arcpy.stats.SpatialAutocorrelation(
    Input_Feature_Class="Oklahoma Tracts",
    Input_Field="OKtracts_coveragescore.csv.Score",
    Generate_Report=None,
    Conceptualization_of_Spatial_Relationships="INVERSE_DISTANCE",
    Distance_Method="EUCLIDEAN_DISTANCE",
    Standardization="ROW",
    Distance_Band_or_Threshold_Distance=None,
    Weights_Matrix_File=None,
    number_of_neighbors=None
)
