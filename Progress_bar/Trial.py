#%%
import time
for i in range(5):
    time.sleep(.3)
    print(str(i)*10)

#%%
import time
for i in range(5):
    time.sleep(.3)
    print(str(i)*10,end='')
print()
# %%
import time
import sys
for i in range(5):
    time.sleep(.3)
    print(str(i)*10,end='')
    sys.stdout.flush()
print()
# %%
import time
import sys
for i in range(5):
    time.sleep(.3)
    print('\r',end='')
    print(str(i)*10,end='')
    sys.stdout.flush()
print()
# %%
import time
import sys
n=10
for i in range(n):
    time.sleep(0.3)
    sys.stdout.write('\r')
    sys.stdout.write(str(i)*(n-i))
    sys.stdout.flush()
sys.stdout.write('\n')

# %%
