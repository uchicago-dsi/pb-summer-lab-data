# %%
import pandas as pd
import geopandas as gpd
# remove pandas display column limit
pd.set_option('display.max_columns', None)
# %%
test_load = gpd.read_file("../Data/vision_providers_geocoded.gpkg")
# %%
# Read in the data
# read in data 
# account for  'utf-8' codec can't decode byte 0xd8 in position 63: invalid continuation byte
# %%
# convert lat/lon to geometry
df = pd.read_csv('../Data/vision_providers_geocoded.csv')
# gdf = gpd.GeoDataFrame(
#     df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
# gdf.crs = {'init': 'epsg:4326'}
# %%
# columns with Taxonomy Group in the column name
taxonomy_columns = [col for col in df.columns if 'Taxonomy Code' in col]
# %%
# concat the taxonomy columns into a single column separated by |
df['Taxonomy'] = df[taxonomy_columns].apply(
    lambda x: '|'.join(x.fillna('_').astype(str)),
    axis=1
)
# %%
min_columns = [
 'NPI',
 'Entity Type Code',
 'Replacement NPI',
 'Employer Identification Number (EIN)',
 'Provider Organization Name (Legal Business Name)',
 'Provider Last Name (Legal Name)',
 'Provider First Name',
 'Provider Middle Name',
 'Provider Name Prefix Text',
 'Provider Name Suffix Text',
 'Provider Credential Text',
 'Provider Other Organization Name',
 'Provider Other Organization Name Type Code',
 'Provider Other Last Name',
 'Provider Other First Name',
 'Provider Other Middle Name',
 'Provider Other Name Prefix Text',
 'Provider Other Name Suffix Text',
 'Provider Other Credential Text',
 'Provider Other Last Name Type Code',
 'Provider First Line Business Mailing Address',
 'Provider Second Line Business Mailing Address',
 'Provider Business Mailing Address City Name',
 'Provider Business Mailing Address State Name',
 'Provider Business Mailing Address Postal Code',
 'Provider Business Mailing Address Country Code (If outside U.S.)',
 'Provider Gender Code',
 'Authorized Official Last Name',
 'Authorized Official First Name',
 'Authorized Official Middle Name',
 'Authorized Official Title or Position',
 'Authorized Official Telephone Number',
 'Certification Date',
 'Clean Zip',
 'Full Address',
 'Latitude',
 'Longitude',
 "Taxonomy"
]
# %%
min_df = df[min_columns]
# %%
min_df['Provider Business Mailing Address Postal Code'] = min_df['Clean Zip'].astype(str)
min_df['Clean Zip'] = min_df['Clean Zip'].astype(str)
# %%
min_df.to_parquet('data/vision_providers_minimal.parquet', index=False)

# %%
