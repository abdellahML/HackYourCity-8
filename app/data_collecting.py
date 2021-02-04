import pandas as pd
import random

class dataCollecting:

    def return_activities_places(self, what, location, animation):

        if what == "sport":
            if location == "interior":
                if animation == "foule":
                    print("Rien pour le moment, on sait qu'il y a le laser game")
                
                elif animation == "solo":
                    print("Rien pour le moment")
            
            elif location =="exterior":
                if animation == "foule":
                    df = pd.read_csv("assets/festivMF.csv")
                
                elif animation == "solo":
                    df = pd.read_csv("Data/hannut_centre_equestre.csv")
        
        elif what == "musee":
            if location == "interior":
                if animation == "foule":
                    files['assets/brasserieMF.csv', 'assets/cinemaMF.csv']
                    i = random.randint(len(files))
                    df = pd.read_csv(files[i])
                
                elif animation == "solo":
                    df = pd.read_csv('assets/museesMF.csv')
            
            elif location =="exterior":
                if animation == "foule":
                    print('rien pour le moment')
                
                elif animation == "solo":
                    df = pd.read_csv('assets/patrimonesMF.csv')