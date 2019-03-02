import threading

# Use a global Lock instance for protecting std output
# from getting jumbled up

print_lock = threading.Lock()

def safeprint(msg):
  with print_lock:
    print(msg)

class UpdateFile(threading.Thread):
  file_sem = threading.Semaphore()
  file_event = threading.Event()
  def __init__(self, updatefile, id):
    threading.Thread.__init__(self, name = 'Thread_' + str(id))
    self.updatefile = updatefile
    self.id = id
  def run(self):
    UpdateFile.file_event.wait()
    with UpdateFile.file_sem:
      safeprint(f'{self.name} starting execution');
      with open(self.updatefile + '.txt','a+') as file:
          file.write(self.name + '\n')
      safeprint(f'{self.name} executed');
  @classmethod
  def runall(cls):
    cls.file_event.set()
    cls.file_event.clear()
	
threads = [];
	
for x in range(1,9):
  threads.append(UpdateFile(r'c:\temp\updatefile', x))
  
for t in threads:
  safeprint(f'Starting thread {t.name}')
  t.start()
  safeprint(f'Thread {t.name} started') 

print(f'Running all threads') 
UpdateFile.runall()
  
for t in threads:
  safeprint(f'Waiting on thread {t.name} to finish')
  t.join()
  safeprint(f'Thread {t.name} finished')

safeprint('Thread execution complete')
