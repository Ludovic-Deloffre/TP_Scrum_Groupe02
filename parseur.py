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

def get_introduction(rawTxt, nbMot):
	a, b = rawTxt.find('Introduction'), rawTxt.find('\n2\n')
	if len(rawTxt[a:b]) > nbMot/10:
		a, b = rawTxt.find('Introduction'), rawTxt.find('\n2 ')
		if len(rawTxt[a:b]) > nbMot/10:
			a, b = rawTxt.find('Introduction'), rawTxt.find('\nII. ')
	elif len(rawTxt[a:b]) == 0:
		a, b = rawTxt.find('INTRODUCTION'), rawTxt.find('\nII.')

	return(rawTxt[a:b])

def get_conclusion(rawTxt):
	a, b = rawTxt.find('Conclusion'), rawTxt.find('References')
	if (len(rawTxt[a:b]) > 10000) or (len(rawTxt[a:b]) == 0) :
		a, b = rawTxt.find('Conclusions'), rawTxt.find('References')
	if (len(rawTxt[a:b]) > 10000) or (len(rawTxt[a:b]) == 0):
		a, b = rawTxt.find('CONCLUSION'), rawTxt.find('REFERENCES')
	if (len(rawTxt[a:b]) > 10000) or (len(rawTxt[a:b]) == 0):
		a, b = rawTxt.find('CONCLUSIONS'), rawTxt.find('REFERENCES')

	return(rawTxt[a:b])

def get_discussion(rawTxt):
	a, b, c = rawTxt.find('Conclusion'), rawTxt.find('Acknowledgements'), rawTxt.find('References')
	if (len(rawTxt[b:c]) > 1000) or (len(rawTxt[b:c]) == 0) :
		a, b, c = rawTxt.find('CONCLUSION'), rawTxt.find('Acknowledgements'), rawTxt.find('REFERENCES')
	if (len(rawTxt[b:c]) > 1000) or (len(rawTxt[b:c]) == 0) :
		a, b, c = rawTxt.find('CONCLUSIONS'), rawTxt.find('Acknowledgements'), rawTxt.find('REFERENCES')
	if (len(rawTxt[b:c]) > 1000) or (len(rawTxt[b:c]) == 0) :
		a, b, c = rawTxt.find('Conclusions'), rawTxt.find('Acknowledgements'), rawTxt.find('References')
	return(rawTxt[b:c])

def get_developpement(rawTxt, nbMot):
	a, b, c = rawTxt.find('Introduction'), rawTxt.find('\n2\n'), rawTxt.find('Conclusion')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0) :
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\n2 '), rawTxt.find('Conclusion')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0) :
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\n2 '), rawTxt.find('Conclusions')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0) :
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\n2 '), rawTxt.find('CONCLUSION')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\n2 '), rawTxt.find('CONCLUSIONS')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\nII. '), rawTxt.find('Conclusion')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\nII. '), rawTxt.find('Conclusions')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\nII. '), rawTxt.find('CONCLUSION')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('Introduction'), rawTxt.find('\nII. '), rawTxt.find('CONCLUSIONS')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('INTRODUCTION'), rawTxt.find('\nII. '), rawTxt.find('Conclusion')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('INTRODUCTION'), rawTxt.find('\nII. '), rawTxt.find('Conclusions')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('INTRODUCTION'), rawTxt.find('\nII. '), rawTxt.find('CONCLUSION')
	if (len(rawTxt[b:c]) > nbMot * 0.9) or (len(rawTxt[b:c]) == 0):
		 a, b, c = rawTxt.find('INTRODUCTION'), rawTxt.find('\nII. '), rawTxt.find('CONCLUSIONS')

	return(rawTxt[b:c])

def get_references(rawTxt):
	c=  rawTxt.find('References')
	if len(rawTxt[c:]) == 0:
		c=  rawTxt.find('REFERENCES')
	return(rawTxt[c:-1].encode('ascii','ignore').decode('ascii'))

def get_title(lines):
	
	title = str(lines[0:1]) + "\n"
	return(title)

def get_author(lines, numLigne):
	authors = str(lines[2:numLigne]) + "\n"
	return(authors)

def remove_create():
	dir = 'sorties'
	if os.path.exists(dir):
		shutil.rmtree(dir)

	os.mkdir(dir)


dossierTxt = input('Entrez le nom du dossier : ')

fileList = (glob.glob(dossierTxt + "/*.txt"))

for i in range(len(fileList)):
		print(str(i)+" : "+fileList[i])
		
txtList = list();
yes = True
while(yes):
		numero = int(input("Entrez le numéro du dossier choisi, tapez -1 pour valider : "))
		if(numero != -1 and numero < len(fileList)):
				txtList.append(fileList[numero])
		else:
				yes = False

remove_create()


for i in range(len(txtList)) :

	numLigne = 0
	lookup1 = "Abstract"

	g = open(txtList[i], "r", encoding="utf-8")
	lines = [line.rstrip() for line in g]
	g.close()
	title = get_title(lines)

	
	
	f = open(txtList[i], "r", encoding="utf-8")
	for i in range(20):
		
		if lookup1 in lines[i]:
			numLigne = i
			break
		if lookup1.upper() in lines[i]:
			numLigne = i
			break
		
	if lookup1 in lines:
		numLigne = lines.index(lookup1)
	elif lookup1.upper() in lines:
		numLigne = lines.index(lookup1.upper())
	authors = ''.join(get_author(lines,numLigne))
	
	fileName = f.name.split('/')
	fileName = fileName[len(fileName)-1]
	rawTxt = f.read()
	nbMot = len(rawTxt)

	abstract = get_abstract(rawTxt)
	references = get_references(rawTxt)
	conclusion = get_conclusion(rawTxt)
	developpement = get_developpement(rawTxt, nbMot)
	introduction = get_introduction(rawTxt, nbMot)
	discussion = get_discussion(rawTxt)

	os.chmod("sorties/", 0o777)

	if args.txt:
		g = open("sorties/"+ fileName, "w", encoding="utf-8")

		g.write(fileName+"\n")
		g.write(title)
		g.write(authors)
		g.write(abstract)
		g.write(introduction)
		g.write(developpement)
		g.write(conclusion)
		g.write(references)
		g.close()

	elif args.xml:
		article = ET.Element("article")

		ET.SubElement(article, "preamble").text = fileName
		ET.SubElement(article, "titre").text = title
		ET.SubElement(article, "auteur").text = authors
		ET.SubElement(article, "abstract").text = abstract
		ET.SubElement(article, "introduction").text = introduction
		ET.SubElement(article, "developpement").text = developpement
		ET.SubElement(article, "conclusion").text = conclusion
		ET.SubElement(article, "discussion").text = discussion
		ET.SubElement(article, "biblio").text = references

		tree = ET.ElementTree(article)
		fileName = fileName[:-4]
		tree.write("sorties/" + fileName + ".xml")