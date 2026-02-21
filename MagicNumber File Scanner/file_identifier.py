import os
import filetype

# Extension categories
audio_ext = ['mp3', 'wav']
video_ext = ['mp4', 'flv', 'mkv', 'avi']
doc_ext = ['pdf', 'doc', 'docx', 'xls', 'ppt', 'txt']
photo_ext = ['jpg', 'jpeg', 'png', 'img', 'tmb']
exe_ext = ['exe']

def classify_by_extension(extension):
    if extension in audio_ext:
        return "Audio File"
    elif extension in video_ext:
        return "Video File"
    elif extension in doc_ext:
        return "Document File"
    elif extension in photo_ext:
        return "Image File"
    elif extension in exe_ext:
        return "Executable File"
    else:
        return "Miscellaneous File"

def scan_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    print("\nScanning Folder:", folder_path)
    print("-" * 50)

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isdir(full_path):
            print(f"\n{file} → Folder")
            continue

        print(f"\nFile: {file}")

        # Extension detection
        file_name, file_ext = os.path.splitext(file)
        file_ext = file_ext.replace('.', '').lower()
        extension_type = classify_by_extension(file_ext)

        print("Extension Type:", extension_type)

        # Magic number detection
        kind = filetype.guess(full_path)

        if kind is None:
            print("Magic Detection: Unknown file type")
            continue

        print("Magic Extension:", kind.extension)
        print("MIME Type:", kind.mime)

        # Compare extension with magic
        if file_ext != kind.extension:
            print("WARNING The Extension does NOT match real file type!")
        else:
            print("Extension matches real file typepy   ")

    print("\nScan Completed")

if __name__ == "__main__":
    folder_path = input("Enter folder path to scan: ")
    scan_folder(folder_path)
