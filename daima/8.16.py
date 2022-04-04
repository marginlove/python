#contact.txt文件在运行前必须先创建在文件目录中
import pickle  # Python的标准模块，将对象存储在文件中
class Contact:
    total_amount = 0
    contacts_dict = {}
    @classmethod # 类方法（不需要实例化类就可以被类本身调用）
    def add_contact(cls):
        name = input("请输入添加的联系人姓名：")
        if name in Contact.contacts_dict:
            print("该联系人已经存在")
        else:
            telephone = input("请输入电话号码：")
            email = input("请输入邮件：")
            address = input("请输入地址：")
            birthday = input("请输入生日：")
            label = {"tele": telephone, "email": email, "addr": address, "birth": birthday}
            Contact.contacts_dict[name] = label
            Contact.total_amount += 1
            print("添加成功，当前已有联系人{}人".format(Contact.total_amount))
    @classmethod
    def delete_contact(cls):
        name = input("请输入要删除的联系人姓名：")
        if name in Contact.contacts_dict:
            del Contact.contacts_dict[name]  # del语句用来删除某一键值对
            print(Contact.contacts_dict)
            Contact.total_amount -= 1
            print("删除成功，当前已有联系人{}人".format(Contact.total_amount))
        else:
            print("{}人不在通讯录中".format(name))
    @classmethod
    def search_contact(cls):
        name = input("请输入要搜索的联系人姓名：")
        if name in Contact.contacts_dict:
            print(Contact.contacts_dict[name])
        else:
            print("{}人不在通讯录中".format(name))
    @classmethod
    def modify_contact(cls):
        name = input("请输入要修改的联系人姓名：")
        if name in Contact.contacts_dict:
            print("修改前：")
            print(Contact.contacts_dict[name])
            modify_tele = input("请输入修改后的电话")
            modify_email = input("请输入修改后的邮件")
            modify_address = input("请输入修改后的地址")
            modify_birth = input("请输入修改后的生日")
            modify_label = {"tele": modify_tele, "email": modify_email, "addr": modify_address, "birth": modify_birth}
            Contact.contacts_dict[name] = modify_label
            print("修改后：")
            print(Contact.contacts_dict[name])
        else:
            print("{}人不在通讯录中".format(name))
    @classmethod
    def write(cls):
        f = open('contact.txt', 'wb')
        pickle.dump(Contact.contacts_dict, f)
        f.close()
    @classmethod
    def read(cls):
        file = 'contact.txt'
        try:
            f = open(file, 'rb')
            Contact.contacts_dict = pickle.load(f)
            print("已经保存联系人{}位".format(len(Contact.contacts_dict)))
            Contact.total_amount += len(Contact.contacts_dict)
            #print(Contact.contacts_dict)
            f.close()
        except EOFError:
            print("尚未保存联系人")
        except FileNotFoundError:
            f.close()

def contact_menu():
    print("欢迎来到Leaf通讯录，系统提供以下功能：\n"
          "1：添加用户 \n"
          "2：删除用户 \n"
          "3：修改信息 \n"
          "4：搜索用户 \n"
          "5：显示全部 \n"
          "6：保存退出\n")
contact_person = Contact()
contact_person.read()
while True:
    try:
        contact_menu()
        choice = int(input("请选择功能：输入对应的数字"))
        if choice == 1:  # 添加
            contact_person.add_contact()
        elif choice == 2:  # 删除
            contact_person.delete_contact()
        elif choice == 3:  # 修改
            contact_person.modify_contact()
        elif choice == 4:  # 搜索
            contact_person.search_contact()
        elif choice == 5: #显示全部
            print(Contact.contacts_dict)
        elif choice == 6:  # 退出
            contact_person.write()  # 字典中数据重写写到文件中
            break
        else:
            print("输入不合法，请重新输入")
    except ValueError:
        print("请输入相应的数字")
