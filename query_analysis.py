#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
import math 

raw_data_source = open('myData.csv', 'r')
significant_data_source = open('significantData.csv', 'w')
raw_data = csv.DictReader(raw_data_source)
significant_data = csv.DictWriter(significant_data_source, None)


def cleanCsv():

    """
    Return the count of each row 
    return dict: {count_emotion: key} 
    """ 

    count_neutral = 0
    count_sad = 0
    count_angry = 0
    count_happy = 0

    count_session_neutral = 0 

    for column_values in raw_data:

        if significant_data.fieldnames is None:
            dh = dict((h, h) for h in raw_data.fieldnames)
            significant_data.fieldnames = raw_data.fieldnames
            significant_data.writerow(dh)

        if column_values['AOI[Sad_Right]Hit'] == '1':
            significant_data.writerow(column_values)
            count_sad = count_sad + 1

        if column_values['AOI[Neutral_Left]Hit'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

        if column_values['AOI[Neutral_Left]Hit_0'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

        if column_values['AOI[Neutral_Right]Hit'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

        if column_values['AOI[Angry_Left]Hit'] == '1':
            significant_data.writerow(column_values)
            count_angry = count_angry + 1

        if column_values['AOI[Neutral_Right]Hit_0'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

        if column_values['AOI[Happy_Right]Hit'] == '1':
            significant_data.writerow(column_values)
            count_happy = count_happy + 1

        if column_values['AOI[Neutral_Left]Hit_1'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

        if column_values['AOI[Happy_Left]Hit'] == '1':
            significant_data.writerow(column_values)
            count_happy = count_happy + 1

        if column_values['AOI[Neutral_Right]Hit_1'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

        if column_values['AOI[Sad_Left]Hit'] == '1':
            significant_data.writerow(column_values)
            count_sad = count_sad + 1

        if column_values['AOI[Neutral_Right]Hit_2'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

        if column_values['AOI[Angry_Right]Hit'] == '1':
            significant_data.writerow(column_values)
            count_angry = count_angry + 1

        if column_values['AOI[Neutral_Left]Hit_2'] == '1':
            significant_data.writerow(column_values)
            count_neutral = count_neutral + 1

    return {
        'count_neutral': count_neutral,
        'count_sad': count_sad,
        'count_angry': count_angry,
        'count_happy': count_happy,
        }


def findTotalTime(count_dict):
    
    total_neutral = count_dict.get('count_neutral') * 4998
    total_sad = count_dict.get('count_sad') * 4998
    total_angry = count_dict.get('count_angry') * 4998
    total_happy = count_dict.get('count_happy') * 4998
    print 'The total amount of time the infant is fixating on neutral {} miliseconds'.format(total_neutral)
    print 'The total amount of time the infant is fixating on sad {} miliseconds'.format(total_sad)
    print 'The total amount of time the infant is fixating on angry {} miliseconds'.format(total_angry)
    print 'The total amount of time the infant is fixating on happy {} miliseconds'.format(total_happy)

def findAverageDuration(): 

    print("not sure what will go here ?")

def findBins():
    
    """
    Return the dictionary of rows in order 
    return dict: {starting_value: key, my_list: [keys]} 
    """ 

    df = pd.read_csv('significantData.csv')
    df = df.sort_values('RecordingTimestamp')
    df.to_csv('significantData.csv', index=False)
    read_in = pd.read_csv('significantData.csv')
    count = 0
    this = []
    return_bins = {}
    word = (read_in['AOI[Neutral_Left]Hit_0']).tolist()
    
    if word[0] == '1':
        return_bins.update({'start_value': 1})
    else: 
        return_bins.update({'start_value': 0})
    for v, w in zip(word[:-1], word[1:]):
        if v == w and v != '': 
            print v
            count = count + 1
        else: 
            total = count
            this.append(count)
        my_list = sorted(list(set(this)))
    return_bins.update({'my_list': my_list})
    return return_bins

def findSignificantBins(return_bins):
    
    """
    Return the consequative values of even and odd rows 
    """
    
    count = 0
    range_even = []
    range_odd = []
    for i in xrange(1,len(return_bins['my_list'])):
        value_range = (return_bins['my_list'][i] - return_bins['my_list'][(i-1)])
        count = count + 1
        if (count % 2 == 0) :
            range_even.append(value_range)
        else: 
            range_odd.append(value_range)

    print "This is the even {}".format(range_even)
    print "This is the odd {}".format(range_odd)
    if (return_bins.get('start_value') == 0) : 
        return range_even
    else:
        return range_odd

def find_conseq_avg():
    print("Blah")


if __name__ == '__main__':
    count_dict = cleanCsv()
    findTotalTime(count_dict)
    my_list = findBins()
    findSignificantBins (my_list)
    significant_data_source.close()
    raw_data_source.close()



            