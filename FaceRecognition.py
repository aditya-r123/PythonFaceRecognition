import cv2
body_cascade = cv2.CascadeClassifier(r"C:\Users\adity\Downloads\haarcascades\haarcascades\haarcascade_upperbody.xml")

cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    body = body_cascade.detectMultiScale(gray, 1.1, 5)

    for (bx, by, bw, bh) in body:
        cv2.rectangle(img, (bx,by), (bx+bw+bw,by+bh), (183, 0, 255),2)
        roi_gray = gray[by:by+bh, bx:bx+bw]
        roi_color = img[by:by+bh, bx:bx+bw]
                
    cv2.imshow( 'Upper Body Recognition', img)
    k = cv2.waitKey(30)
    if k == 27:
        cv2.destroyAllWindows()
        break
