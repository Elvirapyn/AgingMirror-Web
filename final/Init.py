# 图片预处理
# 输入参数：输入图片文件夹路径（具体文件夹结构见原文档）、输出图片文件夹路径
# 函数无直接输出


import facenet
import align.align_dataset_mtcnn
import sys
import os
import argparse
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def main(args):
    if os.path.exists(args.in_dir):
        if __name__ == '__main__':
            align.align_dataset_mtcnn.main(align.align_dataset_mtcnn.parse_arguments([args.in_dir,args.out_dir,'--image_size','160','--margin','20','--random_order']))
        '''     
        out = facenet.get_image_paths(args.in_dir)
        for imgs in out:
            imgs_path = facenet.get_image_paths(imgs)
            path=args.out_dir+imgs[len(args.in_dir):]
            if not os.path.exists(path):  # 如果路径不存在
                os.makedirs(path)
            for img in imgs_path:
                name=args.out_dir+img[len(args.in_dir):]
                print(name)
                final.Align.main(final.Align.parse_arguments(["-in_dir", img,"-out_dir",name]))
        '''

    else:
        print("no such path!")

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('-in_dir', type=str , default='../in')

    parser.add_argument('-out_dir', type=str , default='../out')

    return parser.parse_args(argv)


if __name__ == '__main__':
    # 这是一个从外部输入参数的代码。
    main(parse_arguments(sys.argv[1:]))