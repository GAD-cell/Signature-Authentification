import csv
import os
import itertools
import pandas as pd

forgery_type=['Opposite Hand','Skilled','Simple']

genuine=os.listdir('./UTSig/Genuine')

final_combination=[]
label=[]
genuine_path='./UTSig/Genuine/'
forgery_path='./UTSig/Forgery/'
for signature in genuine :
    dataset_genuine=os.listdir(genuine_path+str(signature))
    genuine_list=[os.path.join(genuine_path+signature+'/', file) for file in dataset_genuine]
    
    #genuine with forgery
    for forgery in forgery_type:
        dataset_forgery=os.listdir(forgery_path+forgery+'/'+signature)
        forgery_list=[os.path.join(forgery_path+forgery+'/'+signature+'/', file) for file in dataset_forgery]
        combinations=list(itertools.product(genuine_list, forgery_list))
        final_combination=final_combination+combinations
        temp_label=[1 for i in range(len(combinations))]
        label=label+temp_label
    
    #genuine with genuine
    combinations=list(itertools.product(genuine_list, genuine_list))
    final_combination=final_combination+combinations
    temp_label=[0 for i in range(len(combinations))]
    label=label+temp_label




df = pd.DataFrame(final_combination, columns=["Authentique", "Falsifié"])
df['label']=label

df.to_csv("combinations.csv", index=False)



