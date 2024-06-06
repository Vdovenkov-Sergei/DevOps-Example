#ifndef DYN_ARRAY_HPP
#define DYN_ARRAY_HPP

#include <iostream>
#include <vector>

template <class T>
class DynArray
{
public:
    std::vector<T> array;
    int size;

    DynArray();
    DynArray(int N);
    DynArray(const DynArray& other);
    void appendElem(T elem);
    T& operator[](int ind);
    DynArray& operator=(const DynArray& rht);
    DynArray operator+(const DynArray& rht);
    DynArray operator>>(int shift);
    DynArray operator<<(int shift);
    void print();
};

#endif