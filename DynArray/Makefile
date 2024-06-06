CXX = g++
CXXFLAGS = -g -O1
INCLUDE = include

all: main clean
clean:
	rm *.o
main: main.o DynArray.o
	mkdir bin | $(CXX) $(CXXFLAGS) $^ -o bin/$@.exe

main.o:
	$(CXX) $(CXXFLAGS) -I $(INCLUDE) -c src/main.cpp

DynArray.o:
	$(CXX) $(CXXFLAGS) -I $(INCLUDE) -c src/DynArray.cpp

.PHONY: all clean