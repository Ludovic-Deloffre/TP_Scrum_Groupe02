import glob, re, os, shutil, stat
dossierTxt = input('Entrez le nom du dossier : ')

txtList = (glob.glob(dossierTxt + "/*.txt"))

dir = 'sorties'
if os.path.exists(dir):
    shutil.rmtree(dir)

os.mkdir(dir)

for i in range(len(txtList)) :
    
    fileTxt = open(txtList[i], "r", encoding="utf8")
    # Nom du fichier
    fileName = fileTxt.name.split('/')
    fileName = fileName[len(fileName)-1]

    # titre de l'article
    for i in range(0,2):
        title = fileTxt.readline()


    # Abstract
    rawTxt = fileTxt.read()
    a, b = rawTxt.find('Abstract'), rawTxt.find('\n1\n')
    if len(rawTxt[a:b]) > 10000 :
        a, b = rawTxt.find('Abstract'), rawTxt.find('\n1 ')
        if len(rawTxt[a:b]) > 10000 :
            a, b = rawTxt.find('Abstract'), rawTxt.find('\nI. ')
    elif len(rawTxt[a:b]) == 0:
        a, b = rawTxt.find('ABSTRACT'), rawTxt.find('1.')
        
    
    os.chmod("sorties/", 0o777)
    g = open("sorties/"+ fileName, "w")
    g.write(fileName+"\n")
    g.write(title+"\n")
    g.write(rawTxt[a:b])
    g.close()

fileTxt.close()
