## Excel

##### VLOOKUP批量查找插入



![image-20210923104158803](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210923104158803.png)



- `Lookup_value`：需要填充的第一格
- `Table_array`：本表格中查找的键值
- `Col_index_num`：查找的范围
- `Range_lookup`：精确查找使用`FALSE`，模糊查找使用`TRUE`

###### 注意

1. 查找范围的第一列必须是查找的键值，否则查询不到。
2. 点击表格右下角批量向下复制公式。
3. 复制之前需要先进行筛选，去除有值的和查找值为空的行，否则自动填充会中断。

公式填充完毕后，复制所有公式格，选择性粘贴中选择 值粘贴 便可以给表格赋值脱离公式。



![image-20210923105144392](https://raw.githubusercontent.com/windsoul124/blogPic/main/img/image-20210923105144392.png)