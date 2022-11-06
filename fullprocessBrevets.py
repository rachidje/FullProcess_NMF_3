import os
from FullProcess.FullprocessEn import FullProcessText as FPTEn
from FullProcess.FullprocessEs import FullProcessText as FPTEs
from FullProcess.FullprocessFr import FullProcessText as FPTFr
from WassatiLib.divers.modules import getCurrentDate
from FullProcess.fullProcess_functions import *
from tqdm import tqdm

tqdm.pandas()

## Fullprocess sur les datas
filename = "dataToPredict/descriptions_brevets.csv"
output = f"processed_petitions/brevets_marocain_processed_{getCurrentDate(['year', 'month'])}.csv"
df = getDataframe(filename)

def runFullprocess(brevet):
    title_description = brevet
    fpt = FPTFr()
    
    return fpt.fullProcess(title_description)

if not os.path.isfile(output):
    df['final_content'] = df['title_description'].progress_apply(runFullprocess)
    df = df.dropna(subset=['final_content'])

    df.to_csv(output, index= False)
