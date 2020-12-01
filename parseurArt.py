import xml.etree.cElementTree as ET
import argparse
import glob, re, os, shutil, stat

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--txt", help="Sortir un fichier .txt", action="store_true")
parser.add_argument("-x", "--xml", help="Sortir un fichier .xml", action="store_true")
args = parser.parse_args()

def get_abstract(rawTxt):
    a, b = rawTxt.find('Abstract'), rawTxt.find('\n1\n')
    if len(rawTxt[a:b]) > 10000:
        a, b = rawTxt.find('Abstract'), rawTxt.find('\n1 ')
        if len(rawTxt[a:b]) > 10000:
            a, b = rawTxt.find('Abstract'), rawTxt.find('\nI. ')
    elif len(rawTxt[a:b]) == 0:
        a, b = rawTxt.find('ABSTRACT'), rawTxt.find('1.')

    return(rawTxt[a:b])

def get_references(rawTxt):
    c=  rawTxt.find('References')
    if len(rawTxt[c:]) == 0:
        c=  rawTxt.find('REFERENCES')
    return(rawTxt[c:-1].encode('ascii','ignore').decode('ascii'))

def get_title(f):
    lines = [line.rstrip() for line in f]
    title = str(lines[0:1]) + "\n"
    f.close()
    return(title)

def get_author(f, numLigne):
    lines = [line.rstrip() for line in f]
    title = str(lines[2:numLigne]) + "\n"
    f.close()
    return(title)

def remove_create():
    dir = 'sorties'
    if os.path.exists(dir):
        shutil.rmtree(dir)

    os.mkdir(dir)

def txt():
	# dossierTxt = input('Entrez le nom du dossier : ')
    dossierTxt = "pdftotext"
    txtList = (glob.glob(dossierTxt + "/*.txt"))

    remove_create()

    
    for i in range(len(txtList)) :
        
        f = open(txtList[i], "r", encoding="utf-8")
        fileName = f.name.split('/')
        fileName = fileName[len(fileName)-1]
        rawTxt = f.read()

        os.chmod("sorties/", 0o777)
        g = open("sorties/"+ fileName, "w")

        abstract = get_abstract(rawTxt)
        references = get_references(rawTxt)

        g.write(fileName+"\n")

        h = open(txtList[i], "r", encoding="utf-8")
        title = get_title(h)


        v = open(txtList[i], "r", encoding="utf-8")
        numLigne = 0
        lookup1 = 'Abstract'
        lookup2 = 'ABSTRACT'
        f = open(txtList[i], "r", encoding="utf8")
        for num, line in enumerate(f, 1):
            # test = line.find(lookup)
            if lookup1 in line:
                if(num < 70):
                    numLigne = num - 1
                    # print(numLigne)
            elif lookup2 in line:
                if(num < 70):
                    numLigne = num - 1
                    # print(numLigne)
                # print(num)
        author = get_author(v, numLigne)
        g.write(title)
        g.write(author)
        g.write(abstract)
        g.write(references)
        g.close()

def xml():
	# dossierTxt = input('Entrez le nom du dossier : ')
	dossierTxt = "pdftotext"
	txtList = (glob.glob(dossierTxt + "/*.txt"))

	remove_create()

    
	for i in range(len(txtList)) :
        
		f = open(txtList[i], "r", encoding="utf-8")
		fileName = f.name.split('/')
		fileName = fileName[len(fileName)-1]
		rawTxt = f.read()

		os.chmod("sorties/", 0o777)

		abstract = get_abstract(rawTxt)
		references = get_references(rawTxt)

		h = open(txtList[i], "r", encoding="utf-8")
		title = get_title(h)


		v = open(txtList[i], "r", encoding="utf-8")
		numLigne = 0
		lookup1 = 'Abstract'
		lookup2 = 'ABSTRACT'
		f = open(txtList[i], "r", encoding="utf8")
		for num, line in enumerate(f, 1):
			# test = line.find(lookup)
			if lookup1 in line:
				if(num < 70):
					numLigne = num - 1
					# print(numLigne)
			elif lookup2 in line:
				if(num < 70):
					numLigne = num - 1
                    # print(numLigne)
                # print(num)
		author = get_author(v, numLigne)

		article = ET.Element("article")

		ET.SubElement(article, "preamble").text = fileName
		ET.SubElement(article, "titre").text = title
		ET.SubElement(article, "auteur").text = author
		ET.SubElement(article, "abstract").text = abstract
		ET.SubElement(article, "biblio").text = references

		tree = ET.ElementTree(article)
		fileName = fileName[:-4]
		tree.write("sorties/" + fileName + ".xml")


if args.txt:
	txt()
	print("TXT EFFECTUE")
elif args.xml:
	xml()
	print("XML EFFECTUE")
    