"""
Task: Filter for and remove any dud records where there is no value for SiteID or there is a mismatch between SiteID and Location.
(This script should print the lines number and mismatch field values for each dud record.)
"""
# delimeter used for seperation and low_memory because of large data
# import pandas lib

import pandas as pd
crop_df = pd.read_csv("crop.csv", sep = ";", low_memory = False,)   
print('total records in the csv imported is {0}'.format(len(crop_df.values.tolist())))


# I created a list of my site id and 18 site locations

df_site = pd.DataFrame([
[188, 'AURN Bristol Centre'],
[203, 'Brislington Depot'],
[206, 'Rupert Street'],
[209, 'IKEA M32'],
[213, 'Old Market'],
[215, 'Parson Street School'],
[228, 'Temple Meads Station'],
[270, 'Wells Road'],
[271, 'Trailer Portway P&R'],
[375, 'Newfoundland Road Police Station'],
[395, "Shiner's Garage"],
[452, 'AURN St Pauls'],
[447, 'Bath Road'],
[459, 'Cheltenham Road \ Station Road'],
[463, 'Fishponds Road'],
[481, 'CREATE Centre Roof'],
[500, 'Temple Way'],
[501, 'Colston Avenue']

], columns = ('SiteID','Location'))


# I merged the two columns with a left join mapping with df_site to get the actual locations
new_merge = crop_df.merge(df_site, on='SiteID', how='left', suffixes=('', '_p'))


# I make my siteID and location columns
new_merge = new_merge[['SiteID', 'Location', 'Location_p']]


# I make a column "is_mismatch" that returns True or False to show if there is a mismatch or not
new_merge['is_mismatch'] = new_merge.apply(
    lambda x: 'False' if x['Location'] == x['Location_p'] else 'True', axis=1)

# assign  all my mismatch data into the "dud_record"
dud_record = new_merge[new_merge['is_mismatch'] == 'True']

dud_record = dud_record[['SiteID', 'Location']]

# print the annoying mismatch values
pd.set_option('display.max_rows', None)
print(dud_record)


# remove columns where mismatch exist and where site id or location is null
clean_df = crop_df[new_merge['is_mismatch'] == 'False']

# finally, my cleansed data to "clean.csv" (after sleepless nights)
clean_df.to_csv ("clean.csv", sep=";", index=False)

