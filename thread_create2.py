import threading, os, contextlib

# Define CopyFile Thread-descendant class for copying source files to destination files
# run method does the heavy lifting and is automatically called by the Thread.start method

class CopyFile(threading.Thread):
  def __init__(self, source, dest, id):
    threading.Thread.__init__(self, name = 'Thread_' + str(id))
    self.source = source
    self.dest = dest
    self.id = id
  def run(self):
    with open(self.source + str(self.id) + '.txt','rb') as sourcefile:
      with open(self.dest + str(self.id) + '.txt','wb') as destfile:
        data = sourcefile.read()
        destfile.write(data)

# Delete any existing destination files

for x in range(1,9):
    with contextlib.suppress(FileNotFoundError):
      os.remove(r'c:\temp\destfile' + str(x) + '.txt')

# Initialize list for storing CopyFile instances
	
threads = [];

# Create 8 CopyFile instances (threads)
	
for x in range(1,9):
  threads.append(CopyFile(r'c:\temp\sourcefile', r'c:\temp\destfile', x))

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
