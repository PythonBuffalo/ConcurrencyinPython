import multiprocessing.dummy, os, contextlib, collections

# Define CopyFile function for copying source files to destination files
# This version uses a thread pool for completing the work

def CopyFile(work):
#    print(f'Thread{id} starting execution');
    with open(work.sourcefile + str(work.id) + '.txt','rb') as sourcefile:
        with open(work.destfile + str(work.id) + '.txt','wb') as destfile:
           data = sourcefile.read()
           destfile.write(data)        
#    print(f'Thread{id} executed');

# Delete any existing destination files

for x in range(1,9):
    with contextlib.suppress(FileNotFoundError):
      os.remove(r'c:\temp\destfile' + str(x) + '.txt')

# Create the thread pool with 4 worker threads
	
threadpool = multiprocessing.dummy.Pool(4)

# Create a list of named tuples (Work) to process

print('Creating work items')

Work = collections.namedtuple('Work', ['sourcefile', 'destfile', 'id'])

sourcefile = r'c:\temp\sourcefile'
destfile = r'c:\temp\destfile'

workitems = [Work(sourcefile, destfile, 1),
    Work(sourcefile, destfile, 2),
    Work(sourcefile, destfile, 3),
    Work(sourcefile, destfile, 4),
    Work(sourcefile, destfile, 5),
    Work(sourcefile, destfile, 6),
    Work(sourcefile, destfile, 7),
    Work(sourcefile, destfile, 8)]

# Fire off the map function on all of the work items

print('Starting Map execution')

threadpool.map(CopyFile, workitems)
threadpool.close()
threadpool.join()

print('Map execution complete')
