import logging
import random
import time
from pathlib import Path
logging.basicConfig(
    level=logging.DEBUG,
    filename='ma_logging.txt',
    filemode='w',
    format='{asctime} - {levelname} - {message}',
    datefmt='%m-%d %H:%M:%S',
    encoding='utf-8',
    style='{'
)

names = ["matin",'ali','reza','sobhan','mohammad','amir','kasra']
for i in range(25):
    random.shuffle(names)
    for name in names:
        if name == 'matin':
            logging.warning(f'Round {i+1} -{name}`s turn')
        else:
            logging.info(f'Round {i+1} -{name}`s turn')
            
            
txt = Path('ma_logging.txt')

with txt.open('r',encoding='utf-8') as file:
    for line in file.readlines():
        if 'WARNING' in line and int(line[33:35]) % 2 == 0 :
            # print(line)
            pass
            
print('create a custom logger'.title())
file_name = __file__[(__file__.rfind('/')) + 1:]
logger = logging.getLogger(file_name)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('ma_logging.log','w',encoding='utf-8')

console_handler.setLevel(logging.ERROR)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '{asctime} - {name} - {message}',
    style='{',
    datefmt='%y-%m-%d %H:%M:%S'
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
console_handler.addFilter(lambda x: x.levelname == 'CRITICAL')

print('test Logger'.title())

logger.info("start ma_logging.py")
logger.error("error in ma_logging.py")
logger.critical('python file crashed')


# use our custom Json loggin Handler
print('Test Json_Logging_Handler')
from json_formatter import json_logger
try:
    while True:
        for i in range(25):
            random.shuffle(names)
            
            for name in names:
                if name == 'matin':
                        json_logger.warning(f'Round {i+1} - {name}`s turn')
                else:
                        json_logger.info(f'Round {i+1} - {name}`s turn')
        time.sleep(1)
        
    
except Exception:
    pass