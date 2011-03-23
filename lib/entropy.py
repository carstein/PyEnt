#!/usr/bin/env python
#-*- coding:utf-8 -*-

import freq
import Image,ImageDraw

class EntCalc:
    data=""
    samples=[]
    entropy=[]
    sample_size=0
    
    def __init__(self):
        self.frq = freq.Frequency()
    
    def calculate_sample_size(self):
        if self.sample_size!=0:
            print("Sample size set to %d"%self.sample_size)
        else:
            print("Adjusting sample size")
            self.sample_size=128
            l=len(self.data)
            
            while self.sample_size < 2048:
                if l/self.sample_size > 500:
                    self.sample_size*=2
                else:
                    break
                              
            print("Feed has %d bytes so choosen sample size is %d"%(len(self.data),self.sample_size))
    
    def calculate_entropy(self,data):
        if len(data) < 320:
            print("No point in calculating entropy for such small feed")
            return 0
        else:
            self.data = data
            
        self.calculate_sample_size()
     

        while self.data != '':
            # Split data into samples
            sample, self.data = self.data[:self.sample_size],self.data[self.sample_size:]
            
            # Make histogram for sample
            self.frq.feed(sample)
            histogram = self.frq.calculate_frequency()
            
            # calculate entropy
            e=0
            
            for c in histogram.values():
                e+=(c*c)/float(self.sample_size)
            
            e=1-(e/float(self.sample_size))
            self.entropy.append(e**2)
            
            self.frq.clear()
            
        # Overall entropy
        

    
    def make_image(self):
        imgw=len(self.entropy)
        
        img = Image.new("RGB", (imgw,300), "#000000")
        draw = ImageDraw.Draw(img)
    
        for i in xrange(imgw):
            draw.line([(i,300),(i,300-(self.entropy[i]*300))],fill="white")
    
        img.save("out.png", "PNG")
