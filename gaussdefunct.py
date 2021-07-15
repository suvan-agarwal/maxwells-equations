#DEFUNCT. decided to pivot to making program with dragged rectangle and live electric flux feedback.
#This program draws x random points and draws lines between all of them to make a shape. 


import picture
import random
import time
import math

def main():
    #chargenum = int(input("Enter number of charges"))
    surfacenum = int(input("Enter number of vertices for desired gaussian surface (3 or more): "))
    #charges = randompoints(chargenum)
    window = picture.Picture(1000,1000)
    window.setFillColor(0,0,0)
    surfacepoints = arrangeclosest(randompoints(surfacenum))
    for point in surfacepoints:
        window.drawCircleFill(point[0],point[1],4)
    window.setOutlineColor(255,0,0)
    for index, point in enumerate(surfacepoints[:-1]):
        window.drawLine(point[0], point[1], surfacepoints[index+1][0], surfacepoints[index+1][1])
    window.drawLine(surfacepoints[len(surfacepoints)-1][0], surfacepoints[len(surfacepoints)-1][1], surfacepoints[0][0], surfacepoints[0][1])
    window.display()
    input("Press enter to exit")

def randompoints(numpoints):
    points = []
    for i in range(numpoints):
        x = random.randint(0,1000)
        y = random.randint(0,1000)
        points.append((x,y))
    return points

def arrangeclosest(points):
    for i in range(len(points[:-1])):
        min = i+1
        #default index of closest point
        mindistance = math.sqrt((points[min][0]-points[i][0])**2 + (points[min][1]-points[i][1])**2)
        #distance between min and i
        for j in range(i+1,i+len(points[i:])): #iterate from i+1 to end of points list
            newdistance = math.sqrt((points[j][0]-points[i][0])**2 + (points[j][1]-points[i][1])**2)
            if newdistance < mindistance:
                min = j
                mindistance = newdistance
        points.insert(i+1, points.pop(min))
    return points

main()
