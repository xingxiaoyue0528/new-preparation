letters=[];
n=int(raw_input('������Ԫ�ظ���:'));
print '���������飺'
for i in range(n):
    letters.append(raw_input());
    i=i+1;
letters.sort();
target=raw_input('������Ŀ����ĸ��');
for i in range(n):
    if letters[i]>target:
        print letters[i];
        break;
    

    
