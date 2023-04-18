import random 

## Random

lenpassword = int(input('pls send password length : ')) ;
#typepassword = int(input('pls send type : 1-hard 2-normal 3-esay ')) ;
typepassword = 1 ;
if typepassword == 1 : 
    all_charckters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','$','@','%'] ;
    def PassWordMaker (lengh): 
        i = 0;
        password = '';
        while i < lengh : 
            newpass = random.choice(all_charckters) ; 
            password = password + newpass;
            i = i + 1; 
        return password ; 
    
    newpass = PassWordMaker(lenpassword);
    print('your password is : %s' % newpass );
    
