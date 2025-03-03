import pandas as pd
import numpy as np 


def spanishNames():
    maleNames = pd.read_csv('./helpers/male_names.csv')['name']
    femaleNames = pd.read_csv('./helpers/female_names.csv')['name']
    maleNames =[str(x).lower() for x in maleNames]
    femaleNames =[str(x).lower() for x in femaleNames]
    extraFemaleNames = ['alicia', 'ana', 'anaia', 'anayeli', 'blanca', 'brenda',
                        'carmen', 'cynthia', 'diana', 'dulce', 'edith', 'elena',
                        'elizeth', 'eliseth', 'emilia', 'erika', 'érika', 'erica',
                        'érica', 'estela', 'imelda', 'jaciel', 'jimena', 'jorge', 'ximena',
                        'julia', 'kareni', 'kenya', 'leticia', 'maría', 'maria', 'marielena',
                        'miriam', 'paula', 'sofia', 'sofía', 'sonia', 'tania', 'teresita',
                        'valeria', 'valery', 'xochitl', 'yolanda']
    femaleNames = femaleNames + extraFemaleNames
    extraMaleNames = ['arturo', 'edgar', 'elias', 'elías', 'eliezer', 'gelacio', 'giovanni', 'ivan', 
                  'jesus', 'jesús', 'nicolás', 'nicolas', 'paco', 'raul', 'ruben', 'sergio',
                  'victor']
    maleNames= maleNames + extraMaleNames
    maleNamesDict = {x:'male' for x in maleNames}
    femaleNamesDict ={x:'female' for x in femaleNames}
    namesDict = { **maleNamesDict, **femaleNamesDict}
    return pd.DataFrame.from_dict(namesDict)