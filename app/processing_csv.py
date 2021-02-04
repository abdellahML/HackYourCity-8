import pandas as pd

class processing:

    def create_finale_csv(self, files):
        """In this function we will create a new csv file with only columns that are interesting for us.
            For that, we need a list of csv file name and this function will create the new dataset
        """

        df1 = pd.read_csv('assets/brasserieMF.csv',)

        df = pd.DataFrame(df1, columns=["societe", "rue", "numero", "cp", 
                                                "localite", "telephone", "website", "longitude", 
                                                "latitude", "date_fin", "date_debut", "lieu_nom"])

        df5 = pd.read_csv('assets/patrimonesMF.csv')
        df5 = df5.rename(columns={'descriptif': 'rue', 'type': 'societe'})
        df5 = pd.DataFrame(df5, columns=["societe", "rue", "numero", "cp", 
                                                "localite", "telephone", "website", "longitude", 
                                                "latitude", "date_fin", "date_debut", "lieu_nom"])
        df = df.append(df5)

        df5 = pd.read_csv('assets/festivMF.csv')
        df5 = df5.rename(columns={'lieu_nom': 'rue', 'titre': 'societe'})
        df5 = pd.DataFrame(df5, columns=["societe", "rue", "numero", "cp", 
                                                "localite", "telephone", "website", "longitude", 
                                                "latitude", "date_fin", "date_debut", "lieu_nom"])
        df = df.append(df5)


        for name in files:

            df2 = pd.read_csv(name)

            df2 = pd.DataFrame(df2, columns=["societe", "rue", "numero", "cp", 
                                                "localite", "telephone", "website", "longitude", 
                                                "latitude", "date_fin", "date_debut", "lieu_nom"])
    
            df = df.append(df2)

        df = df.reset_index()
        df = df.drop('index', axis=1)
        df.to_csv("final.csv")



files = ['assets/campingMF.csv', 'assets/chambresMF.csv', 'assets/cinemaMF.csv',
         'assets/gitesMF.csv', 'assets/glacierMF.csv', 'assets/hotelsMF.csv', 
        'assets/museesMF.csv', 'assets/SnackfriteMF.csv', 'assets/traiteursMF.csv']

processing().create_finale_csv(files)

