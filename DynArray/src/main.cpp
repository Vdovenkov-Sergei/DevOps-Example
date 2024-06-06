#define COUNT 10
#define KOEF 1.57

#include <iostream>
#include "DynArray.hpp"

int main()
{
    DynArray<double> array;                     // конструктор по умолчанию
    array.appendElem(1.8);
    for (size_t i = 0; i < COUNT; i++) array.appendElem(i * KOEF);
    array.print();

    DynArray<double> copyArray1 = array;        // конструктор копирования
    DynArray<double> copyArray2(10);            // однопараметрический конструктор
    copyArray2 = array;                         // оператор (=) присваивания с копированием

    copyArray1.print();
    copyArray1[0] = 11.5;                       // оператор []
    copyArray1.print();

    DynArray<double> newArray(5);               // однопараметрический конструктор
    newArray.print();
    newArray = array + copyArray2;              // конкатенация двух массивов, оператор +
    newArray.print();

    array = array << 4;                         // оператор <<
    array.print();

    copyArray2.print();
    copyArray2 = copyArray1 >> 5;               // оператор >> + оператор (=) присваивания с копированием
    copyArray2.print();

    return 0;
}