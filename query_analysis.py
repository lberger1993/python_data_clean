#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

a = open('myData.csv', 'r')
b = open('significantData.csv', 'w')
ra = csv.DictReader(a)
wb = csv.DictWriter(b, None)


def cleanCsv():
    
    # declares count of each row 
    count_sad = 0
    count_neutral = 0
    count_angry = 0
    count_happy = 0
    for d in ra:
        
        if wb.fieldnames is None:
            dh = dict((h, h) for h in ra.fieldnames)
            wb.fieldnames = ra.fieldnames
            wb.writerow(dh)
        
        if d['AOI[Sad_Right]Hit'] == '1':
            wb.writerow(d)
            count_sad = count_sad + 1
        
        if d['AOI[Neutral_Left]Hit'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1
        
        if d['AOI[Neutral_Left]Hit_0'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1
        
        if d['AOI[Neutral_Right]Hit'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1
        
        if d['AOI[Angry_Left]Hit'] == '1':
            wb.writerow(d)
        
        if d['AOI[Neutral_Right]Hit_0'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1
        
        if d['AOI[Happy_Right]Hit'] == '1':
            wb.writerow(d)
        
        if d['AOI[Neutral_Left]Hit_1'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1
        
        if d['AOI[Happy_Left]Hit'] == '1':
            wb.writerow(d)
        
        if d['AOI[Neutral_Right]Hit_1'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1
        
        if d['AOI[Sad_Left]Hit'] == '1':
            wb.writerow(d)
            count_sad = count_sad + 1
        
        if d['AOI[Neutral_Right]Hit_2'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1
        
        if d['AOI[Angry_Right]Hit'] == '1':
            wb.writerow(d)
        
        if d['AOI[Neutral_Left]Hit_2'] == '1':
            wb.writerow(d)
            count_neutral = count_neutral + 1

    print (count_neutral)
if __name__ == '__main__':
    cleanCsv()
    b.close()
    a.close()

			