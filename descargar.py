#!/usr/bin/env python3
#coding=utf-8

from utilidades.ficheros.GestorFicheros import GestorFicheros
import constantes
import bs4, glob, os
from mako.template import Template

gf=GestorFicheros()

for i in range(0, 14):
    FICHERO_DESTINO=constantes.RUTA_FICHEROS_DESCARGADOS.format(i)
    if not gf.existe_fichero ( FICHERO_DESTINO ): 
        gf.descargar_fichero (constantes.URL_BASE.format ( i ),
                          FICHERO_DESTINO)
        
        
contador_comics=0
for i in range(0, 14):
    FICHERO_A_PROCESAR=constantes.RUTA_FICHEROS_DESCARGADOS.format(i)
    sopa=bs4.BeautifulSoup ( open(FICHERO_A_PROCESAR, "r"), "html5lib" )
    divs_miniatura=sopa.find_all("div", "bg_comic")
    for div in divs_miniatura:
        enlace=div.find("a")
        URL_COMIC = constantes.URL + enlace["href"]
        print (URL_COMIC)
        COMIC_DESCARGA=constantes.RUTA_COMICS_DESCARGADOS.format ( contador_comics )
        if not gf.existe_fichero ( COMIC_DESCARGA ):
            gf.descargar_fichero ( URL_COMIC, COMIC_DESCARGA )
        contador_comics=contador_comics + 1
        
ficheros_comic=glob.glob( constantes.CARPETA_COMICS + os.sep + "*.html")
for f in ficheros_comic:
    sopa = bs4.BeautifulSoup ( open (f, "r") , "html5lib")
    panel=sopa.find_all("div", "panel")
    for p in panel:
        imagenes=p.find_all("img")
        for i in imagenes:
            if i["src"].find("thumbna")==-1:
                print (i["src"])