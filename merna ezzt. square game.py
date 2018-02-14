coin1=int(input("enter all coin:  "))
while coin1 !=0:
    x=int(input("player_1 enter num of coin (4,9,,16,25,..... ) :"))
    if x<coin1:
        coin=coin1-x
        if coin==0:
            print ("playrer_1  is winer  :")
        else:
            y=int(input("player_2 enter num of coins(4,9,16,......):"))
            if y<coin1 :
                coin=coin-y
                if coin==0:
                    print("player_2 is winer  ")
            else:
                
                
                print("error num of coins > expected")

    else :
        print("error num of coins > expected  ")
    
        
