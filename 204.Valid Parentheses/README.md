使用stack来做来存储左边的括号，当有右边括号来临时，判断stack.pop()和dic[i]是否相等(dic存储相应右括号所对应的左括号), 注意stack为空等一系列的边界。 
