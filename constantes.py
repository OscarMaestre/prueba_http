#!/usr/bin/env python3

import os

CARPETA_HTML="descargas"
CARPETA_COMICS="comics"
URL="http://theoatmeal.com"
URL_BASE=URL+"/comics_pg/page:{0}"

RUTA_FICHEROS_DESCARGADOS= CARPETA_HTML + os.sep + "fichero_{0}.html"

RUTA_COMICS_DESCARGADOS = CARPETA_COMICS + os.sep+"comic_{0}.html"