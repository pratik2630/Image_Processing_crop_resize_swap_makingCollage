import cv2 , numpy
#original cat image
photo1 = cv2.imread("cat.jpg")
photo1 = cv2.resize(photo1 , ( 400 ,400 ))

#original tigers image
photo2 = cv2.imread("tiger.jpg")
photo2 = cv2.resize(photo2 , ( 400 ,400 ))

#original cat image
photo1 = cv2.imread("cat.jpg")
#resized it for ease of use
photo1 = cv2.resize(photo1 , ( 400 ,400 ))
cv2.imshow("Img1",photo1)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 



#original tigers image
photo2 = cv2.imread("tiger.jpg")
photo2 = cv2.resize(photo2 , ( 400 ,400 ))
cv2.imshow("Img1",photo2)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 

#verticaly added image
vimg1 = numpy.vstack((photo1 , photo2))
cv2.imshow("Img1",vimg1)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 

#horizontaly added image

himg1 = numpy.hstack((photo1 , photo2))
cv2.imshow("Img1",himg1)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 



#croped cat's face
cimg1 = photo1[45:270, 35:265 , : ]
cimg1 = cv2.resize(cimg1 , (255 , 270  ))


#croped tigers's face
cimg2 = photo2[40:310, 90:345 , : ]
print(cimg2.shape)
cimg2 = cv2.resize(cimg2 , (230, 225  ))

#put tigers face on cat's face
finalimg1 = photo1
finalimg1[45:270, 35:265 , : ]= cimg2[:,:,:]
cv2.imshow("Img1",finalimg1)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 


#put tigers face on cat's face
finalimg2 = photo2
finalimg2[40:310, 90:345 , : ]= cimg1[:,:,:]
cv2.imshow("Img1",finalimg2)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 

himg2 = numpy.hstack(( finalimg1 , finalimg2 ))
cv2.imshow("Img1",himg2)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 

vimg = numpy.vstack((himg1,himg2))
cv2.imshow("Img1",vimg)
if cv2.waitKey() == 13:
    pass
cv2.destroyAllWindows() 