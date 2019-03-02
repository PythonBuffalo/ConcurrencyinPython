import threading

# Define filetoupdate Thread-descendant class for updating a file with the thread name
# run method does the heavy lifting and is automatically called by the Thread.start method

class UpdateFile(threading.Thread):
  file_sem = threading.Semaphore()
  def __init__(self, updatefile, id):
    threading.Thread.__init__(self, name = 'Thread_' + str(id))
    self.updatefile = updatefile
    self.id = id
  def run(self):
    UpdateFile.file_sem.acquire()
    try:
      # print(f'{self.name} starting execution');
      with open(self.updatefile + '.txt','a+') as file:
          file.write(self.name + '\n')
      # print(f'{self.name} executed');
    finally:
      UpdateFile.file_sem.release()
	
threads = [];
	
for x in range(1,9):
  threads.append(UpdateFile(r'c:\temp\updatefile', x))
  
for t in threads:
  print(f'Starting thread {t.name}')
  t.start()
  print(f'Thread {t.name} started') 
  
for t in threads:
  print(f'Waiting on thread {t.name} to finish')
  t.join()
  print(f'Thread {t.name} finished')

print('Thread execution complete')
