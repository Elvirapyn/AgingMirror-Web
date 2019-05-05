# coding:utf-8
'''
人脸位置校准
'''
import cv2
import dlib
import argparse
import sys

predictor_path = 'C:/Users/67506/Desktop/Facenet/final/shape_predictor_5_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)

def main(args):
    if args.in_dir:
        #out = facenet.get_image_paths(args.out_dir)
        frame=cv2.imread(args.in_dir)
        frame_new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 检测脸部
        dets = detector(frame_new, 1)
        #print("Number of faces detected: {}".format(len(dets)))
        num_faces = len(dets)
        if num_faces == 0:
            print("Sorry, there were no faces found in current frame")
            exit(0)
        # 查找脸部位置
        faces = dlib.full_object_detections()
        for detection in dets:
            faces.append(sp(frame_new, detection))
        image = dlib.get_face_chip(frame_new, faces[0])
        cv_bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        cv2.imwrite(args.out_dir, cv_bgr_img)
        return cv_bgr_img
    else:
        print("no such path!")

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('-in_dir', type=str , default='../in/inin/Man2.jpg')

    parser.add_argument('-out_dir', type=str, default='../final/testPic.jpg')

    return parser.parse_args(argv)

if __name__ == '__main__':
    # 这是一个从外部输入参数的代码。
    main(parse_arguments(sys.argv[1:]))


'''
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("cannot open camear")
    exit(0)
    
    
while True:
    ret, frame = camera.read()

    if not ret:
        continue
    cv2.imshow('camera', frame)
    frame_new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 检测脸部
    dets = detector(frame_new, 1)
    print("Number of faces detected: {}".format(len(dets)))
    num_faces = len(dets)
    if num_faces == 0:
        print("Sorry, there were no faces found in current frame")
        continue
    # 查找脸部位置
    faces = dlib.full_object_detections()
    for detection in dets:
        faces.append(sp(frame_new, detection))
    images = dlib.get_face_chips(frame_new, faces, size=320)
    for image in images:
        cv_bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow('image', cv_bgr_img)
    image = dlib.get_face_chip(frame_new, faces[0])
    cv_bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('image', cv_bgr_img)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
'''
