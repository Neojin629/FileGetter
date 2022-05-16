import shutil
import os
import time
import fnmatch




#stores file names in this list
fullfilelist = []
 
#Asks user for Div to use to look for Full Files for that Division.  
 
div = input("Enter Division Number: ")
 
#Asks user for Location Number with DIV to create variable for the rest of the script
locationnumber = input("Enter 5 Digit Location Number: ")
 
#Asks User for Location Region
region = input("Enter Region - NTAM, Europe: ")
 

if region == 'Europe':
    #Country Intials for Europe Build
    country = input("Enter Europe Country Initials: ")
    #Used to search for Div specific files: Europe.
    pattern_full_europe = div+'*'+country+'_'+'*full*'
elif region == 'NTAM':
    #Country Intials for NTAM Build
    country = input("Enter NTAM Country Initials: ")
    if country == 'CA' and div == '76':
        subdiv = input("Is this a Blank or Blank?: ")
    elif country == 'US':
        subdiv = input("Is this a NY/NJ Location?  Y/N: ")
 

#Used to search for Div specific files: NTAM.  
pattern_full = div +'*full*'
 

#File Directory
directory = "Files" +div+locationnumber
 
#Parent Directory
parent_directory = "C:\Desktop"
 
#path
path = os.path.join(parent_directory, directory)
 
#Creates directory on C:\Desktop, unless error occurs due to improper path etc.  
try:
    os.makedirs(path, exist_ok = True)
    print("Directory '%s' created successfully" % directory)
    print("\nPlease wait while files are being collected...")
except OSError as error:
    print("Directory '%s' can not be created" % directory)
 
path =\\\\path\\
path2 = \\\\path\\
path3 = \\\\path\\
path4 = \\\\path\\
path5 = \\\\path\\
path6 = \\\\path\\
path7 = \\\\path\\
path8 = \\\\path\\
path9 = \\\\path\\
path10 = \\\\path\\
path11 = \\\\path\\
path12 = \\\\path\\
path13 = \\\\path\\
path14 = \\\\path\\
path15 = \\\\path\\
path16 = \\\\path\\



for root, dirs, files in os.walk(path):
    for file in files:
        if(file.startswith(div+locationnumber) or (file.startswith("Blank") or (file.startswith("Blank")))):
            fullfilelist.append(os.path.join(root,file))
 
#Collects files from Path            
for root, dirs, files in os.walk(path2):
    for file in files:
        if(file.startswith("Country") or (file.startswith("Non_Physical_Item") or (file.startswith("State")))):
            fullfilelist.append(os.path.join(root,file))
 
#Collects files from Path
for root, dirs, files in os.walk(path3):
    for file in files:
        if(file.startswith("Blank")):
            fullfilelist.append(os.path.join(root,file))      
 
#Collects latest Full Files
if region == 'NTAM':            
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, pattern_full):
            fullfilelist.append(os.path.join(root, filename))
elif region == 'Europe':
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, pattern_full_europe):
            fullfilelist.append(os.path.join(root, filename))
 
#Collects Region Specific Files
if region == 'NTAM':
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.startswith(region)):
                fullfilelist.append(os.path.join(root,file))
elif region == 'Europe':
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.startswith(region)):
                fullfilelist.append(os.path.join(root,file))  
if region == 'Europe':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("Blank") or (file.startswith("PostalCode"))):
                fullfilelist.append(os.path.join(root,file))  
elif region == 'NTAM':
    for root, dirs, files in os.walk(path5):
        for file in files:
            if(file.startswith("PostalCode_")):
                fullfilelist.append(os.path.join(root,file))  
               
#Collects European Country Specific Files - Some countries have empty folders but adding for future intergration if needed.  
 
if country == 'AT':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("AT")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'BE':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("BE") or (file.endswith("Blank"))):
                fullfilelist.append(os.path.join(root,file))
elif country == 'CI':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("CI")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'CZ':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("CZ")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'DK':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("DK")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'FR':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("FR") or (file.endswith("FR") or (file.startswith("Blank")))):
                fullfilelist.append(os.path.join(root,file))
elif country == 'DE':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.endswith("Blank") or (file.startswith("DE"))):
                fullfilelist.append(os.path.join(root,file))
elif country == 'HK':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("HK")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'HU':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("HU")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'IE':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("IE")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'IT':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("IT")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'LU':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("LU")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'MY':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("MY")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'NL':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("NL") or (file.startswith(".") or (file.endswith("Blank")))):
                fullfilelist.append(os.path.join(root,file))            
elif country == 'NO':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("NO_")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'PL':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("PL")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'PT':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("PT")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'RO':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("RO_")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'SG':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("SG_")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'ES':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("ES_")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'SE':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("SE_")):
                fullfilelist.append(os.path.join(root,file))
elif country == 'CH':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.endswith("Blank") or (file.startswith("CH"))):
                fullfilelist.append(os.path.join(root,file))
elif country == 'UK':
    for root, dirs, files in os.walk(path4):
        for file in files:
            if(file.startswith("UK") or (file.startswith("GB"))):
                fullfilelist.append(os.path.join(root,file))



#Divisional Files Lookups
if div == '18':
    for root, dirs, files in os.walk(path6):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
    for root, dirs, files in os.walk(path12):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
elif div == '77':
    for root, dirs, files in os.walk(path7):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
    for root, dirs, files in os.walk(path14):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))  
elif div == '03':
    for root, dirs, files in os.walk(path8):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
    for root, dirs, files in os.walk(path16):
        for file in files:
            if(file.startswith("3"+locationnumber) or (file.endswith(div+locationnumber+".file"))):
                fullfilelist.append(os.path.join(root,file))
elif div == '76' and subdiv == 'Blank':
    for root, dirs, files in os.walk(path9):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
    for root, dirs, files in os.walk(path13):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
elif div == '76' and subdiv == 'Blank':
    for root, dirs, files in os.walk(path10):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
    for root, dirs, files in os.walk(path13):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
elif div == '16':
    for root, dirs, files in os.walk(path11):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
elif subdiv == 'Y':
    for root, dirs, files in os.walk(path15):
        for file in files:
            if(file.startswith("Blank")):
                fullfilelist.append(os.path.join(root,file))
 
#Location specific Files for DIV's except 03, as that is above.  
for root, dirs, files in os.walk(path16):
    for file in files:
        if(file.startswith(div+locationnumber) or (file.endswith(div+locationnumber+"_Prod.file") or (file.endswith(div+locationnumber+".file")))):
            fullfilelist.append(os.path.join(root,file))
 

#This part of the script confirms we are grabbing the lastest Files for the location
current_time = time.time()
 
modifiedfilelist = []
for file in fullfilelist:
    time_delta = current_time - os.path.getmtime(file)
    time_delta_days = time_delta / (60 * 60 * 24)
    if time_delta_days < 8:
        modifiedfilelist.append(file)
    elif time_delta_days > 45:
        modifiedfilelist.append(file)
 

#This part of the script copies the Files into the local folder on the Desktop
destination = "C:\Desktop\\"+ directory
 

for file in modifiedfilelist:
    print(file)
    source = file
    try:
        shutil.copy(source,destination)
        print("File copied successfully")
    except shutil.SameFileError:
        print("Source and destination represents the same file")
 
    # If destination is a directory.
    except IsADirectoryError:
        print("Destination is a directory.")
   
    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
   
    # For other errors
    except:
        print("Error occurred while copying file.")
 
