# Prevent Blindness -- CAN Summer Lab

## Project Background
Prevent Blindness, originally created in 1908 as an advocacy campaign to eradicate infant blindness, is a Chicago-based nonprofit that works to “eliminate unnecessary vision loss and inequities in public health.” Its main services include lobbying national policy makers; partnering with corporations to provide vouchers for free and discounted eye care and eyeglasses; offering annual certified vision screening training to thousands of volunteers; and maintaining a large online library of educational resources. This summer project will be completed in partnership with Prevent Blindness and the University of Chicago Data Science Institute (DSI) Open Spatial Lab (OSL).  Our main point of contact will be Dylan Halpern, technical lead at the OSL.

## Problem Statement

According to the latest estimate from the Centers for Disease Control and Prevention (CDC), over seven million Americans have uncorrectable vision loss, including blindness. Meanwhile, the National Institute of Health (NIH) predicts that the number of Americans affected by cataracts and age-related macular degeneration will increase from 24.4 to 50 million and 2.1 to 5.4 million, respectively, by 2050. These eye and vision problems cost the country an estimated $172 billion annually, in addition to harming individuals’ wellness, autonomy, and performance in school and on the job.
Half of all blindness and many diseases can be prevented, especially when treated early. However, access to vision care providers is “shockingly still a challenge for far too many,” especially historically underserved communities. To address this issue, we will collaborate with Prevent Blindness and the OSL to map communities’ access to optometrists and ophthalmologists across the U.S. at different spatial scales (e.g., census tracts, counties, and states) and then analyze trends in access for different demographics (e.g., race, ethnicity) and social determinants of health (e.g., education level, income).

## Research Questions
- Where are eyecare providers geographically clustered? How does the quality of eye care vary by region?
- Is there a statistically significant relationship (or strong correlation) between demographic variables like race or socioeconomic status (and social determinants of health like healthcare and education access) and distance to the nearest optometrist or ophthalmologist? How does eyecare provider access vary by region? 

## Project Deliverables
- A Jupyter notebook that aggregates raw counts of optometrist and ophthalmologist locations and types by different geographies (e.g., census tracts, counties), displays the results as choropleth maps, and then computes the spatial lag of the counts to identify clusters.

- A Jupyter notebook that maps optometrist and ophthalmologist locations across the United States, draws “zones” of eyecare provider access using a spatial interaction model based on driving distance and building characteristics, and then merges the zones with different geographies of interest.

- A Jupyter notebook that merges demographic variables with the computed access zones and raw provider counts and then explores whether access significantly varies by race, ethnicity, education level, etc.

This repo contains data for the CAN Summer Lab Prevent blindness data. In this repo, the `data` folder contains a number of useful and relevant datasets for use on this project:

## Data Description

- `vision_providers_geocoded.gpkg` contains locations of providers, derived from the [National Provider Identity Standard (NPI)](https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand) and geocoded (Addres >> Lat/Lon) via Google Map's Geocoding API. 
- `Taxonomy_List.csv` contains the provider taxonomy codes. See additional documentation from [CMS](https://www.cms.gov/medicare/provider-enrollment-and-certification/find-your-taxonomy-code#:~:text=What%20is%20a%20taxonomy%20code,referred%20to%20as%20an%20NPI)
- `county.gpkg`, `states.gpkg`, `tracts.gpkg`, `zcta.gpkg` are census geographies at the county, state, census tract, and zip code tabulation area scale, repsectively. These geospatial data are in the WGS84 (EPSG:4326) projection, and should be converted to an appropriate CRS for doing area-based calcuations. These files derive from Social Explorer GeoData based on [Tiger/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).

