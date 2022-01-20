from math import sqrt,fabs,cos,acos,pi
try:
    a=float(input("Nhập giá trị a: "))
    try:
        b=float(input("Nhâp giá trị b: "))
        try:
            c=float(input("Nhập giá trị c: "))
            try:
                d=float(input("Nhập giá trị d: "))
                if a==0:
                    print("\nPhương trình vô nghiệm")
                else:
                    delta=pow(b,2)-3*a*c
                    k=(9*a*b*c-2*pow(b,3)-27*pow(a,2)*d)/(2*sqrt(pow(fabs(delta),3)))
                    if delta>0:
                        if fabs(k)<=1:
                            x1=(2*sqrt(delta)*cos(acos(k)/3)-b)/(3*a)
                            x2=(2*sqrt(delta)*cos(acos(k)/3-(2*pi/3))-b)/(3*a)
                            x3=(2*sqrt(delta)*cos(acos(k)/3+(2*pi/3))-b)/(3*a)
                            print("\nPhương trình có 3 nghiệm phân biệt\n X1= ",x1,"\n X2= ",x2,"\n X3= ",x3)
                        if fabs(k)>1:
                            x=((sqrt(delta)*fabs(k))/(3*a*k))*(pow((fabs(k)+sqrt(pow(k,2)-1)),1.0/3)+pow((fabs(k)-sqrt(pow(k,2)-1)),1.0/3))-(b/(3*a))
                            print("\nPhương trình có 1 nghiệm duy nhất\n X= ",x)
                    elif delta==0:
                        x=(-b-pow(-(pow(b,3)-27*a*a*d),1.0/3))/(3*a)
                        print("\nPhương trình có nghiệm bởi:",x)
                    else:
                        x=(sqrt(fabs(delta))/(3*a))*(pow((k+sqrt(k*k+1)),1.0/3)-pow(-(k-sqrt(k*k+1)),1.0/3))-(b/(3*a))
                        print("\nPhương trình có 1 nghiệm duy nhất\n X= :",x)
            except ValueError:
                # Phương trình bật 2
                delta=(b**2)-4*(a*c)
                if a!=0:
                    Xi=-b/(2*a)
                    Yi=-delta/(4*a)
                    print("\nBài Làm:")
                    print("\ndelta = b²-4ac =",b**2,"- 4 x",a,"x",c,"=",delta)
                    if delta<0:
                        print("\nPhương trình vô nghiệm")
                    elif delta==0:
                        print("\nPhương trình có nghiệm kép:\n\n x1 = x2 = -b(2/a)\n\t\t=>",-b,"x(2/",a,") =",-b*(2/a))
                    else:
                        x1=(-b-sqrt(delta))/(2*a)
                        x2=(-b+sqrt(delta))/(2*a)
                        print("\n\nPhương trình có 2 nghiệm phân biệt:\n\n x1= -b-Căn delta/(2a)\n => (",-b,"-",("{0:.{1}f}".format(sqrt(delta),2)),")/(2x",a,")=",("{0:.{1}f}".format(x1,2)),"\n x2= -b+Căn delta/(2a)\n => (",-b,"+",("{0:.{1}f}".format(sqrt(delta),2)),")/(2x",a,")=",("{0:.{1}f}".format(x2,1)))
                    print("\nXi = -b/2a = -",b,"/ 2 x",a,"=",Xi,"\nYi = -Delta/4a =",delta,"/ 4 x",a,"=",Yi)
                    print("\n Kết quả:")
                    print("Delta= ",delta)
                    if delta==0:
                        print("X1,X2= ",-b*(2/a))
                    elif delta>0:
                        print("X1= ",("{0:.{1}f}".format(x1,2)),"\nX2= ",("{0:.{1}f}".format(x2,2)))
                    print("Xi= ",Xi,"\nYi= ",Yi)
                    if(a>0):
                        print("\n Bản biến thiên:\n\tX|  -∞\t",("{0:.{1}f}".format(Xi,1)),"\t+∞\n     －－|－－－－－－－－－\n\tY|  +∞\t\t+∞\n    (a>0)|     ⬊      ⬋\n\t |\t",("{0:.{1}f}".format(Yi,1)))
                        print("\nHàm số nghịch biến trên khoảng (-∞;",("{0:.{1}f}".format(Xi,1)),")")
                        print("Hàm số đồng biến trên khoảng (",("{0:.{1}f}".format(Xi,1)),"+∞)")
                    else:
                        print("\n Bản biến thiên:\n\tX|  -∞  ",("{0:.{1}f}".format(Xi,1)),"\t+∞\n     －－|－－－－－－－－－\n\tY|\t",("{0:.{1}f}".format(Yi,1)),"\n    (a<0)|      ⬈   ⬉\n\t |    -∞     -∞")
                        print("\nHàm số đồng biến trên khoảng (-∞;",("{0:.{1}f}".format(Xi,1)),")")
                        print("Hàm số nghịch biến trên khoảng (",("{0:.{1}f}".format(Xi,1)),"+∞)\n")
                    if Xi>0:
                        Xi11=(Xi)-(Xi)
                        Xi22=(Xi11)-(Xi)
                        Xi1=(Xi)+(Xi)
                        Xi2=(Xi1)+(Xi)
                    else:
                        Xi11=(Xi)+(Xi)
                        Xi22=(Xi11)+(Xi)
                        Xi1=(Xi)-(Xi)
                        Xi2=(Xi1)-(Xi)
                    Yi1=(a*(pow(Xi1,2)))+(b*Xi1)+c
                    Yi2=(a*(pow(Xi2,2)))+(b*Xi2)+c
                    Yi22=Yi2
                    Yi11=Yi1
                    Yi22=("{0:.{1}f}".format(Yi22,1))
                    Yi11=("{0:.{1}f}".format(Yi11,1))
                    Yi=("{0:.{1}f}".format(Yi,1))
                    Yi1=("{0:.{1}f}".format(Yi1,1))
                    Yi2=("{0:.{1}f}".format(Yi2,1))
                    Xi22=("{0:.{1}f}".format(Xi22,1))
                    Xi11=("{0:.{1}f}".format(Xi11,1))
                    Xi=("{0:.{1}f}".format(Xi,1))
                    Xi1=("{0:.{1}f}".format(Xi1,1))
                    Xi2=("{0:.{1}f}".format(Xi2,1))
                    print("\n\tBản giá trị:\n\tX| ",Xi22," ",Xi11," ",Xi," ",Xi1," ",Xi2,"\n     －－|－－－－－－－－－－－－－－－－－\n\tY| ",Yi22," ",Yi11," ",Yi," ",Yi1," ",Yi2)
                else:
                    print("Phương trình vô nghiệm")
        except ValueError:
            # Phương trình bật 1
            if a==0 and b==0:
                print("\nPhương trình vô nghiệm")
            elif a==0 and b!=0:
                print("\nPhương trình vô nghiệm")
            else:
                print("\n Phương trình có nghiệm X=(-b/a)\n\t=>",-b,"/",a,"=",-b/a)
                if -b/a<0:
                    if b<0:
                        print("\n\t Bản giá trị:\n\tx|   0    |",("{0:.{1}f}".format(-b/a,1)),"|\n     －－|－－－－|－－－|\n\tY| ",("{0:.{1}f}".format(b,1))," |   0  |")
                    else:
                        print("\n\t Bản giá trị:\n\tx|   0    |",("{0:.{1}f}".format(-b/a,1)),"|\n     －－|－－－－|－－－|\n\tY| ",("{0:.{1}f}".format(b,1)),"  |   0  |")
                else:
                    if b<0:
                        print("\n\t Bản giá trị:\n\tx|   0    | ",("{0:.{1}f}".format(-b/a,1)),"|\n     －－|－－－－|－－－|\n\tY| ",("{0:.{1}f}".format(b,1))," |   0  |")
                    else:
                        print("\n\t Bản giá trị:\n\tx|   0    | ",("{0:.{1}f}".format(-b/a,1)),"|\n     －－|－－－－|－－－|\n\tY| ",("{0:.{1}f}".format(b,1)),"  |   0  |")
                print("\n\tBản biến thiên:\n\tX|  0\t",("{0:.{1}f}".format(-b/a,1)),"\n       －|－－－－－－－")
                if b<0:
                    print("\tY|       0\n\t |     ⬈\n\t |",b)
                else:
                    print("\tY|",b,"\n\t |     ⬊\n\t |\t  0")
    except ValueError:
        print("\nGiá trị b không thể bỏ qua")
except ValueError:
    print("\nGiá trị a không thể bỏ qua")