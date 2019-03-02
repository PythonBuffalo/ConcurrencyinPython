import threading, os, contextlib, queue, collections

# Define CopyFile function for copying source files to destination files
# This version uses a queue for determining what work to do

workqueue = queue.Queue()

def CopyFile():
#    print(f'Thread{id} starting execution');
    while True:
        work = workqueue.get()
        if work is None:
            break
        with open(work.sourcefile + str(work.id) + '.txt','rb') as sourcefile:
          with open(work.destfile + str(work.id) + '.txt','wb') as destfile:
            data = sourcefile.read()
            destfile.write(data)        
        workqueue.task_done()
#    print(f'Thread{id} executed');

# Delete any existing destination files

for x in range(1,9):
    with contextlib.suppress(FileNotFoundError):
      os.remove(r'c:\temp\destfile' + str(x) + '.txt')

# Initialize list for storing Thread instances
	
threads = [];

# Create 4 Thread instances, using the CopyFile function as the target callable
	
for x in range(1,5):
  threads.append(threading.Thread(target = CopyFile, name = 'Thread_' + str(x)))

# Start the threads
  
for t in threads:
  print(f'Starting thread {t.name}')
  t.start()
  print(f'Thread {t.name} started') 

# Add some named tuples (Work) to the queue

Work = collections.namedtuple('Work', ['sourcefile', 'destfile', 'id'])

sourcefile = r'c:\temp\sourcefile'
destfile = r'c:\temp\destfile'

workqueue.put(Work(sourcefile, destfile, 1))
workqueue.put(Work(sourcefile, destfile, 2))
workqueue.put(Work(sourcefile, destfile, 3))
workqueue.put(Work(sourcefile, destfile, 4))
workqueue.put(Work(sourcefile, destfile, 5))
workqueue.put(Work(sourcefile, destfile, 6))
workqueue.put(Work(sourcefile, destfile, 7))
workqueue.put(Work(sourcefile, destfile, 8))

# Wait for the threads to finish the work

workqueue.join()

# Send each thread a None to cause them to break out of their execution loop

for t in threads:
    workqueue.put(None)

# Wait for the threads to finish executing
  
for t in threads:
  print(f'Waiting on thread {t.name} to finish')
  t.join()
  print(f'Thread {t.name} finished')

print('Thread execution complete')
