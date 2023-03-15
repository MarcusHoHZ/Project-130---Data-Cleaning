import pandas as pd 
import csv 

df = pd.read_csv("final.csv")

print(df.shape)

del df["light_years_from_earth"]
del df["discovery_date"]
del df["hyperlink"]
del df["temp_discovery_date"]
del df["temp_mass"]
del df["orbital_radius"]
del df["orbital_period"]

df = df.rename({"pl_hostname" : "solar_system_name","pl_discmethod" : "planet_discovery_method", "pl_orbincl" : "planet_orbital_inclination", "pl_dens" : "planet_density", "ra_str" : "right_ascension", "dec_str" : "declination", "st_peff" : "host_temperature", "st_mass" : "host_mass", "st_rad" : "host_radius"}, axis = "columns")
df.to_csv("main.csv")

print(df.shape)
