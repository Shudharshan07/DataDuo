#include <iostream>
#include <cmath>
#include <vector>
#include <string>


std::vector<char> vec;
void input_list(std::string S)
{
    int i = 0;
    for(i; i< S.length(); i++)
    {   
        vec.push_back(S[i]);
        
    }
}


std::vector<int> Lascii;
int str_ascii()
{   int j = 0;
    std::string str;
    std::cin.ignore();
    std::getline (std::cin , str);
    input_list(str);
    for(j; j< str.length(); j++)
    {   
        Lascii.push_back((int)vec[j]);

    }
    vec.clear();
    
    return 0;
}


std::vector<int> bin_list;
int str_bin(int Cascii)
{   
    int k = 0;
    int r = 7;
    int b;
    for(k; k< 8; k++)
    {
        b = Cascii %2;
        Cascii = Cascii/2;
        //std::cout << b;
        bin_list.push_back(b);
    }
    for(r; r>=0; r--)
    {
        std::cout << bin_list[r];
    }
    bin_list.clear();
    std::cout << " ";
    
    return 0;
}

std::vector<int> Lbin_ascii;
int bin_ascii()
{
    int i = 0;
    int k = -1;
    int l = 0;
    int bin_num = 0;
    std::string str;
    std::cin.ignore();
    std::getline (std::cin , str);
    input_list(str);
    vec.push_back(' ');
    for(i; i< vec.size(); i++)
    {
        if(*&vec[i] != ' ')
        {
            k++;
        }
        else if (*&vec[i] == ' ')
        {
            for(l; l<= k; l++)
            {
                if(*&vec[l] == '1')
                {
                    bin_num += pow(2,(k-l));
                }
            }
            k++;
            Lbin_ascii.push_back(bin_num);
            bin_num = 0;
        }
    }
    vec.clear();
    return 0;
}

//for 3 and 6 getting ascii as string and appending it to a list and converting it to int;

std::vector<int> Lstr_list;
std::vector<int> Lws;
int str_int()
{   
    int i = 0;
    std::string str;
    std::cin.ignore();
    std::getline (std::cin , str);
    input_list(str);
    Lws.push_back(0);
    for(i; i<vec.size(); i++)
    {
        if(*&vec[i] == ' ')
        {
            Lws.push_back(i+1);   
        }
    }
    for(int j : Lws)
    {
      Lstr_list.push_back(atoi(&vec[j]));
    }
    Lws.clear();
    vec.clear();
    
    return 0;
}



int main()
{   
    int num;
    int after_out;
    do
    {   
        std::cout << "\n***********************************\n";
        std::cout << "Enter the number to: \n";
        std::cout << "1. Convert text to binary\n";
        std::cout << "2. Convert text to ascii\n";
        std::cout << "3. Convert ascii to binary\n";
        std::cout << "-----------------------------------\n";
        std::cout << "4. Convert binary to text\n";
        std::cout << "5. Convert binary to ascii\n";
        std::cout << "6. Convert ascii to text\n";
        std::cout << "7. Exit\n";
        std::cout << "-----------------------------------\n";
        std::cout << "Number: ";
        std::cin >> num;
        switch(num)
        {
            case 1: 
            {   
                std::cout << "Enter text to covert to binary: \n";
                str_ascii();
                int n = 0;
                std::cout << "\nResult value: ";
                for(n; n< Lascii.size(); n++)
                {
                    str_bin(*&Lascii[n]);
                }
                Lascii.clear();
                std::cout << "\n";
                break;
            }
            case 2:
            {   
                std::cout << "Enter text to convert to ascii: \n";
                str_ascii();
                int m = 0;
                std::cout << "\nResult value: ";
                for(m; m < Lascii.size(); m++)
                {
                    std::cout << Lascii[m] << " ";
                }
                Lascii.clear();
                std::cout << "\n";
                break;
            }
            case 3:
            {   
                std::cout << "Enter ascii to convert to binary: \n";
                str_int();
                int n = 0;
                std::cout << "\nResult value: ";
                for(n; n< Lstr_list.size(); n++)
                {
                    str_bin(*&Lstr_list[n]);
                }
                Lstr_list.clear();
                std::cout << "\n";
                break;
            }
            case 4:
            {   
                std::cout << "Enter binary to convert to text: \n";
                int q = 0;
                bin_ascii();
                std::cout << "\nResult value: ";
                for(q; q<Lbin_ascii.size(); q++)
                {
                    std::cout << (char)Lbin_ascii[q];
                }
                Lbin_ascii.clear();
                std::cout << "\n";
                break;
            }
            case 5:
            {   
                std::cout << "Enter binary to convert to ascii: \n";
                int p = 0;
                bin_ascii();
                std::cout << "\nResult value: ";
                for(p; p<Lbin_ascii.size(); p++)
                {
                    std::cout << Lbin_ascii[p] << " ";
                }
                Lbin_ascii.clear();
                std::cout << "\n";
                break;
            }
            case 6:
            {   
                std::cout << "Enter ascii to convert to text: \n";
                int q = 0;
                str_int();
                std::cout << "\nResult value: ";
                for(q; q<Lstr_list.size(); q++)
                {
                    std::cout << (char)Lstr_list[q];
                }
                Lstr_list.clear();
                std::cout << "\n";
                break;
            }
            case 7:
            {   
                break;
            }
            default:
            {
                std::cout << "Enter a valid number\n";
            }
        }
    }while(num != 7);

}