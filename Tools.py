#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from urllib.parse import urljoin
import pandas as pd
import numpy as np
import urllib.request
import os.path
from os import path

import os
import shutil
from shutil import copyfile

class Tools():

    def employee_picture_download(self, crawlerName):
        
        self.crawlerName = crawlerName
        
        exportDirectory = "Exports/"+ crawlerName + "/"
        
        dfRaw = pd.read_excel(exportDirectory + crawlerName + " Mitarbeiter.xlsx", dtype=str)
        
        downloads = 0
        downloadErrors = 0
        downloadStatus = []
        standardImageUrl = None
        
        new_df = dfRaw[["Nachname", "Vorname","Bild","PLZ (Geschäft)"]]

        for index, row in new_df.iterrows():
            
            try:
                vorname = str(row["Vorname"])
            except:
                vorname = ""
            
            try:
                nachname = str(row["Nachname"])
            except:
                nachname = ""
            
            try:
                plz = str(row["PLZ (Geschäft)"])
            except:
                plz = ""
            
            #try:
            image_name = "Exports/" + crawlerName + "/Mitarbeiter Bilder/" + vorname + "_" + nachname + "_" + plz + ".jpg"
            url = row["Bild"]
            
            if crawlerName == "Barmenia":
                standardImageUrl = "https://barmenia.de/media/images/adm_fotos_240x180/00000000.jpg"
            
            if crawlerName == "VPV":
                standardImageUrl = "https://www.vpv.de/service/bilder/vermittler/VPV_Icon.jpg"
            
            if crawlerName == "BHW":
                standardImageUrl = "https://finanzberatung.postbank.de/oruc.altin//images/mitarbeiter/brille.gif"
            
            if crawlerName == "DieBayrische":
                standardImageUrl = "https://www.diebayerische.de/.resources/bayerische-lm/webresources/img/placeholder-berater.jpg"

            if url == standardImageUrl:
                
                # make a duplicate of an existing file
                src = "Exports/" + crawlerName + "/Mitarbeiter Bilder/Standard.jpg"
                dst = image_name
                copyfile(src, dst)
                
                downloads += 1
                
            else:    
                dlCounter = 0

                if not path.exists(image_name):
                    #print("File " + image_name + " is not in folder")
                    if url != standardImageUrl:
                        time.sleep(1)
                    while dlCounter < 10:
                        try:
                            urllib.request.urlretrieve(url, image_name)
                            dlCounter += 1
                        except:
                            dlCounter += 1

                        if path.exists(image_name):
                            downloads += 1
                            break
                        else:
                            downloadErrors += 1
        
        downloadStatus.append("Downloads: " + str(downloads))
        downloadStatus.append("Download Errors: " + str(downloadErrors))
        
        return downloadStatus
    
    def write_employee_xlsx(self, dfRaw, crawlerName, cols):
        
        self.dfRaw = dfRaw
        self.crawlerName = crawlerName
        self.cols = cols
                
        df = pd.DataFrame.from_dict(dfRaw)
        df = df[cols]
        #df[:]

        #Write Dataframe to Excel Sheet
        writer = pd.ExcelWriter(crawlerName + "/" + crawlerName + " Mitarbeiter.xlsx")
        df.to_excel(writer, crawlerName)
        writer.save()
    
    def write_urlList_xlsx(self, dfRaw, crawlerName, cols):
               
        self.dfRaw = dfRaw
        self.crawlerName = crawlerName
        self.cols = cols
                
        df = pd.DataFrame.from_dict(dfRaw)
        df = df[cols]
        #df[:]

        #Write Dataframe to Excel Sheet
        writer = pd.ExcelWriter(crawlerName + "/" + crawlerName + "urlList" + ".xlsx")
        df.to_excel(writer, crawlerName)
        writer.save()
        
    def dictionaryList_to_pandasDf(self, employeeList):
        
        self.employeeList = employeeList
        
        dfRaw = pd.DataFrame.from_dict(employeeList)
        
        return dfRaw
    
    def get_cols(self, columnsList):
        
        self.columnsList = columnsList
        
        cols = []
        
        allColumns = ["Funktion","Nachname","Vorname","PLZ (Geschäft)","Ort (Geschäft)","Telefon (Geschäft)","Organisation","Qualifikation","Bild","Strasse","Eigene Website","EMail","Xing"]
        
        for name in allColumns:
            if name in columnsList:
                cols.append(name)
        
        return cols

