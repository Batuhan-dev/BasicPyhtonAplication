firstInput=input('')
secondInput=input('')

if firstInput=="rock":
    if secondInput=="paper":
        print("second player win")
    elif  secondInput=="rock":
        print("draw")
    else:
        print("firsth player win")
elif firstInput=="paper":
    if secondInput=="paper":
        print("draw")
    elif  secondInput=="rock":
        print("firsth player win")
    else:
        print("second player win")
else:
    if secondInput=="paper":
            print("firsth player win")
    elif  secondInput=="rock":
        print("second player win")
    else:
        print("draw")
