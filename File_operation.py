import os

class FileOperation:
    def __init__(self):
        self.f_path = ""

    def set_path(self):
        self.f_path = input("Enter your file path: ")
        return self.f_path
        
    def read_file(self):
        try:
            with open(self.f_path, "r") as f:
                content = f.read()
                print("\n📄 File Content:\n", content)
        except FileNotFoundError:
            print("❌ File not found at:", self.f_path)
        except Exception as e:
            print("❌ Error reading file:", e)

    def write_file(self):
        try:
            with open(self.f_path, "w") as f:
                data = input("✍️ Enter the data to write to the file:\n")
                f.write(data + "\n")
                print("✅ Data written successfully.")
        except Exception as e:
            print("❌ Error writing to file:", e)

    def delete_file(self):
        try:
            if os.path.exists(self.f_path):
                os.remove(self.f_path)
                print("🗑️ File deleted successfully.")
            else:
                print("❌ File not found at:", self.f_path)
        except Exception as e:
            print("❌ Error deleting file:", e)

