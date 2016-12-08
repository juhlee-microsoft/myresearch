def parentfun():
    myaaa = 1
    def childfun():
            myaaa = 10
            print myaaa
    childfun()
    print myaaa

if __name__=="__main__":
	parentfun()
	childfun()
