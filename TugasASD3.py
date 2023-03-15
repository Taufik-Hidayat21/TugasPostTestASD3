#Nama : Taufik Hidayat
#NIM : 2209116097
#Kelas : Sistem Informasi B '22
from prettytable import PrettyTable
import os
import time
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None     
class linkedlist_real:
    def __init__(self):
        self.head = None
    
    def tambahdepan1(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    def deletenode(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
            # current = None #Optional statement
    def getindex(self, index):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node

            current_node = current_node.next
            current_index += 1
    def printlist1(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table = PrettyTable()
            table.field_names = ["No","Nama Narapidana"]
            current_node = self.head
            x1 = 1
            while current_node is not None:
                table.add_row([x1,current_node.data])
                x1 += 1
                current_node = current_node.next
            print(table)   
class linkedlist_insertion:
    def __init__(self):
        self.head = None
    
    def tambahdepan2(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def printlist2(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table1 = PrettyTable()
            table1.field_names = ["No","Nama Narapidana"]
            current_node = self.head
            x2 = 1
            while current_node is not None:
                table1.add_row([x2,current_node.data])
                x2 += 1
                current_node = current_node.next
            print(table1)
class linkedlist_delete:
    def __init__(self):
        self.head = None
    
    def tambahdepan3(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def printlist3(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table2 = PrettyTable()
            table2.field_names = ["No","Nama Narapidana"]
            current_node = self.head
            x3 = 1
            while current_node is not None:
                table2.add_row([x3,current_node.data])
                x3 += 1
                current_node = current_node.next
            print(table2)
listnya1 = linkedlist_real()
listnya2 = linkedlist_insertion()
listnya3 = linkedlist_delete()
def tambahdata():
        print("===Menu Tambah Data===")
        input1 = input("Masukan Nama Narapidana: ")
        # input2 = input('Masukan Nomor Narapidana: ')
        listnya1.tambahdepan1(input1)
        listnya2.tambahdepan2(input1)
def hapusdata():
    print("===Menu Hapus Data===")
    inputhapus = int(input("Masukan Nomor Narapidana : "))
    ss = listnya1.getindex(inputhapus-1)
    listnya3.tambahdepan3(ss.data)
    listnya1.deletenode(inputhapus-1)
while True:
    print('''
    Menu Yang Tersedia
    1.Tambah Data
    2.Hapus Data 
    3.Lihat Data
    4.Lihat History Data
    5.Keluar Menu
    ''')
    inputmenu = input('Masukan menu yang diinginkan: ')
    os.system('cls')
    if inputmenu == "1":
        tambahdata()
        os.system('cls')
    elif inputmenu == "2":
        listnya1.printlist1()
        hapusdata()
        os.system('cls')
    elif inputmenu == "3":
        while True:
            print('===Ini List Data Narapidana===')
            listnya1.printlist1()
            inputx = input('Keluar?(y/t) :')
            if inputx == "y":
                os.system('cls')
                break
            else:
                print()
                os.system('cls')
    elif inputmenu == "4":
        while True:
            print('''
            Menu Data History
            
            1. Narapidana Yang Pernah Masuk Lapas
            2. Narapidana Yang Keluar
            3. Keluar Menu History
            ''')
            inputhistory = input("Masukan Menu : ")
            if inputhistory == "1":
                print('Ini List Data Narapidana Yang ')
                listnya2.printlist2()
                time.sleep(2)
            elif inputhistory == "2":
                print('\n Ini List Data Deletion')
                listnya3.printlist3()
                time.sleep(2)
            elif inputhistory == "3":
                os.system('cls')
                break
            else:
                print('Input Salah')
                time.sleep(2)
                os.system('cls')
    elif inputmenu == "5":
        exit()
    else:
        print("Masukan Menu Dengan Benar")
        time.sleep(2)
        os.system('cls')
