class Versenyző:
    def __init__(self, list):
        self.csapat = list[0]
        self.nev = list[1]
        self.eletkor = list[2]
        self.palya = list[3]
        self.kor_ido = list[4]
        self.kor = list[5]
        self.in_sec = self.showInSec(list)

    def showInSec(self, list):
        h = int(list[4].split(":")[0])
        m = int(list[4].split(":")[1])
        s = int(list[4].split(":")[2])

        temp = s
        temp += m*60
        temp += h*3600
        return temp

def MakingObjects():
    list = []
    temp = ImportFromTXT()
    for i in temp:
        list.append(Versenyző(i.split(";")))
    return list

def ImportFromTXT():
    f = open("autoverseny.csv", "r", encoding="UTF8").read()
    lines = f.split("\n")
    return lines[1:len(lines)]

def feladat4(list):
    for i in list:
        if i.nev == "Fürge Ferenc" and i.palya == "Gran Prix Circuit" and i.kor == "3":
            return i.in_sec

def feladat6(list, nev):
    temp_id = 0
    if list[0].nev != nev:
        for i in range(len(list)):
            if list[i].nev == nev:
                temp_id = i
        if temp_id == 0:
            return "Nincs ilyen versenyző az állományban!"    

    for i in range(len(list)):
        if list[i].nev == nev and list[temp_id].in_sec > list[i].in_sec:
            temp_id = i
    
    return f"{list[temp_id].palya}, {list[temp_id].kor_ido}"

def main():
    main_list = MakingObjects()
    print(f"3. feladat: {len(main_list)}")
    print(f"4. feladat: {feladat4(main_list)} másodperc")
    print(f"5. feladat:")
    versenyzo_nev = input(f"Kérem egy versenyző nevét:")
    print(f"6. feladat: {feladat6(main_list, versenyzo_nev)}")
    
main()
