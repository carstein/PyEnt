#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Frequency:
    entropy=0
    data=""
    frequency_list={}
    
    def clear(self):
        self.data=""
        self.frequency_list={}
    
    def feed(self,data):
        self.data+=data
        return 0
    
    def calculate_frequency(self):
        for c in self.data:
            if self.frequency_list.has_key(ord(c)):
                self.frequency_list[ord(c)]+= 1
            else:
                self.frequency_list[ord(c)] = 1  
        
        return self.frequency_list
