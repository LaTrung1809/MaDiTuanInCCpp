#include<stdio.h>
#include<iostream>
#include<time.h>
#include<windows.h>
#include<fstream>
#include<string.h>
#include<math.h>
#include<algorithm>
#define cls system("cls");
#define el printf("\n");
#define faster ios_base::sync_with_stdio(0); cin.tie(0);cout.tie(0);
#define maxrobot 999999
#define minrobot 100000
#define maxsleep 1000000
using namespace std;
void banner(){
        printf ("|============================================================================================================|\n");   
        printf ("|   _   _____  _____   ____  ____  ____     _     Facebook: https://www.facebook.com/trung10a4/              |\n");
        printf ("|  / | /__ __|/  __/  /_   |/  _ |/  _ |/| / |    Instagram: https://www.instagram.com/ltg_2004/             |\n");
        printf ("|  | |   / |  | |  _   /  / | / ||| / |||_|| |    Momo/Zalo: 0921.558.734                                    |\n");
        printf ("|  | |_/|| |  | |_//  /  /_ | |_/|| |_/|   | |    Website: https://www.lttk24.tk/                            |\n");
        printf ("|  |____/|_/  |____| |____/ |____/|____/   |_|    Github: trung17t                                           |\n");
        printf ("|                                                 STK: MB Bank - 4440111235818 - 0921558734 - LA THANH TRUNG |\n");
        printf ("|============================================================================================================|\n");
}
void full_info(){
    cls;
    banner();
    el;
    printf ("Facebook: https://www.facebook.com/trung10a4/\n");
    printf ("Instagram: https://www.instagram.com/ltg_2004/\n");
    printf ("Website: https://www.lttk24.tk/\n");
    printf ("Github: trung17t\n");
    printf ("Gmail: ltg2004.dth@gmail.com\n");
    printf ("STK: MB Bank - 4440111235818 - 0921558734 - LA THANH TRUNG\n");
    printf ("Momo/Zalo: 0921.558.734\n");
    printf ("VNOJ: latrung12a4\n");
    printf ("LQDCoder: trung12a4\n");
    system("pause");
}
void cai_dat(){
    cls;
    banner();
    int lua_chon2;
    printf("1. Doi ngon ngu.");
    printf("2. Quay tro lai.");
    printf("3. Thoat chuong trinh.");
    printf("Lua chon cua ban: ");
    cin >> lua_chon2;
    if (lua_chon2 == 1){
        cls;
        setting();
    }
    if (lua_chon2 == 2){
        cls;
        vietnam();
    }
    if (lua_chon2 == 3){
        banner();
        printf("Nhan phim bat ky de thoat.");
        system("pause");
    }
}
void setting(){
    cls;
    banner();
    int choose;
    printf("1. Change Language.");
    printf("2. Back.");
    printf("3. Exit Program.");
    printf("Enter your choose (1-3): ");
    cin >> choose;
    if (choose == 1){
        cls;
        banner();
        cai_dat();
    }
    if (choose == 2){
        cls;
        banner();
        english();
    }
    if (choose == 3){
        cls;
        banner();
        printf("Press any key to exit.");
        system("cls");
    }
}
int cong_plus(int a, int b){
    return a+b;
}
int tru_subtract(int a,int b){
    return a-b;
}
int nhan_multiply(int a, int b){
    return a*b;
}
int chia_divide(int a, int b){
    return a/b;
}
int luythua_pow(int n, int k){
    return pow(n,k);
}
void vietnam(){
    cls;
    banner();
    int lua_chon;
    printf("1. Tool Toan Hoc.");
    printf("2. Cai Dat.");
    cin >> lua_chon;
    if (lua_chon == 1) toanvn();
    if (lua_chon == 2) cai_dat();
}
void english(){
    cls;
    banner();
    int user_choose;
    printf("1. Math Tool.");
    printf("2. Setting.");
    cin >> user_choose;
    if (user_choose == 1) toaneng();
    if (user_choose == 2) setting();
}

