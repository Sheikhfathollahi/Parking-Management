import cv2
import numpy as np

video_source = "Parking3.mp4"
cap = cv2.VideoCapture(video_source)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (900, 572))
    img_blur = cv2.GaussianBlur(frame[:, :, 0], (3, 5), 1)
    edge = cv2.Canny(img_blur, 1, 255)
    frame_2 = cv2.threshold(edge, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    j = 1
    for j in range(4):
        #cv2.rectangle(frame, (25 + (85 * j), 410), (40 + (90 * j), 470), (0, 255, 0), 2)
        contours, hier = cv2.findContours(frame_2[410:470 , 25 + (85 * j):40 + (90 * j)], cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
        contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
        print(len(contours))
        if len(contours) > 0:
            cv2.circle(frame, (45 + (90 * j), 339), 6, (0, 0, 255), 7)
        else:
            cv2.circle(frame, (45 + (90 * j), 339), 6, (0, 255, 0), 7)
        j += 1

    t = 1
    for t in range(5):
        #cv2.rectangle(frame, (470 + (85 * t), 410), (510 + (85 * t), 470), (0, 255, 0), 2)
        contours1, hier = cv2.findContours(frame_2[410:470, 470 + (85 * t):510 + (90 * t)], cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
        contours1 = sorted(contours1, key=lambda ctr: cv2.boundingRect(ctr)[0])
        print(len(contours1))
        if len(contours1) > 0:
            cv2.circle(frame, (470 + (90 * t), 339), 6, (0, 0, 255), 7)
        else:
            cv2.circle(frame, (470 + (90 * t), 339), 6, (0, 255, 0), 7)
        t += 1

    i = 1
    for i in range(10):
        #cv2.rectangle(frame, (35 + (90 * i), 55), (70 + (88 * i), 110), (0, 255, 0), 2)
        contours, hier = cv2.findContours(frame_2[55:110, 35 + (90 * i):70 + (88 * i)], cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
        contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
        print(len(contours))
        if len(contours) > 0:
            cv2.circle(frame, (60 + (88 * i), 190), 6, (0, 0, 255), 7)
        else:
            cv2.circle(frame, (60 + (88 * i), 190), 6, (0, 255, 0), 7)
        i += 1

        #########Down line##################################################
        cv2.rectangle(frame, (1, 360), (80, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (86, 360), (175, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (180, 360), (260, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (265, 360), (339, 520), (0, 255, 0), 2)
        #cv2.rectangle(frame, (343, 360), (438, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (444, 360), (520, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (524, 360), (610, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (615, 360), (700, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (704, 360), (790, 520), (0, 255, 0), 2)
        cv2.rectangle(frame, (794, 360), (887, 520), (0, 255, 0), 2)

        #########Up line##################################################
        cv2.rectangle(frame, (22, 7), (107, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (111, 7), (192, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (196, 7), (281, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (285, 7), (372, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (376, 7), (456, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (460, 7), (545, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (549, 7), (638, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (642, 7), (723, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (727, 7), (813, 170), (0, 255, 0), 2)
        cv2.rectangle(frame, (817, 7), (895, 170), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()