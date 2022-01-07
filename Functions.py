import sys,time


######################
#### Functions #######
######################

# Function slow text & validation
class Functions:
    def sprint(str):
        for c in str + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(3./90)


    def validation(self):
        test = input().lower()
        if test == '1':
            return True
        elif test == '2':
            return False
        else:
            print('your quest cannot continue without your correct input')
            print('please choose 1 or 2 ')
            return self.validation(Functions)
            