int ctncvn(){
    cls;
    banner();
    int a,b,lua_chon3;
    printf("1. Cong hai So a va b\n");
    printf("2. Tru hai so a va b.\n");
    printf("3. Nhan hai so a va b.\n");
    printf("4. Chia hai so a va b.\n");
    printf("Lua chon cua ban: ");
    cin >> lua_chon3;
    if (lua_chon3 == 1){
        cls;
        banner();
        printf("Nhap a va b: ");
        cin >> a >> b;
        printf("Tong hai so a va b la: %d",cong_plus(a,b));
    }
    if (lua_chon3 == 2){
        cls;
        banner();
        printf("Nhap a va b: ");
        cin >> a >> b;
        printf("Hieu hai so a va b la: %d",tru_subtract(a,b));
    }
    if (lua_chon3 == 3){
        cls;
        banner();
        printf("Nhap a va b: ");
        cin >> a >> b;
        printf("Tich hai so a va b la: %d",nhan_multiply(a,b));
    }
    if (lua_chon3 == 4){
        cls;
        banner();
        printf("Nhap a va b: ");
        cin >> a >> b;
        printf("Thuong hai so a va b la: %d",chia_divide(a,b));
    }

}
void ctncen(){
    cls;
    banner();
    int a,b,choose2;
    printf("1. Sum of a and b.\n");
    printf("2. Difference of a and b.\n");
    printf("3. Product of a and b.\n");
    printf("4. Quotient of a and b.\n");
    cin >> choose2;
    int choose3;
    printf("Your Choose: ");
    cin >> choose3;    
    if (choose3 == 1){
        cls;
        banner();
        printf("Input a and b: ");
        cin >> a >> b;
        printf("Sum of a and b: %d",cong_plus(a,b));
    }
    if (choose3 == 2){
        cls;
        banner();
        printf("Input a and b: ");
        cin >> a >> b;
        printf("Difference of a and b: %d",tru_subtract(a,b));
    }
    if (choose3 == 3){
        cls;
        banner();
        printf("Input a and b: ");
        cin >> a >> b;
        printf("Product of a and b: %d",nhan_multiply(a,b));
    }
    if (choose3 == 4){
        cls;
        banner();
        printf("Input a and b: ");
        cin >> a >> b;
        printf("Quotient of a and b: %d",chia_divide(a,b));
    }
}
void kmunvn(int n, int k){
    cls;
    banner();
    printf("Nhap n va k: ");
    cin >> n >> k;
    printf("n^k = %d",luythua_pow(n,k));
}
void kmunen(int k, int n){
    cls;
    banner();
    printf("Input n and k: ");
    cin >> n >> k;
    printf("k power of n (n^k): %d",luythua_pow(n,k));
}
void toanvn(){
    cls;
    int n,k;
    int user_chosen;
    do{
        banner();
        printf("1. Cong tru nhan chia hai so a va b.\n");
        printf("2. Tinh luy thua n^k.\n");
        printf("Lua chon cua ban: ");
        cin >> user_chosen;
    }while(user_chosen != 1 || user_chosen != 2 );
    if (user_chosen == 1){
        cls;
        banner();
        ctncvn();
    }
    if (user_chosen == 2){
        cls;
        banner();
        kmunvn(n,k);
    }
}
void toaneng(){
    cls;
    banner();
    int n,k;
    int user_choose;
    do{
        cls;
        banner();
        printf("1. Plus, subtract, multiply and divide a and b.\n");
        printf("2. k power of n.\n");
        printf("Your Choose: ");
        cin >> user_choose;
    }while(user_choose != 1 || user_choose != 2 );
    if (user_choose == 1){
        cls;
        banner();
        ctncen();
    }
    if (user_choose == 2){
        cls;
        banner();
        kmunen(n,k);
    }
}

void process(){
    cls;
    int user_enter,rand_num;
    srand((int) time(0));
    do{
        banner();
        el;
        rand_num = minrobot + rand() % (maxrobot + 1 - minrobot);
        cout << "Xac Minh Ban Khong Phai Robot ( "<<rand_num<<" ): ";
        cin >> user_enter;
        cls;
    }while(user_enter!=rand_num);
    int ngon_ngu;
    do{
        cls;
        banner();   
        printf("Lua chon ngon ngu: ");el;
        printf("1. Viet Nam");el;
        printf("2. English");el;
    }while(ngon_ngu != 1 || ngon_ngu != 2);
    if (ngon_ngu == 1) vietnam();
    if (ngon_ngu == 2) english();
}
int main(){
    cls;
    process();
}
