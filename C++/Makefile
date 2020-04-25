# Makefile

# Name of the project
PROJ_NAME=main
 
# .cpp files
C_SOURCE=$(wildcard *.cpp)
 
# .h files
H_SOURCE=$(wildcard *.h)
 
# Object files
OBJ=$(C_SOURCE:.cpp=.o)
 
# Compiler
CC=g++
 
# Flags for compiler
prefix = /usr/local
exec_prefix = /usr/local
libdir = ${exec_prefix}/lib
globesconf= $(exec_prefix)/bin/globes-config

local_CFLAGS = -g -O4 -std=c99

INCFLAGS:=$(shell $(globesconf) --include)
local_LDFLAGS:=$(shell $(globesconf) --libs)
preopen_modules:=$(shell $(globesconf) --dlpreopen)
local_LTLDFLAGS:=$(shell $(globesconf) --ltlibs)
ifdef preopen_modules
predefs = -DGLB_STATIC
endif

CC_FLAGS= -c -W -Wall -ansi -pedantic -g -O4 -std=c99 
OMP_FLAGS= -fopenmp
 

# Compilation and linking

all: $(PROJ_NAME)
 
$(PROJ_NAME): $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS) $(local_LDFLAGS) $(OMP_FLAGS)
 
%.o: %.cpp %.h
 
	$(CC) -o $@ $< $(CC_FLAGS) $(LDFLAGS) $(local_LDFLAGS) $(INCFLAGS) $(OMP_FLAGS)
 
main.o: main.cpp $(H_SOURCE)
	$(CC) -o $@ $< $(CC_FLAGS) $(LDFLAGS) $(local_LDFLAGS) $(INCFLAGS) $(OMP_FLAGS)
 
#clean:
#	 rm -rf *.o $(PROJ_NAME) *~
