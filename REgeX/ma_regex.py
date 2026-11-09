import builtins
# customize print function
_original_print = builtins.print
def custom_print(*args,**kwargs):
    _original_print('-'*50)
    _original_print(*args,**kwargs)
    _original_print()

builtins.print = custom_print
########################################################
s = 'foo123bar'
print('Contain->','123' in s)
print('Find->',s.find('123'))
print('index'.title(),s.index('123'))
########################################################
import re

print('regex search->',re.search('123',s))

span = re.search('123',s).span()
print('get span of s->',s[span[0]:span[1]])

print('ba[artz]',re.search('ba[artz]','foobarqux'))

print(re.search(r'bar$','foobar'))

print(re.search(r'foo\**bar','foo****bar'))

print(re.search(r'(foo(bar)?)+(\d\d\d)*','foofoobar123'))

############################

text1 = 'لطفاً با 09123456789 تماس بگیرید یا به 09351112233 پیام دهید. شماره دفتر 02144556677 است.'
re_text1 = re.search(r'09\d{9}',text1)
print('text_1->',re_text1)

text2 = 'یک روز عالی در #طبیعت_گردی با دوستان! جای بقیه خالی. #تهران #1402'
re_text2 = re.findall(r'(#\w+)',text2)

print('text_2->',re_text2)

text3 = 'لپ‌تاپ به قیمت $1200 و موس به قیمت $25 فروخته شد اما تخفیف 10 درصدی شامل آنها نشد'
re_text3 = re.findall(r'\$\d+',text3)
print('txt_3->',re_text3)

text4 = 'تاریخ ثبت نام 2023/11/05 است و پایان دوره 2024/02/14 خواهد بود. فرمت 1402/1/1 اشتباه است'
re_text4 = re.findall(r'\d{4}/\d{2}/\d{2}',text4)
print('text_4->',re_text4)


text5 = 'این یک <b>متن مهم</b> است و این <b>یکی دیگر</b>.'
re_txt5 = re.findall(r'(<b>.*?</b>)',text5)
print(re_txt5)


# Top 10 Pattern