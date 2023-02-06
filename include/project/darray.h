/**
 * @file darray
 * @author M Zaki (zaki.x86@gmail.com)
 * @brief dynamic array container header file, aka, vector in the standard STL
 * @version 0.1
 * @date 2022-12-16
 * @copyright Copyright (c) 2022
 * 
 */

#ifndef _DARRAY_H_

#define _DARRAY_H_

template<typename Type>
struct store
{
    Type data;

    store() = default;

    store( Type _data ) : data(_data) {}

    Type fetch_data()
    {
        return data;
    }
};


#endif // !_DARRAY_H_
