import os
import shutil
from datetime import datetime


project_name_file = os.path.join(os.path.expanduser('~'), 'project_name.txt')

def load_project_name():
    if os.path.exists(project_name_file):
        with open(project_name_file, 'r') as file:
            return file.read().strip()
    return None

def save_project_name(project_name):
    with open(project_name_file, 'w') as file:
        file.write(project_name)

def organise_screenshots(project_name):
    desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
    screenshot_folder = os.path.join(os.path.expanduser('~'), 'Downloads', 'screenshots')

    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
        print(f'Created screenshot folder: {screenshot_folder}')

    screenshot_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    count = 0

    for filename in os.listdir(desktop_folder):
        if filename.lower().endswith(screenshot_extensions):
            src_path = os.path.join(desktop_folder, filename)

            try:
                date_str = filename.split('Screenshot ')[1].split(' at ')[0]
                date_created = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d-%m-%Y")
            except IndexError:
                print(f"Skipping file {filename} as it doesn't match the expected format.")
                continue
            except ValueError:
                print(f"Skipping file {filename} due to invalid date format.")
                continue

            dest_folder = os.path.join(screenshot_folder, date_created + " : " + project_name)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                print(f'Created folder: {dest_folder}')

            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            count += 1
            print(f'Moved: {src_path} to {dest_path}')

    temp_file = os.path.join(os.path.expanduser('~'), 'screenshot_count.txt')
    with open(temp_file, 'w') as file:
        file.write(str(count))

    print(f'Saved count {count} to {temp_file}')
    print('Organizing screenshots completed.')

if __name__ == "__main__":
    organise_screenshots()