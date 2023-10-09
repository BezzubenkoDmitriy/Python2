import os


def batch_rename_files(source_dir, end_name, num_digits, source_extension, destination_extension, name_range):
    matching_files = [f for f in os.listdir(source_dir) if f.endswith(source_extension)]

    for i, filename in enumerate(matching_files, 1):
        name_part = filename[name_range[0] - 1:name_range[1]]
        new_name = f"{name_part}_{end_name}{str(i).zfill(num_digits)}.{destination_extension}"

        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(source_dir, new_name)

        os.rename(source_path, destination_path)


source_directory = 'files_to_rename'
desired_end_name = 'newname'
num_digits_in_ordinal = 3
source_file_extension = '.one'
destination_file_extension = 'doc'
name_range = (3, 6)

batch_rename_files(
    source_directory,
    desired_end_name,
    num_digits_in_ordinal,
    source_file_extension,
    destination_file_extension,
    name_range
)