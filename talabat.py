m={1:['Khyati','khyati@gmail.com','computer'],2:['Sarah','sarah@gmail.com','computer'],3:['Chloe','chloe@gmail.com','computer']}
print('-'*100)
print('%50s'%'Welcome to Talabat')
print('-'*100)
print('%50s'%'Guest   or   Admin')
mode=input('Enter choice: ')
r=False
if mode=='Guest' or mode=='guest':
    print('1-Login')
    print('2-Sign up')
    info=int(input('Enter choice: '))
    if info==1:
        while r==False:
            print('-'*100)
            print('%50s'%'LOGIN')
            print('-'*100)
            name=input('Enter username: ')
            pw=input('Enter password: ')
            lmem=list(m.values())
            for i in range(len(lmem)):
                if name==lmem[i][0] and pw==lmem[i][2]:
                    r=True
                    print('LOGIN SUCCESSFUL')
            if r==False:
                print('USER NOT FOUND')
    elif info==2:
        print('%50s'%'SIGN UP')
        fname=input('Enter first name: ')
        lname=input('Enter last name: ')
        email=input('Enter email ID: ')
        pw=input('Enter password: ')
        name=fname+' '+lname
        key=list(mem.keys())
        mem[max(key)+1]=[name,email,pw]
        r=True
    if r==True:
        x=False
        while x==False:
         print('-'*100)
         print('%50s'%'WELCOME TO TALABAT')
         print('-'*100)
         print('1-To search according to restaurant')
         print('2-To search according to preferred cuisine')
         print('-'*100)
         n=int(input('Enter search method: '))
         x=True
         while x==True:
            if n==1:
                print('1-KFC')
                print('2-Pizza Hut')
                print('3-Subway')
                print('4-Burger King')
                print("5-Hardee's")
                print('6-India Palace')
                print("7-Papa John's")
                print('8-Go back to previous menu')
                print('-'*100)
            elif n==2:
                print('1-Burgers')
                print('2-Pizza')
                print('3-Indian')
                print('8-Go back to previous menu')
                print('-'*100)
                cch=int(input('Enter cuisine of choice: '))
                if cch==1:
                    print('1-KFC')
                    print('3-Subway')
                    print('4-Burger King')
                    print("5-Hardee's")
                    print('8-Go back to previous menu')
                    print('-'*100)
                elif cch==2:
                    print('2-Pizza Hut')
                    print("7-Papa John's")
                    print('8-Go back to previous menu')
                    print('-'*100)
                elif cch==3:
                    print('6-India Palace')
                    print('8-Go back to previous menu')
                    print('-'*100)
                elif cch==8:
                    x=False
            while x==True:
             y=False
             ch=int(input('Enter choice of restaurant: '))
             total=0
             noi=0
             loi=[]
             while y==False:
                if ch==1:
                    print('-'*100)
                    print('KFC')
                    print('Delivery within 40 mins')
                    print('Delivery fee - AED 7.50')
                    print('-'*100)
                    print('Menu:')
                    print('1-Twister Sandwich')
                    print('2-Dinner crispy strips meal')
                    print('3-Bucket for Two')
                    print('4-Mighty Zinger Box-Medium')
                    print('5-Shrimp Box')
                    print('6-Chicken rice meal')
                    print('7-Mighty Zinger')
                    print('8-Fillet Supreme')
                    print('9-8 pcs super bucket')
                    print('10-18 pcs bucket')
                    print('11-Go back to previous menu')
                    print('-'*50)
                    d=7.50
                    kfcc=int(input('Enter Choice: '))
                    if kfcc==1:
                        print('Twister Sandwich')
                        print('AED 9.00')
                        t=9
                        de=['Twister Sandwich']
                        sp=input('Spicy or Original? ')
                        s=sp.capitalize()
                        de+=s,
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('-'*50)
                            print('Shopping cart: ',loi)
                            print('-'*50)
                    elif kfcc==2:
                        print('Dinner crispy strips meal')
                        print('4pcs strips + Fries + Coleslaw + 2 sauces + Bun + Drink')
                        print('AED 28.00')
                        t=28
                        de=['Dinner crispy strips meal']
                        sp=input('Spicy or Original? ')
                        s=sp.capitalize()
                        de+=s,
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('Choice of first Side item')
                        print('1-Coleslaw salad')
                        print('2-Medium Fries')
                        print('3-Medium Spicy Fries   +AED 2.00')
                        ch1=int(input('Enter choice of first side item: '))
                        if ch1==1:
                            de+='Coleslaw Salad',
                        elif ch1==2:
                            de+='Medium Fries',
                        elif ch1==3:
                            de+='Medium Spicy fries',
                            t+=2
                        print('Choice of Second Side item')
                        print('1-Coleslaw salad')
                        print('2-Regular Fries         +AED 2.00')
                        print('3-Regular Spicy Fries   +AED 3.00')
                        ch2=int(input('Enter choice of second side item: '))
                        if ch2==1:
                            de+='Coleslaw Salad',
                        elif ch2==2:
                            de+='Regular Fries',
                            t+=2
                        elif ch2==3:
                            de+='Regular Spicy fries',
                            t+=3
                        print('Choice of Beverage')
                        print('1-Pepsi')
                        print('2-Miranda')
                        print('3-7UP')
                        print('4-Diet Pepsi')
                        print('5-Mountain Dew ')
                        bev=int(input('Enter choice of Beverage: '))
                        if bev==1:
                            de+='Pepsi',
                        elif bev==2:
                            de+='Miranda',
                        elif bev==3:
                            de+='7UP',
                        elif bev==4:
                            de+='Diet Pepsi',
                        elif bev==5:
                            de+='Mountain Dew',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==3:
                        print('Bucket for Two')
                        print('6 pcs Chicken + Fries + 2 small coleslaw + Drinks')
                        print('AED 45.00')
                        t=45
                        de=['Bucket for two']
                        sp=input('Spicy or Original? ')
                        s=sp.capitalize()
                        de+=s,
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('Choice of Beverage')
                        print('1-Pepsi')
                        print('2-Miranda')
                        print('3-7UP')
                        print('4-Diet Pepsi')
                        print('5-Mountain Dew ')
                        bev=int(input('Enter choice of Beverage: '))
                        if bev==1:
                            de+='Pepsi',
                        elif bev==2:
                            de+='Miranda',
                        elif bev==3:
                            de+='7UP',
                        elif bev==4:
                            de+='Diet Pepsi',
                        elif bev==5:
                            de+='Mountain Dew',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==4:
                        print('Mighty Zinger Box - Medium')
                        print('Mighty Zinger Sandwich + 1 pc Chicken + Fries + Coleslaw + Drink')
                        print('AED 35.00')
                        t=35
                        de=['Mighty Zinger Box - Medium']
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        chee=input('Do you want to add cheese?   +AED 2.00 ')
                        if chee=='yes' or chee=='Yes':
                            t+=2
                            de+='American cheese',
                        spc=input('Chicken: Spicy or Original? ')
                        sc=spc.capitalize()
                        de+=sc,
                        print('Choice of first Side item')
                        print('1-Coleslaw salad')
                        print('2-Medium Fries')
                        print('3-Medium Spicy Fries   +AED 2.00')
                        ch1=int(input('Enter choice of first side item: '))
                        if ch1==1:
                            de+='Coleslaw Salad',
                        elif ch1==2:
                            de+='Medium Fries',
                        elif ch1==3:
                            de+='Medium Spicy fries',
                            t+=2
                        print('Choice of Second Side item')
                        print('1-Coleslaw salad')
                        print('2-Regular Fries         +AED 2.00')
                        print('3-Regular Spicy Fries   +AED 3.00')
                        ch2=int(input('Enter choice of second side item: '))
                        if ch2==1:
                            de+='Coleslaw Salad',
                        elif ch2==2:
                            de+='Regular Fries',
                            t+=2
                        elif ch2==3:
                            de+='Regular Spicy fries',
                            t+=3
                        print('Choice of Beverage')
                        print('1-Pepsi')
                        print('2-Miranda')
                        print('3-7UP')
                        print('4-Diet Pepsi')
                        print('5-Mountain Dew ')
                        bev=int(input('Enter choice of Beverage: '))
                        if bev==1:
                            de+='Pepsi',
                        elif bev==2:
                            de+='Miranda',
                        elif bev==3:
                            de+='7UP',
                        elif bev==4:
                            de+='Diet Pepsi',
                        elif bev==5:
                            de+='Mountain Dew',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==5:
                        print('Shrimp Box')
                        print('10 pcs Shrimp + Fries + Coleslaw + Drink + Bun + Colonel Sauce + Dynamite sauce')
                        print('AED 38.00')
                        t=38
                        de=['Shrimp Box']
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('Choice of Second Side item')
                        print('1-Coleslaw salad')
                        print('2-Regular Fries         +AED 2.00')
                        print('3-Regular Spicy Fries   +AED 3.00')
                        ch2=int(input('Enter choice of second side item: '))
                        if ch2==1:
                            de+='Coleslaw Salad',
                        elif ch2==2:
                            de+='Regular Fries',
                            t+=2
                        elif ch2==3:
                            de+='Regular Spicy fries',
                            t+=3
                        print('Choice of Beverage')
                        print('1-Pepsi')
                        print('2-Miranda')
                        print('3-7UP')
                        print('4-Diet Pepsi')
                        print('5-Mountain Dew ')
                        bev=int(input('Enter choice of Beverage: '))
                        if bev==1:
                            de+='Pepsi',
                        elif bev==2:
                            de+='Miranda',
                        elif bev==3:
                            de+='7UP',
                        elif bev==4:
                            de+='Diet Pepsi',
                        elif bev==5:
                            de+='Mountain Dew',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==6:
                        print('Chicken rice meal')
                        print('2 pcs Chicken + Rice + Drink + 1 sauce')
                        print('AED 27.00')
                        t=27
                        de=['Chicken rice meal']
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        sau=input('Sauce: Arabiatta sauce or Chilli sauce? ')
                        sa=sau.capitalize()
                        des+=sa
                        spc=input('Chicken: Spicy or Original? ')
                        sc=spc.capitalize()
                        de+=sc
                        print('Choice of Beverage')
                        print('1-Pepsi')
                        print('2-Miranda')
                        print('3-7UP')
                        print('4-Diet Pepsi')
                        print('5-Mountain Dew ')
                        bev=int(input('Enter choice of Beverage: '))
                        if bev==1:
                            de+='Pepsi',
                        elif bev==2:
                            de+='Miranda',
                        elif bev==3:
                            de+='7UP',
                        elif bev==4:
                            de+='Diet Pepsi',
                        elif bev==5:
                            de+='Mountain Dew',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==7:
                        print('Mighty Zinger')
                        print('AED 18.00')
                        t=18
                        de=['Mighty Zinger']
                        chee=input('Do you want to add cheese?   +AED 2.00 ')
                        if chee=='yes' or chee=='Yes':
                            t+=2
                            de+='American cheese',
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==8:
                        print('Fillet supreme')
                        print('AED 16.00')
                        t=16
                        de=['Fillet supreme']
                        chee=input('Do you want to add cheese?   +AED 2.00 ')
                        if chee=='yes' or chee=='Yes':
                            t+=2
                            de+='American cheese',
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==9:
                        print('8 pcs super bucket')
                        print('8 pcs chicken + 5 strips + 1 Family fries + 1 large Coleslaw + 500ml drink')
                        print('AED 75.00')
                        t=75
                        de=['8 pcs super bucket']
                        spc=input('Chicken: Spicy or Original? ')
                        sc=spc.capitalize()
                        de+=sc,
                        print('Choice of first Side item')
                        print('1-Coleslaw salad')
                        print('2-Medium Fries')
                        print('3-Medium Spicy Fries    +AED 2.00')
                        ch1=int(input('Enter choice of first side item: '))
                        if ch1==1:
                            de+='Coleslaw Salad',
                        elif ch1==2:
                            de+='Medium Fries',
                        elif ch1==3:
                            de+='Medium Spicy fries',
                            t+=2
                        print('Choice of Second Side item')
                        print('1-Coleslaw salad')
                        print('2-Regular Fries         +AED 2.00')
                        print('3-Regular Spicy Fries   +AED 3.00')
                        ch2=int(input('Enter choice of second side item: '))
                        if ch2==1:
                            de+='Coleslaw Salad',
                        elif ch2==2:
                            de+='Regular Fries',
                            t+=2
                        elif ch2==3:
                            de+='Regular Spicy fries',
                            t+=3
                        print('Choice of Beverage')
                        print('1-Pepsi')
                        print('2-Miranda')
                        print('3-7UP')
                        print('4-Diet Pepsi')
                        print('5-Mountain Dew ')
                        bev=int(input('Enter choice of Beverage: '))
                        if bev==1:
                            de+='Pepsi',
                        elif bev==2:
                            de+='Miranda',
                        elif bev==3:
                            de+='7UP',
                        elif bev==4:
                            de+='Diet Pepsi',
                        elif bev==5:
                            de+='Mountain Dew',
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==10:
                        print('18 pcs bucket')
                        print('18 pcs chicken + 1 Family fries + 1 large Coleslaw + 2.25l drink')
                        print('AED 119.00')
                        t=119
                        de=['18 pcs bucket']
                        spc=input('Chicken: Spicy or Original? ')
                        sc=spc.capitalize()
                        de+=sc,
                        print('Choice of first Side item')
                        print('1-Coleslaw salad')
                        print('2-Medium Fries')
                        print('3-Medium Spicy Fries     +AED 2.00')
                        ch1=int(input('Enter choice of first side item: '))
                        if ch1==1:
                            de+='Coleslaw Salad',
                        elif ch1==2:
                            de+='Medium Fries',
                        elif ch1==3:
                            de+='Medium Spicy fries',
                            t+=2
                        print('Choice of Second Side item')
                        print('1-Coleslaw salad')
                        print('2-Regular Fries         +AED 2.00')
                        print('3-Regular Spicy Fries   +AED 3.00')
                        ch2=int(input('Enter choice of second side item: '))
                        if ch2==1:
                            de+='Coleslaw Salad',
                        elif ch2==2:
                            de+='Regular Fries',
                            t+=2
                        elif ch2==3:
                            de+='Regular Spicy fries',
                            t+=3
                        print('Choice of Beverage')
                        print('1-Pepsi')
                        print('2-Miranda')
                        print('3-7UP')
                        print('4-Diet Pepsi')
                        print('5-Mountain Dew ')
                        bev=int(input('Enter choice of Beverage: '))
                        if bev==1:
                            de+='Pepsi',
                        elif bev==2:
                            de+='Miranda',
                        elif bev==3:
                            de+='7UP',
                        elif bev==4:
                            de+='Diet Pepsi',
                        elif bev==5:
                            de+='Mountain Dew',
                        print('Add ons')
                        print('1-Coleslaw          +AED 3.00')
                        print('2-2 psc strips      +AED 3.00')
                        print('3-Cookie            +AED 5.50')
                        print('4-Cheesecake        +AED 9.50')
                        print('5-Chocolate cake    +AED 9.50')
                        print('6-Rice              +AED 7.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add ons: '))
                        if add==1:
                            de+='Coleslaw',
                            t+=3
                        elif add==2:
                            de+='2 pcs strips',
                            t+=5
                        elif add==3:
                            de+='Cookie',
                            t+=5.50
                        elif add==4:
                            de+='Cheesecake',
                            t+=9.50
                        elif add==5:
                            de+='Chocolate cake',
                            t+=9.50
                        elif add==6:
                            de+='Rice',
                            t+=7
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif kfcc==11:
                        y=True
                elif ch==2:
                    y=True
                    print('-'*50)
                    print('Pizza Hut')
                    print('Delivery within 60 mins')
                    print('Delivery fee - AED 8.00')
                    print('-'*50)
                    print('Menu:')
                    print("1-Hut's Chicken Kofta")
                    print('2-Ultimate Cheese')
                    print('3-Super Limo')
                    print('4-My Box')
                    print('5-Spicy Chicken Ranch')
                    print('6-Chicken Super Supreme')
                    print('7-Very Veggie')
                    print('8-Margherita')
                    print('9-Chicken BBQ')
                    print('10-Hot stuff')
                    print('11-Go back to previous menu')
                    print('-'*50)
                    d=8
                    pizc=int(input('Enter choice: '))
                    if pizc==1:
                        print("Hut's Chicken Kofta")
                        de=["Hut's Chicken Kofta"]
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            print('Choose dough')
                            print('1-Handcrafted Sourdough  +AED 31.00')
                            print('2-Pan                    +AED 30.00')
                            print("3-Thin 'n' Crispy        +AED 30.00")
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Handcrafted Sourdough',
                                t+=31
                            elif dough==2:
                                de+='Pan crust',
                                t+=30
                            elif dough==3:
                                de+="Thin 'n' Crispy",
                                t+=30
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            print('Choose dough')
                            print('1-Handcrafted Sourdough  +AED 46.00')
                            print('2-Pan                    +AED 45.00')
                            print('3-Stuffed Crust          +AED 47.00')
                            print("4-Thin 'n' Crispy        +AED 45.00")
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Handcrafted Sourdough',
                                t+=46
                            elif dough==2:
                                de+='Pan crust',
                                t+=45
                            elif dough==3:
                                de+='Stuffed Crust',
                                t+=47
                            elif dough==4:
                                de+="Thin 'n' Crispy",
                                t+=45
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            print('Choose dough')
                            print('1-Handcrafted Sourdough  +AED 61.00')
                            print('2-Pan                    +AED 60.00')
                            print('3-Stuffed Crust          +AED 63.00')
                            print("4-Thin 'n' Crispy        +AED 60.00")
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Handcrafted Sourdough',
                                t+=61
                            elif dough==2:
                                de+='Pan crust',
                                t+=60
                            elif dough==3:
                                de+='Stuffed Crust',
                                t+=63
                            elif dough==4:
                                de+="Thin 'n' Crispy",
                                t+=60
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==2:
                        print("Ultimate Cheese")
                        de=["Ultimate Cheese"]
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            print('Choose dough')
                            print('1-Handcrafted Sourdough  +AED 31.00')
                            print('2-Pan                    +AED 30.00')
                            print("3-Thin 'n' Crispy        +AED 30.00")
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Handcrafted Sourdough',
                                t+=31
                            elif dough==2:
                                de+='Pan crust',
                                t+=30
                            elif dough==3:
                                de+="Thin 'n' Crispy",
                                t+=30
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            print('Choose dough')
                            print('1-Handcrafted Sourdough  +AED 46.00')
                            print('2-Pan                    +AED 45.00')
                            print('3-Stuffed Crust          +AED 47.00')
                            print("4-Thin 'n' Crispy        +AED 45.00")
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Handcrafted Sourdough',
                                t+=46
                            elif dough==2:
                                de+='Pan crust',
                                t+=45
                            elif dough==3:
                                de+='Stuffed Crust',
                                t+=47
                            elif dough==4:
                                de+="Thin 'n' Crispy",
                                t+=45
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            print('Choose dough')
                            print('1-Handcrafted Sourdough  +AED 61.00')
                            print('2-Pan                    +AED 60.00')
                            print('3-Stuffed Crust          +AED 63.00')
                            print("4-Thin 'n' Crispy        +AED 60.00")
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Handcrafted Sourdough',
                                t+=61
                            elif dough==2:
                                de+='Pan crust',
                                t+=60
                            elif dough==3:
                                de+='Stuffed Crust',
                                t+=63
                            elif dough==4:
                                de+="Thin 'n' Crispy",
                                t+=60
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==3:
                        print('Super Limo')
                        print('36 pizza slices + 3 dips + 3 sides')
                        print('AED 99.00')
                        t=99
                        de=['Super Limo']
                        print('Choose First pizza')
                        print('1-Chicken Shawerma')
                        print('2-Classic Pepperoni')
                        print('3-Margarita')
                        print('4-Very Veggie')
                        print('5-Spicy Chicken Ranch')
                        print('6-Chicken BBQ')
                        print('7-Super Supreme')
                        ch1=int(input('Enter choice of first pizza: '))
                        if ch1==1:
                            de+='Chicken Shawarma',
                        elif ch1==2:
                            de+='Classic Pepperoni',
                        elif ch1==3:
                            de+='Margarita',
                        elif ch1==4:
                            de+='Very Veggie',
                        elif ch1==5:
                            de+='Spicy Chicken Ranch',
                        elif ch1==6:
                            de+='Chicken BBQ',
                        elif ch1==7:
                            de+='Super Supreme',
                        print('Choose Second pizza')
                        print('1-Chicken Shawerma')
                        print('2-Classic Pepperoni')
                        print('3-Margarita')
                        print('4-Very Veggie')
                        print('5-Spicy Chicken Ranch')
                        print('6-Chicken BBQ')
                        print('7-Super Supreme')
                        ch2=int(input('Enter choice of second pizza: '))
                        if ch2==1:
                            de+='Chicken Shawarma',
                        elif ch2==2:
                            de+='Classic Pepperoni',
                        elif ch2==3:
                            de+='Margarita',
                        elif ch2==4:
                            de+='Very Veggie',
                        elif ch2==5:
                            de+='Spicy Chicken Ranch',
                        elif ch2==6:
                            de+='Chicken BBQ',
                        elif ch2==7:
                            de+='Super Supreme',
                        print('Choose Third pizza')
                        print('1-Chicken Shawerma')
                        print('2-Classic Pepperoni')
                        print('3-Margarita')
                        print('4-Very Veggie')
                        print('5-Spicy Chicken Ranch')
                        print('6-Chicken BBQ')
                        print('7-Super Supreme')
                        ch3=int(input('Enter choice of third pizza: '))
                        if ch3==1:
                            de+='Chicken Shawarma',
                        elif ch3==2:
                            de+='Classic Pepperoni',
                        elif ch3==3:
                            de+='Margarita',
                        elif ch3==4:
                            de+='Very Veggie',
                        elif ch3==5:
                            de+='Spicy Chicken Ranch',
                        elif ch3==6:
                            de+='Chicken BBQ',
                        elif ch3==7:
                            de+='Super Supreme',
                        print('Choose Pasta')
                        print('1-Vegi Pasta')
                        print('2-Chicken Pasta')
                        pas=int(input('Enter coice of pasta: '))
                        if pas==1:
                            de+='Vegi Pasta',
                        elif pas==2:
                            de+='Chicken pasta',
                        print('Choose first sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau1=int(input('Enter Choice of Sauce: '))
                        if sau1==1:
                            de+='Creamy Ranch Dip',
                        elif sau1==2:
                            de+='Chipotle BBQ Dip',
                        elif sau1==3:
                            de+='Fiery Peri Dip',
                        print('Choose second sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau2=int(input('Enter Choice of Sauce: '))
                        if sau2==1:
                            de+='Creamy Ranch Dip',
                        elif sau2==2:
                            de+='Chipotle BBQ Dip',
                        elif sau2==3:
                            de+='Fiery Peri Dip',
                        print('Choose third sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau3=int(input('Enter Choice of Sauce: '))
                        if sau3==1:
                            de+='Creamy Ranch Dip',
                        elif sau3==2:
                            de+='Chipotle BBQ Dip',
                        elif sau3==3:
                            de+='Fiery Peri Dip',
                        print('Add on sides')
                        print('1-No add on')
                        print('2-Supreme Salad + Drink + Garlic Bread   +AED 25.00')
                        sid=int(input('Enter choice of sides: '))
                        if sid==2:
                            de+='Supreme Salad + Drink + Garlic Bread',
                            t+=25
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==4:
                        print('My box')
                        print('AED 30.00')
                        de=['My box']
                        t=30
                        print('Choose pizza')
                        print('1-Chicken Shawerma')
                        print('2-Classic Pepperoni')
                        print('3-Margarita')
                        print('4-Very Veggie')
                        print('5-Spicy Chicken Ranch')
                        print('6-Chicken BBQ')
                        print('7-Super Supreme')
                        ch1=int(input('Enter choice of first pizza: '))
                        if ch1==1:
                            de+='Chicken Shawarma',
                        elif ch1==2:
                            de+='Classic Pepperoni',
                        elif ch1==3:
                            de+='Margarita',
                        elif ch1==4:
                            de+='Very Veggie',
                        elif ch1==5:
                            de+='Spicy Chicken Ranch',
                        elif ch1==6:
                            de+='Chicken BBQ',
                        elif ch1==7:
                            de+='Super Supreme',
                        print('Choose first side')
                        print('1-Buffalo wings')
                        print('2-Potato Wedges')
                        sid1=int(input('Enter choice of first side: '))
                        if sid1==1:
                            de+='Buffalo Wings',
                        elif sid1==2:
                            de+='Potato Wedges',
                        print('Choose second side')
                        print('1-Chicken BBQ rolls')
                        print('2-2pcs Garlic Bread Supreme')
                        sid2=int(input('Enter choice of second side: '))
                        if sid2==1:
                            de+='Chicken BBQ rolls',
                        elif sid2==2:
                            de+='2pcs Garlic Bread Supreme',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==5:
                        print('Spicy Chicken Ranch')
                        de=['Spicy Chicken Ranch']
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            t+=28
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            t+=43
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            t+=58
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==6:
                        print('Chicken Super Supreme')
                        de=['Chicken Super Supreme']
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            t+=28
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            t+=43
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            t+=58
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==7:
                        print('Very Veggie')
                        de=['Very Veggie']
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            t+=28
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            t+=43
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            t+=58
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==8:
                        print('Margherita')
                        de=['Margherita']
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            t+=28
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            t+=43
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            t+=58
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==9:
                        print('Chicken BBQ')
                        de=['Chicken BBQ']
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            t+=28
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            t+=43
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            t+=58
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==10:
                        print('Hot Stuff')
                        de=['Hot Stuff']
                        t=0
                        print('Choose Size')
                        print('1-Small')
                        print('2-Medium')
                        print('3-Large')
                        size=int(input('Enter choice: '))
                        if size==1:
                            de+='Small',
                            t+=28
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif size==2:
                            de+='Medium',
                            t+=43
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif size==3:
                            de+='Large',
                            t+=58
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print('Choose sauce')
                        print('1-Creamy Ranch Dip')
                        print('2-Chipotle BBQ Dip')
                        print('3-Fiery Peri Dip')
                        sau=int(input('Enter Choice of Sauce: '))
                        if sau==1:
                            de+='Creamy Ranch Dip',
                        elif sau==2:
                            de+='Chipotle BBQ Dip',
                        elif sau==3:
                            de+='Fiery Peri Dip',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pizc==11:
                        y=True
                elif ch==3:
                    print('-'*50)
                    print('Subway')
                    print('Delivery within 22 mins')
                    print('Delivery fee - AED 8.00')
                    print('-'*50)
                    print('Menu:')
                    print('1-Crumbed Chicken Sub Roll')
                    print('2-Crumbed Chicken Pane 6-inch Sandwich')
                    print('3-Roast Beef 6 inch')
                    print('4-Steak and cheese 6 inch')
                    print('5-Peri Peri Chicken 6 inch')
                    print('6-Turkey Breast Footlong')
                    print('7-Chicken Teriyaki Footlong')
                    print('8-Sandwich platter')
                    print('9-Giant Sub')
                    print('10-Cookies Box 12 pcs')
                    print('11-Go back to previous menu')
                    print('-'*50)
                    d=8
                    subc=int(input('Enter choice: '))
                    if subc==1:
                        print('Crumbed Chicken Sub Roll')
                        print('AED 10.00')
                        t=10
                        de=['Crumbed Chicken Sub Roll']
                        print('Choice of cheese')
                        print('1-American cheese            +AED 2.00')
                        print('2-Mozzarella cheese          +AED 2.00')
                        print('3-No cheese')
                        print('4-Mixed Cheddar cheese       +AED 2.00')
                        che=int(input('Enter choice of cheese: '))
                        if che==1:
                            de+='American cheese',
                            t+=2
                        elif che==2:
                            de+='Mozarella cheese',
                            t+=2
                        elif che==4:
                            de+='Mixed Cheddar cheese',
                            t+=2
                        print('Choice of sides')
                        print('1-Hash Browns                       +AED 8.00')
                        print('2-Chicken and Cheese toastie        +AED 7.00')
                        print('3-Veggies and Cheese toastie        +AED 5.00')
                        print('4-Pepperoni and Cheese toastie      +AED 7.00')
                        print('5-No sides')
                        sid=int(input('Enter choice of sides'))
                        if sid==1:
                            de+='Hash Browns',
                            t+=8
                        elif sid==2:
                            de+='Chicken and Cheese toastie',
                            t+=7
                        elif sid==4:
                            de+='Pepperoni and Cheese toastie',
                            t+=7
                        elif sid==3:
                            de+='Veggies and Cheese toastie',
                            t+=5
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==2:
                        print('Crumbed Chicken Pane 6-inch Sandwich')
                        print('AED 15.00')
                        t=15
                        de=['Crumbed Chicken Pane 6-inch Sandwich']
                        print('Choice of bread')
                        print('1-Italian bread')
                        print('2-Wheat bread')
                        print('3-Parmesan Oregano bread')
                        print('4-Honey Oat bread')
                        bre=int(input('Enter choice of bread: '))
                        if bre==1:
                            de+='Italian bread',
                        elif bre==2:
                            de+='Wheat bread',
                        elif bre==3:
                            de+='Parmesan Oregano bread',
                        elif bre==4:
                            de+='Honey oat bread',
                        print('Choice of cheese')
                        print('1-American cheese')
                        print('2-Mozzarella cheese')
                        print('3-No cheese')
                        print('4-Mixed Cheddar cheese')
                        che=int(input('Enter choice of cheese: '))
                        if che==1:
                            de+='American cheese',
                        elif che==2:
                            de+='Mozarella cheese',
                        elif che==4:
                            de+='Mixed Cheddar cheese',
                        to=input('Toasted or Not Toasted? ')
                        if to=='Toasted' or to=='toasted':
                            de+='Toasted',
                        print('Choice of Vegetables')
                        print('Choose 7')
                        print('1-Mixed Lettuce')
                        print('2-Tomatoes')
                        print('3-Cucumbers')
                        print('4-Extra Pickles')
                        print('5-Green Peppers')
                        print('6-Black Olives')
                        print('7-White Onions')
                        print('8-Jalepeno')
                        print('9-Sun dried Tomato')
                        print('10-Rocket leaves')
                        print('11-White Slices Mushrooms')
                        print('12-Guacamole                 +AED 3.00')
                        for i in range(7):
                            veg=int(input('Choose Vegetable: '))
                            if veg==1:
                                de+='Mixed Lettuce',
                            elif veg==2:
                                de+='Tomatoes',
                            elif veg==3:
                                de+='Cucumbers',
                            elif veg==4:
                                de+='Extra Pickles',
                            elif veg==5:
                                de+='Green Peppers',
                            elif veg==6:
                                de+='Black Olives',
                            elif veg==7:
                                de+='White Onions',
                            elif veg==8:
                                de+='Jalapeno',
                            elif veg==9:
                                de+='Sun dried Tomato',
                            elif veg==10:
                                de+='Rocket leaves',
                            elif veg==11:
                                de+='White Sliced Mushroom',
                            elif veg==12:
                                de+='Guacamole',
                                t+=3
                        print('Choice of Condiments')
                        print('Choose 3')
                        print('1-BBQ Sauce')
                        print('2-Ceasar Sauce')
                        print('3-Chipotle Southwest')
                        print('4-Honey mustard')
                        print('5-Hot Sauce')
                        print('6-Ketchup')
                        print('7-Ranch Sauce')
                        print('8-Thousand Islands')
                        print('9-Crushed Peppercorn')
                        for i in range(3):
                            con=int(input('Choose Condiment: '))
                            if con==1:
                                de+='BBQ Sauce',
                            elif con==2:
                                de+='Ceasar Sauce',
                            elif con==3:
                                de+='Chipotle Southwest',
                            elif con==4:
                                de+='Honey Mustard',
                            elif con==5:
                                de+='Hot Sauce',
                            elif con==6:
                                de+='Ketchup',
                            elif con==7:
                                de+='Ranch Sauce',
                            elif con==8:
                                de+='Thousand Islands',
                            elif con==9:
                                de+='Crushed Peppercorn',
                        print('Choose Add-ons')
                        print('1-Extra Double Meat             +AED 5.00')
                        print('2-Extra Pepperoni               +AED 3.00')
                        print('3-Extra Salami                  +AED 3.00')
                        print('4-Extra American Cheese         +AED 2.00')
                        print('5-Extra Mozzerella Cheese       +AED 2.00')
                        print('6-Extra Mixed Cheddar Cheese    +AED 2.00')
                        print('7-No add ons')
                        add=int(input('Enter choice of add-ons: '))
                        if add==1:
                            de+='Extra Double Meat',
                            t+=5
                        elif add==2:
                            de+='Extra Pepperoni',
                            t+=3
                        elif add==3:
                            de+='Extra Salami',
                            t+=3
                        elif add==4:
                            de+='Extra American cheese',
                            t+=2
                        elif add==5:
                            de+='Extra Mozarella cheese',
                            t+=2
                        elif add==6:
                            de+='Extra Mixed Cheddar cheese',
                            t+=2
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==3:
                        print('Roast Beef 6 inch')
                        print('AED 22.00')
                        t=22
                        de=['Roast Beef 6 inch']
                        print('Choice of bread')
                        print('1-Italian bread')
                        print('2-Wheat bread')
                        print('3-Parmesan Oregano bread')
                        print('4-Honey Oat bread')
                        print('5-Habanero Wrap')
                        print('6-Spinach Wrap')
                        print('7-Canola Wrap')
                        print('8-Salad')
                        bre=int(input('Enter choice of bread: '))
                        if bre==1:
                            de+='Italian bread',
                        elif bre==2:
                            de+='Wheat bread',
                        elif bre==3:
                            de+='Parmesan Oregano bread',
                        elif bre==4:
                            de+='Honey oat bread',
                        elif bre==5:
                            de+='Habanero Wrap',
                            t+=8
                        elif bre==6:
                            de+='Spinach Wrap',
                            t+=8
                        elif bre==7:
                            de+='Canola Wrap',
                            t+=8
                        elif bre==8:
                            de+='Salad',
                            t+=6
                        print('Choice of cheese')
                        print('1-American cheese')
                        print('2-Mozzarella cheese')
                        print('3-No cheese')
                        print('4-Mixed Cheddar cheese')
                        che=int(input('Enter choice of cheese: '))
                        if che==1:
                            de+='American cheese',
                        elif che==2:
                            de+='Mozarella cheese',
                        elif che==4:
                            de+='Mixed Cheddar cheese',
                        to=input('Toasted or Not Toasted? ')
                        if to=='Toasted' or to=='toasted':
                            de+='Toasted',
                        print('Choice of Vegetables')
                        print('Choose 7')
                        print('1-Mixed Lettuce')
                        print('2-Tomatoes')
                        print('3-Cucumbers')
                        print('4-Extra Pickles')
                        print('5-Green Peppers')
                        print('6-Black Olives')
                        print('7-White Onions')
                        print('8-Jalepeno')
                        print('9-Sun dried Tomato')
                        print('10-Rocket leaves')
                        print('11-White Slices Mushrooms')
                        print('12-Guacamole                 +AED 3.00')
                        for i in range(7):
                            veg=int(input('Choose Vegetable: '))
                            if veg==1:
                                de+='Mixed Lettuce',
                            elif veg==2:
                                de+='Tomatoes',
                            elif veg==3:
                                de+='Cucumbers',
                            elif veg==4:
                                de+='Extra Pickles',
                            elif veg==5:
                                de+='Green Peppers',
                            elif veg==6:
                                de+='Black Olives',
                            elif veg==7:
                                de+='White Onions',
                            elif veg==8:
                                de+='Jalapeno',
                            elif veg==9:
                                de+='Sun dried Tomato',
                            elif veg==10:
                                de+='Rocket leaves',
                            elif veg==11:
                                de+='White Sliced Mushroom',
                            elif veg==12:
                                de+='Guacamole',
                                t+=3
                        print('Choice of Condiments')
                        print('Choose 3')
                        print('1-BBQ Sauce')
                        print('2-Ceasar Sauce')
                        print('3-Chipotle Southwest')
                        print('4-Honey mustard')
                        print('5-Hot Sauce')
                        print('6-Ketchup')
                        print('7-Ranch Sauce')
                        print('8-Thousand Islands')
                        print('9-Crushed Peppercorn')
                        for i in range(3):
                            con=int(input('Choose Condiment: '))
                            if con==1:
                                de+='BBQ Sauce',
                            elif con==2:
                                de+='Ceasar Sauce',
                            elif con==3:
                                de+='Chipotle Southwest',
                            elif con==4:
                                de+='Honey Mustard',
                            elif con==5:
                                de+='Hot Sauce',
                            elif con==6:
                                de+='Ketchup',
                            elif con==7:
                                de+='Ranch Sauce',
                            elif con==8:
                                de+='Thousand Islands',
                            elif con==9:
                                de+='Crushed Peppercorn',
                        print('Choose Add-ons')
                        print('1-Extra Double Meat             +AED 5.00')
                        print('2-Extra Pepperoni               +AED 3.00')
                        print('3-Extra Salami                  +AED 3.00')
                        print('4-Extra American Cheese         +AED 2.00')
                        print('5-Extra Mozzerella Cheese       +AED 2.00')
                        print('6-Extra Mixed Cheddar Cheese    +AED 2.00')
                        print('7-Hash Browns                   +AED 8.00')
                        print('8-No add ons')
                        add=int(input('Enter choice of add-ons: '))
                        if add==1:
                            de+='Extra Double Meat',
                            t+=5
                        elif add==2:
                            de+='Extra Pepperoni',
                            t+=3
                        elif add==3:
                            de+='Extra Salami',
                            t+=3
                        elif add==4:
                            de+='Extra American cheese',
                            t+=2
                        elif add==5:
                            de+='Extra Mozarella cheese',
                            t+=2
                        elif add==6:
                            de+='Extra Mixed Cheddar cheese',
                            t+=2
                        elif add==7:
                            de+='Hash Browns',
                            t+=8
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==4:
                        print('Steak and cheese 6 inch')
                        print('AED 22.00')
                        t=22
                        de=['Steak and cheese 6 inch']
                        print('Choice of bread')
                        print('1-Italian bread')
                        print('2-Wheat bread')
                        print('3-Parmesan Oregano bread')
                        print('4-Honey Oat bread')
                        print('5-Habanero Wrap')
                        print('6-Spinach Wrap')
                        print('7-Canola Wrap')
                        print('8-Salad')
                        bre=int(input('Enter choice of bread: '))
                        if bre==1:
                            de+='Italian bread',
                        elif bre==2:
                            de+='Wheat bread',
                        elif bre==3:
                            de+='Parmesan Oregano bread',
                        elif bre==4:
                            de+='Honey oat bread',
                        elif bre==5:
                            de+='Habanero Wrap',
                            t+=8
                        elif bre==6:
                            de+='Spinach Wrap',
                            t+=8
                        elif bre==7:
                            de+='Canola Wrap',
                            t+=8
                        elif bre==8:
                            de+='Salad',
                            t+=6
                        print('Choice of cheese')
                        print('1-American cheese')
                        print('2-Mozzarella cheese')
                        print('3-No cheese')
                        print('4-Mixed Cheddar cheese')
                        che=int(input('Enter choice of cheese: '))
                        if che==1:
                            de+='American cheese',
                        elif che==2:
                            de+='Mozarella cheese',
                        elif che==4:
                            de+='Mixed Cheddar cheese',
                        to=input('Toasted or Not Toasted? ')
                        if to=='Toasted' or to=='toasted':
                            de+='Toasted',
                        print('Choice of Vegetables')
                        print('Choose 7')
                        print('1-Mixed Lettuce')
                        print('2-Tomatoes')
                        print('3-Cucumbers')
                        print('4-Extra Pickles')
                        print('5-Green Peppers')
                        print('6-Black Olives')
                        print('7-White Onions')
                        print('8-Jalepeno')
                        print('9-Sun dried Tomato')
                        print('10-Rocket leaves')
                        print('11-White Slices Mushrooms')
                        print('12-Guacamole                 +AED 3.00')
                        for i in range(7):
                            veg=int(input('Choose Vegetable: '))
                            if veg==1:
                                de+='Mixed Lettuce',
                            elif veg==2:
                                de+='Tomatoes',
                            elif veg==3:
                                de+='Cucumbers',
                            elif veg==4:
                                de+='Extra Pickles',
                            elif veg==5:
                                de+='Green Peppers',
                            elif veg==6:
                                de+='Black Olives',
                            elif veg==7:
                                de+='White Onions',
                            elif veg==8:
                                de+='Jalapeno',
                            elif veg==9:
                                de+='Sun dried Tomato',
                            elif veg==10:
                                de+='Rocket leaves',
                            elif veg==11:
                                de+='White Sliced Mushroom',
                            elif veg==12:
                                de+='Guacamole',
                                t+=3
                        print('Choice of Condiments')
                        print('Choose 3')
                        print('1-BBQ Sauce')
                        print('2-Ceasar Sauce')
                        print('3-Chipotle Southwest')
                        print('4-Honey mustard')
                        print('5-Hot Sauce')
                        print('6-Ketchup')
                        print('7-Ranch Sauce')
                        print('8-Thousand Islands')
                        print('9-Crushed Peppercorn')
                        for i in range(3):
                            con=int(input('Choose Condiment: '))
                            if con==1:
                                de+='BBQ Sauce',
                            elif con==2:
                                de+='Ceasar Sauce',
                            elif con==3:
                                de+='Chipotle Southwest',
                            elif con==4:
                                de+='Honey Mustard',
                            elif con==5:
                                de+='Hot Sauce',
                            elif con==6:
                                de+='Ketchup',
                            elif con==7:
                                de+='Ranch Sauce',
                            elif con==8:
                                de+='Thousand Islands',
                            elif con==9:
                                de+='Crushed Peppercorn',
                        print('Choose Add-ons')
                        print('1-Extra Double Meat             +AED 5.00')
                        print('2-Extra Pepperoni               +AED 3.00')
                        print('3-Extra Salami                  +AED 3.00')
                        print('4-Extra American Cheese         +AED 2.00')
                        print('5-Extra Mozzerella Cheese       +AED 2.00')
                        print('6-Extra Mixed Cheddar Cheese    +AED 2.00')
                        print('7-Hash Browns                   +AED 8.00')
                        print('8-No add ons')
                        add=int(input('Enter choice of add-ons: '))
                        if add==1:
                            de+='Extra Double Meat',
                            t+=5
                        elif add==2:
                            de+='Extra Pepperoni',
                            t+=3
                        elif add==3:
                            de+='Extra Salami',
                            t+=3
                        elif add==4:
                            de+='Extra American cheese',
                            t+=2
                        elif add==5:
                            de+='Extra Mozarella cheese',
                            t+=2
                        elif add==6:
                            de+='Extra Mixed Cheddar cheese',
                            t+=2
                        elif add==7:
                            de+='Hash Browns',
                            t+=8
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==5:
                        print('Peri Peri Chicken 6 inch')
                        print('AED 22.00')
                        t=22
                        de=['Peri Peri Chicken 6 inch']
                        print('Choice of bread')
                        print('1-Italian bread')
                        print('2-Wheat bread')
                        print('3-Parmesan Oregano bread')
                        print('4-Honey Oat bread')
                        print('5-Habanero Wrap')
                        print('6-Spinach Wrap')
                        print('7-Canola Wrap')
                        print('8-Salad')
                        bre=int(input('Enter choice of bread: '))
                        if bre==1:
                            de+='Italian bread',
                        elif bre==2:
                            de+='Wheat bread',
                        elif bre==3:
                            de+='Parmesan Oregano bread',
                        elif bre==4:
                            de+='Honey oat bread',
                        elif bre==5:
                            de+='Habanero Wrap',
                            t+=8
                        elif bre==6:
                            de+='Spinach Wrap',
                            t+=8
                        elif bre==7:
                            de+='Canola Wrap',
                            t+=8
                        elif bre==8:
                            de+='Salad',
                            t+=6
                        print('Choice of cheese')
                        print('1-American cheese')
                        print('2-Mozzarella cheese')
                        print('3-No cheese')
                        print('4-Mixed Cheddar cheese')
                        che=int(input('Enter choice of cheese: '))
                        if che==1:
                            de+='American cheese',
                        elif che==2:
                            de+='Mozarella cheese',
                        elif che==4:
                            de+='Mixed Cheddar cheese',
                        to=input('Toasted or Not Toasted? ')
                        if to=='Toasted' or to=='toasted':
                            de+='Toasted',
                        print('Choice of Vegetables')
                        print('Choose 7')
                        print('1-Mixed Lettuce')
                        print('2-Tomatoes')
                        print('3-Cucumbers')
                        print('4-Extra Pickles')
                        print('5-Green Peppers')
                        print('6-Black Olives')
                        print('7-White Onions')
                        print('8-Jalepeno')
                        print('9-Sun dried Tomato')
                        print('10-Rocket leaves')
                        print('11-White Slices Mushrooms')
                        print('12-Guacamole                 +AED 3.00')
                        for i in range(7):
                            veg=int(input('Choose Vegetable: '))
                            if veg==1:
                                de+='Mixed Lettuce',
                            elif veg==2:
                                de+='Tomatoes',
                            elif veg==3:
                                de+='Cucumbers',
                            elif veg==4:
                                de+='Extra Pickles',
                            elif veg==5:
                                de+='Green Peppers',
                            elif veg==6:
                                de+='Black Olives',
                            elif veg==7:
                                de+='White Onions',
                            elif veg==8:
                                de+='Jalapeno',
                            elif veg==9:
                                de+='Sun dried Tomato',
                            elif veg==10:
                                de+='Rocket leaves',
                            elif veg==11:
                                de+='White Sliced Mushroom',
                            elif veg==12:
                                de+='Guacamole',
                                t+=3
                        print('Choice of Condiments')
                        print('Choose 3')
                        print('1-BBQ Sauce')
                        print('2-Ceasar Sauce')
                        print('3-Chipotle Southwest')
                        print('4-Honey mustard')
                        print('5-Hot Sauce')
                        print('6-Ketchup')
                        print('7-Ranch Sauce')
                        print('8-Thousand Islands')
                        print('9-Crushed Peppercorn')
                        for i in range(3):
                            con=int(input('Choose Condiment: '))
                            if con==1:
                                de+='BBQ Sauce',
                            elif con==2:
                                de+='Ceasar Sauce',
                            elif con==3:
                                de+='Chipotle Southwest',
                            elif con==4:
                                de+='Honey Mustard',
                            elif con==5:
                                de+='Hot Sauce',
                            elif con==6:
                                de+='Ketchup',
                            elif con==7:
                                de+='Ranch Sauce',
                            elif con==8:
                                de+='Thousand Islands',
                            elif con==9:
                                de+='Crushed Peppercorn',
                        print('Choose Add-ons')
                        print('1-Extra Double Meat             +AED 5.00')
                        print('2-Extra Pepperoni               +AED 3.00')
                        print('3-Extra Salami                  +AED 3.00')
                        print('4-Extra American Cheese         +AED 2.00')
                        print('5-Extra Mozzerella Cheese       +AED 2.00')
                        print('6-Extra Mixed Cheddar Cheese    +AED 2.00')
                        print('7-Hash Browns                   +AED 8.00')
                        print('8-No add ons')
                        add=int(input('Enter choice of add-ons: '))
                        if add==1:
                            de+='Extra Double Meat',
                            t+=5
                        elif add==2:
                            de+='Extra Pepperoni',
                            t+=3
                        elif add==3:
                            de+='Extra Salami',
                            t+=3
                        elif add==4:
                            de+='Extra American cheese',
                            t+=2
                        elif add==5:
                            de+='Extra Mozarella cheese',
                            t+=2
                        elif add==6:
                            de+='Extra Mixed Cheddar cheese',
                            t+=2
                        elif add==7:
                            de+='Hash Browns',
                            t+=8
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==6:
                        print('Turkey Breast Footlong')
                        print('AED 31.00')
                        t=31
                        de=['Turkey Breast Footlong']
                        print('Choice of bread')
                        print('1-Italian bread')
                        print('2-Wheat bread')
                        print('3-Parmesan Oregano bread')
                        print('4-Honey Oat bread')
                        bre=int(input('Enter choice of bread: '))
                        if bre==1:
                            de+='Italian bread',
                        elif bre==2:
                            de+='Wheat bread',
                        elif bre==3:
                            de+='Parmesan Oregano bread',
                        elif bre==4:
                            de+='Honey oat bread',
                        print('Choice of cheese')
                        print('1-American cheese')
                        print('2-Mozzarella cheese')
                        print('3-No cheese')
                        print('4-Mixed Cheddar cheese')
                        che=int(input('Enter choice of cheese: '))
                        if che==1:
                            de+='American cheese',
                        elif che==2:
                            de+='Mozarella cheese',
                        elif che==4:
                            de+='Mixed Cheddar cheese',
                        to=input('Toasted or Not Toasted? ')
                        if to=='Toasted' or to=='toasted':
                            de+='Toasted',
                        print('Choice of Vegetables')
                        print('Choose 7')
                        print('1-Mixed Lettuce')
                        print('2-Tomatoes')
                        print('3-Cucumbers')
                        print('4-Extra Pickles')
                        print('5-Green Peppers')
                        print('6-Black Olives')
                        print('7-White Onions')
                        print('8-Jalepeno')
                        print('9-Sun dried Tomato')
                        print('10-Rocket leaves')
                        print('11-White Slices Mushrooms')
                        print('12-Guacamole                 +AED 5.00')
                        for i in range(7):
                            veg=int(input('Choose Vegetable: '))
                            if veg==1:
                                de+='Mixed Lettuce',
                            elif veg==2:
                                de+='Tomatoes',
                            elif veg==3:
                                de+='Cucumbers',
                            elif veg==4:
                                de+='Extra Pickles',
                            elif veg==5:
                                de+='Green Peppers',
                            elif veg==6:
                                de+='Black Olives',
                            elif veg==7:
                                de+='White Onions',
                            elif veg==8:
                                de+='Jalapeno',
                            elif veg==9:
                                de+='Sun dried Tomato',
                            elif veg==10:
                                de+='Rocket leaves',
                            elif veg==11:
                                de+='White Sliced Mushroom',
                            elif veg==12:
                                de+='Guacamole',
                                t+=5
                        print('Choice of Condiments')
                        print('Choose 3')
                        print('1-BBQ Sauce')
                        print('2-Ceasar Sauce')
                        print('3-Chipotle Southwest')
                        print('4-Honey mustard')
                        print('5-Hot Sauce')
                        print('6-Ketchup')
                        print('7-Ranch Sauce')
                        print('8-Thousand Islands')
                        print('9-Crushed Peppercorn')
                        for i in range(3):
                            con=int(input('Choose Condiment: '))
                            if con==1:
                                de+='BBQ Sauce',
                            elif con==2:
                                de+='Ceasar Sauce',
                            elif con==3:
                                de+='Chipotle Southwest',
                            elif con==4:
                                de+='Honey Mustard',
                            elif con==5:
                                de+='Hot Sauce',
                            elif con==6:
                                de+='Ketchup',
                            elif con==7:
                                de+='Ranch Sauce',
                            elif con==8:
                                de+='Thousand Islands',
                            elif con==9:
                                de+='Crushed Peppercorn',
                        print('Choose Add-ons')
                        print('1-Extra Double Meat             +AED 9.00')
                        print('2-Extra Pepperoni               +AED 5.00')
                        print('3-Extra Salami                  +AED 5.00')
                        print('4-Extra American Cheese         +AED 3.00')
                        print('5-Extra Mozzerella Cheese       +AED 3.00')
                        print('6-Extra Mixed Cheddar Cheese    +AED 3.00')
                        print('7-Extra Turkey Bacon            +AED 5.00')
                        print('8-Hash Browns                   +AED 8.00')
                        print('9-No add ons')
                        add=int(input('Enter choice of add-ons: '))
                        if add==1:
                            de+='Extra Double Meat',
                            t+=5
                        elif add==2:
                            de+='Extra Pepperoni',
                            t+=3
                        elif add==3:
                            de+='Extra Salami',
                            t+=3
                        elif add==4:
                            de+='Extra American cheese',
                            t+=2
                        elif add==5:
                            de+='Extra Mozarella cheese',
                            t+=2
                        elif add==6:
                            de+='Extra Mixed Cheddar cheese',
                            t+=2
                        elif add==7:
                            de+='Extra Turkey Bacon',
                            t+=5
                        elif add==8:
                            de+='Hash Browns',
                            t+=8
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==7:
                        print('Chicken Teriyaki Footlong')
                        print('AED 31.00')
                        t=31
                        de=['Chicken Teriyaki Footlong']
                        print('Choice of bread')
                        print('1-Italian bread')
                        print('2-Wheat bread')
                        print('3-Parmesan Oregano bread')
                        print('4-Honey Oat bread')
                        bre=int(input('Enter choice of bread: '))
                        if bre==1:
                            de+='Italian bread',
                        elif bre==2:
                            de+='Wheat bread',
                        elif bre==3:
                            de+='Parmesan Oregano bread',
                        elif bre==4:
                            de+='Honey oat bread',
                        print('Choice of cheese')
                        print('1-American cheese')
                        print('2-Mozzarella cheese')
                        print('3-No cheese')
                        print('4-Mixed Cheddar cheese')
                        che=int(input('Enter choice of cheese: '))
                        if che==1:
                            de+='American cheese',
                        elif che==2:
                            de+='Mozarella cheese',
                        elif che==4:
                            de+='Mixed Cheddar cheese',
                        to=input('Toasted or Not Toasted? ')
                        if to=='Toasted' or to=='toasted':
                            de+='Toasted',
                        print('Choice of Vegetables')
                        print('Choose 7')
                        print('1-Mixed Lettuce')
                        print('2-Tomatoes')
                        print('3-Cucumbers')
                        print('4-Extra Pickles')
                        print('5-Green Peppers')
                        print('6-Black Olives')
                        print('7-White Onions')
                        print('8-Jalepeno')
                        print('9-Sun dried Tomato')
                        print('10-Rocket leaves')
                        print('11-White Slices Mushrooms')
                        print('12-Guacamole                 +AED 5.00')
                        for i in range(7):
                            veg=int(input('Choose Vegetable: '))
                            if veg==1:
                                de+='Mixed Lettuce',
                            elif veg==2:
                                de+='Tomatoes',
                            elif veg==3:
                                de+='Cucumbers',
                            elif veg==4:
                                de+='Extra Pickles',
                            elif veg==5:
                                de+='Green Peppers',
                            elif veg==6:
                                de+='Black Olives',
                            elif veg==7:
                                de+='White Onions',
                            elif veg==8:
                                de+='Jalapeno',
                            elif veg==9:
                                de+='Sun dried Tomato',
                            elif veg==10:
                                de+='Rocket leaves',
                            elif veg==11:
                                de+='White Sliced Mushroom',
                            elif veg==12:
                                de+='Guacamole',
                                t+=5
                        print('Choice of Condiments')
                        print('Choose 3')
                        print('1-BBQ Sauce')
                        print('2-Ceasar Sauce')
                        print('3-Chipotle Southwest')
                        print('4-Honey mustard')
                        print('5-Hot Sauce')
                        print('6-Ketchup')
                        print('7-Ranch Sauce')
                        print('8-Thousand Islands')
                        print('9-Crushed Peppercorn')
                        for i in range(3):
                            con=int(input('Choose Condiment: '))
                            if con==1:
                                de+='BBQ Sauce',
                            elif con==2:
                                de+='Ceasar Sauce',
                            elif con==3:
                                de+='Chipotle Southwest',
                            elif con==4:
                                de+='Honey Mustard',
                            elif con==5:
                                de+='Hot Sauce',
                            elif con==6:
                                de+='Ketchup',
                            elif con==7:
                                de+='Ranch Sauce',
                            elif con==8:
                                de+='Thousand Islands',
                            elif con==9:
                                de+='Crushed Peppercorn',
                        print('Choose Add-ons')
                        print('1-Extra Double Meat             +AED 9.00')
                        print('2-Extra Pepperoni               +AED 5.00')
                        print('3-Extra Salami                  +AED 5.00')
                        print('4-Extra American Cheese         +AED 3.00')
                        print('5-Extra Mozzerella Cheese       +AED 3.00')
                        print('6-Extra Mixed Cheddar Cheese    +AED 3.00')
                        print('7-Extra Turkey Bacon            +AED 5.00')
                        print('8-Hash Browns                   +AED 8.00')
                        print('9-No add ons')
                        add=int(input('Enter choice of add-ons: '))
                        if add==1:
                            de+='Extra Double Meat',
                            t+=5
                        elif add==2:
                            de+='Extra Pepperoni',
                            t+=3
                        elif add==3:
                            de+='Extra Salami',
                            t+=3
                        elif add==4:
                            de+='Extra American cheese',
                            t+=2
                        elif add==5:
                            de+='Extra Mozarella cheese',
                            t+=2
                        elif add==6:
                            de+='Extra Mixed Cheddar cheese',
                            t+=2
                        elif add==7:
                            de+='Extra Turkey Bacon',
                            t+=5
                        elif add==8:
                            de+='Hash Browns',
                            t+=8
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==8:
                        print('Sandwich platter')
                        print('AED 125.00')
                        t=125
                        de=['Sandwich platter']
                        print('Choice of Sandwich')
                        print('Choose 5 Flavours')
                        print('1-Roast beef')
                        print('2-Smoked Turkey')
                        print('3-Turkey Breast')
                        print('4-Italian BMT')
                        print('5-Veggie Delight')
                        print('6-Tuna')
                        for i in range(5):
                            sand=int(input('Enter Choice of Sandwich: '))
                            if sand==1:
                                de+='Roast beef',
                            elif sand==2:
                                de+='Smoked Turkey',
                            elif sand==3:
                                de+='Turkey Breast',
                            elif sand==4:
                                de+='Italian BMT',
                            elif sand==5:
                                de+='Veggie Delight',
                            elif sand==6:
                                de+='Tuna',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==9:
                        print('Giant Sub')
                        t=320
                        de=['Giant Sub']
                        print('Contains 36 two inch portions, Serves 18 to 25. \nPreparation time 24 hours')
                        print('AED 320.00')
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==10:
                        print('Cookies box 12 pcs')
                        print('AED 40.00')
                        t=40
                        de=['Cookie Box']
                        print('1st Flavour choice for 4 pieces')
                        print('1-Chocolate chip Cookie')
                        print('2-Double Chocolate chip Cookie')
                        print('3-White Chip Macadamia Nuts Cookie')
                        coo1=int(input('Enter choice: '))
                        if coo1==1:
                            de+='Chocolate Chip Cookie',
                        elif coo1==2:
                            de+='Double Chocolate chip Cookie',
                        elif coo1==3:
                            de+='White Chip Macadamia Nuts Cookie',
                        print('2nd Flavour choice for 4 pieces')
                        print('1-Chocolate chip Cookie')
                        print('2-Double Chocolate chip Cookie')
                        print('3-White Chip Macadamia Nuts Cookie')
                        coo2=int(input('Enter choice: '))
                        if coo2==1:
                            de+='Chocolate Chip Cookie',
                        elif coo2==2:
                            de+='Double Chocolate chip Cookie',
                        elif coo2==3:
                            de+='White Chip Macadamia Nuts Cookie',
                        print('3rd Flavour choice for 4 pieces')
                        print('1-Chocolate chip Cookie')
                        print('2-Double Chocolate chip Cookie')
                        print('3-White Chip Macadamia Nuts Cookie')
                        coo3=int(input('Enter choice: '))
                        if coo3==1:
                            de+='Chocolate Chip Cookie',
                        elif coo3==2:
                            de+='Double Chocolate chip Cookie',
                        elif coo3==3:
                            de+='White Chip Macadamia Nuts Cookie',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif subc==11:
                        y=True
                elif ch==4:
                    print('-'*50)
                    print('Burger King')
                    print('Delivery within 30 mins')
                    print('Delivery fee - AED 7.00')
                    print('-'*50)
                    print('Menu:')
                    print('1-King Box for 3 people')
                    print('2-Smokey BBQ Angus Meal')
                    print('3-Cheddar Herb Angus Meal')
                    print('4-Big King')
                    print('5-Double Whopper')
                    print('6-Fiery Chicken Fillet Sandwich')
                    print('7-Paneer King Meal')
                    print('8-Chicken Fries 10 pcs')
                    print('9-Spicy Tex Mex Fries')
                    print('10-Crispy Chicken Tenders')
                    print('11-Go back to previous menu')
                    print('-'*50)
                    d=7
                    burc=int(input('Enter Choice: '))
                    if burc==1:
                        print('King Box for 3 people')
                        print('AED 39.00')
                        t=39
                        de=['King Box for 3 people']
                        print('Choice of Sandwich')
                        print('1-Chicken Royale')
                        print('2-Chicken Royale cheese    +AED 2.00')
                        print('3-Whopper')
                        print('Whopper cheese             +AED 2.00')
                        for i in range(3):
                            s=[]
                            sand=int(input('Enter choice of Sandwich: '))
                            if sand==1:
                                s+='Chicken Royale',
                            elif sand==2:
                                s+='Chicken Royale cheese',
                                t+=2
                            elif sand==3:
                                s+='Whopper',
                            elif sand==4:
                                s+='Whopper cheese',
                                t+=2
                            print('Choice of Add-ons')
                            print('Choose 7 items')
                            print('1-Add Bacon Slices      +AED 2.00')
                            print('2-Add Cheese            +AED 2.00')
                            print('3-Add BBQ Sauce')
                            print('4-Add Swiss cheese      +AED 1.00')
                            print('5-Add Fiery Sauce       +AED 2.00')
                            print('6-Add Melted cheese     +AED 2.00')
                            print('7-Add Chicken patty     +AED 8.00')
                            print('8-Add Whopper patty     +AED 7.00')
                            print('9-Add Ketchup')
                            print('10-Add Mayo')
                            print('11-Add Mustard')
                            print('12-No Add-ons')
                            for i  in range(7):
                                add=int(input('Enter choice of Add on: '))
                                if add==1:
                                    s+='Add Bacon slices'
                                    t+=2
                                elif add==2:
                                    s+='Add Cheese',
                                    t+=2
                                elif add==3:
                                    s+='Add BBQ sauce',
                                elif add==4:
                                    s+='Add Swiss cheese',
                                    t+=1
                                elif add==5:
                                    s+='Add Fiery sauce',
                                    t+=2
                                elif add==6:
                                    s+='Add Melted cheese',
                                    t+=2
                                elif add==7:
                                    s+='Add Chicken Royal patty',
                                    t+=8
                                elif add==8:
                                    s+='Add Whopper patty',
                                    t+=7
                                elif add==9:
                                    s+='Add Ketchup',
                                elif add==10:
                                    s+='Add Mayo',
                                elif add==11:
                                    s+='Add Mustard',
                            print('Choice of side')
                            print('1-Spicy Tex Mex fries      +AED 6.00')
                            print('2-French fries small')
                            print('3-Onion Rings small        +AED 1.00')
                            print('4-Strip fries              +AED 5.00')
                            sid=int(input('Enter choice of sides: '))
                            if sid==1:
                                s+='Spicy Tex Mex fries'
                                t+=6
                            elif sid==2:
                                s+='French fries small'
                            elif sid==3:
                                s+='Onion Rings small'
                                t+=1
                            elif sid==4:
                                s+='Strip fries'
                                t+=5
                            print('Choice of Drink')
                            print('1-Coke Can')
                            print('2-Fanta Can')
                            print('3-Sprite Can')
                            print('4-Coke Zero Can')
                            dri=int(input('Enter Choice of drink: '))
                            if dri==1:
                                s+='Coke Can',
                            elif dri==2:
                                s+='Fanta Can',
                            elif dri==3:
                                s+='Sprite Can',
                            elif dri==4:
                                s+='Coke Zero Can',
                            de+=s
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==2:
                        print('Smokey BBQ Angus Meal')
                        print('AED 37.00')
                        t=37
                        de=['Smokey BBQ Angus Meal']
                        print('Choice of Add-ons')
                        print('Choose 7 items')
                        print('1-Add Bacon Slices      +AED 2.00')
                        print('2-Add Cheese            +AED 2.00')
                        print('3-Add BBQ Sauce')
                        print('4-Add Swiss cheese      +AED 1.00')
                        print('5-Add Fiery Sauce       +AED 2.00')
                        print('6-Add Melted cheese     +AED 2.00')
                        print('7-Add Whopper patty     +AED 7.00')
                        print('8-Add Ketchup')
                        print('9-Add Mayo')
                        print('10-Add Mustard')
                        print('11-No Add-ons')
                        for i  in range(7):
                            add=int(input('Enter choice of Add on: '))
                            if add==1:
                                de+='Add Bacon slices'
                                t+=2
                            elif add==2:
                                de+='Add Cheese',
                                t+=2
                            elif add==3:
                                de+='Add BBQ sauce',
                            elif add==4:
                                de+='Add Swiss cheese',
                                t+=1
                            elif add==5:
                                de+='Add Fiery sauce',
                                t+=2
                            elif add==6:
                                de+='Add Melted cheese',
                                t+=2
                            elif add==7:
                                de+='Add Whopper patty',
                                t+=7
                            elif add==8:
                                de+='Add Ketchup',
                            elif add==9:
                                de+='Add Mayo',
                            elif add==10:
                                de+='Add Mustard',
                        print('Choice of side')
                        print('1-Spicy Tex Mex fries      +AED 11.00')
                        print('2-French fries small       +AED 5.00')
                        print('3-Onion Rings small        +AED 6.00')
                        print('4-Strip fries              +AED 10.00')
                        sid=int(input('Enter choice of sides: '))
                        if sid==1:
                            de+='Spicy Tex Mex fries'
                            t+=11
                        elif sid==2:
                            de+='French fries small'
                            t+=5
                        elif sid==3:
                            de+='Onion Rings small'
                            t+=6
                        elif sid==4:
                            de+='Strip fries'
                            t+=10
                        print('Choice of Drink')
                        print('1-Coke 500ml')
                        print('2-Fanta 500ml')
                        print('3-Sprite 500ml')
                        print('4-Coke Zero 500ml')
                        dri=int(input('Enter Choice of drink: '))
                        if dri==1:
                            s+='Coke 500ml',
                        elif dri==2:
                            s+='Fanta 500ml',
                        elif dri==3:
                            s+='Sprite 500ml',
                        elif dri==4:
                            s+='Coke Zero 500ml',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==3:
                        print('Cheddar Herb Angus Meal')
                        print('AED 37.00')
                        t=37
                        de=['Cheddar Herb Angus Meal']
                        print('Choice of Add-ons')
                        print('Choose 7 items')
                        print('1-Add Bacon Slices      +AED 2.00')
                        print('2-Add Cheese            +AED 2.00')
                        print('3-Add BBQ Sauce')
                        print('4-Add Swiss cheese      +AED 1.00')
                        print('5-Add Fiery Sauce       +AED 2.00')
                        print('6-Add Melted cheese     +AED 2.00')
                        print('7-Add Whopper patty     +AED 7.00')
                        print('8-Add Ketchup')
                        print('9-Add Mayo')
                        print('10-Add Mustard')
                        print('11-No Add-ons')
                        for i  in range(7):
                            add=int(input('Enter choice of Add on: '))
                            if add==1:
                                de+='Add Bacon slices'
                                t+=2
                            elif add==2:
                                de+='Add Cheese',
                                t+=2
                            elif add==3:
                                de+='Add BBQ sauce',
                            elif add==4:
                                de+='Add Swiss cheese',
                                t+=1
                            elif add==5:
                                de+='Add Fiery sauce',
                                t+=2
                            elif add==6:
                                de+='Add Melted cheese',
                                t+=2
                            elif add==7:
                                de+='Add Whopper patty',
                                t+=7
                            elif add==8:
                                de+='Add Ketchup',
                            elif add==9:
                                de+='Add Mayo',
                            elif add==10:
                                de+='Add Mustard',
                        print('Choice of side')
                        print('1-Spicy Tex Mex fries      +AED 11.00')
                        print('2-French fries small       +AED 5.00')
                        print('3-Onion Rings small        +AED 6.00')
                        print('4-Strip fries              +AED 10.00')
                        sid=int(input('Enter choice of sides: '))
                        if sid==1:
                            de+='Spicy Tex Mex fries'
                            t+=11
                        elif sid==2:
                            de+='French fries small'
                            t+=5
                        elif sid==3:
                            de+='Onion Rings small'
                            t+=6
                        elif sid==4:
                            de+='Strip fries'
                            t+=10
                        print('Choice of Drink')
                        print('1-Coke 500ml')
                        print('2-Fanta 500ml')
                        print('3-Sprite 500ml')
                        print('4-Coke Zero 500ml')
                        dri=int(input('Enter Choice of drink: '))
                        if dri==1:
                            s+='Coke 500ml',
                        elif dri==2:
                            s+='Fanta 500ml',
                        elif dri==3:
                            s+='Sprite 500ml',
                        elif dri==4:
                            s+='Coke Zero 500ml',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==4:
                        print('Big King')
                        print('AED 18.00')
                        t=18
                        de=['Big King']
                        print('Choice of Add-ons')
                        print('Choose 7 items')
                        print('1-Add Bacon Slices      +AED 2.00')
                        print('2-Add Cheese            +AED 2.00')
                        print('3-Add BBQ Sauce')
                        print('4-Add Swiss cheese      +AED 1.00')
                        print('5-Add Fiery Sauce       +AED 2.00')
                        print('6-Add Melted cheese     +AED 2.00')
                        print('7-Add Whopper patty     +AED 7.00')
                        print('8-Add Ketchup')
                        print('9-Add Mayo')
                        print('10-Add Mustard')
                        print('11-No Add-ons')
                        for i  in range(7):
                            add=int(input('Enter choice of Add on: '))
                            if add==1:
                                de+='Add Bacon slices'
                                t+=2
                            elif add==2:
                                de+='Add Cheese',
                                t+=2
                            elif add==3:
                                de+='Add BBQ sauce',
                            elif add==4:
                                de+='Add Swiss cheese',
                                t+=1
                            elif add==5:
                                de+='Add Fiery sauce',
                                t+=2
                            elif add==6:
                                de+='Add Melted cheese',
                                t+=2
                            elif add==7:
                                de+='Add Whopper patty',
                                t+=7
                            elif add==8:
                                de+='Add Ketchup',
                            elif add==9:
                                de+='Add Mayo',
                            elif add==10:
                                de+='Add Mustard',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==5:
                        print('Double Whopper')
                        print('AED 25.00')
                        t=15
                        de=['Double Whopper']
                        print('Choice of Add-ons')
                        print('Choose 7 items')
                        print('1-Add Bacon Slices      +AED 2.00')
                        print('2-Add Cheese            +AED 2.00')
                        print('3-Add BBQ Sauce')
                        print('4-Add Swiss cheese      +AED 1.00')
                        print('5-Add Fiery Sauce       +AED 2.00')
                        print('6-Add Melted cheese     +AED 2.00')
                        print('7-Add Whopper patty     +AED 7.00')
                        print('8-Add Ketchup')
                        print('9-Add Mayo')
                        print('10-Add Mustard')
                        print('11-No Add-ons')
                        for i  in range(7):
                            add=int(input('Enter choice of Add on: '))
                            if add==1:
                                de+='Add Bacon slices'
                                t+=2
                            elif add==2:
                                de+='Add Cheese',
                                t+=2
                            elif add==3:
                                de+='Add BBQ sauce',
                            elif add==4:
                                de+='Add Swiss cheese',
                                t+=1
                            elif add==5:
                                de+='Add Fiery sauce',
                                t+=2
                            elif add==6:
                                de+='Add Melted cheese',
                                t+=2
                            elif add==7:
                                de+='Add Whopper patty',
                                t+=7
                            elif add==8:
                                de+='Add Ketchup',
                            elif add==9:
                                de+='Add Mayo',
                            elif add==10:
                                de+='Add Mustard',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==6:
                        print('Fiery Chicken Fillet Sandwich')
                        print('AED 25.00')
                        t=25
                        de=['Fiery Chicken Fillet Sandwich']
                        print('Choice of Add-ons')
                        print('Choose 7 items')
                        print('1-Add Bacon Slices      +AED 2.00')
                        print('2-Add Cheese            +AED 2.00')
                        print('3-Add BBQ Sauce')
                        print('4-Add Swiss cheese      +AED 1.00')
                        print('5-Add Fiery Sauce       +AED 2.00')
                        print('6-Add Melted cheese     +AED 2.00')
                        print('7-Add Chicken patty     +AED 7.00')
                        print('8-Add Ketchup')
                        print('9-Add Mayo')
                        print('10-Add Mustard')
                        print('11-No Add-ons')
                        for i  in range(7):
                            add=int(input('Enter choice of Add on: '))
                            if add==1:
                                de+='Add Bacon slices'
                                t+=2
                            elif add==2:
                                de+='Add Cheese',
                                t+=2
                            elif add==3:
                                de+='Add BBQ sauce',
                            elif add==4:
                                de+='Add Swiss cheese',
                                t+=1
                            elif add==5:
                                de+='Add Fiery sauce',
                                t+=2
                            elif add==6:
                                de+='Add Melted cheese',
                                t+=2
                            elif add==7:
                                de+='Add Chicken patty',
                                t+=7
                            elif add==8:
                                de+='Add Ketchup',
                            elif add==9:
                                de+='Add Mayo',
                            elif add==10:
                                de+='Add Mustard',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==7:
                        print('Paneer King Meal')
                        print('AED 14.00')
                        t=14
                        de=['Paneer King Meal']
                        print('Choice of Add-ons')
                        print('Choose 7 items')
                        print('1-Add Bacon Slices      +AED 2.00')
                        print('2-Add Cheese            +AED 2.00')
                        print('3-Add BBQ Sauce')
                        print('4-Add Swiss cheese      +AED 1.00')
                        print('5-Add Fiery Sauce       +AED 2.00')
                        print('6-Add Melted cheese     +AED 2.00')
                        print('7-Add Ketchup')
                        print('8-Add Mayo')
                        print('9-Add Mustard')
                        print('10-No Add-ons')
                        for i  in range(7):
                            add=int(input('Enter choice of Add on: '))
                            if add==1:
                                de+='Add Bacon slices'
                                t+=2
                            elif add==2:
                                de+='Add Cheese',
                                t+=2
                            elif add==3:
                                de+='Add BBQ sauce',
                            elif add==4:
                                de+='Add Swiss cheese',
                                t+=1
                            elif add==5:
                                de+='Add Fiery sauce',
                                t+=2
                            elif add==6:
                                de+='Add Melted cheese',
                                t+=2
                            elif add==7:
                                de+='Add Ketchup',
                            elif add==8:
                                de+='Add Mayo',
                            elif add==9:
                                de+='Add Mustard',
                        print('Choice of side')
                        print('1-Spicy Tex Mex fries      +AED 11.00')
                        print('2-French fries small       +AED 5.00')
                        print('3-Onion Rings small        +AED 6.00')
                        print('4-Strip fries              +AED 10.00')
                        sid=int(input('Enter choice of sides: '))
                        if sid==1:
                            de+='Spicy Tex Mex fries'
                            t+=11
                        elif sid==2:
                            de+='French fries small'
                            t+=5
                        elif sid==3:
                            de+='Onion Rings small'
                            t+=6
                        elif sid==4:
                            de+='Strip fries'
                            t+=10
                        print('Choice of Drink')
                        print('1-Coke 500ml')
                        print('2-Fanta 500ml')
                        print('3-Sprite 500ml')
                        print('4-Coke Zero 500ml')
                        dri=int(input('Enter Choice of drink: '))
                        if dri==1:
                            s+='Coke 500ml',
                        elif dri==2:
                            s+='Fanta 500ml',
                        elif dri==3:
                            s+='Sprite 500ml',
                        elif dri==4:
                            s+='Coke Zero 500ml',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==8:
                        print('Chicken Fries 10 pcs')
                        print('AED 14.00')
                        t=14
                        de=['Chicken Fries 10 pcs']
                        print('Choice of sauce')
                        print('1-Garlic sauce')
                        print('2-Fiery sauce')
                        print('3-BBQ sauce')
                        print('4-No sauce')
                        sau=int(input('Enter choice: '))
                        if sau==1:
                            de+='Garlic sauce',
                        elif sau==2:
                            de+='Fiery sauce',
                        elif sau==3:
                            de+='BBQ sauce',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==9:
                        print('Spicy Tex Mex Fries')
                        print('AED 14.00')
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==10:
                        print('Crispy Chicken Tenders')
                        print('AED 13.00')
                        t=13
                        de=['Crispy Chicken Tenders']
                        print('Choice of sauce')
                        print('1-Garlic sauce')
                        print('2-Fiery sauce')
                        print('3-BBQ sauce')
                        print('4-No sauce')
                        sau=int(input('Enter choice: '))
                        if sau==1:
                            de+='Garlic sauce',
                        elif sau==2:
                            de+='Fiery sauce',
                        elif sau==3:
                            de+='BBQ sauce',
                        print('-'*50)
                        print(de,'\n Total Amount - AED',float(t))
                        print('-'*50)
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif burc==11:
                        y=True
                elif ch==5:
                    print('-'*50)
                    print("Hardee's")
                    print('Delivery within 40 mins')
                    print('Delivery fee - AED 8.00')
                    print('-'*50)
                    print('Menu:')
                    print('1-Frisco Chicken')
                    print('2-Big Boss')
                    print('3-Classic Angus Thickburger')
                    print('4-Steak Loader')
                    print('5-Super Star')
                    print('6-Chicken Santa Fe')
                    print('7-Chicken Tender Wrap BBQ')
                    print('8-Vegetarian Burger')
                    print('9-Loaded Fries')
                    print('10-Hand scooped Milkshake')
                    print('11-Go back to previous menu')
                    print('-'*50)
                    d=8
                    harc=int(input('Enter Choice: '))
                    if harc==1:
                        print('Frisco Chicken')
                        print('1-Combo          +AED 31.00')
                        print('2-Sandwich       +AED 19.00')
                        de=['Frisco Chicken']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 31.00')
                            t=31
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                        elif meal==2:
                            print('Sandwich -AED 19.00')
                            t=19
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==2:
                        print('Big Boss')
                        print('1-Combo          +AED 29.50')
                        print('2-Sandwich       +AED 19.00')
                        de=['Big Boss']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 29.50')
                            t=29.50
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                        elif meal==2:
                            print('Sandwich -AED 19.00')
                            t=19
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==3:
                        print('Classic Angus Thickburger')
                        print('1-Combo          +AED 35.00')
                        print('2-Sandwich       +AED 23.00')
                        de=['Classic Angus Thickburger']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 29.50')
                            t=29.50
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        elif meal==2:
                            print('Sandwich -AED 23.00')
                            t=23
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==4:
                        print('Steak Loader')
                        print('1-Combo          +AED 29.00')
                        print('2-Sandwich       +AED 19.00')
                        de=['Steak Loader']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 29.00')
                            t=29.00
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        elif meal==2:
                            print('Sandwich - AED 19.00')
                            t=19
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==5:
                        print('Super Star')
                        print('1-Combo          +AED 29.50')
                        print('2-Sandwich       +AED 19.00')
                        de=['Super Star']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 29.50')
                            t=29.50
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        elif meal==2:
                            print('Sandwich - AED 19.00')
                            t=19
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==6:
                        print('Chicken Santa Fe')
                        print('1-Combo          +AED 29.00')
                        print('2-Sandwich       +AED 18.00')
                        de=['Chicken Santa Fe']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 29.00')
                            t=29.00
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        elif meal==2:
                            print('Sandwich - AED 18.00')
                            t=18
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==7:
                        print('Chicken Tender Wrap BBQ')
                        print('1-Combo          +AED 21.00')
                        print('2-Sandwich       +AED 10.50')
                        de=['Chicken Tender Wrap BBQ']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 29.00')
                            t=29.00
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        elif meal==2:
                            print('Sandwich - AED 10.50')
                            t=10.50
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==8:
                        print('Vegetarian')
                        print('1-Combo          +AED 23.00')
                        print('2-Sandwich       +AED 12.00')
                        de=['Vegetarian']
                        meal=int(input('Enter choice: '))
                        if meal==1:
                            print('Combo - AED 23.00')
                            t=23
                            de+='Combo',
                            print('Choose Fries')
                            print('1-Spicy skin fries       +AED 1.00')
                            print('2-Skin on fries')
                            print('3-Spicy curly fries      +AED 2.00')
                            print('4-Curly fries            +AED 1.00')
                            fr=int(input('Enter choice of fries: '))
                            if fr==1:
                                de+='Spicy skin fries'
                                t+=1
                            elif fr==2:
                                de+='Skin on fries'
                            elif fr==3:
                                de+='Spicy curly fries'
                                t+=2
                            elif fr==4:
                                de+='Curly fries'
                                t+=1
                            print('Choose Drink')
                            print('1-Lotus Biscoff Hand-Scooped Ice cream Shake   +AED 5.00')
                            print('2-Pepsi')
                            print('3-Large Pepsi                                  +AED 1.00')
                            print('4-7UP')
                            print('5-Large 7UP                                    +AED 1.00')
                            print('6-Miranda')
                            print('7-Large Miranda                                +AED 1.00')
                            print('8-Mountain Dew')
                            print('9-Large Mountain Dew                           +AED 1.00')
                            print('10-Diet Pepsi')
                            print('11-Large Diet Pepsi                            +AED 1.00')
                            print('12-Water')
                            dri=int(input('Enter Choice: '))
                            if dri==1:
                                de+='Lotus Biscoff Hand-Scooped Ice cream Shake',
                                t+=5
                            elif dri==2:
                                de+='Pepsi',
                            elif dri==3:
                                de+='Large Pepsi',
                                t+=1
                            elif dri==4:
                                de+='7UP',
                            elif dri==5:
                                de+='Large 7UP',
                                t+=1
                            elif dri==6:
                                de+='Miranda',
                            elif dri==7:
                                de+='Large Miranda',
                                t+=1
                            elif dri==8:
                                de+='Mountain Dew',
                            elif dri==9:
                                de+='Large Mountain Dew',
                                t+=1
                            elif dri==10:
                                de+='Diet Pepsi',
                            elif dri==11:
                                de+='Large Diet Pepsi',
                                t+=1
                            elif dri==12:
                                de+='Water',
                            print('Choose Add-ons')
                            print('1-Cookie                              +AED 5.00')
                            print('2-Golden Chicken bites                +AED 5.50')
                            print('3-Cheese Burger Sandwich              +AED 5.00')
                            print('4-Original Chicken Tender             +AED 5.00')
                            print('5-Spicy Chicken Tender                +AED 5.00')
                            print('6-Spicy Chicken Tender Sandwich       +AED 5.00')
                            print('7-Original Chicken Tender Sandwich    +AED 5.00')
                            print('8-No add-ons')
                            add=int(input('Enter choice of Add-ons'))
                            if add==1:
                                de+='Cookie',
                                t+=5
                            elif add==2:
                                de+='Golden Chicken bites',
                                t+=5.50
                            elif add==3:
                                de+='Cheese Burger Sandwich',
                                t+=5
                            elif add==4:
                                de+='Original Chicken Tender',
                                t+=5
                            elif add==5:
                                de+='Spicy Chicken Tender',
                                t+=5
                            elif add==6:
                                de+='Spicy Chicken Tender Sandwich',
                                t+=5
                            elif add==7:
                                de+='Original Chicken Tender Sandwich',
                                t+=5
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        elif meal==2:
                            print('Sandwich - AED 12.00')
                            t=12
                            de+='Sandwich',
                            print('Choose Add ons')
                            print('Choose 3')
                            print('1-Jalepeno coins               +AED 2.00')
                            print('2-Philly Steak                 +AED 4.00')
                            print('3-Pepper Jack cheese           +AED 3.00')
                            print('4-Beef patty                   +AED 6.50')
                            print('5-Grilled Chicken Patty        +AED 7.00')
                            print('6-Cheddar Cheese               +AED 2.00')
                            print('7-Speical Sauce                +AED 2.00')
                            print('8-No Add ons')
                            for i in range(3):
                                add=int(input('Enter choice: '))
                                if add==1:
                                    de+='Jalepeno coins',
                                    t+=2
                                elif add==2:
                                    de+='Philly steak',
                                    t+=4
                                elif add==3:
                                    de+='Pepper Jack cheese',
                                    t+=3
                                elif add==4:
                                    de+='Beef Patty',
                                    t+=6.50
                                elif add==5:
                                    de+='Grilled Chicken Patty',
                                    t+=7
                                elif add==6:
                                    de+='Cheddar cheese',
                                    t+=2
                                elif add==7:
                                    de+='Special Sauce',
                                    t+=2
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==9:
                        print('Loaded Fries')
                        print('AED 12.50')
                        t=12.50
                        de=['Loaded Fries']
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==10:
                        print('Handscooped Milkshake')
                        print('AED 12.50')
                        print('Choice of flavour')
                        print('1-Chocolate')
                        print('2-Strawberry')
                        print('3-Vanilla')
                        fla=int(input('Enter Choice: '))
                        if fla==1:
                            de+='Chocolate',
                        elif fla==2:
                            de+='Strawberry',
                        elif fla==3:
                            de+='Vanilla',
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif harc==11:
                        y=True
                elif ch==6:
                    print('-'*50)
                    print('India Palace')
                    print('Delivery within 35 mins')
                    print('Delivery fee - 5.00')
                    print('-'*50)
                    print('Menu:')
                    print('1-Butter Chicken')
                    print('2-Hyderabad Masala Biryani Chicken')
                    print('3-Jhinga Dum Ki Biryani')
                    print('4-Murg E Tandoori')
                    print('5-Raan')
                    print('6-Saundhi Fish Tikka')
                    print('7-Paneer Tikka Masala')
                    print('8-Kadai Mutton')
                    print('9-Bread Basket')
                    print('10-Shahi Tukda')
                    print('11-Go back to previous menu')
                    print('-'*50)
                    d=5
                    inc=int(input('Enter choice'))
                    if inc==1:
                        print('Butter Chicken')
                        print('AED 42.00')
                        t=42
                        de=['Butter Chicken']
                        print('Choice of Add-ons')
                        print('1-Biryani Rice')
                        print('2-Biryani rice with sauce')
                        print('3-Roomali Roti')
                        print('4-Roti Tandoori')
                        print('5-Pudina Paratha')
                        print('6-Lachedar Paratha')
                        print('7-Lasooni Naan')
                        print('8-Makhani Butter Naan')
                        print('9-Naan')
                        print('10-Bharwan Cheese Kulcha')
                        print('11-No Add on')
                        add=int(input('Enter choice: '))
                        if add==1:
                            de+='Biryani Rice',
                            t+=27
                        elif add==2:
                            de+='Biryani Rice with sauce',
                            t+=27
                        elif add==3:
                            de+='Roomali Roti',
                            t+=8
                        elif add==4:
                            de+='Roti Tandoori',
                            t+=6
                        elif add==5:
                            de+='Pudhina Paratha',
                            t+=10
                        elif add==6:
                            de+='Lachedar Paratha',
                            t+=8
                        elif add==7:
                            de+='Lasooni Naan',
                            t+=9
                        elif add==8:
                            de+='Makhani Butter Naan',
                            t+=8
                        elif add==9:
                            de+='Naan',
                            t+=7
                        elif add==10:
                            de+='Bharwan Cheese Kulcha',
                            t+=16
                        print('Choice of Add-on Salad')
                        print('1-Boondi Raita')
                        print('2-Cucumber Raita')
                        print('3-Mixed Raita')
                        print('4-Masala Papad')
                        print('5-No add ons')
                        sadd=int(input('Enter choice: '))
                        if sadd==1:
                            de+='Boondhi Raita',
                            t+=14
                        elif sadd==2:
                            de+='Cucumber Raita',
                            t+=14
                        elif sadd==3:
                            de+='Mixed Raita',
                            t+=14
                        elif sadd==4:
                            de+='Masala Papad',
                            t+=14
                        print('Choice of Add-ons Dessert')
                        print('1-Kesar Kulfi')
                        print('2-Gulab Jamun')
                        print('3-Rasmalai')
                        print('4-Shahi Tukda')
                        print('5-Shahi Brownie')
                        print('6-No add-ons')
                        dadd=int(input('Enter Choice'))
                        if dadd==1:
                            de+='Kesar Kulfi',
                            t+=19
                        elif dadd==2:
                            de+='Gulab Jamun',
                            t+=19
                        elif dadd==3:
                            de+='Rasmalai',
                            t+=19
                        elif dadd==4:
                            de+='Shahi Tukda',
                            t+=19
                        elif dadd==5:
                            de+='Shahi Brownie',
                            t+=28
                        print('Choice of Drinks')
                        print('1-Coca-Cola')
                        print('2-Sprite')
                        print('3-Fanta')
                        print('4-Plain Lassi')
                        print('5-Saffron Lassi')
                        print('6-Mango Lassi')
                        print('7-Strawberry Lassi')
                        print('8-Masala Chaas')
                        print('9-Mint Cooler')
                        print('10-No add-ons')
                        dri=int(input('Enter Choice: '))
                        if dri==1:
                            de+='Coca-Cola',
                            t+=6
                        elif dri==2:
                            de+='Sprite',
                            t+=6
                        elif dri==3:
                            de+='Fanta',
                            t+=6
                        elif dri==4:
                            de+='Plain Lassi',
                            t+=18
                        elif dri==5:
                            de+='Saffron Lassi',
                            t+=24
                        elif dri==6:
                            de+='Mango Lassi',
                            t+=20
                        elif dri==7:
                            de+='Strawberry Lassi',
                            t+=22
                        elif dri==8:
                            de+='Masala Chaas',
                            t+=18
                        elif dri==9:
                            de+='Mint Cooler',
                            t+=15
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==2:
                        print('Hyderabad Masala Biryani Chicken')
                        print('AED 42.00')
                        t=42
                        de=['Hyderabad Masala Biryani Chicken']
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==3:
                        print('Jhinga Dum Ki Biryani')
                        print('AED 68.00')
                        t=68
                        de=['Jhinga Dum Ki Biryani']
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==4:
                        print('Murg E Tandoori')
                        de=['Murg E Tandoori']
                        print('1-Half      +AED 29.00')
                        print('2-Whole     +AED 54.00')
                        siz=int(input('Enter Choice: '))
                        if siz==1:
                            t=29
                            de+='Half',
                        elif siz==2:
                            t=54
                            de+='Whole',
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==5:
                        print('Raan')
                        print('AED 120.00')
                        t=120
                        de=['Raan']
                        print('Choice of Add-ons')
                        print('1-Biryani Rice')
                        print('2-Biryani rice with sauce')
                        print('3-Roomali Roti')
                        print('4-Roti Tandoori')
                        print('5-Pudina Paratha')
                        print('6-Lachedar Paratha')
                        print('7-Lasooni Naan')
                        print('8-Makhani Butter Naan')
                        print('9-Naan')
                        print('10-Bharwan Cheese Kulcha')
                        print('11-No Add on')
                        add=int(input('Enter choice: '))
                        if add==1:
                            de+='Biryani Rice',
                            t+=27
                        elif add==2:
                            de+='Biryani Rice with sauce',
                            t+=27
                        elif add==3:
                            de+='Roomali Roti',
                            t+=8
                        elif add==4:
                            de+='Roti Tandoori',
                            t+=6
                        elif add==5:
                            de+='Pudhina Paratha',
                            t+=10
                        elif add==6:
                            de+='Lachedar Paratha',
                            t+=8
                        elif add==7:
                            de+='Lasooni Naan',
                            t+=9
                        elif add==8:
                            de+='Makhani Butter Naan',
                            t+=8
                        elif add==9:
                            de+='Naan',
                            t+=7
                        elif add==10:
                            de+='Bharwan Cheese Kulcha',
                            t+=16
                        print('Choice of Add-on Salad')
                        print('1-Boondi Raita')
                        print('2-Cucumber Raita')
                        print('3-Mixed Raita')
                        print('4-Masala Papad')
                        print('5-No add ons')
                        sadd=int(input('Enter choice: '))
                        if sadd==1:
                            de+='Boondhi Raita',
                            t+=14
                        elif sadd==2:
                            de+='Cucumber Raita',
                            t+=14
                        elif sadd==3:
                            de+='Mixed Raita',
                            t+=14
                        elif sadd==4:
                            de+='Masala Papad',
                            t+=14
                        print('Choice of Add-ons Dessert')
                        print('1-Kesar Kulfi')
                        print('2-Gulab Jamun')
                        print('3-Rasmalai')
                        print('4-Shahi Tukda')
                        print('5-Shahi Brownie')
                        print('6-No add-ons')
                        dadd=int(input('Enter Choice'))
                        if dadd==1:
                            de+='Kesar Kulfi',
                            t+=19
                        elif dadd==2:
                            de+='Gulab Jamun',
                            t+=19
                        elif dadd==3:
                            de+='Rasmalai',
                            t+=19
                        elif dadd==4:
                            de+='Shahi Tukda',
                            t+=19
                        elif dadd==5:
                            de+='Shahi Brownie',
                            t+=28
                        print('Choice of Drinks')
                        print('1-Coca-Cola')
                        print('2-Sprite')
                        print('3-Fanta')
                        print('4-Plain Lassi')
                        print('5-Saffron Lassi')
                        print('6-Mango Lassi')
                        print('7-Strawberry Lassi')
                        print('8-Masala Chaas')
                        print('9-Mint Cooler')
                        print('10-No add-ons')
                        dri=int(input('Enter Choice: '))
                        if dri==1:
                            de+='Coca-Cola',
                            t+=6
                        elif dri==2:
                            de+='Sprite',
                            t+=6
                        elif dri==3:
                            de+='Fanta',
                            t+=6
                        elif dri==4:
                            de+='Plain Lassi',
                            t+=18
                        elif dri==5:
                            de+='Saffron Lassi',
                            t+=24
                        elif dri==6:
                            de+='Mango Lassi',
                            t+=20
                        elif dri==7:
                            de+='Strawberry Lassi',
                            t+=22
                        elif dri==8:
                            de+='Masala Chaas',
                            t+=18
                        elif dri==9:
                            de+='Mint Cooler',
                            t+=15
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==6:
                        print('Saundhi Fish Tikka')
                        print('AED 48.00')
                        t=48
                        de=['Saundhi Fish Tikka']
                        print('Choice of Add-ons')
                        print('1-Biryani Rice')
                        print('2-Biryani rice with sauce')
                        print('3-Roomali Roti')
                        print('4-Roti Tandoori')
                        print('5-Pudina Paratha')
                        print('6-Lachedar Paratha')
                        print('7-Lasooni Naan')
                        print('8-Makhani Butter Naan')
                        print('9-Naan')
                        print('10-Bharwan Cheese Kulcha')
                        print('11-No Add on')
                        add=int(input('Enter choice: '))
                        if add==1:
                            de+='Biryani Rice',
                            t+=27
                        elif add==2:
                            de+='Biryani Rice with sauce',
                            t+=27
                        elif add==3:
                            de+='Roomali Roti',
                            t+=8
                        elif add==4:
                            de+='Roti Tandoori',
                            t+=6
                        elif add==5:
                            de+='Pudhina Paratha',
                            t+=10
                        elif add==6:
                            de+='Lachedar Paratha',
                            t+=8
                        elif add==7:
                            de+='Lasooni Naan',
                            t+=9
                        elif add==8:
                            de+='Makhani Butter Naan',
                            t+=8
                        elif add==9:
                            de+='Naan',
                            t+=7
                        elif add==10:
                            de+='Bharwan Cheese Kulcha',
                            t+=16
                        print('Choice of Add-on Salad')
                        print('1-Boondi Raita')
                        print('2-Cucumber Raita')
                        print('3-Mixed Raita')
                        print('4-Masala Papad')
                        print('5-No add ons')
                        sadd=int(input('Enter choice: '))
                        if sadd==1:
                            de+='Boondhi Raita',
                            t+=14
                        elif sadd==2:
                            de+='Cucumber Raita',
                            t+=14
                        elif sadd==3:
                            de+='Mixed Raita',
                            t+=14
                        elif sadd==4:
                            de+='Masala Papad',
                            t+=14
                        print('Choice of Add-ons Dessert')
                        print('1-Kesar Kulfi')
                        print('2-Gulab Jamun')
                        print('3-Rasmalai')
                        print('4-Shahi Tukda')
                        print('5-Shahi Brownie')
                        print('6-No add-ons')
                        dadd=int(input('Enter Choice'))
                        if dadd==1:
                            de+='Kesar Kulfi',
                            t+=19
                        elif dadd==2:
                            de+='Gulab Jamun',
                            t+=19
                        elif dadd==3:
                            de+='Rasmalai',
                            t+=19
                        elif dadd==4:
                            de+='Shahi Tukda',
                            t+=19
                        elif dadd==5:
                            de+='Shahi Brownie',
                            t+=28
                        print('Choice of Drinks')
                        print('1-Coca-Cola')
                        print('2-Sprite')
                        print('3-Fanta')
                        print('4-Plain Lassi')
                        print('5-Saffron Lassi')
                        print('6-Mango Lassi')
                        print('7-Strawberry Lassi')
                        print('8-Masala Chaas')
                        print('9-Mint Cooler')
                        print('10-No add-ons')
                        dri=int(input('Enter Choice: '))
                        if dri==1:
                            de+='Coca-Cola',
                            t+=6
                        elif dri==2:
                            de+='Sprite',
                            t+=6
                        elif dri==3:
                            de+='Fanta',
                            t+=6
                        elif dri==4:
                            de+='Plain Lassi',
                            t+=18
                        elif dri==5:
                            de+='Saffron Lassi',
                            t+=24
                        elif dri==6:
                            de+='Mango Lassi',
                            t+=20
                        elif dri==7:
                            de+='Strawberry Lassi',
                            t+=22
                        elif dri==8:
                            de+='Masala Chaas',
                            t+=18
                        elif dri==9:
                            de+='Mint Cooler',
                            t+=15
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==7:
                        print('Paneer Tikka Masala')
                        print('AED 38.00')
                        t=38
                        de=['Paneer Tikka Masala']
                        print('Choice of Add-ons')
                        print('1-Biryani Rice')
                        print('2-Biryani rice with sauce')
                        print('3-Roomali Roti')
                        print('4-Roti Tandoori')
                        print('5-Pudina Paratha')
                        print('6-Lachedar Paratha')
                        print('7-Lasooni Naan')
                        print('8-Makhani Butter Naan')
                        print('9-Naan')
                        print('10-Bharwan Cheese Kulcha')
                        print('11-No Add on')
                        add=int(input('Enter choice: '))
                        if add==1:
                            de+='Biryani Rice',
                            t+=27
                        elif add==2:
                            de+='Biryani Rice with sauce',
                            t+=27
                        elif add==3:
                            de+='Roomali Roti',
                            t+=8
                        elif add==4:
                            de+='Roti Tandoori',
                            t+=6
                        elif add==5:
                            de+='Pudhina Paratha',
                            t+=10
                        elif add==6:
                            de+='Lachedar Paratha',
                            t+=8
                        elif add==7:
                            de+='Lasooni Naan',
                            t+=9
                        elif add==8:
                            de+='Makhani Butter Naan',
                            t+=8
                        elif add==9:
                            de+='Naan',
                            t+=7
                        elif add==10:
                            de+='Bharwan Cheese Kulcha',
                            t+=16
                        print('Choice of Add-on Salad')
                        print('1-Boondi Raita')
                        print('2-Cucumber Raita')
                        print('3-Mixed Raita')
                        print('4-Masala Papad')
                        print('5-No add ons')
                        sadd=int(input('Enter choice: '))
                        if sadd==1:
                            de+='Boondhi Raita',
                            t+=14
                        elif sadd==2:
                            de+='Cucumber Raita',
                            t+=14
                        elif sadd==3:
                            de+='Mixed Raita',
                            t+=14
                        elif sadd==4:
                            de+='Masala Papad',
                            t+=14
                        print('Choice of Add-ons Dessert')
                        print('1-Kesar Kulfi')
                        print('2-Gulab Jamun')
                        print('3-Rasmalai')
                        print('4-Shahi Tukda')
                        print('5-Shahi Brownie')
                        print('6-No add-ons')
                        dadd=int(input('Enter Choice'))
                        if dadd==1:
                            de+='Kesar Kulfi',
                            t+=19
                        elif dadd==2:
                            de+='Gulab Jamun',
                            t+=19
                        elif dadd==3:
                            de+='Rasmalai',
                            t+=19
                        elif dadd==4:
                            de+='Shahi Tukda',
                            t+=19
                        elif dadd==5:
                            de+='Shahi Brownie',
                            t+=28
                        print('Choice of Drinks')
                        print('1-Coca-Cola')
                        print('2-Sprite')
                        print('3-Fanta')
                        print('4-Plain Lassi')
                        print('5-Saffron Lassi')
                        print('6-Mango Lassi')
                        print('7-Strawberry Lassi')
                        print('8-Masala Chaas')
                        print('9-Mint Cooler')
                        print('10-No add-ons')
                        dri=int(input('Enter Choice: '))
                        if dri==1:
                            de+='Coca-Cola',
                            t+=6
                        elif dri==2:
                            de+='Sprite',
                            t+=6
                        elif dri==3:
                            de+='Fanta',
                            t+=6
                        elif dri==4:
                            de+='Plain Lassi',
                            t+=18
                        elif dri==5:
                            de+='Saffron Lassi',
                            t+=24
                        elif dri==6:
                            de+='Mango Lassi',
                            t+=20
                        elif dri==7:
                            de+='Strawberry Lassi',
                            t+=22
                        elif dri==8:
                            de+='Masala Chaas',
                            t+=18
                        elif dri==9:
                            de+='Mint Cooler',
                            t+=15
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==8:
                        print('Kadai Mutton')
                        print('AED 40.00')
                        t=40
                        de=['Kadai Mutton']
                        print('Choice of Add-ons')
                        print('1-Biryani Rice')
                        print('2-Biryani rice with sauce')
                        print('3-Roomali Roti')
                        print('4-Roti Tandoori')
                        print('5-Pudina Paratha')
                        print('6-Lachedar Paratha')
                        print('7-Lasooni Naan')
                        print('8-Makhani Butter Naan')
                        print('9-Naan')
                        print('10-Bharwan Cheese Kulcha')
                        print('11-No Add on')
                        add=int(input('Enter choice: '))
                        if add==1:
                            de+='Biryani Rice',
                            t+=27
                        elif add==2:
                            de+='Biryani Rice with sauce',
                            t+=27
                        elif add==3:
                            de+='Roomali Roti',
                            t+=8
                        elif add==4:
                            de+='Roti Tandoori',
                            t+=6
                        elif add==5:
                            de+='Pudhina Paratha',
                            t+=10
                        elif add==6:
                            de+='Lachedar Paratha',
                            t+=8
                        elif add==7:
                            de+='Lasooni Naan',
                            t+=9
                        elif add==8:
                            de+='Makhani Butter Naan',
                            t+=8
                        elif add==9:
                            de+='Naan',
                            t+=7
                        elif add==10:
                            de+='Bharwan Cheese Kulcha',
                            t+=16
                        print('Choice of Add-on Salad')
                        print('1-Boondi Raita')
                        print('2-Cucumber Raita')
                        print('3-Mixed Raita')
                        print('4-Masala Papad')
                        print('5-No add ons')
                        sadd=int(input('Enter choice: '))
                        if sadd==1:
                            de+='Boondhi Raita',
                            t+=14
                        elif sadd==2:
                            de+='Cucumber Raita',
                            t+=14
                        elif sadd==3:
                            de+='Mixed Raita',
                            t+=14
                        elif sadd==4:
                            de+='Masala Papad',
                            t+=14
                        print('Choice of Add-ons Dessert')
                        print('1-Kesar Kulfi')
                        print('2-Gulab Jamun')
                        print('3-Rasmalai')
                        print('4-Shahi Tukda')
                        print('5-Shahi Brownie')
                        print('6-No add-ons')
                        dadd=int(input('Enter Choice'))
                        if dadd==1:
                            de+='Kesar Kulfi',
                            t+=19
                        elif dadd==2:
                            de+='Gulab Jamun',
                            t+=19
                        elif dadd==3:
                            de+='Rasmalai',
                            t+=19
                        elif dadd==4:
                            de+='Shahi Tukda',
                            t+=19
                        elif dadd==5:
                            de+='Shahi Brownie',
                            t+=28
                        print('Choice of Drinks')
                        print('1-Coca-Cola')
                        print('2-Sprite')
                        print('3-Fanta')
                        print('4-Plain Lassi')
                        print('5-Saffron Lassi')
                        print('6-Mango Lassi')
                        print('7-Strawberry Lassi')
                        print('8-Masala Chaas')
                        print('9-Mint Cooler')
                        print('10-No add-ons')
                        dri=int(input('Enter Choice: '))
                        if dri==1:
                            de+='Coca-Cola',
                            t+=6
                        elif dri==2:
                            de+='Sprite',
                            t+=6
                        elif dri==3:
                            de+='Fanta',
                            t+=6
                        elif dri==4:
                            de+='Plain Lassi',
                            t+=18
                        elif dri==5:
                            de+='Saffron Lassi',
                            t+=24
                        elif dri==6:
                            de+='Mango Lassi',
                            t+=20
                        elif dri==7:
                            de+='Strawberry Lassi',
                            t+=22
                        elif dri==8:
                            de+='Masala Chaas',
                            t+=18
                        elif dri==9:
                            de+='Mint Cooler',
                            t+=15
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==9:
                        print('Bread Basket')
                        print('AED 26.00')
                        t=26
                        de=['Bread Basket']
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==10:
                        print('Shahi Tukda')
                        print('AED 19.00')
                        t=19
                        de=['Shahi Tukda']
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif inc==11:
                        y=True
                elif ch==7:
                    print('-'*50)
                    print("Papa John's")
                    print('Delivery within 33 mins')
                    print('Delivery fee - AED 7.00')
                    print('-'*50)
                    print('Menu:')
                    print("1-Papa's Chicken Poppers")
                    print('2-Chicken Wings')
                    print('3-Cheddar Cheeseburger Papadia')
                    print('4-All the Meats')
                    print('5-Garden Special')
                    print('6-Hot and Spicy')
                    print('7-Spicy Chicken Ranch')
                    print("8-Papa's Club Salad")
                    print("9-Papa's House Pasta")
                    print('10-Chocolate Scrolls')
                    print('11-Go back to previous menu')
                    print('-'*50)
                    d=7
                    pac=int(input('Enter choice: '))
                    if pac==1:
                        print("Papa's Chicken Poppers")
                        print('AED 25.00')
                        de=["Papa's Chicken Poppers"]
                        t=25
                        print('Choice of Sauce')
                        print('1-Buffalo Sauce')
                        print('2-Ranch Sauce')
                        print('3-BBQ Sauce')
                        print('4-Pizza Sauce')
                        print('5-Garlic Sauce')
                        print('6-No Sauce')
                        sau=int(input('Enter choice: '))
                        if sau==1:
                            de+='Buffalo Sauce',
                        elif sau==2:
                            de+='Ranch Sauce',
                        elif sau==3:
                            de+='BBQ Sauce',
                        elif sau==4:
                            de+='Pizza Sauce',
                        elif sau==5:
                            de+='Garlic Sauce',
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==2:
                        print('Chicken Wings')
                        print('AED 26.00')
                        de=['Chicken Wings']
                        t=26
                        print('Choice of Sauce')
                        print('1-Buffalo Sauce')
                        print('2-Ranch Sauce')
                        print('3-BBQ Sauce')
                        print('4-Pizza Sauce')
                        print('5-Garlic Sauce')
                        print('6-No Sauce')
                        sau=int(input('Enter choice: '))
                        if sau==1:
                            de+='Buffalo Sauce',
                        elif sau==2:
                            de+='Ranch Sauce',
                        elif sau==3:
                            de+='BBQ Sauce',
                        elif sau==4:
                            de+='Pizza Sauce',
                        elif sau==5:
                            de+='Garlic Sauce',
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==3:
                        print('Cheddar Cheeseburger Papadia')
                        print('AED 29.00')
                        de=['Cheddar Cheeseburger Papadia']
                        t=29
                        print('Choice of Sauce')
                        print('1-Buffalo Sauce')
                        print('2-Ranch Sauce')
                        print('3-BBQ Sauce')
                        print('4-Pizza Sauce')
                        print('5-Garlic Sauce')
                        print('6-No Sauce')
                        sau=int(input('Enter choice: '))
                        if sau==1:
                            de+='Buffalo Sauce',
                        elif sau==2:
                            de+='Ranch Sauce',
                        elif sau==3:
                            de+='BBQ Sauce',
                        elif sau==4:
                            de+='Pizza Sauce',
                        elif sau==5:
                            de+='Garlic Sauce',
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==4:
                        print('All the Meats')
                        print('1-Small    +AED 29.00')
                        print('2-Medium   +AED 44.00')
                        print('3-Large    +AED 61.00')
                        de=['All the Meats']
                        siz=int(input('Enter Choice: '))
                        if siz==1:
                            de+='Small',
                            t=29
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 4.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 2.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=4
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=2
                            print('Add Pizza toppings')
                            print('1-Beef                        +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif siz==2:
                            de+='Medium',
                            t=44
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 8.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 5.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=8
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=5
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif siz==3:
                            de+='Large',
                            t=61
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==5:
                        print('Garden Special')
                        print('1-Small    +AED 29.00')
                        print('2-Medium   +AED 44.00')
                        print('3-Large    +AED 61.00')
                        de=['Garden Special']
                        siz=int(input('Enter Choice: '))
                        if siz==1:
                            de+='Small',
                            t=29
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 4.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 2.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=4
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=2
                            print('Add Pizza toppings')
                            print('1-Beef                        +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif siz==2:
                            de+='Medium',
                            t=44
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 8.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 5.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=8
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=5
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif siz==3:
                            de+='Large',
                            t=61
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==6:
                        print('Hot and spicy')
                        print('1-Small    +AED 29.00')
                        print('2-Medium   +AED 44.00')
                        print('3-Large    +AED 61.00')
                        de=['Hot and spicy']
                        siz=int(input('Enter Choice: '))
                        if siz==1:
                            de+='Small',
                            t=29
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 4.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 2.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=4
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=2
                            print('Add Pizza toppings')
                            print('1-Beef                        +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif siz==2:
                            de+='Medium',
                            t=44
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 8.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 5.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=8
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=5
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif siz==3:
                            de+='Large',
                            t=61
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==7:
                        print('Spicy Chicken Ranch')
                        print('1-Small    +AED 29.00')
                        print('2-Medium   +AED 44.00')
                        print('3-Large    +AED 61.00')
                        de=['Spicy Chicken Ranch']
                        siz=int(input('Enter Choice: '))
                        if siz==1:
                            de+='Small',
                            t=29
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 4.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 2.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=4
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=2
                            print('Add Pizza toppings')
                            print('1-Beef                        +AED 3.50')
                            print('2-Sliced Black Olives         +AED 3.50')
                            print('3-Green Chilies               +AED 3.50')
                            print('4-Shrimps                     +AED 3.50')
                            print('5-Fresh Tomatoes              +AED 3.50')
                            print('6-Mozerlla                    +AED 3.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=3.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=3.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=3.50
                            elif add==4:
                                de+='Shrimps',
                                t+=3.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=3.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=3.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 1.00')
                            print('2-Cool Ranch            +AED 1.00')
                            print('3-Fiery peri peri       +AED 1.00')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=1
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=1
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=1
                        elif siz==2:
                            de+='Medium',
                            t=44
                            print('Choose Crust')
                            print('1-Thin crust')
                            print('2-Stuffed Crust            +AED 8.00')
                            print("3-Original Crust")
                            print('4-Garlic Parmesan Crust    +AED 5.00')
                            dough=int(input('Enter choice: '))
                            if dough==1:
                                de+='Thin Crust',
                            elif dough==2:
                                de+='Stuffed Crust',
                                t+=8
                            elif dough==3:
                                de+="Original Crust",
                            elif dough==4:
                                de+='Garlic Parmesan Crust',
                                t+=5
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 4.50')
                            print('2-Sliced Black Olives         +AED 4.50')
                            print('3-Green Chilies               +AED 4.50')
                            print('4-Shrimps                     +AED 4.50')
                            print('5-Fresh Tomatoes              +AED 4.50')
                            print('6-Mozerlla                    +AED 4.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=4.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=4.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=4.50
                            elif add==4:
                                de+='Shrimps',
                                t+=4.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=4.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=4.50
                            print('Choose Drizzle')
                            print('1-Bold BBQ              +AED 2.50')
                            print('2-Cool Ranch            +AED 2.50')
                            print('3-Fiery peri peri       +AED 2.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=2.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=2.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=2.50
                        elif siz==3:
                            de+='Large',
                            t=61
                            print('Add Pizza toppings')
                            print('1-Ground Beef                 +AED 5.50')
                            print('2-Sliced Black Olives         +AED 5.50')
                            print('3-Green Chilies               +AED 5.50')
                            print('4-Shrimps                     +AED 5.50')
                            print('5-Fresh Tomatoes              +AED 5.50')
                            print('6-Mozerlla                    +AED 5.50')
                            print('7-No add ons')
                            add=int(input('Enter choice of add-ons: '))
                            if add==1:
                                de+='Ground Beef',
                                t+=5.50
                            elif add==2:
                                de+='Sliced Black Olives',
                                t+=5.50
                            elif add==3:
                                de+='Green Chilies',
                                t+=5.50
                            elif add==4:
                                de+='Shrimps',
                                t+=5.50
                            elif add==5:
                                de+='Fresh Tomatoes',
                                t+=5.50
                            elif add==6:
                                de+='Mozerlla',
                                t+=5.50
                            print('1-Bold BBQ              +AED 3.50')
                            print('2-Cool Ranch            +AED 3.50')
                            print('3-Fiery peri peri       +AED 3.50')
                            print('4-No Drizzle')
                            dr=int(input('Enter Choice of Drizzle: '))
                            if dr==1:
                                de+='Bold BBQ',
                                t+=3.50
                            elif dr==2:
                                de+='Cool Ranch',
                                t+=3.50
                            elif dr==3:
                                de+='Fiery peri peri',
                                t+=3.50
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==8:
                        print("Papa's Club Salad")
                        print('AED 24.00')
                        de=["Papa's Club Salad"]
                        t=24
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==9:
                        print("Papa's House Pasta")
                        print('AED 24.00')
                        de=["Papa's House Pasta"]
                        t=24
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==10:
                        print('Chocolate Scrolls')
                        print('AED 15.00')
                        de=['Chocolate Scrolls']
                        t=15
                        print(de,'\n Total Amount - AED',float(t))
                        cart=input('Add to cart?')
                        if cart=='yes' or cart=='Yes':
                            noi+=1
                            total+=t
                            p='AED '+str(float(t))
                            de+=p,
                            loi+=de,
                            print('Shopping cart: ',loi)
                    elif pac==11:
                        y=True
                elif ch==8:
                    x=False
                if loi!=[]:
                        chk=input('Do you wish to proceed to check out? ')
                        if chk=='yes' or chk=='Yes':
                            print('-'*50)
                            print('Shopping Cart:',loi)
                            print('Subtotal:','AED '+str(float(total)))
                            print('Delivery fee: ','AED '+str(float(d)))
                            print('-'*50)
                            total+=d
                            a=input('Enter Delivery Address: ')
                            b=input('Enter Building details: \n(eg:Building Name,Flat no.)')
                            print(a,b)
                            print('-'*50)
                            print('Total:','AED '+str(float(total)))
                            print('Payment method')
                            print('1-COD')
                            print('2-Card')
                            pay=int(input('Enter choice: '))
                            if pay==2:
                                print('1-ADCB       5% Discount')
                                print('2-RAK        7% Discount')
                                print('3-FAB')
                                print('4-HSBC       10% Discount')
                                print('5-Other')
                                car=int(input('Enter choice: '))
                                if car==1:
                                    total=((95/100)*total)
                                    print('Total: ',total)
                                elif car==2:
                                    total=((93/100)*total)
                                    print('Total: ',total)
                                elif car==4:
                                    total=((90/100)*total)
                                    print('Total: ',total)
                                cn=input('Enter Card Number: ')
                                ce=input('Enter Expiry Date: ')
                                cvv=input('Enter CVV: ')
                            ord=input('Place Order? ')
                            if ord=='yes' or ord=='Yes':
                                print('-'*50)
                                print('Order has been placed!')
                                point=0
                                if total>=100:
                                    points+=20
                                print('Total Number of points: ',point)
                                print('Thank you for choosing Talabat')
                                print('-'*50)
                                x=True
                                break
elif mode=='Admin' or mode=='admin':
    while r==False:
        print('%50s'%'LOGIN')
        name=input('Enter username: ')
        pw=input('Enter password: ')
        lmem=list(m.values())
        for i in range(len(lmem)):
            if name==lmem[i][0] and pw==lmem[i][2]:
                r=True
                print('LOGIN SUCCESSFUL')
        if r==False:
            print('USER NOT FOUND')
    if r==True:
        print('1-User Details')
        print('2-Add Item')
        print('3-Delete Item')
        print('4-Modify prices')
        ad=int(input('Enter choice: '))
        if ad==1:
            print(m)
