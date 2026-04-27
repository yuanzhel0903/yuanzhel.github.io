import mmcv
import sys

ori_img = mmcv.imread(sys.argv[1])
new_img = mmcv.imresize(ori_img, (480, 240))
mmcv.imwrite(new_img, sys.argv[2])
