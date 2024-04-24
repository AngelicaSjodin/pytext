
while True:
        print("whats your player name?")
        name=input(": ")
        print("weird name but ok "+name)
        start()
        

        def start():
            print("you wake up on a large golden throne surrounded by a bufet of exotic cheeses and gold spread across the stone floor")
            options=[1,2,3]
            playerChoice=""

            while playerChoice not in options:
                print("Options: 1.feast, 2.fill your pockets w gold, 3.jump out the window")
                playerChoice=int(input(": "))

                if playerChoice == 1:
                    mice()
                elif playerChoice == 2:
                    guards()
                elif playerChoice == 3:
                    ouch()
                else:
                    print("choose one of the available options.")
                
            def mice():
                print("ok")

            def guards():
                print("yup")

            def ouch():
                print("mhm")    
          
