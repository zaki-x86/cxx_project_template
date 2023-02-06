#include <iostream>
#include <project/darray.h>


int main(void)
{
    store<int> st(5);

    std::cout << st.fetch_data() << std::endl;

    return 0;
}

