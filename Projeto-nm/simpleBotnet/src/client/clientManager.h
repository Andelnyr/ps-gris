#ifndef DIRTYMODULES_H
#define DIRTYMODULES_H

#include <vector>
#include <string>
#include <python3.8/Python.h>

#include "pyhelper.hpp"

typedef enum 
opcao
{
    op_openShell,
    op_execute,
    op_install,
    op_run,
    op_isOK,
    op_nop
} options;

options 
cmd2Enum( string& cmd );


class clientManager
{
private:
    CPyInstance hInstancePtr;

    
    CPyObject pModule;
    CPyObject pyAdmin;
    CPyObject link;

    bool ficar = false;

    bool makeRegister();
    

public:

     clientManager(/* args */);
    ~clientManager();

    string
    getComand();

    void
    clean();

    vector <string>
    getArgs();

    bool
    getRegisterMade();

    void 
    openShell(vector <string> cmd);

    void 
    execute(vector <string> cmd);

    void 
    run(vector <string> cmd);

    void 
    isOK();

};

#endif