import pandas as pd
import random
import numpy as np

class dataCollecting:

    def return_activities_places(self, what, location, animation, city="default_value"):

        if what == "sport":
            if location == "interior":
                if animation == "foule":

                    print("Rien pour le moment, on sait qu'il y a le laser game")
                
                elif animation == "solo":

                    print("Rien pour le moment, salle de fitness à ajouter")
            
            elif location =="exterior":
                if animation == "foule":

                    df = pd.read_csv("assets/festivMF.csv")
                    df.drop("Unnamed: 0", inplace=True,axis=1)
                    propositions = []
                    for i in range(5):
                        propositions.append(df.iloc[random.randint(0,len(df)),[1,3,6,9,11,14,17]].values)
                    return propositions

                elif animation == "solo":

                    files=["Data/hannut_centre_equestre.csv", '"Data/marche_pt_vert.csv"']
                    i = random.randint(0,len(files))
                    df = pd.read_csv(files[i])
                    
        
        elif what == "musee":
            if location == "interior":
                if animation == "foule":

                    files=['assets/brasserieMF.csv', 'assets/cinemaMF.csv']
                    i = random.randint(0,len(files))
                    df = pd.read_csv(files[i])
                
                elif animation == "solo":

                    files=['assets/museesMF.csv', 'Data/hannut_femme_detente.csv']
                    i = random.randint(0,len(files))
                    df = pd.read_csv(files[i])
            
            elif location =="exterior":
                if animation == "foule":
                    print('rien pour le moment, on pourra mettre les marchés, evenement culturelle, marché artisanal')
                
                elif animation == "solo":
                    df = pd.read_csv('assets/patrimonesMF.csv')
        return df


    
    def create_list_csv_by_city(self, file_name, city_name):
        """This function will sort the database according to the city, so it will take only places which are in the city
        and return it"""

        #We couldn't make it for this hackathon because we hadn't enough data and especially good data
        pass

    def choose_a_place(self, df, persona):
        """This function will choose place according to criteria, but since for now we didn't have enough response
        we make a mock to be able to finish our project. This function will give points according to the personna
        and will put in descending order"""

        score = np.array([[5, 0, 3, 3, 3], 
                          [3, 5, 4, 4, 1],
                          [2, 3, 5, 4, 4],
                          [3, 3, 3, 5, 3],
                          [3, 1, 3, 4, 5]])

        if persona == "famille":
            val = self.switch_type(df['type'])
            df['score'] = score[val, 0]
        elif persona == "seul":
            val = self.switch_type(df['type'])
            df['score'] = score[val, 1]
        elif persona =='amis':
            val = self.switch_type(df['type'])
            df['score'] = score[val, 2]
        elif persona =='touriste':
            val = self.switch_type(df['type'])
            df['score'] = score[val, 3]
        elif persona =='couple':
            val = self.switch_type(df['type'])
            df['score'] = score[val, 4]
        
        df['score'] = df['score'] + df['score_given']

        return df
    

    def switch_type(self, type_name):
        
        if type_name == 'famille':
            val = 0
        elif type_name == 'seul':
            val = 1
        elif type_name == 'amis':
            val = 2
        elif type_name == 'touriste':
            val = 3
        elif type_name == 'couple':
            val = 4

        return val
