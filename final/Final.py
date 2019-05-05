
import compare_
import sys
import os
import argparse
import facenet
import align.align_dataset_mtcnn
import shutil
import math

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def sigmoid(num):
    return 1/(1+math.e**-num)

def start(image_file,model):
    print(os.getcwd());
    out_str='out'#待比较的文件夹
    imagein_str='E:/AgingMirror5/final/testin/image/testPic.jpg'#待比较的文件复制过来的地址
    pathin_str='final/testin'
    pathout_str='final/testout'
    imageout_str='final/testout/image/testPic.png'#待比较的文件复制过来的地址
    if os.path.exists(image_file):
        shutil.copy(image_file, imagein_str)
        align.align_dataset_mtcnn.main(align.align_dataset_mtcnn.parse_arguments([pathin_str,pathout_str,'--image_size','160','--margin','20','--random_order']))
        Args = [model, imageout_str]
        out = facenet.get_image_paths(out_str)

        for imgs in out:
            imgs_path=facenet.get_image_paths(imgs)
            for img in imgs_path:
           #     print(img)
                Args.append(img)
        pic, dist=compare_.main(compare_.parse_arguments(Args))
        similarity=sigmoid(20*(0.95-dist))
        name=os.path.basename(os.path.dirname(pic))

        if similarity>0.8:
            print("该图片与图片"+pic+"最接近，属于类"+name+"，其相似度为",end='')
            print(similarity)
        else:
            print("无相似图片，请新建类")
        os.remove(imageout_str)
        return pic, similarity,name
    else:
        print('no such path')


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('image_file', type=str, help='Image to compare')

    parser.add_argument('--model', type=str,
                        help='Could be either a directory containing the meta_file and ckpt_file or a model protobuf (.pb) file',
                        default='../20180408-102900')

    return parser.parse_args(argv)


if __name__ == '__main__':
#     # 这是一个从外部输入参数的代码。
     main(parse_arguments(sys.argv[1:]))
