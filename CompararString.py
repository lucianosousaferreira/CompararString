from Levenshtein import *
import pandas as pd
from tqdm import tqdm

a = ['123-textotexto','222-textuuulllll','8888-rrrrtextoooo']
b = ['33-textotexto','22444-textuuulllll','8888ppppptextoooo']
list_similaridades = []

def CompararStrings(list_A: list,list_B: list):
    for txt_1 in tqdm(list_A):
        for txt_2 in list_B:
            total = len(txt_1)
            distancia = distance(txt_1, txt_2)
            diferenca = total-distancia
            similar = (100*diferenca)/total
            similaridade = round(similar,2)
            if similaridade > 67:
                list_similaridades.append(str(txt_1)+'|'+str(txt_2)+'|'+str(similaridade)+' %')

    df_out = pd.DataFrame([list_similaridades]).T
    df_out = df_out[0].str.split("|",expand=True)
    df_out.rename(columns={0:'aplicacao_1',1:'aplicacao_2',2:'similaridade'},inplace=True)
    df_out.to_excel('aplicacoes_similares.xlsx',index=False)

CompararStrings(list_A = a,list_B = b)
