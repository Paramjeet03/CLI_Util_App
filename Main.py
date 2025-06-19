from File_operation import FileOperation
from Math_utility import Math_util
from Text_Utilities import Text_Util
from datetime import datetime

class Main_menu:
    def __init__(self):
        self.option = ""

    def Welcome(self):
            print("\n" + "=" * 60)
            print("🧰".center(60))
            print("   PYTHON UTILITY APP - Dominate the World".center(60))
            print("🧰".center(60))
            print("=" * 60)
            print("Select a utility category to continue:\n")
            print("  1. 📁 File Operations        - Read, Create, or Delete files")
            print("  2. 🔢 Math Utilities         - Factorial, Prime Check, etc.")
            print("  3. 📝 Text Utilities         - Upper/lower,Reverse,Word_Count")
            print("  4. ❌ Exit                   - Close the application")
            print("-" * 60)

            
            User_name=input("Enter Your Name ")
            with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Utilty_And_logging_app\Log.txt","w") as F:
                F.writelines("-" * 60)
                F.writelines(User_name)
                F.writelines("User Enter at "+str(datetime.now())+"/n")
                F.close()
            
            
            self.option = input("Enter your choice (1-4): ").strip()
            while self.option not in ["1", "2", "3", "4"]:
                self.option = input("Enter a valid option (1/2/3/4): ").strip()

            if self.option == "1":
                with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Utilty_And_logging_app\Log.txt","a") as F:
                    F.writelines("Select File Operation"+"/n")
                    F.close()
                self.File_wale_kaam()
            elif self.option == "2":
                with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Utilty_And_logging_app\Log.txt","a") as F:
                    F.writelines("Select Math Operation"+"/n")
                    F.close()
                self.Math_wale_kaam()
            elif self.option == "3":
                with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Utilty_And_logging_app\Log.txt","a") as F:
                    F.writelines("Select Text Operation"+"/n")
                    F.close()
                self.Text_wale_kaam()
            elif self.option == "4":
                with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Utilty_And_logging_app\Log.txt","a") as F:
                    F.writelines("User Exit at :- "+str(datetime.now())+"/n")
                    F.close()
                print("👋 Thank you for using the app.")
            with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Utilty_And_logging_app\Log.txt","a") as F:
                F.writelines("User Exit at :- "+str(datetime.now())+"/n")
                F.writelines("\n"+"-" * 60)
                F.close()

    def File_wale_kaam(self):
            print("=" * 60)
            print("📁 FILE OPERATIONS MENU".center(60))
            print("=" * 60)
            print("  1. Read File")
            print("  2. Create/Write File")
            print("  3. Delete File")
            print("  4. 🔙 Return to Main Menu")
            print("-" * 60)

            option_f = input("Enter your choice (1-4):- ").strip()
            while option_f not in ["1", "2", "3", "4"]:
                option_f = input("Enter a valid option (1/2/3/4):- ").strip()

            if option_f == "4":
                print("🔙 Returning to Main Menu...\n")
                self.Welcome()

            f = FileOperation()
            f.set_path()

            if option_f == "1":
                f.read_file()
            elif option_f == "2":
                f.write_file()
            elif option_f == "3":
                f.delete_file()

    
    def Text_wale_kaam(self):
        print("=" * 60)
        print("📝 TEXT UTILITIES MENU".center(60))
        print("=" * 60)
        print("  1. Word Count")
        print("  2. Convert to UPPERCASE or Lowercase")
        print("  3. Reverse Text")
        print("  4. 🔙 Return to Main Menu")
        print("-" * 60)

        option = input("Enter your choice (1-5):- ").strip()
        while option not in ["1", "2", "3", "4", "5"]:
            option = input("Enter a valid option (1/2/3/4/5):- ").strip()

        if option == "4":
            print("🔙 Returning to Main Menu...\n")
            self.Welcome()
        t = Text_Util()
        text = input("Enter your text:- ")

        if option == "1":
            t.Word_count(self,text)
        elif option == "2":
            case_u_l=input("Enter ur case upper/lower :- ").strip()
            t.case_converter(text,case_u_l)
        elif option == "3":
            t.reverse_text(text)


    def Math_wale_kaam(self):
        print("=" * 60)
        print("🧮 MATH OPERATIONS MENU".center(60))
        print("=" * 60)
        print("  1. Factorial")
        print("  2. Prime Check")
        print("  3. Calculator")
        print("  4. 🔙 Return to Main Menu")
        print("-" * 60)
        m=Math_util()

        option_M = input("Enter your choice (1-4):- ").strip()
        while option_M not in ["1", "2", "3", "4"]:
            option_M = input("Enter a valid option (1/2/3/4):- ").strip()

        if option_M == "4":
            print("🔙 Returning to Main Menu...\n")
            self.Welcome()

        if option_M == "1":
            n = int(input("Enter a number: "))
            result = m.factorial(n)
            print(f"✅ Factorial of {n} is: {result}")

        elif option_M == "2":
            n = int(input("Enter a number: "))
            result = m.is_prime(n)
            print(f"✅ Is {n} a prime number? {'Yes' if result else 'No'}")

        elif option_M == "3":
            n1 = float(input("Enter 1st number: "))
            n2 = float(input("Enter 2nd number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            result = m.calculator(n1, n2, op)
            print(f"✅ Result: {result}")


if __name__ == "__main__":
   app= Main_menu()
   app.Welcome()

            