def main():
    shopping_list = []

    while True:
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")

        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")

        elif choice == "3":
            if shopping_list:
                print("\nYour Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
