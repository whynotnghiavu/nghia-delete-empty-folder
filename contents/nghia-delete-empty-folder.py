import os


def delete_empty_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"🚀 Đã xóa thư mục trống: {dir_path}")


folder_path = r"input-nghia-delete-empty-folder"
folder_path = r"/home/vvn20206205/Desktop/input-nghia-delete-empty-folder"
folder_path = r"/home/vvn20206205/Desktop/input"
folder_path = r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu"
folder_path = r"C:\Users\vvn20206205\Desktop\ddddddddddddd"
folder_path = r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu"


if not os.path.exists(folder_path):
    print(f"Không có thư mục {folder_path}")
    # os.mkdir(folder_path)


delete_empty_folder(folder_path)
