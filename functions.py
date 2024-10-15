from nltk.sentiment import SentimentIntensityAnalyzer as sia
import glob
import os
from pathlib import Path

analyser = sia()
texts = []
filenames = []

for filename in glob.glob('diary/*'):
    name = Path(filename).stem
    filenames.append(name)
    with open(filename,'r') as file:
        filecontent = file.read()
        texts.append(filecontent)

for text in texts:
    score = analyser.polarity_scores(text)




# {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}