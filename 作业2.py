accounts=[];
n=int(raw_input('�����˻�������'));
i=0;
for i in range(n):
    print '�����',i+1,'���˻���������Ԫ�ظ�����'
    m=int(raw_input());
    print '����������˻��������͵�ַ��'
    for j in range(m):
        account=[];
        account.append(raw_input());
    accounts.extend(account);
for a in range(n):
    for b in range(n):
        if b>a:
            for c in range(1,len(accounts[a])):
                for d in range(1,len(accounts[b])):
                    if accounts[a][c]==accounts[b][d]:
                        accounts[a].append(ccounts[b][d]);
    print accounts[a];
 
            
        
