import support_module


def main():
    user_message = ""
    key = []
    menu_choice = ""
    while menu_choice != "5":
        support_module.print_menu(user_message)
        menu_choice = support_module.get_choice("Input choice (1/2/3/4/5): ")
        match menu_choice:
            case "1":
                user_message = support_module.get_choice("Add message: ")
            case "2":
                key = input('Add key values, use "," between numbers: ').split(",")
                key = [int(x) for x in key]
            case "3":
                if not key:
                    print("Invalid, selection please insert key values")
                else:
                    user_message = support_module.encrypt_or_decrypt_message(user_message, key, False)
            case "4":
                if not key:
                    print("Invalid, selection please insert key values")
                else:
                    user_message = support_module.encrypt_or_decrypt_message(user_message, key, True)
            case "5": 
                continue
            case _:
                print("Invalid Input")


if __name__ == "__main__":
    main()