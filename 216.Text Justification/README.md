用cur来存储当前行的单词, 用num_of_letters来记录当前行的cur内所有字符数量, 当len(cur) + num_of_letters + len(w)(遍历到的单词) > maxLenth时, 说明cur内的单词足够构成一行了, 之后就是按顺序在cur的单词间填入空格, 直到达到长度要求.
