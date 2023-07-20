# %%
import geopandas as gpd
import pandas as pd
import numpy as np
from mgwr.gwr import GWR
from mgwr.sel_bw import Sel_BW
from mgwr.summary import summaryModel, summaryGLM, summaryGWR
from os import path
pd.set_option('display.max_columns', None)
# %%
data_dir = path.join('..', 'data')
# %%
vision = pd.read_parquet(path.join(data_dir, "vision_providers_minimal.parquet"))
censusTractok = gpd.read_file(path.join(data_dir, "Oklahoma", "OK Tracts Collect.zip"))
##This dataframe contains information for ophthalmology only; Contains distances, geometry, and GEOID
oklahomamerged = pd.read_csv(path.join(data_dir, "correctdf.csv"))
okdemographs = pd.read_csv(path.join(data_dir, "Oklahoma","Socio-Econ_Factor_OK_by_Tract.csv"))
# %%
OKcentroids = censusTractok.copy().to_crs("ESRI:102008")
OKcentroids['geometry'] = OKcentroids['geometry'].centroid
# %%
#subsetting vision provider data based on classification (ie optometrist/ophthamologist) and entity type
#Filtering for vision care providers
vision2 = vision[vision["Entity Type Code"] == 1]

#Checking if taxonomy code starts with 152
vision2['Optometry'] = vision2['Taxonomy'].apply(lambda x: any(code.startswith('152') for code in x.split('|')))

#Checking if taxonomy code starts with 207
vision2['Ophthalmology'] = vision2['Taxonomy'].apply(lambda x: any(code.startswith('207') for code in x.split('|')))

#Checking if taxonomy code starts with 156
vision2['Others'] = vision2['Taxonomy'].apply(lambda x: any(code.startswith('156') for code in x.split('|')))

#Creating a GeoDataFrame with geometry from latitude and longitude
vision3 = gpd.GeoDataFrame(
   vision2, geometry=gpd.points_from_xy(vision2.Longitude, vision2.Latitude),
    crs="EPSG:4326")

#Filtering for providers in Oklahoma
vision3 = vision3[vision3["Provider Business Mailing Address State Name"] == 'OK']

#Changing the CRS to a projected CRS
vision3p = vision3.to_crs("ESRI:102008")
# %%
merged_df = pd.merge(oklahomamerged, okdemographs, on='GEOID', how='inner')
merged_df['GEOID']=merged_df['GEOID'].astype(int)
censusTractok['GEOID']=censusTractok['GEOID'].astype(int)
# %%
zipmerge = pd.merge(censusTractok, merged_df, how= 'left', on= "GEOID")
zipmerge = zipmerge.set_geometry(zipmerge["geometry_x"])
y = zipmerge['Distances'].values.reshape((-1,1)) # reshape is needed to have column array
White = zipmerge['WhitePerc'].values.reshape((-1,1))

# %%
MHI = zipmerge['Median_household_income'].values.reshape((-1,1))
Bache = zipmerge['Bach_or_higher_perc'].values.reshape((-1,1))
X = np.array([MHI, Bache, White]).reshape((-1, 3))
X_shape = X.shape

# %%
u = zipmerge['Longitude']
v = zipmerge['Latitude']
coords = list(zip(u,v))
# %%
gwr_selector = Sel_BW(coords, y, X)
gwr_bw = gwr_selector.search()
# %%
gwr_bw = 118.0
gwr_results = GWR(coords, y, X, gwr_bw).fit()
gwr_results.summary()
# %%