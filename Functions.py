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


    def validation():
        if input().lower() == '1':
            return True
        elif input().lower() == '2':
            return False
        else:
            print('your quest cannot continue with your correct input')


