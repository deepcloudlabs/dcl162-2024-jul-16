"""
Thread Programming
i. multitasking
   a. process -> application -> cpu, virtual memory, disk, ...
                                     Text, Data, Stack, Heap
            parent process -- fork --> child process
   b. thread  -> process Text, Data, Stack, Heap
                      t1             S(1M)
                      t2             Stack
                      t3             Stack
                 context -> RAM
                 RAM     -> context
                 context switching
   cpu -> multicore
   single cpu -> concurrent programming
   multicore -> concurrent programming + parallel programming
        data parallelism vs task parallelism

   MultiProcess-MultiThread
"""