# TP_Scrum_Groupe02
## Membres du groupes :
#### Ludovic DELOFFRE
#### Thomas LEGRAND
#### Josué ORCIERE

### Langage : Python 

Le parseur est programmé sur un seul fichier : parser.py

Le fichier python se trouve dans le même répertoire que le dossier contenant les articles à parser.
Lancement du programme : 
2 options de lancement : -x et -t

-x : crée un fichier XML à la sortie
-t : crée un fichier TXT à la sortie

Exécution : 

### $ python3 ./parseur.py -t
ou 
### $ python3 ./parseur.py -x

#### Exemple d'execution avec le dossier contenant les fichiers de test 'pdftotext' :

#### $ python3 ./parseur.py -x
#### Entrez le nom du dossier : pdftotext
#### 0 : pdftotext/Torres-moreno1998.txt
#### 1 : pdftotext/Stolcke_1996_Automatic linguistic.txt
#### 2 : pdftotext/Das_Martins.txt
#### 3 : pdftotext/Gonzalez_2018_Wisebe.txt
#### 4 : pdftotext/Mikolov.txt
#### 5 : pdftotext/Torres.txt
#### 6 : pdftotext/Boudin-Torres-2006.txt
#### 7 : pdftotext/Iria_Juan-Manuel_Gerardo.txt
#### 8 : pdftotext/Nasr.txt
#### 9 : pdftotext/mikheev J02-3002.txt
#### 10 : pdftotext/Eissen_2002_Analysis of clustering algorithms for web-based search.txt
#### Entrez le numéro du dossier choisi, tapez -1 pour valider : 2
#### Entrez le numéro du dossier choisi, tapez -1 pour valider : 5
#### Entrez le numéro du dossier choisi, tapez -1 pour valider : 7
#### Entrez le numéro du dossier choisi, tapez -1 pour valider : -1
#### $

Suite à cette execution, le parseur va parser les documents renseigné et extraire les résultats dans un fichier XML avec les balises adèquates.
Les fichiers XML se trouveront dans le dossier 'sorties', se trouvant lui aussi dans le meme repertoire que le parseur et le dossier à parser.
