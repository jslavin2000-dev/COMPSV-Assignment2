class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

        return f"{name} added to the front of the waitlist"

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        if self.head is None:
            return f"{name} not found"

        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        current = self.head

        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return f"Removed {name} from the waitlist"

            current = current.next

        return f"{name} not found"

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        print("Current waitlist:")

        current = self.head

        while current is not None:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    waitlist = LinkedList()

    print("--- Waitlist Manager ---")

    while True:
        print("\n1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            print(waitlist.add_front(name))

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            print(waitlist.remove(name))

        elif choice == "4":
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    waitlist_generator()