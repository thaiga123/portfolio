import os

def organize_files():
    # Define the path to the main folder
    main_folder = "C:/File/To/Your/Path"
    
    # Ensure the main folder exists
    if not os.path.exists(main_folder):
        print(f"The folder '{main_folder}' does not exist.")
        return
    
    # Define paths for subfolders
    videos_folder = os.path.join(main_folder, "Videos")
    audios_folder = os.path.join(main_folder, "Audios")
    
    # Create subfolders if they don't exist
    if not os.path.exists(videos_folder):
        os.mkdir(videos_folder)
    if not os.path.exists(audios_folder):
        os.mkdir(audios_folder)
    
    # Iterate through files in the main folder
    for filename in os.listdir(main_folder):
        filepath = os.path.join(main_folder, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
        
        # Organize files based on their extensions
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension == ".mp4":
            destination_path = os.path.join(videos_folder, filename)
            os.rename(filepath, destination_path)
            print(f"Moved {filename} to Videos folder.")
        elif file_extension == ".mp3":
            destination_path = os.path.join(audios_folder, filename)
            os.rename(filepath, destination_path)
            print(f"Moved {filename} to Audios folder.")
        else:
            print(f"Skipped {filename} (unsupported format).")

# Call the function
organize_files()
