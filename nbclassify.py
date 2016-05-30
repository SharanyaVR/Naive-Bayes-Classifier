'''
Created on Feb 7, 2016

@author: SharanyaV
'''
import os
import fnmatch
import string
import sys

def nbclassify(pathtotestdata):
    #pathtotestdata = "C:\\Users\\SharanyaV\\workspace\\NaiveBaiyesClassifier\\root\\TestData"
    modeldict = {} 
    nboutputfilepointer = open("nboutput.txt", "w")

    with open('nbmodel.txt', 'r') as nbmodelfilepointer:
        for line in nbmodelfilepointer:
            paramterlist = line.split(';')
            probabilitylistofword = {}
            word = paramterlist[0]
            for i in xrange(1,len(paramterlist)-1):
                classifiervaluepair = paramterlist[i].split(':')
                classifierkey = classifiervaluepair[0]
                probablityofkey = classifiervaluepair[1]
                probabilitylistofword[classifierkey] = float(probablityofkey)
                modeldict[word] = probabilitylistofword  
        
    print(modeldict)
            
    for dirpath, dirs, files in os.walk(pathtotestdata):
        for filename in fnmatch.filter(files, '*.txt'):
            print(filename)
            PDscore = 0
            PTscore = 0
            NDscore = 0
            NTscore = 0 
            with open(os.path.join(dirpath, filename)) as fp:               
                for line in fp:
                    for word in line.split():
                    #in string.translate the second parameter is optional
                        word = word.translate(string.maketrans("",""), string.punctuation)
                        if word in modeldict.keys():
                            classifieddataonword = modeldict.get(word) 
                            for classifierkey in classifieddataonword:
                                
                                score = classifieddataonword[classifierkey]
                                print(type(score))
                                if classifierkey == 'PD':
                                    PDscore += score
                                elif classifierkey == 'PT':
                                    PTscore += score
                                elif classifierkey == 'NT':
                                    NTscore += score
                                else:
                                    NDscore += score
            if PDscore >= PTscore and PDscore >= NDscore and PDscore >= NTscore:
                nboutputfilepointer.write("deceptive positive "+os.path.join(dirpath, filename)+"\n")
            elif PTscore >= PDscore and PTscore >= NDscore and PTscore >= NTscore:
                nboutputfilepointer.write("truthful positive "+os.path.join(dirpath, filename)+"\n")
            elif NTscore >= PDscore and NTscore >= NDscore and NTscore >= NDscore:
                nboutputfilepointer.write("truthful negative "+os.path.join(dirpath, filename)+"\n")  
            else:
                nboutputfilepointer.write("deceptive negative "+os.path.join(dirpath, filename)+"\n")                      
    nboutputfilepointer.close()
                         
nbclassify(sys.argv[1])