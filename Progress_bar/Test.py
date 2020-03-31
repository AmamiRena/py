import progress_b
import time
n=50
flag=input('1~4: ')
if '1' in flag:
    print('='*79)
    bar=progress_b.progBar(n,monitor=True)
    for i in range(n):
        time.sleep(.1)
        bar.update()
    print(bar)

if '2' in flag:
    print('='*79)
    for i in progress_b.prog_bar(range(n)):
        time.sleep(.1)

if '3' in flag:
    print('='*79)
    bar=progress_b.progPercent(n,monitor=True)
    for i in range(n):
        time.sleep(.1)
        bar.update()
    print(bar)

if '4' in flag:
    print('='*79)
    for i in progress_b.prog_percent(range(n)):
        time.sleep(.1)