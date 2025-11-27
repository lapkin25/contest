import sys

from config import root_jury, root_contestant

problemset = ['1 - factorial', '2 - vltokyo', '3 - detox', '4 - classify', '5 - 3dprint', '6 - mincover', '7 - underground', '8 - sakura']

for p in problemset:
    sys.path.append(root_jury + '/' + p)
    #sys.path.append(root_contestant + '/' + p)
sys.path.append(root_contestant)

#print("sys.path =", sys.path)

import check_factorial
import check_vltokyo
import check_detox
import check_classify
import check_3dprint
import check_mincover
import check_underground
import check_sakura
