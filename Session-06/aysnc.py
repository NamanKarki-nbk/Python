#async io is our chouce for tasks that wait a lot like network requests or reading files.
#IT EXCELS ON HANDLING MANY TASKS COnCURRENTLY WITHOUT USING MUCH CPU power
#--------------------------------------------------------------------------#

#Threads are suitable for the parllel tasks that may need to wait but also share data. They can run in parallel within the same application that are I\O bind but less CPU intensive.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#For CPU heavy tasks processes are way to go.

#--------------------------------------------------#

#Event Loop in AYSNCIO


#--------------------------------#

#Task
#--> Task is a way to schedule a corutine to run as soon as possible and allows to run multiple corutine run simaltaniulsy

#--> TaskFroup() this provides builin error handling and if anyofthe task in our evenhandling fails it will automatically cancels all of the tasks making the application more robust


#---------------------------------------------------------------------------------#

#Future
#It is the promise of future result

#------------------------------------------------#

#Synchroniization
#Now these are tools that wil allow us the syncronize the execution of coroutines
#lock for cricical section
#semaphore=>A semaphore is a synchronization tool used in concurrent programming to control access to a shared resource by multiple threads or processes.
#Even-> it is something a allows basic syncronizations
#A Python Event is a synchronization tool used in multithreading or async programming to signal between threads or tasks — basically, it's a way to say: "Hey, something just happened! You can go now."

