from File_operation import FileOperation
from Math_utility import Math_util
from Text_Utilities import Text_Util

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
            print("  3. 📝 Text Utilities         - (Coming soon...)")
            print("  4. ❌ Exit                   - Close the application")
            print("-" * 60)

            self.option = input("Enter your choice (1-4): ").strip()
            while self.option not in ["1", "2", "3", "4"]:
                self.option = input("Enter a valid option (1/2/3/4): ").strip()

            if self.option == "1":
                self.File_wale_kaam()
            elif self.option == "2":
                self.Math_wale_kaam()
            elif self.option == "3":
                self.Text_wale_kaam()
            elif self.option == "4":
                print("👋 Thank you for using the app.")

    def File_wale_kaam(self):
            print("=" * 60)
            print("📁 FILE OPERATIONS MENU".center(60))
            print("=" * 60)
            print("  1. Read File")
            print("  2. Create/Write File")
            print("  3. Delete File")
            print("  4. 🔙 Return to Main Menu")
            print("-" * 60)

            option_f = input("Enter your choice (1-4): ").strip()
            while option_f not in ["1", "2", "3", "4"]:
                option_f = input("Enter a valid option (1/2/3/4): ").strip()

            if option_f == "4":
                print("🔙 Returning to Main Menu...\n")

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

        option = input("Enter your choice (1-5): ").strip()
        while option not in ["1", "2", "3", "4", "5"]:
            option = input("Enter a valid option (1/2/3/4/5): ").strip()

        if option == "5":
            print("🔙 Returning to Main Menu...\n")
        t = Text_Util()
        text = input("Enter your text: ")

        if option == "1":
            t.Word_count(self,text)
        elif option == "2":
            case_u_l=input("Enter ur case upper/lower ").strip()
            t.case_converter(text,case_u_l)
        elif option == "3":
            t.reverse_text(text)
            