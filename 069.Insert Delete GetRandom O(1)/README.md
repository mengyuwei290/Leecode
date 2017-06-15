核心思想用hash的key存储元素的key, value存储放在数组里的index, 数组即直接放入value即可.

删除是重点, 用hash 得到最后一个元素和要删除元素的index, 然后在数组里交换后pop, 字典里直接pop(val).
