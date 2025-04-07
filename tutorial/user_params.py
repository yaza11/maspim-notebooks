import os
import shutil


def checkpoint(folder: str, class_name: str | None, tag: str | None = None) -> str:
    if (folder in ('full example', 'small example')) and (class_name in ('MSI', 'Spectra', 'TimeSeries')):
        d_folder = f'{folder}.d'  
    else:
        d_folder = ''
    if class_name is None:
        name = ''
    elif tag is not None:
        name = f'{class_name}_{tag}.pickle'
    else:
        name = f'{class_name}.pickle'
    return os.path.join(path_folder_workshop, 'checkpoints', folder, d_folder, name)


def copy_checkpoint(chapter: int | float):
    if chapter == 3:
        source = checkpoint('full example', 'ImageClassified')
        destination = os.path.join(path_folder_real_data, 
                                   os.path.basename(source))
        shutil.copyfile(source, destination)
        print(f'copied {source} to {destination}')
    elif chapter in (4, 5):
        source = checkpoint('full example', 'SampleImageHandlerMSI')
        destination = os.path.join(path_folder_real_data, 
                                   os.path.basename(source))
        shutil.copyfile(source, destination)
        print(f'copied {source} to {destination}')
        source = checkpoint('full example', 'ImageSample')
        destination = os.path.join(path_folder_real_data, 
                                   os.path.basename(source))
        shutil.copyfile(source, destination)
        print(f'copied {source} to {destination}')
        source = checkpoint('full example', 'ImageROI')
        destination = os.path.join(path_folder_real_data, 
                                   os.path.basename(source))
        shutil.copyfile(source, destination)
        print(f'copied {source} to {destination}')
        source = checkpoint('full example', 'ImageClassified')
        destination = os.path.join(path_folder_real_data, 
                                   os.path.basename(source))
        shutil.copyfile(source, destination)
        print(f'copied {source} to {destination}')
    elif chapter in (5, 6):
        # MSI with images
        source = checkpoint('full example', 'MSI', 'with_images')
        destination = os.path.join(path_folder_real_data, 
                                   d_folder_real_data, 
                                   os.path.basename(source))
        shutil.copyfile(source, destination)
        print(f'copied {source} to {destination}')
        source = checkpoint('full example', 'ImageClassified')
        destination = os.path.join(path_folder_real_data,
                                   os.path.basename(source))
        shutil.copyfile(source, destination)
        print(f'copied {source} to {destination}')
    else:
        raise NotImplementedError(f'{chapter=} missing')


path_folder_workshop = os.path.dirname(os.path.dirname(__file__))

data_folder = 'data'

path_folder_test_data = os.path.join(path_folder_workshop, data_folder, 'small example')
d_folder_test_data = "small example.d"

path_folder_real_data = os.path.join(path_folder_workshop, data_folder, 'full example')
d_folder_real_data = "full example.d"

path_age_model = r'Data\64-480_age.txt'

path_xray_long = os.path.join(path_folder_workshop, data_folder, 'X-ray', 'xray_long.tif')

path_xrf_data = os.path.join(path_folder_workshop, data_folder, 'S0343c XRF')
