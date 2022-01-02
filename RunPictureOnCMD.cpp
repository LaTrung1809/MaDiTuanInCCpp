#include<stdio.h>
#include<iostream>
#include<time.h>
#include<windows.h>
#include<fstream>
#include<string.h>
#define el printf("\n");
#define maxrobot 999999
#define minrobot 100000
#define maxsleep 1000000
using namespace std;
void banner(){
        cout << "==================================================\n";
        cout << "|   _   _____  _____   ____  ____  ____     _    |\n";
        cout << "|  / | /__ __|/  __/  /_   |/  _ |/  _ |/| / |   |\n";
        cout << "|  | |   / |  | |  _   /  / | / ||| / |||_|| |   |\n";
        cout << "|  | |_/|| |  | |_//  /  /_ | |_/|| |_/|   | |   |\n";
        cout << "|  |____/|_/  |____| |____/ |____/|____/   |_|   |\n";
        cout << "|                                                |\n";
        cout << "==================================================\n";
}
void info(){
    system("cls");
    banner();
    el;
    cout <<"Gmail: ltg2004.dth@gmail.com\n";
    cout <<"STK: MB Bank - 4440111235818 - 0921558734 - LA THANH TRUNG\n";
    cout <<"Momo/Zalo: 0921.558.734\n";
    cout <<"Facebook: https://www.facebook.com/trung10a4/\n";
    cout <<"Instagram: https://www.instagram.com/ltg_2004/\n";
    cout <<"Website: https://www.lttk24.tk/\n";
    cout <<"Github: trung17t\n";
    cout <<"VNOJ: latrung12a4\n";
    cout <<"LQDCoder: trung12a4\n";
    system("pause");
}
void process(){
    system("cls");
    int user_enter,rand_num,percent_count;
    srand((int) time(0));
    do{
        banner();
        el;
        rand_num = minrobot + rand() % (maxrobot + 1 - minrobot);
        cout << "Xac Minh Ban Khong Phai Robot ("<<rand_num<<"): ";
        cin >> user_enter;
        system("cls");
    }while(user_enter!=rand_num);
    for (percent_count = 0;percent_count <= 100;percent_count++){
        system("cls");
        cout << "Dang Xu Ly "<<percent_count<<"%";
        Sleep(10);
    }
    system("cls");
    char s[1000];
    FILE* f = fopen("dthy.txt", "r");
    while (!feof(f)){
        fgets(s, sizeof(s), f);
        printf("%s", s);
        Sleep(2);
    }
    Sleep(10000);
    system("cls");
    string check_info;
    banner();
    cout << "Chay Lai Chuong Trinh ? (Y/N): ";
    cin >> check_info;
    if (check_info == "Y"){
        process();
    }
    if (check_info == "N") info();
}
int main()
{
    process();
    system("cls");
    
}
// Và bây giờ mình show source code cho anh em :))
// Cảm ơn Hải Yến đã cho mình mượn bức ảnh này :3
// Facebook Hải Yến: Facebook: https://www.facebook.com/dinhtrinhhaiyen
// Thanks For Watching ! :33