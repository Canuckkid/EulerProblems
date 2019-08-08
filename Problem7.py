def prime (num):
        count = 0
        test = 2
        while count < num:
                prime = True
                for i in range(2, test):
                        if test % i == 0:
                                prime = False
                                break
                
                if prime == True:
                        count = count + 1

                if count == num :
                        return test

                test = test + 1
                
                        

