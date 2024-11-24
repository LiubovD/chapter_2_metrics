import zipfile, glob, os.path

inWS = r"D:\Luba\data\Project_americanview\drough\2017_USDM_M"
outWS = r"D:\Luba\data\Project_americanview\drough\2017_drought"

if not os.path.exists(outWS):
    os.makedirs(outWS)

zipfiles = glob.glob(r"%s\*.zip" % inWS)

for zipFile in zipfiles:
    print("Extracting %s" % zipFile)
    z = zipfile.ZipFile(zipFile)
    z.extractall(outWS)