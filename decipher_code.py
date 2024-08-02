
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib as plt

url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"


def decode_url(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    headings = soup.find("table")

    array = np.array([])
    row = 1
    for heading in headings:
        box = heading.getText("_")
        if row >=2:
            array = np.append(array, [box.split("_")[0], box.split("_")[2], box.split("_")[1]])
        row += 1
    array = np.reshape(array, (-1,3))

    for y in range(int(max(array[:,1])), -1, -1):
        s = ""
        for x in range(int(max(array[:,0]))+1):
            x_arr = array[:,0]
            y_arr = array[:,1]
            if np.any((x_arr == str(x)) & (y_arr == str(y))) == False:
                s += ' '
            else:
                index = np.where((x_arr == str(x)) & (y_arr == str(y)))
                s += array[int(index[0]),2]
        print(s)

decode_url(url)













