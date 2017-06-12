在前题目的基础上加上, 判别当前组合不在数组内即可, 即:res += [i + [n] for i in res if i + [n] not in res]
