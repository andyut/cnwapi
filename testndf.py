from netCDF4 import Dataset, MFDataset

rootgrp = MFDataset("/data/cnwapi/3B-DAY.MS.MRG.3IMERG.20120101-S000000-E235959.V06.nc4", "r")

print(rootgrp)
#print(rootgrp)
#f= MFDataset("3B-DAY.MS.MRG.3IMERG.20120101-S000000-E235959.V06.nc4.nc4")
#print(type(f))
def walktree(top):
        yield top.groups.values()
        for value in top.groups.values():
            yield from walktree(value)

for children in walktree(rootgrp):
    for child in children :
        print(child)

rootgrp.close() 