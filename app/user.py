import pandas as pd

'''
mock_users = {'WHAT': ["Sport", "Musée","Sport", "Musée","Sport", "Musée","Sport", "Musée"], 
            'WHERE': ["Jnterior", "Exterior","Jnterior", "Exterior","Jnterior", "Exterior","Jnterior", "Exterior"],
            "Animation":["Animation","Relaxation","Animation","Relaxation","Animation","Relaxation","Animation","Relaxation"],
            "ID" : [i for i in range(8)]
            }

df = pd.DataFrame(mock_users) 
print(df.head())
#df.to_csv("test.csv")
'''
df = pd.read_csv("test.csv")
df.drop("Unnamed: 0",axis=1,inplace=True)
class User:
    def __init__(self,id_=9,personnas="seul",what="Sport",location="Interior",animation="Relaxation"):
        self.id = id_
        self.what = what
        self.location = location
        self.animation = animation
        self.peronnas = personnas
    
    def saveUser(self):
        log = df[df["ID"]==self.id]
        if len(log)==0:
            new_df = pd.DataFrame({"WHAT":[self.what],"WHERE":[self.location],"Animation":[self.animation],"ID":[self.id]})
            updated_df = df.append(new_df, ignore_index=True)
            updated_df.to_csv("test.csv")
            return "User{} added".format(self.id)
        return "User{} already in files".format(self.id)
    
    def __str__(self):
        return "User params are : ID={} \n{} \n{} \n{} \n{}".format(self.id,self.what,self.location,self.animation,self.peronnas)
        


user = User(id_=14)
print(user.saveUser())

df = pd.read_csv("test.csv")
df.drop("Unnamed: 0",axis=1,inplace=True)
print(df)
        
        
