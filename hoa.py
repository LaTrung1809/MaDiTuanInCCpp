hoa_cauhinh=[["h","1","1s1","he","4","1s2"],["li","7","1s22s1","be","9","1s22s2","b","10","1s22s22p1","c","12","1s22s22p2","n","14","1s22s22p3","o","16","1s22s22p4","f","19","1s22s22p5","ne","20","1s22s22p6"],["na","23","1s22s22p63s1","mg","24","1s22s22p63s2","al","27","1s22s22p63s23p1","si","28","1s22s22p63s23p2","p","31","1s22s22p63s23p3","s","32","1s22s22p63s23p4","cl","35.5","1s22s22p63s23p5","ar","40","1s22s22p63s23p6"],["k","39","1s22s22p63s23p64s1","ca","40","1s22s22p63s23p64s2","sc","45","1s22s22p63s23p63d14s2","ti","48","1s22s22p63s23p63d24s2","v","51","1s22s22p63s23p63d34s2","cr","52","1s22s22p63s23p63d54s1","mn","55","1s22s22p63s23p63d54s2","fe","56","1s22s22p63s23p63d64s2","co","59","1s22s22p63s23p63d74s2","ni","58","1s22s22p63s23p63d84s2","cu","63.5","1s22s22p63s23p63d104s1","zn","65","1s22s22p63s23p63d104s2","ga","70","1s22s22p63s23p63d104s24p1","ge","72","1s22s22p63s23p63d104s24p2","as","75","1s22s22p63s23p63d104s24p3","se","79","1s22s22p63s23p63d104s24p4","br","80","1s22s22p63s23p63d104s24p5","kr","84","1s22s22p63s23p63d104s24p6"],["rb","85","1s22s22p63s23p63d104s24p65s1","sr","87","1s22s22p63s23p63d104s24p65s2","y","89","1s22s22p63s23p63d104s24p64d15s2","zr","91","1s22s22p63s23p63d104s24p64d25s2","nb","93","1s22s22p63s23p63d104s24p64d45s1","mo","96","1s22s22p63s23p63d104s24p64d55s1","tc","99","1s22s22p63s23p63d104s24p64d55s2","ru","101","1s22s22p63s23p63d104s24p64d75s1","rh","103","1s22s22p63s23p63d104s24p64d85s1","pd","106","1s22s22p63s23p63d104s24p64d105s0","ag","108","1s22s22p63s23p63d104s24p64d105s1","cd","112","1s22s22p63s23p63d104s24p64d105s2","in","115","1s22s22p63s23p63d104s24p64d105s25p1","sn","119","1s22s22p63s23p63d104s24p64d105s25p2","sb","121","1s22s22p63s23p63d104s24p64d105s25p3","i","127","1s22s22p63s23p63d104s24p64d105s25p5","te","128","1s22s22p63s23p63d104s24p64d105s25p4","xe","131","1s22s22p63s23p63d104s24p64d105s25p6"],["cs","133","1s22s22p63s23p63d104s24p64d105s25p66s1","ba","137","1s22s22p63s23p63d104s24p64d105s25p66s2","la","139","1s22s22p63s23p63d104s24p64d105s25p65d16s2","hf","178","1s22s22p63s23p63d104s24p64d105s25p64f145d26s2","ta","181","1s22s22p63s23p63d104s24p64d105s25p64f145d36s2","w","183.9","1s22s22p63s23p63d104s24p64d105s25p64f145d46s2","re","186","1s22s22p63s23p63d104s24p64d105s25p64f145d56s2","os","190","1s22s22p63s23p63d104s24p64d105s25p64f145d66s2","ir","192","1s22s22p63s23p63d104s24p64d105s25p64f145d76s2","pt","195","1s22s22p63s23p63d104s24p64d105s25p64f145d96s1","au","197","1s22s22p63s23p63d104s24p64d105s25p64f145d106s1","hg","200","1s22s22p63s23p63d104s24p64d105s25p64f145d106s2","tl","204","1s22s22p63s23p63d104s24p64d105s25p64f145d106s26p1","pb","207","1s22s22p63s23p63d104s24p64d105s25p64f145d106s26p2","bi","208.5","1s22s22p63s23p63d104s24p64d105s25p64f145d106s26p3","po","209","1s22s22p63s23p63d104s24p64d105s25p64f145d106s26p4","at","210","1s22s22p63s23p63d104s24p64d105s25p64f145d106s26p5","rn","222","1s22s22p63s23p63d104s24p64d105s25p64f145d106s26p6"]]
def find(ntk,mod):
    c=0
    cauhinh=0
    name=""
    for i in hoa_cauhinh:
        for j in i:
            if mod==1:
                try:
                    o=float(j)
                    if ntk>=c:
                        if ntk<=o:
                            oo=(o-c)/2+c
                            if ntk>=oo:
                                return name
                            else:
                                return namee
                    c=o
                    namee=name
                except ValueError:
                    name=j
            elif mod==2:
                if cauhinh==1:
                    cauhinh=j
                    return cauhinh
                try:
                    o=float(j)
                    if ntk>c:
                        if ntk<=o:
                            cauhinh=1
                    c=o
                except ValueError:
                    name=j
print("1.Tìm Nguyên tử khối biết tổng 3 hạt và số hạt không mang điện ít hơn bao nhiêu: ")
try:
    typee=int(input("Nhập tùy chọn: "))
    if typee==1:
        tong=float(input("Nhập Tổng số hạt: "))
        kmangdien=float(input(" Hạt không mang điện ít hơn bao nhiu: "))
        n2=tong-kmangdien
        n=n2/2
        p=(tong-n)/2
        print("    _|2p+n=",tong,"\n     |2p-n=",kmangdien,"\n\n <=>_|2n=",tong-kmangdien,"\n     |2p-n=",kmangdien,"\n\n <=>_|n=",n,"\n     |p=",p,"\n\n Vậy p = e =",p,"hạt, n =",n,"hạt Ta có số khối của nguyên tử là:\n n + p = ",n,"+",p,"=",n+p,"(đcV)\n Là nguyên tử:",find(n+p,1),"có cấu hình là:\n", find(n+p,2))
except ValueError:
    print("Bạn chỉ có thể nhập số nguyên")