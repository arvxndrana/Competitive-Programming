#include <iostream>

int main(void)
{
    std::string S;
    std::cin >> S;
    int l = S.size();
    int count = 0;

    for (int i=0;i<=l;i++)
        if (S[i]=='o')
        {
            count++;
        }

    if (count % 2 == 0)
        std::cout << "even";
    else
        std::cout << "odd";


    return 0;
}
