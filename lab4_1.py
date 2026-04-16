import numpy as np
import cv2
from matplotlib import pyplot as plt

#task 1
#img = cv2.imread('flori.png',0)
#cv2.imshow('img',img)
#k=cv2.waitKey(0)
#if k == 27: #w8 for ESC to exit
#    cv2.destroyAllWindows()
#elif k == ord('s'): #w8 for s to save and exit
#    cv2.imwrite('florigray.png',img)


#task2
#img = cv2.imread('flori.png',0)#daca ii pun 1 in loc de 0 ii schimba culorile din original for some reason
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([]) #sa ascundem valorile lui X si Y ticks
#plt.show()


#se poate face si videocapture, voi face ulterior cu o alta camera daca am


#task3 - harris detection
#poza = ('flori.png')
#imagine = cv2.imread(poza)
## Micșorăm imaginea la 10% (0.1) din lățimea și înălțimea ei originală
#imagine_afisare = cv2.resize(imagine, (0, 0), fx=0.1, fy=0.1)
#
#gray=cv2.cvtColor(imagine,cv2.COLOR_BGR2GRAY)
#gray=np.float32(gray)
#dst=cv2.cornerHarris(gray,2,3,0.05)
#
#dst=cv2.dilate(dst, None)
#
#imagine[dst>0.01*dst.max()]=[0,0,255]
#
#cv2.imshow('dst', imagine_afisare)
#
#if cv2.waitKey(0) & 0xff == 27:#w8 for 0 sau esc
#    cv2.destroyAllWindows()
#
#cu placa de chess merge dar cu poza mea nu merge, nu stiu de ce, poate e poza prea colorata


#task4 - fast detection - cu cerculete
#img = cv2.imread('flori.png')
#    # Micșorăm imaginea la 10% (0.1) din lățimea și înălțimea ei originală
#img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
## conversie imagine grayscale
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
## Initiaza FAST object with default values
#fast = cv2.FastFeatureDetector_create()
## Gaseste keypoints pe imagagine (grayscale)
#kp = fast.detect(gray,None)
## Deseneaza keypoints in imagagine
#img2 = cv2.drawKeypoints(img, kp, None)
## Print toti parametrii
#print("Threshold: ", fast.getThreshold())
#print("nonmaxSuppression: ", fast.getNonmaxSuppression())
#print("neighborhood: ", fast.getType())
#print("Total Keypoints with nonmaxSuppression: ", len(kp))
## Imagagine cu keypoints desenate pe aceasta
#cv2.imshow("Keypoints with nonmaxSuppression", img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



#task5 - shi tomassi corner detector
#img = cv2.imread('flori.png')
#img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
#corners = np.intp(corners) #ultima versiune de numpy nu mai accepta int0
#for i in corners:
#    x,y = i.ravel()
#    cv2.circle(img,(x,y),3,255,-1)
#img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#plt.imshow(img_rgb),plt.show()


#task6 - Creati un video plecand de la 10 imagini. Identificati obiecte in film
# 1. SETĂRI PENTRU VIDEO
latime, inaltime = 840, 680 # Redimensionam toate pozele la marimea asta
fps = 2.0 # 2 cadre pe secunda, ca sa ai timp sa vezi imaginile
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Formatul video (codec-ul)
video = cv2.VideoWriter('video_laborator.avi', fourcc, fps, (latime, inaltime))

# 2. CREAREA VIDEOCLIPULUI DIN IMAGINI
for i in range(10):
    nume_fisier = f'{i+1}.png' #iau cele 10 poze denumite 1.png, 2.png ,...,10.png
    frame = cv2.imread(nume_fisier)
    if frame is not None:
        # Redimensionam obligatoriu, altfel VideoWriter da eroare
        frame = cv2.resize(frame, (latime, inaltime))
        video.write(frame) # Adaugam imaginea in video

video.release() # Salvam fisierul video 
print("Videoclipul 'video_laborator.avi' a fost creat cu succes!")


# 3. IDENTIFICAREA OBIECTELOR IN FILM
print("Incepem redarea si identificarea trasaturilor...")

# Deschidem videoclipul pe care tocmai l-am creat
cap = cv2.VideoCapture('video_laborator.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    # Daca ret este False, inseamna ca s-a terminat videoclipul
    if not ret: 
        break

    # Convertim in grayscale pentru algoritmul de detectie
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Folosim Shi-Tomasi 
    corners = cv2.goodFeaturesToTrack(gray, 250, 0.01, 10)#vreau 250 de identificari, sau ce numar pun eu acolo
    if corners is not None:
        corners = np.intp(corners)
        for i in corners:
            x, y = i.ravel()
            # Desenam cercuri pe obiectele/trasaturile identificate
            cv2.circle(frame, (x, y), 5, (255, 204, 242), 2) 	

    # Afisam frame-ul
    cv2.imshow('Identificare in Video', frame)

    # Folosim waitKey(1000) ca sa tina fiecare frame o secunda pe ecran
    # Apasa ESC ca sa opresti redarea mai devreme
    if cv2.waitKey(1000) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()