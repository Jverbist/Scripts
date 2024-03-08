from threading import Thread
from threading import Event
import time

# class TermLoading is from the snippet above. It is a class that creates a loading animation in the terminal.
class TermLoading():
    def __init__(self):
        self.message = ""
        self.finish_message = ""
        self.__failed = False
        self.__finished = False
        self.failed_message = ""
        self.__threadEvent = Event()
        self.__thread = Thread(target=self.__loading, daemon=True)
        self.__threadBlockEvent = Event()

    @property
    def finished(self):
        return self.__finished

    @finished.setter
    def finished(self, finished):
        if isinstance(finished, bool):
            self.__finished = finished
            if finished:
                self.__threadEvent.set()
                time.sleep(0.1)
        else:
            raise ValueError

    @property
    def failed(self):
        return self.__failed

    @failed.setter
    def failed(self, failed):
        if isinstance(failed, bool):
            self.__failed = failed
            if failed:
                self.__threadEvent.set()
                time.sleep(0.1)
        else:
            raise ValueError

    def show(self, loading_message: str, finish_message: str = '✅ Finished', failed_message='❌ Failed'):
        self.message = loading_message
        self.finish_message = finish_message
        self.failed_message = failed_message
        self.show_loading()

    def show_loading(self):
        self.finished = False
        self.failed = False
        self.__threadEvent.clear()
        if not self.__thread.is_alive():
            self.__thread.start()
        else:
            self.__threadBlockEvent.set()

    def __loading(self):
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        i = 0
        while True:
            print('')
            while not self.finished and not self.failed:
                i = (i + 1) % len(symbols)
                print('\r\033[K%s %s' % (symbols[i], self.message), flush=True, end='')
                self.__threadEvent.wait(0.1)
                self.__threadEvent.clear()
            if self.finished is True and not self.failed:
                print('\r\033[K%s' % self.finish_message, flush=True)
            else:
                print('\r\033[K%s' % self.failed_message, flush=True)
            print('')
            self.__threadBlockEvent.wait()
            self.__threadBlockEvent.clear()



def importUsernames(usernamefile):
    usernames = []  # Initialize an empty list to store usernames
    try:
        read_file = open(usernamefile, "r") # Open the file in read mode
        usernames = read_file.readlines()
        read_file.close()

        return usernames
    except FileNotFoundError:
        print(f"The file '{usernamefile}' was not found.")
        return None  # Return None to indicate failure
    except PermissionError:
        print(f"Permission denied while trying to read the file '{usernamefile}'.")
        return None  # Return None to indicate failure
    except Exception as e:
        print("An error occurred:", e)
        return None  # Return None to indicate failure

def randomizeUsernames(usernames):
    import random
    random.shuffle(usernames)
    return usernames

def exportUsernames(usernames):
    try:
        write_file = open('UsernamesRandomized.txt', 'w')
        for username in usernames:
            write_file.write(username)
        write_file.close()
    except PermissionError:
        print("Permission denied while trying to write to the file.")
    except Exception as e:
        print("An error occurred:", e)

usernamefile = input("Enter the name of the file containing the usernames: ")
animation: TermLoading = TermLoading()
animation.show("Opening file...")
time.sleep(2)
animation.finished = True

usernames = importUsernames(usernamefile)  # Assign the returned value to a variable
if usernames:
    animation: TermLoading = TermLoading()
    animation.show("Randomizing usernames...")
    time.sleep(2)
    animation.finished = True
    randomized_usernames = randomizeUsernames(usernames)
    animation: TermLoading = TermLoading()
    animation.show("Writing Randomized to new file UsernamesRandomized.txt... ")
    time.sleep(2)
    animation.finished = True
    exportUsernames(randomized_usernames)
else:
    print("Failed to import usernames. Exiting.")
