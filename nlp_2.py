import jieba

str = "我在慕课网上课"

print(" ".join(jieba.cut(str)))
