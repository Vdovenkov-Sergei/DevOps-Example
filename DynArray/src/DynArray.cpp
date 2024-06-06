#include "DynArray.hpp"
#include <vector>

template<class T>
DynArray<T>::DynArray() : array(), size(0) {}

template<class T>
DynArray<T>::DynArray(int N) : array(N, T()), size(N) {}

template<class T>
DynArray<T>::DynArray(const DynArray& other) : DynArray(other.size)
{
    for (size_t i = 0; i < other.size; ++i) this->array[i] = other.array[i];
}

template<class T>
void DynArray<T>::appendElem(T elem)
{
    this->array.push_back(elem); this->size++;
}

template<class T>
T& DynArray<T>::operator[](int ind)
{
    return *(ind + this->array.begin());
}

template<class T>
DynArray<T>& DynArray<T>::operator=(const DynArray& rht)
{
    this->size = rht.size;
    this->array = rht.array;
    return *this;
}

template<class T>
DynArray<T> DynArray<T>::operator+(const DynArray& rht)
{
    DynArray<T> resArray(this->size + rht.size);
    int k = 0;
    for (size_t i = 0; i < this->size; ++i) resArray[k++] = this->array[i];
    for (size_t i = 0; i < rht.size; ++i) resArray[k++] = rht.array[i];
    return resArray;
}

template<class T>
DynArray<T> DynArray<T>::operator>>(int shift)
{
    DynArray<T> newArray = (*this);
    for (size_t i = 0; i < newArray.size; ++i)
        newArray[(i + shift) % newArray.size] = this->array[i];
    return newArray;
}

template<class T>
DynArray<T> DynArray<T>::operator<<(int shift)
{
    DynArray<T> newArray = (*this);
    for (size_t i = 0; i < newArray.size; ++i)
        newArray[(i - shift + newArray.size) % newArray.size] = this->array[i];
    return newArray;
}

template<class T>
void DynArray<T>::print()
{
    for (size_t i = 0; i < this->size; i++) std::cout << this->array[i] << ' ';
    std::cout << std::endl;
}

template DynArray<double>::DynArray();
template DynArray<double>::DynArray(int N);
template DynArray<double>::DynArray(const DynArray& other);
template void DynArray<double>::appendElem(double elem);
template double& DynArray<double>::operator[](int ind);
template DynArray<double>& DynArray<double>::operator=(const DynArray& rht);
template DynArray<double> DynArray<double>::operator+(const DynArray& rht);
template DynArray<double> DynArray<double>::operator>>(int shift);
template DynArray<double> DynArray<double>::operator<<(int shift);
template void DynArray<double>::print();