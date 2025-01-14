#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from datetime import date ,timedelta
from sklearn.preprocessing import MinMaxScaler

class load:
    def __init__ (self,filename):
        self.filename = filename
        self.data   = np.genfromtxt(self.filename,delimiter=',')
        self.date   = \
        np.array( [date(int(str(i)[:4]),int(str(i)[4:6]),int(str(i)[6:8]))\
                 for i in self.data[1:,0]] )
        self.open   = self.data[1:,1]
        self.high   = self.data[1:,2]
        self.low    = self.data[1:,3]
        self.close  = self.data[1:,4]
        self.vol    = self.data[1:,5]    
    
    def avarage(self,nweeks=1):
        self.open_avg  =[] 
        self.high_avg  =[]
        self.low_avg   =[]
        self.close_avg =[] 
        self.vol_avg   =[] 
        
        self.firstSat=self.date[np.where(np.array([d.weekday() for d in self.date])==5)[0][0]]
        while (self.firstSat<date.today() ) :
            self.open_avg.append([])
            self.high_avg.append([])
            self.low_avg.append([])
            self.close_avg.append([])
            self.vol_avg.append([])
            for i in range(nweeks*7-1):
                   self.index = np.where(self.date == self.firstSat+timedelta(i))
                   self.open_avg[-1].append(self.open[self.index])
                   self.high_avg[-1].append(self.high[self.index])
                   self.low_avg[-1].append(self.low[self.index])
                   self.close_avg[-1].append(self.close[self.index])
                   self.vol_avg[-1].append(self.vol[self.index])
            self.firstSat+=timedelta(weeks=nweeks)
        for i in range(len(self.open_avg)):
            self.temp =0
            self.counter =0 
            for j in range(len(self.open_avg[i])):
                try:
                    self.temp += float(self.open_avg[i][j])
                    self.counter += 1
                except: None 
            try:    
                self.open_avg[i] = self.temp/self.counter
                #print(self.counter)
            except: 
                #print('HBDG')
                self.open_avg[i] = None 
        for t in self.open_avg:
            if t == None:
                self.temp=self.open_avg.index(t)
                self.open_avg[self.temp] = self.open_avg[self.temp-1] 
############################################################################
        for i in range(len(self.high_avg)):
            self.temp =0
            self.counter =0 
            for j in range(len(self.high_avg[i])):
                try:
                    self.temp += float(self.high_avg[i][j])
                    self.counter += 1
                except: None 
            try:    
                self.high_avg[i] = self.temp/self.counter
                #print(self.counter)
            except: 
                #print('HBDG')
                self.high_avg[i] = None 
        for t in self.high_avg:
            if t == None:
                self.temp=self.high_avg.index(t)
                self.high_avg[self.temp] = self.high_avg[self.temp-1] 
############################################################################
        for i in range(len(self.low_avg)):
            self.temp =0
            self.counter =0 
            for j in range(len(self.low_avg[i])):
                try:
                    self.temp += float(self.low_avg[i][j])
                    self.counter += 1
                except: None 
            try:    
                self.low_avg[i] = self.temp/self.counter
                #print(self.counter)
            except: 
                #print('HBDG')
                self.low_avg[i] = None 
        for t in self.low_avg:
            if t == None:
                self.temp=self.low_avg.index(t)
                self.low_avg[self.temp] = self.low_avg[self.temp-1] 
############################################################################
        for i in range(len(self.close_avg)):
            self.temp =0
            self.counter =0 
            for j in range(len(self.close_avg[i])):
                try:
                    self.temp += float(self.close_avg[i][j])
                    self.counter += 1
                except: None 
            try:    
                self.close_avg[i] = self.temp/self.counter
                #print(self.counter)
            except: 
                #print('HBDG')
                self.close_avg[i] = None 
        for t in self.close_avg:
            if t == None:
                self.temp=self.close_avg.index(t)
                self.close_avg[self.temp] = self.close_avg[self.temp-1] 
############################################################################
        for i in range(len(self.vol_avg)):
            self.temp =0
            self.counter =0 
            for j in range(len(self.vol_avg[i])):
                try:
                    self.temp += float(self.vol_avg[i][j])
                    self.counter += 1
                except: None 
            try:    
                self.vol_avg[i] = self.temp/self.counter
                #print(self.counter)
            except: 
                #print('HBDG')
                self.vol_avg[i] = None 
        for t in self.vol_avg:
            if t == None:
                self.temp=self.vol_avg.index(t)
                self.vol_avg[self.temp] = self.vol_avg[self.temp-1] 
############################################################################
    def norm(self):
        self.open_avg = np.array(self.open_avg)
        self.open_avg=self.open_avg.reshape(-1,1)
        scaler=MinMaxScaler(feature_range=(-.9,.9))
        scaler.fit(self.open_avg)
        self.open_avg=scaler.transform(self.open_avg)
#####################################
        self.high_avg = np.array(self.high_avg)
        self.high_avg=self.high_avg.reshape(-1,1)
        scaler=MinMaxScaler(feature_range=(-.9,.9))
        scaler.fit(self.high_avg)
        self.high_avg=scaler.transform(self.high_avg)
#####################################
        self.low_avg = np.array(self.low_avg)
        self.low_avg=self.low_avg.reshape(-1,1)
        scaler=MinMaxScaler(feature_range=(-.9,.9))
        scaler.fit(self.low_avg)
        self.low_avg=scaler.transform(self.low_avg)
#####################################
        self.close_avg = np.array(self.close_avg)
        self.close_avg=self.close_avg.reshape(-1,1)
        scaler=MinMaxScaler(feature_range=(-.9,.9))
        scaler.fit(self.close_avg)
        self.close_avg=scaler.transform(self.close_avg)
#####################################
        self.vol_avg = np.array(self.vol_avg)
        self.vol_avg=self.vol_avg.reshape(-1,1)
        scaler=MinMaxScaler(feature_range=(-.9,.9))
        scaler.fit(self.vol_avg)
        self.vol_avg=scaler.transform(self.vol_avg)

############################################################################
AP=load('/home/mohammadreza/Desktop/python stock/Asan Pardakht Pers-a.csv')
AP.avarage()
AP.norm()
print(AP.vol_avg)

import matplotlib.pyplot as plt

plt.plot(np.arange(len(AP.close_avg)) , AP.close_avg)
#plt.plot(np.arange(len(AP.open)) , AP.open)
