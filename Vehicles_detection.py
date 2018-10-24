import cv2
 
# capture 
cap = cv2.VideoCapture('video.avi')

car_cascade = cv2.CascadeClassifier('cars.xml')
 
# loop 
while True:
    # reads 
    ret, frames = cap.read()
     
    # conversion
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
 
    # Detects cars 
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
     
    # To draw a rectangle 
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        #count(s)
        #print(s)
        
   # Display frames 
    cv2.imshow('video2', frames)
     
    
    if cv2.waitKey(33) == 27:
        break
 
 
cv2.destroyAllWindows()
