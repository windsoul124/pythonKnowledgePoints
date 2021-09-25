from langdetect import detect
from langdetect import detect_langs

# 太短或者太模糊的文本不好识别
# 加上以下两行让结果唯一
from langdetect import DetectorFactory
DetectorFactory.seed = 0


str1 = 'Language detection algorithm is non-deterministic'
str2 = 'Ẩm thực, làm đẹp, deal sốc, hoàn tiền'

# 判断语言种类
print(detect(str1))
print(detect(str2))
# 概率
print(detect_langs(str2))