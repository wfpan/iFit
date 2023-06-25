# -*- coding: UTF-8 -*-
'''
@Project ：getPrideScore
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：Du Xin
@Date    ：2023-6-01 15:56
@Abstract: This .py file is used to call function to get Pride Score
'''
import os
import sys
import jpype

def get_Pride_score(INPUT_NET):
    net_AbsPath = os.path.abspath(INPUT_NET)
    jvmPath = jpype.getDefaultJVMPath()
    jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=Pride.jar")
    JDClass = jpype.JClass("cn.edu.zjgsu.algorithms.scoring.WeightedPageRank_wfpan_v15")
    jd = JDClass()
    jd.main(jpype.JString[:]([net_AbsPath]))
    jpype.shutdownJVM()

if __name__ == "__main__":
    INPUT_NET = 'one network file.net'
    get_Pride_score(INPUT_NET)
