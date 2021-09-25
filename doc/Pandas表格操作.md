## Pandas表格操作

1. 读取一列保存为list：

   ```python
   import pandas as pd
   
   data = pd.read_excel('appInfo_test.xlsx')
   result = data.values.tolist()
   for s in result:
     	# s[0]对应第一列
   	url.append('[[["xdSrCf","[[null,[\\"{0}{1}"'.format(s[0], '\\",7],[]]]",null,"1"]]]'))  # 需多加转义字符
   ```

   

