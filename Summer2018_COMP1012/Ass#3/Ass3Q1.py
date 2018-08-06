# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import StatisticsCalculation
import InputOutputHandler
file=input('Enter csv file name: ')#open a file
file='Grades.csv'
headings,data=InputOutputHandler.readCSVFile(file)#a tuple of headings and list
means=StatisticsCalculation.calculateMean(data)#mean value of data
stdDevs=StatisticsCalculation.calculateStdDev(data, means)#std of data
mins=StatisticsCalculation.findMin(data, means)#minimum value
maxs=StatisticsCalculation.findMax(data, means)#maximum value
cutOFF=51    #pass mark, lower than this will be counted as failure
passed,failed=StatisticsCalculation.findPassedFailed(data, cutOFF)#num of pass and faile
final_OUTPUT=InputOutputHandler.printCSVResults(headings, means, stdDevs, mins, maxs,passed, failed)
print(final_OUTPUT)
