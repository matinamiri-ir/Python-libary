from pathlib import Path

path = Path()

ma_pl = Path('./MA_pathlib').mkdir(parents=True,exist_ok=True)

# print(ma_pl) # return none 

print('\nmove courrent file to MA_pathlibb dir\n')
try:
    Path(__file__).resolve().move_into('./MA_pathlib')
except:
    pass


print('\nCreate a txt file\n')

MA_path = Path(__file__).parent
txt_path = MA_path / 'pathlib.txt'
txt_path.touch(exist_ok=True)

with txt_path.open('w',encoding='utf-8') as file:
    for i in range(3230):
        if i % 7 == 0 :
            file.write(f'\tthe line number {i}\n')
        else:
            file.write(f'the line number {i}\n')
        
print('\n----work with file-----\n')
        
with txt_path.open('r+',encoding='utf-8') as file:
    for line in file:
        if line.startswith('t'):
            line.write()
    
    
    



