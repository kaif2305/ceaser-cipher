print("__Additive Cipher__")
ciphertxt= "PXPXKXENVDRUXVTNLXHYMXGMAXYKXJNXGVRFXMAHWGXXWLEHGZXKVBIAXKMXQM"
k=0
while(1):
    plaintxt=""
    k+=1
    for i in range(len(ciphertxt)):
        char=ciphertxt[i]
        plaintxt+=chr(((ord(char)+k-65)%26)+65)
    
    ch=int(input("\nPress 1 to continue \nPress 2 to end \nEnter your choice : "))   
    if ch==1:
        print("Cipher Text : ", plaintxt)
        continue
    if ch==2:
        break

