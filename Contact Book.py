b=[]
c=[]
l='y'
while l=='y' or l=='Y':
    a=int(input('What would you like to do,enter the option number:\n1.Add Contact\n2.Delete Contact\n3.Edit Contact\n4.Show all Contacts\n5.Search a Contact\n6.Close Contacts\n'))
    if a==1:
        temp1=input('Enter the name of the person:')
        c.append(temp1)
        temp2=input('Enter the phone number of the person:')
        c.append(temp2)
        temp2=input('Enter the address of the person:')
        c.append(temp2)
        temp2=input('Enter the e-mail of the person:')
        c.append(temp2)
        b.append(c)
        c=[]
        print('Contact saved!')
    elif a==2:
        m='Y'
        while m=='y'or m=='Y':
            flag1=0
            d=input('Enter the name of the contact to be deleted:')
            for i in range(0,len(b)):
                if d==b[i][0]:
                    flag1=1
                    b.pop(i)
                if flag1==1:
                    break               
            
            if flag1==1:
                print('Contact deleted!')
            else:
                print('There is no such contact!')
            m=input('would you like to delete another contact?(Y/N)')
            
    elif a==3:
        n='y'
        while n=='y' or n=='Y':
            e=input('Enter the name of the contact to be edited:')
            flag2=0
            for i in range(0,len(b)):
                if e==b[i][0]:
                    flag2=1
                    g='y'
                    while g=='Y' or g=='y':
                        f=int(input('What do you want to edit:\n1.Name\n2.Number\n3.Address\n4.E-mail\nEnter an option number:'))
                        if f==1:
                            b[i][0]=input('Enter the name to be replaced:')
                            print('Name edited!')
                        elif f==2:
                            b[i][1]=input('Enter the number to be replaced:')
                            print('Number edited!')
                        elif f==3:
                            b[i][2]=input('Enter the address to be replaced:')
                            print('Address edited!')
                        elif f==4:
                            b[i][3]=input('Enter the e-mail to be edited:')
                            print('E=mail edited!')
                        else:
                            print('There is no such contact!')
                        g=input('Do you want to edit any other options?(Y/N)')
                if flag2==1:
                    break
            if flag2==1:
                print('Contact edited successfully!')
            else:
                print('Enter a valid contact name!')
            n=input('Would you like to edit any other contacts?(Y/N)')
            
    elif a==4:
        print('Contacts\n--------------')
        for i in range(0,len(b)):
            o=b[i]
            print(' '.join(o))
    elif a==5:
        k='y'
        while k=='Y' or k=='y':
            h=input('Enter the name of contact to search or the first letter to filter all contacts with that letter: ')
            flag3=0
            for i in range(0,len(b)):
                if h==b[i][0]:
                    print(' '.join(b[i]))
                    flag3=1
                if flag3==1:
                    break
            if flag3==0:
                flag4=0
                for j in range(0,len(b)):
                    if h==b[j][0][0]:
                        print(' '.join(b[j]))
                        flag4=1
                if flag4==1:
                    print(f'Are the contacts starting with {h}')
            if flag3==0 and flag4==0:
                print('No such contacts!')
            k=input('Do you want to search another contact?(Y/N)')
    elif a==6:
        print('Contacts closed!')
    else:
        print('Enter a valid option number!')
    l=input('Would you like to continue?(Y/N)')