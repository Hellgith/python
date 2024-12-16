class Friend:
    def __init__(self, name=None, mobile=0):
        self.name = name
        self.mobile = mobile

# Implementation class
class PhoneBook:
    def __init__(self):
        self.N = 0  # Number of friends in phonebook
        self.friendList = []  # Friends in phonebook
    
    # 1. Read friends' names and mobile numbers
    def getFriendDetails(self, nof):
        self.N = nof
        for i in range(self.N):
            friend = Friend()
            print(f"Enter Friend name and mobile for Friend-{i+1}")
            name = input("Enter Name of friend::")
            mobile = int(input("Enter mobile no. of friend::"))
            friend.name = name
            friend.mobile = mobile
            self.friendList.append(friend)
        # Sort friends by name after adding all
        self.friendList.sort(key=lambda x: x.name)
    
    # 2. Display Friend Details
    def displayFriendList(self):
        print("\nThe Friend PhoneBook is:")
        for friend in self.friendList:
            print(friend.name, "  ", friend.mobile)
    
    # Binary Search - Non-recursive
    def binarySearchNonRecursive(self, name):
        left, right = 0, len(self.friendList) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.friendList[mid].name == name:
                print(f"Friend found: {self.friendList[mid].name} - {self.friendList[mid].mobile}")
                return mid
            elif self.friendList[mid].name < name:
                left = mid + 1
            else:
                right = mid - 1
        print("Friend not found.")
        return -1

    # Binary Search - Recursive
    def binarySearchRecursive(self, name, left, right):
        if left > right:
            print("Friend not found.")
            return -1
        mid = (left + right) // 2
        if self.friendList[mid].name == name:
            print(f"Friend found: {self.friendList[mid].name} - {self.friendList[mid].mobile}")
            return mid
        elif self.friendList[mid].name < name:
            return self.binarySearchRecursive(name, mid + 1, right)
        else:
            return self.binarySearchRecursive(name, left, mid - 1)
    
    # Fibonacci Search
    def fibonacciSearch(self, name):
        fib2 = 0  # (m-2)'th Fibonacci
        fib1 = 1  # (m-1)'th Fibonacci
        fibM = fib2 + fib1  # m'th Fibonacci

        while fibM < len(self.friendList):
            fib2 = fib1
            fib1 = fibM
            fibM = fib2 + fib1

        offset = -1
        while fibM > 1:
            i = min(offset + fib2, len(self.friendList) - 1)
            if self.friendList[i].name < name:
                fibM = fib1
                fib1 = fib2
                fib2 = fibM - fib1
                offset = i
            elif self.friendList[i].name > name:
                fibM = fib2
                fib1 -= fib2
                fib2 = fibM - fib1
            else:
                print(f"Friend found: {self.friendList[i].name} - {self.friendList[i].mobile}")
                return i
        if fib1 and offset + 1 < len(self.friendList) and self.friendList[offset + 1].name == name:
            print(f"Friend found: {self.friendList[offset + 1].name} - {self.friendList[offset + 1].mobile}")
            return offset + 1
        print("Friend not found.")
        return -1

    # Insert a new friend in the phonebook
    def insertFriend(self, name, mobile):
        new_friend = Friend(name, mobile)
        self.friendList.append(new_friend)
        self.friendList.sort(key=lambda x: x.name)
        print("New friend added successfully.")

# Driver Code
frn = PhoneBook()
choice = 0

while choice != 6:
    print("\n*************FRIEND PHONE BOOK****************")
    print("1. Read Friend name and mobile details")
    print("2. Display Friend details")
    print("3. Search friend name using Binary Search")
    print("4. Search friend name using Fibonacci Search")
    print("5. Insert new friend details")
    print("6. Exit Application")
    choice = int(input("What operation::"))
    
    if choice == 1:
        n = int(input("Enter number of Friends::"))
        frn.getFriendDetails(n)
    elif choice == 2:
        frn.displayFriendList()
    elif choice == 3:
        print("1. Search name using Non-Recursive")
        print("2. Search name using Recursive")
        choice1 = int(input("What operation::"))
        if choice1 == 1:
            name = input("Enter the name to be searched::")
            frn.binarySearchNonRecursive(name)
        elif choice1 == 2:
            name = input("Enter the name to be searched::")
            frn.binarySearchRecursive(name, 0, len(frn.friendList) - 1)
        else:
            print("Wrong Choice")
    elif choice == 4:
        name = input("Enter the name to be searched::")
        frn.fibonacciSearch(name)
    elif choice == 5:
        name = input("Enter Name of friend::")
        mobile = int(input("Enter mobile no. of friend::"))
        frn.insertFriend(name, mobile)
    elif choice == 6:
        print("Goodbye")
        break
    else:
        print("Wrong Choice")
