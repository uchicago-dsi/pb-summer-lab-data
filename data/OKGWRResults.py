import arcpy
arcpy.ImportToolbox(r"@\Spatial Statistics Tools.tbx")
arcpy.stats.MGWR(
    in_features="Oklahoma Tracts",
    dependent_variable="OKtracts_coveragescore.csv.Score",
    model_type="CONTINUOUS",
    explanatory_variables="OKtracts_coveragescore.csv.WhitePerc;OKtracts_coveragescore.csv.Median_household_income;OKtracts_coveragescore.csv.Bach_or_higher_perc",
    output_features=r"C:\Users\alexh\OneDrive\Documents\ArcGIS\Projects\OKGWR\OKGWR.gdb\OklahomaTracts_MGWR",
    neighborhood_type="NUMBER_OF_NEIGHBORS",
    neighborhood_selection_method="GOLDEN_SEARCH",
    minimum_number_of_neighbors=None,
    maximum_number_of_neighbors=None,
    distance_unit="",
    minimum_search_distance=None,
    maximum_search_distance=None,
    number_of_neighbors_increment=None,
    search_distance_increment=None,
    number_of_increments=None,
    number_of_neighbors=None,
    distance_band=None,
    number_of_neighbors_golden="OKtracts_coveragescore.csv.WhitePerc # #;OKtracts_coveragescore.csv.Median_household_income # #;OKtracts_coveragescore.csv.Bach_or_higher_perc # #",
    number_of_neighbors_manual=None,
    number_of_neighbors_defined=None,
    distance_golden=None,
    distance_manual=None,
    distance_defined=None,
    prediction_locations=None,
    explanatory_variables_to_match=None,
    output_predicted_features=None,
    robust_prediction="ROBUST",
    local_weighting_scheme="BISQUARE",
    output_table=None,
    coefficient_raster_workspace=None,
    scale="SCALE_DATA",
    number_of_neighbors_gradient=None,
    distance_gradient=None
)