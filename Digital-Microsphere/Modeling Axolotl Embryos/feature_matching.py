def Sift(image3,image4)
  img1 = image3 # resize(image36)         # queryImage
  img2 = image4 #resize(image37) # trainImage
  # Initiate SIFT detector
  sift = cv.SIFT_create()
  # find the keypoints and descriptors with SIFT
  kp1, des1 = sift.detectAndCompute(img1,None)
  kp2, des2 = sift.detectAndCompute(img2,None)
  # BFMatcher with default params
  bf = cv.BFMatcher()
  matches = bf.knnMatch(des1,des2,k=2)
  # Apply ratio test
  good = []
  for m,n in matches:
      if m.distance < 0.75*n.distance:
          good.append([m])
  # cv.drawMatchesKnn expects list of lists as matches.
  img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
  cv2_imshow(img3)

def Orb(image4,image5)
  query_img = image4
  train_img = image5

  # Convert it to grayscale
  query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
  train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

  # Initialize the ORB detector algorithm
  orb = cv2.ORB_create()

  # Now detect the keypoints and compute
  # the descriptors for the query image
  # and train image
  queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None)
  trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None)
   ￼

  # Initialize the Matcher for matching
  # the keypoints and then match the
  # keypoints
  matcher = cv2.BFMatcher()
  matches = matcher.match(queryDescriptors,trainDescriptors)

  # draw the matches to the final image
  # containing both the images the drawMatches()
  # function takes both images and keypoints
  # and outputs the matched query image with
  # its train image
  final_img = cv2.drawMatches(query_img, queryKeypoints,
  train_img, trainKeypoints, matches[:20],None)

  final_img = cv2.resize(final_img, (1000,650))
  
  # Show the final image
  cv2_imshow(final_img)

def stereo_map(image36,image37)
  imgL = grayscale(image36)
  imgR = grayscale(image37)
  stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
  disparity = stereo.compute(imgL,imgR)
  plt.imshow(disparity,'gray')
  plt.show()