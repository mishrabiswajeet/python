if __name__ == '__main__':
    n=int(input())
    my_dict = {}
    for i in range(n):
        temp=list(map(str,input().split()))
        my_dict[temp[0]]=temp[1:]

    name=input()

    my_list=my_dict[name]
    dup_list=[float(x) for x in my_list]
    avg=sum(dup_list)/len(dup_list)
    print("%.2f" % (avg))
