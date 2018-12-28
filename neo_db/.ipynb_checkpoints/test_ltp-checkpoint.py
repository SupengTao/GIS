# -*- coding: utf-8 -*-
import os
LTP_DATA_DIR = './ltp_data_v3.4.0'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')

from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load(cws_model_path)
words = segmentor.segment('元芳你怎么看')
print (words)
segmentor.release()
