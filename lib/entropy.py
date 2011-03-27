#!/usr/bin/env python
#-*- coding:utf-8 -*-

import freq
import Image,ImageDraw

class EntCalc:
    data=""
    entropy=[]
    sample_size=0
    avg_entropy=0
    
    def __init__(self):
        self.frq = freq.Frequency()
    
    def calculate_sample_size(self):
        if self.sample_size!=0:
            print("Sample size set to %d"%self.sample_size)
        else:
            print("Adjusting sample size")
            self.sample_size=256
            length=len(self.data)
            
            while self.sample_size < 2048:
                if length/self.sample_size > 500:
                    self.sample_size*=2
                else:
                    break
                              
            print("Feed has %d bytes - choosen sample size is %d"%(len(self.data),self.sample_size))
    
    def calculate_entropy(self,data):
        if len(data) < 256:
            print("No point in calculating entropy for such small feed")
            return 0
        else:
            self.data = data
            
        self.calculate_sample_size()

        # Overall file entropy
        self.frq.feed(self.data)
        histogram = self.frq.calculate_frequency()
            
        e=0
            
        for c in histogram.values():
            e+=(c*c)/float(len(data))
            
        e=1-(e/float(len(data)))
        self.avg_entropy=e**2
        print("Entropy of the file is %f"%(self.avg_entropy))
        self.frq.clear()

        while self.data != '':
            # Split data into samples
            sample, self.data = self.data[:self.sample_size],self.data[self.sample_size:]

            # Make histogram for sample
            self.frq.feed(sample)
            histogram = self.frq.calculate_frequency()

            # calculate entropy for sample
            e=0

            for c in histogram.values():
                e+=(c*c)/float(self.sample_size)

            e=1-(e/float(self.sample_size))
            self.entropy.append(e**2)

            self.frq.clear()
    
    def make_image(self,filename):
        # Calculate width of the image
        imgw=len(self.entropy)
        
        # Prepare drawing space
        img = Image.new("RGB", ((imgw*2)+40,340), "#FFFFFF")
        draw = ImageDraw.Draw(img)

        for i in xrange(imgw):
            bar_heigth=self.entropy[i]*300
            p_bar=320 #Recalculate
            g_bar=320-(320*0.6)
            y_bar=320-(320*0.8)
            r_bar=320-(320*0.9)
            
            for colour,bar in [("#7f007f",p_bar),("#007f00",g_bar),("#c3bf00",y_bar),("#c40000",r_bar)]: 
                
                h = 0.25*300
                x1 = (i*2)+20
                y1 = bar
                x2 = x1+1
                y2 = 320-bar_heigth
                
                if y1>y2:
                    draw.rectangle(((x1,y1),(x2,y2)),fill=colour)


        # Add short description
        text="Filename: %s - Entropy: %.2f%%"%(filename,self.avg_entropy*100)
        draw.text((20,325),text,fill="black")

        img.save("out.png", "PNG")
