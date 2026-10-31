#include <iostream>
#include <vector>

int main(void)
{
    std::string s1,s2,s3,s4,s5;
    std::cin >> s1;
    std::cin >> s2;
    std::cin >> s3;
    std::cin >> s4;
    std::cin >> s5;

    std::vector<std::string> S = {s1,s2,s3,s4,s5};
    int l[]  = {0,0,0,0,0,0,0,0,0,0,0,0}; // how many to cross for bingo

    // rows
    
    for (int i=0;i<5;i++)
    {
        int c = 0;
        for (char n : S[i])
            if (n == 'o')
                c++;
        l[i] = 5 - c;
    }

    // column
    
    for (std::string s : S)
    {
        for (int i=0;i<5;i++)
        {
            if (s[i] == '.')
                l[5+i]++;
        }
    }

    // cross
    
    for (int i=0;i<5;i++)
    {
        if ((S[i][i]) == '.')
        {
            l[10]++;
        }
        if (S[4-i][4-i] == '.')
        {
            l[11]++;
        }
    }


    int min = 5;
    for (int i: l)
    {
        if (i < min)
        {
            min = i;
        }
    }
    std::cout << min;


    return 0;
}
