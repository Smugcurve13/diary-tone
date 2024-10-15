from nltk.sentiment import SentimentIntensityAnalyzer as sia
import glob
import os
from pathlib import Path
import pandas
import plotly.express as px


def plotfigure(choice):

    analyser = sia()
    texts = []
    filenames = []
    scores = []

    for filename in glob.glob('diary/*'):
        name = Path(filename).stem
        filenames.append(name)
        with open(filename,'r') as file:
            filecontent = file.read()
            texts.append(filecontent)

    for text in texts:
        score = analyser.polarity_scores(text)
        scores.append(score)

    pos_list = []
    neg_list = []

    for s in scores:
        pos_list.append(s['pos'])
        neg_list.append(s['neg'])



    if choice == 'pos':
        plot = px.line(x=filenames,y=pos_list,labels={'x':'Date','y':'Postivity'})
        return plot

    if choice == 'neg':
        plot = px.line(x=filenames,y=neg_list,labels={'x':'Date','y':'Negativity'})
        return plot


# {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}