'''
Created on Feb 6, 2016

@author: SharanyaVR
'''
import string
import os
import fnmatch
import re
import math
import sys
import pickle

def main(pathtotrainingdata):
    #pathtotrainingdata = "C:\\Users\\SharanyaV\\workspace\\NaiveBaiyesClassifier\\root\\TrainingData"
    classifieddictionary = {}
    countPDvalue=0
    countPTvalue=0
    countNDvalue=0 
    countNTvalue=0
    fileclass = 'none'
    #Python doesn't support wildcards directly in filenames to the open() call
    for dirpath, dirs, files in os.walk(pathtotrainingdata):
        for filename in fnmatch.filter(files, '*.txt'):
           with open(os.path.join(dirpath, filename)) as fp:
                if 'pos' in dirpath and 'dec' in dirpath:
                    fileclass='PD'
                    
                elif 'pos' in dirpath and 'tru' in dirpath:
                    fileclass='PT'
                    
                elif 'neg' in dirpath and 'dec' in dirpath:
                    fileclass='ND'
                    
                else:
                    fileclass='NT'
                    
                    
                for line in fp:
                    for word in line.split():
                    #in string.translate the second parameter is optional
                        word = word.translate(string.maketrans("",""), string.punctuation)
                        if word == '' or word == None:
                            continue
                        if word not in classifieddictionary:
                            classifieddictionary.update({word:{'PT':0, 'PD':0, 'ND':0, 'NT':0}})
                        if word in classifieddictionary:
                            if fileclass =='PD':
                                countPDvalue += 1
                                classifieddictionary[word]['PD'] +=1
                               
                            elif fileclass =='PT':
                                countPTvalue += 1
                                classifieddictionary[word]['PT'] +=1
                                                                    
                            elif fileclass =='ND':
                                countNDvalue += 1
                                classifieddictionary[word]['ND'] +=1
                                
                            else:
                                countNTvalue += 1
                                classifieddictionary[word]['NT'] +=1
                                
                        

    numberofuniquewordsinvocabulary = len(classifieddictionary.keys())
    
    nbmodelfilepointer = open("nbmodel.txt", "w")
    for word, values in classifieddictionary.iteritems():
        
        nbmodelfilepointer.write(word+';')
        #nbmodelfilepointer.flush()
        if('PD' not in classifieddictionary[word]):
            probofwordinclass = float(1)/ float(countPDvalue + numberofuniquewordsinvocabulary)
            logofprobofword = math.log(probofwordinclass)
            nbmodelfilepointer.write('PD:')
            nbmodelfilepointer.flush()
            nbmodelfilepointer.write(str(logofprobofword)+';')
            nbmodelfilepointer.flush()
        if('PT' not in classifieddictionary[word]):
            probofwordinclass = float(1)/ float(countPDvalue + numberofuniquewordsinvocabulary)
            logofprobofword = math.log(probofwordinclass)
            nbmodelfilepointer.write('PT:')
            nbmodelfilepointer.flush()
            nbmodelfilepointer.write(str(logofprobofword)+';')
            nbmodelfilepointer.flush()
        if('ND' not in classifieddictionary[word]):
            probofwordinclass = float(1)/ float(countPDvalue + numberofuniquewordsinvocabulary)
            logofprobofword = math.log(probofwordinclass)
            nbmodelfilepointer.write('ND:')
            nbmodelfilepointer.flush()
            nbmodelfilepointer.write(str(logofprobofword)+';')
            nbmodelfilepointer.flush()
        if('NT' not in classifieddictionary[word]):
            probofwordinclass = float(1)/ float(countPDvalue + numberofuniquewordsinvocabulary)
            logofprobofword = math.log(probofwordinclass)
            nbmodelfilepointer.write('NT:')
            nbmodelfilepointer.flush()
            nbmodelfilepointer.write(str(logofprobofword)+';')
            nbmodelfilepointer.flush()
                    
        for parameterclass, noofcoccurenceofwordinclass in classifieddictionary[word].iteritems():
            if parameterclass == 'PD':
                probofwordinclass = float(noofcoccurenceofwordinclass+1)/ float(countPDvalue + numberofuniquewordsinvocabulary)
                logofprobofword = math.log(probofwordinclass)
                nbmodelfilepointer.write('PD:')
                nbmodelfilepointer.flush()
                nbmodelfilepointer.write(str(logofprobofword)+';')
                nbmodelfilepointer.flush()
            elif parameterclass == 'PT':
                probofwordinclass = float(noofcoccurenceofwordinclass+1)/ float(countPTvalue + numberofuniquewordsinvocabulary)
                logofprobofword = math.log(probofwordinclass)
                nbmodelfilepointer.write('PT:')
                nbmodelfilepointer.flush()
                nbmodelfilepointer.write(str(logofprobofword)+';')
                nbmodelfilepointer.flush()
            elif parameterclass == 'ND':
                probofwordinclass = float(noofcoccurenceofwordinclass+1)/float(countNDvalue + numberofuniquewordsinvocabulary)
                logofprobofword = math.log(probofwordinclass)
                nbmodelfilepointer.write('ND:')
                nbmodelfilepointer.flush()
                nbmodelfilepointer.write(str(logofprobofword)+';')
                nbmodelfilepointer.flush()
            else:
                probofwordinclass = float(noofcoccurenceofwordinclass+1)/float(countNTvalue + numberofuniquewordsinvocabulary)
                logofprobofword =  math.log(probofwordinclass)
                nbmodelfilepointer.write('NT:')
                nbmodelfilepointer.flush()
                nbmodelfilepointer.write(str(logofprobofword)+';')
                nbmodelfilepointer.flush()
        nbmodelfilepointer.write('\n')
        nbmodelfilepointer.flush()
       
    
    nbmodelfilepointer.close()
    
    
main(sys.argv[1])  