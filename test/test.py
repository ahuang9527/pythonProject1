#coding='utf-8'
import jieba

def getText(fileName):
    f=open(fileName, 'r', encoding = 'utf-8')
    txt=f.read()
    f.close()
    return txt
def main():
    txt=getText(r'./中国人工智能兴起的原因及其经济意义.txt')
    words=jieba.__lcut(txt)
    counts={}
    for x in words:
        if len(x)==1:
            continue
        else:
            counts[x]=counts.get(x,0)+1
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(10):
        key,value=items[i]
        print("{0:<10}{1:5}".format(key,value))
        #main() 这里入口位置不对，你无限循环了，我给你写在下面了。

if __name__ == '__main__':
    main()
    #以后要运行什么直接改这里的东西