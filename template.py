import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'textSummarizer'

files_list = [
    '.github/workflows/.gitkeep', # for CI/CD deployment
    f'src/{project_name}/__init__.py', # local package
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yml',
    'params.yml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

for fp in files_list:
    filepath = Path(fp)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != '':
        logging.info(f'Creating directory {file_dir} ...')
        os.makedirs(file_dir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        logging.info(f'Creating file {filepath} ...')
        with open(filepath, 'w'):
            pass
    else:
        logging.info(f'File {filepath} already exists')
    