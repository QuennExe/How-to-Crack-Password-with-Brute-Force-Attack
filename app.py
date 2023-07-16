# HOW TO BREAK PASSWORD WITH PYTHON BRUTE FORCE ATTACK?
#1 - CREATING PASSWORD

passwd = "415263"
flag = False
numbers = '0123456789'

for step1 in numbers:
    for step2 in numbers:
        for step3 in numbers:
            for step4 in numbers:
                for step5 in numbers:
                    for step6 in numbers:
                        attempt = step1 + step2 + step3 + step4 + step5 + step6
                        print(attempt)
                        if attempt == passwd:
                            print("Your Password: " + attempt)
                            flag = True
                            break
                    if flag == True:
                        break
                if flag == True:
                    break
            if flag == True:
                break
        if flag == True:
            break
    if flag == True:
        break
        
    
                          