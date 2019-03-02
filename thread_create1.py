import threading, os, contextlib

# Define CopyFile function for copying source files to destination files

def CopyFile(source, dest, id):
#    print(f'Thread{id} starting execution');
    with open(source + str(id) + '.txt','rb') as sourcefile:
      with open(dest + str(id) + '.txt','wb') as destfile:
        data = sourcefile.read()
        destfile.write(data)
#    print(f'Thread{id} executed');

# Delete any existing destination files

for x in range(1,9):
    with contextlib.suppress(FileNotFoundError):
      os.remove(r'c:\temp\destfile' + str(x) + '.txt')

# Initialize list for storing Thread instances
	
threads = [];

# Create 8 Thread instances, using the CopyFile function as the target callable
	
for x in range(1,9):
  threads.append(threading.Thread(target = CopyFile, name = 'Thread_' + str(x), args = (r'c:\temp\sourcefile', r'c:\temp\destfile', x)))

# Start the threads
  
for t in threads:
  print(f'Starting thread {t.name}')
  t.start()
  print(f'Thread {t.name} started') 

# Wait for the threads to finish executing
  
for t in threads:
  print(f'Waiting on thread {t.name} to finish')
  t.join()
  print(f'Thread {t.name} finished')

print('Thread execution complete')
