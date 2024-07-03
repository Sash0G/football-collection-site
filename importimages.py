import os

fileNames = {}
for type in ['Cards', 'Flags', 'Badges', 'Books']:
    folderPath='Images/'+type
    fileNames[type] = []
    for filename in os.listdir(folderPath):
        fileNames[type].append(filename)

    with open(type+'.html', 'r') as file:
        filedata = file.read()
    
    startPos = filedata.find('<div class="gallery">') + len('<div class="gallery">')
    endPos = filedata.find('<!--here--></div>', startPos)

    new='\n'

    for k,image in enumerate(fileNames[type]):
        new+= '\t\t<img src="'+folderPath+'/'+image+'" alt="Image'+str(k+1)+'"onclick="openModal(\''+folderPath+'/'+image+'\')">\n'
    print(new)
    new_filedata = filedata[:startPos] +  new + filedata[endPos:]
    print(startPos)
    print(endPos)
    with open(type+'.html', 'w') as file:
        file.write(new_filedata)
