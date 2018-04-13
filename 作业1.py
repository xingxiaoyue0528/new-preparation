letters=[];
n=int(raw_input('请输入元素个数:'));
print '请输入数组：'
for i in range(n):
    letters.append(raw_input());
    i=i+1;
letters.sort();
target=raw_input('请输入目标字母：');
for i in range(n):
    if letters[i]>target:
        print letters[i];
        break;
    

    
