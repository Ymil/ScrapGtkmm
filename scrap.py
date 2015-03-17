import urllib2 
import bs4
url = 'https://developer.gnome.org/gtkmm-tutorial/stable/' 
request = urllib2.Request(url, headers={"Accept-Language":"es-ES"})
pagina = urllib2.urlopen(request) #descagamos el sitio web (HTML)
soup = bs4.BeautifulSoup(pagina) #Traduse el html a una estructura manejable.
structure = open('structure.html',"r") #Abrimos nuestro archivo con las estructura html
parseStructure = structure.read() #Leemos su contenido
structure.seek(0)
structure.close()

downloadList = soup.select('.autotoc a') #Obtenemos todos los indices del contenido de su manual
indice = str(soup.select('.content')[0]) #Obtenemos el texto de la clase .content
for href in downloadList:
	#Descargamos el contenido de su indice
    urlPage = href.attrs.get('href')
    namePage = urlPage[0:-3] #Quitamos el .es
    indice = indice.replace(urlPage, namePage) 
    pageContent = urllib2.urlopen(url+urlPage)
    soupPage = bs4.BeautifulSoup(pageContent)
    contentPage = str(soupPage.select('.content')[0]) 
    downloadList2 = soup.select('.autotoc a')
    for href in downloadList2:
	    urlPage = href.attrs.get('href') #Obtenemos todo los enlaces del artico
	    contentPage = contentPage.replace(urlPage, urlPage[0:-3]) #Quitamos el .es
    pageHtml = open(namePage,"wb")
    pageHtml.write(parseStructure.replace("{htmlEntry}", contentPage)) #remplasamos el {htmlEntry} de nuestro template
    pageHtml.close()



#print indice
indexH = open('indice.html',"wb")
#print parseStructure.replace("{htmlEntry}", indice)
indexH.write(parseStructure.replace("{htmlEntry}", indice))

indexH.close()


