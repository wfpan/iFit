# -*- coding: UTF-8 -*-
'''
@Project ：iFit
@File    ：CG_main.py
@IDE     ：PyCharm
@Author  ：Du Xin
@Date    ：2023-5-31 15:09
@Abstract: This is main function to calculate CG metric
'''
import pandas as pd
from CG import CG

def readPride2csv(Pride_OUTPUT):
    CNPride = {'ClassName':[],'Pride':[]}
    f = open(Pride_OUTPUT, "r")
    lines = f.readlines()
    for line in lines:
        value = line.strip().split("\t")
        CNPride['ClassName'].append(value[0])
        CNPride['Pride'].append(float(value[1]))
    return CNPride

def Exec(Pride_INPUT,Pride_OUTPUT,READCOLUMN,METRIC):
    _CNPride = readPride2csv(Pride_OUTPUT)
    _PrideDF = pd.DataFrame(_CNPride)
    READCOLUMN.append('iFit')
    cg = CG(_NetPath=Pride_INPUT, _PrideDF=_PrideDF,METRIC=METRIC)
    cg._Calculate_CG().to_csv(CG_OUTPUT,index=False)

if __name__ == "__main__":
    Pride_INPUT = 'one network file.net'  # you just need to modify the file Name of network
    Pride_OUTPUT = Pride_INPUT.replace('.net','_pride.txt')
    CG_OUTPUT = Pride_INPUT.replace('.net','_iFit.csv')
    METRIC = 'Pride'
    READCOLUMN = ['ClassName']
    Exec(Pride_INPUT,Pride_OUTPUT,READCOLUMN,METRIC)