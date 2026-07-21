
    nokia_phone_is_on = True

    while nokia_phone_is_on:
        nokia_phone_menu = """
        Welcome to your Nokia Phone
        Your Nokia Menu Map
        
        1. Phone book
        2. Messages.
        3. Chaty-umaru
        4. Call register
        5. Tones
        6. Settings
        7. Call divert
        8. Games
        9. Calculator
        10. Reminders
        11. Clock
        12. Profiles
        13. Sim Services
        0. Power Off / Exit
        """

        print(nokia_phone_menu)
        
        try:
            phone_book = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if phone_book == 0:
            print("Goodbye!")
            nokia_phone_is_on = False
            break

        elif phone_book == 1:
            in_phonebook = True
            while in_phonebook:
                print("Phone book")
                phonebook_menu_options = """
                Press 1 to search
                Press 2 for Service Nos.
                Press 3 to Add name
                Press 4 to Erase
                Press 5 to Edit
                Press 6 to Assign tone
                Press 7 to Send b'card
                Press 8 for Options
                Press 9 to Speed dials
                Press 10 for Voice tags
                Press 0 to Go Back to Main Menu
                """
                print(phonebook_menu_options)
                try:
                    phone_book_choices = int(input())
                except ValueError:
                    continue

                if phone_book_choices == 0:
                    in_phonebook = False
                    break

                if phone_book_choices == 1:
                    print("Click here to search anything?")
                elif phone_book_choices == 2:
                    print("Call 911 for Emergencies, Call 211 for Support")
                elif phone_book_choices == 3:
                    print("What name do you want to save?, input it here!")
                elif phone_book_choices == 4:
                    print("Click here to erase all phone numbers")
                elif phone_book_choices == 5:
                    print("Click here to edit your contact name")
                elif phone_book_choices == 6:
                    print("Add your callertone: Dreamland, AfroSense, Tiktokk")
                elif phone_book_choices == 7:
                    print("Send your business card")
                elif phone_book_choices == 8:
                    in_pb_options = True
                    while in_pb_options:
                        print("1. Type of view\n2. Memory status\n 0. Back")
                        try:
                            opt_choice = int(input())
                        except ValueError:
                            continue
                        
                        if opt_choice == 0:
                            in_pb_options = False
                            break
                        
                        if opt_choice == 1:
                            print("Type of view selected.")
                        elif opt_choice == 2:
                            print("Memory status selected.")
                        else:
                            print("Invalid option.")
                elif phone_book_choices == 9:
                    print("Speed dial your favourite contacts")
                elif phone_book_choices == 10:
                    print("Tag your contacts through voicenotes")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 2:
            in_messages = True
            while in_messages:
                print("Messages")
                message_menu = """
                Press 1 to Write messages
                Press 2 to check your inboxes
                Press 3 to check your outbox
                Press 4 to Picture your messages
                Press 5 for Templates
                Press 6 for Smileys
                Press 7 for Message Settings
                Press 8 for Info service
                Press 9 for Voice mailbox number
                Press 10 for Service command editor
                Press 0 to Go Back to Main Menu
                """
                print(message_menu)
                try:
                    message_menu_choices = int(input())
                except ValueError:
                    continue

                if message_menu_choices == 0:
                    in_messages = False
                    break

                if message_menu_choices == 1:
                    print("Write a long message, write here.")
                elif message_menu_choices == 2:
                    print("You have 500 new messages, click here to read")
                elif message_menu_choices == 3:
                    print("You have 3 unsent messages?")
                elif message_menu_choices == 4:
                    print("You have 4 photos add a message you want to picture")
                elif message_menu_choices == 5:
                    print("You do not have any template, create new one here?")
                elif message_menu_choices == 6:
                    print("Add your favourite smileys?")
                elif message_menu_choices == 7:
                    in_msg_settings = True
                    while in_msg_settings:
                        print("Message Settings:\n1. Set 1\n2. Common\n0. Back")
                        try:
                            msg_set_choice = int(input())
                        except ValueError:
                            continue
                        
                        if msg_set_choice == 0:
                            in_msg_settings = False
                            break

                        if msg_set_choice == 1:
                            in_set1 = True
                            while in_set1:
                                print("Set 1:\n1. Message centre number\n2. Message sent as\n3. Message validity\n0. Back")
                                try:
                                    set1_choice = int(input())
                                except ValueError:
                                    continue
                                
                                if set1_choice == 0:
                                    in_set1 = False
                                    break
                                
                                if set1_choice == 1:
                                    print("Message centre number updated.")
                                elif set1_choice == 2:
                                    print("Message sent as Text.")
                                elif set1_choice == 3:
                                    print("Message validity set.")
                                else:
                                    print("Invalid.")
                        elif msg_set_choice == 2:
                            in_common = True
                            while in_common:
                                print("Common:\n1. Delivery reports\n2. Reply via same centre\n3. Character support\n0. Back")
                                try:
                                    common_choice = int(input())
                                except ValueError:
                                    continue
                                
                                if common_choice == 0:
                                    in_common = False
                                    break
                                
                                if common_choice == 1:
                                    print("Delivery reports turned on.")
                                elif common_choice == 2:
                                    print("Reply via same centre enabled.")
                                elif common_choice == 3:
                                    print("Character support full.")
                                else:
                                    print("Invalid.")
                        else:
                            print("Invalid option.")
                elif message_menu_choices == 8:
                    print("You have 5 info services?")
                elif message_menu_choices == 9:
                    print("You don't have any voice mailbox number?")
                elif message_menu_choices == 10:
                    print("This is service command center, what do you want to edit")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 3:
            in_chat = True
            while in_chat:
                print("Chat")
                chat_options = """
                Press 1 to chat with your loved ones
                Press 2 to Make video calls
                Press 3 to Send photos
                Press 4 to Update statuses
                Press 0 to Go Back to Main Menu
                """
                print(chat_options)
                try:
                    chat_menu_options = int(input())
                except ValueError:
                    continue

                if chat_menu_options == 0:
                    in_chat = False
                    break

                if chat_menu_options == 1:
                    print("Click here to chat with your loved ones.")
                elif chat_menu_options == 2:
                    print("Make video calls now, click here to try")
                elif chat_menu_options == 3:
                    print("Send photos to your friends")
                elif chat_menu_options == 4:
                    print("Update your statuses")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 4:
            in_call_register = True
            while in_call_register:
                print("Call Register")
                call_register_options = """
                Press 1 for Missed calls
                Press 2 for Received calls
                Press 3 to See Dialed numbers
                Press 4 to Erase recent call lists
                Press 5 to Show call durations
                Press 6 to Show call costs
                Press 7 for Call Cost Settings
                Press 8 for prepaid credit
                Press 0 to Go Back to Main Menu
                """
                print(call_register_options)
                try:
                    call_register_menu_choices = int(input())
                except ValueError:
                    continue

                if call_register_menu_choices == 0:
                    in_call_register = False
                    break

                if call_register_menu_choices == 1:
                    print("You have 5 missed calls.")
                elif call_register_menu_choices == 2:
                    print("You have three received calls")
                elif call_register_menu_choices == 3:
                    print("You have 35 dialed numbers?")
                elif call_register_menu_choices == 4:
                    print("Click here to erase recent calls")
                elif call_register_menu_choices == 5:
                    in_durations = True
                    while in_durations:
                        print("Call Durations:\n1. Last call cost\n2. All calls duration\n3. Received call durations\n4. Dialed calls' durations\n5. Clear timers\n0. Back")
                        try:
                            dur_choice = int(input())
                        except ValueError:
                            continue
                        if dur_choice == 0:
                            in_durations = False
                            break
                        print("Duration option selected.")
                elif call_register_menu_choices == 6:
                    in_costs = True
                    while in_costs:
                        print("Call Costs:\n1. Last call cost\n2. All calls' cost\n3. Clear counters\n0. Back")
                        try:
                            cost_choice = int(input())
                        except ValueError:
                            continue
                        if cost_choice == 0:
                            in_costs = False
                            break
                        print("Cost option selected.")
                elif call_register_menu_choices == 7:
                    in_cost_settings = True
                    while in_cost_settings:
                        print("Call Cost Settings:\n1. Call cost limit\n2. Show cost in\n0. Back")
                        try:
                            cost_set_choice = int(input())
                        except ValueError:
                            continue
                        if cost_set_choice == 0:
                            in_cost_settings = False
                            break
                        print("Cost setting updated.")
                elif call_register_menu_choices == 8:
                    print("You have N500 Prepaid credit left?")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 5:
            in_tones = True
            while in_tones:
                print("Tones")
                tones_menu = """
                Press 1 for ringing tones
                Press 2 for Ringing volume
                Press 3 for Incoming call alert
                Press 4 for Composer
                Press 5 for Message alert tone
                Press 6 for Keypad tones
                Press 7 for Warning and Game tones
                Press 8 for Vibrating alert
                Press 9 for Screen saver
                Press 0 to Go Back to Main Menu
                """
                print(tones_menu)
                try:
                    tones_menu_choices = int(input())
                except ValueError:
                    continue

                if tones_menu_choices == 0:
                    in_tones = False
                    break

                if tones_menu_choices == 1:
                    print("Dreamland, Halo, Cross Me Over, Buzz")
                elif tones_menu_choices == 2:
                    print("Volume Options: Increase volume, Reduce volume, Unmute, Mute, Silent, Meeting")
                elif tones_menu_choices == 3:
                    print("Incoming call alerts?")
                elif tones_menu_choices == 4:
                    print("Click here to see your composer options")
                elif tones_menu_choices == 5:
                    print("Message alert tones: Old telephone, Trot, Xylem, Iphone ringing tone, Fairyland")
                elif tones_menu_choices == 6:
                    print("Turn on/off keypad tone?")
                elif tones_menu_choices == 7:
                    print("Turn on/off warning or game tone")
                elif tones_menu_choices == 8:
                    print("Turn on/off vibrating alert")
                elif tones_menu_choices == 9:
                    print("Reduce/Increase screen brighness")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 6:
            in_settings = True
            while in_settings:
                print("Settings")
                settings_menu = """
                Press 1 for Call Settings
                Press 2 for Phone Settings
                Press 3 for Security settings
                Press 4 for Restore Factory
                Press 0 to Go Back to Main Menu
                """
                print(settings_menu)
                try:
                    settings_menu_choices = int(input())
                except ValueError:
                    continue

                if settings_menu_choices == 0:
                    in_settings = False
                    break

                if settings_menu_choices == 1:
                    in_call_set = True
                    while in_call_set:
                        print("Call Settings:\n1. Automatic redial\n2. Speed dialing\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer\n0. Back")
                        try:
                            call_set_choice = int(input())
                        except ValueError:
                            continue
                        if call_set_choice == 0:
                            in_call_set = False
                            break
                        print("Setting applied.")
                elif settings_menu_choices == 2:
                    in_phone_set = True
                    while in_phone_set:
                        print("Phone Settings:\n1. Language\n2. Cell info display\n3. Welcome notes\n4. Network selection\n5. Light\n6. Confirm sim actions\n0. Back")
                        try:
                            phone_set_choice = int(input())
                        except ValueError:
                            continue
                        if phone_set_choice == 0:
                            in_phone_set = False
                            break
                        print("Setting applied.")
                elif settings_menu_choices == 3:
                    in_sec_set = True
                    while in_sec_set:
                        print("Security Settings:\n1. Pin code request\n2. Call barring service\n3. Fixed dialing\n4. Closed user group\n5. Phone security\n6. Change access codes\n0. Back")
                        try:
                            sec_choice = int(input())
                        except ValueError:
                            continue
                        if sec_choice == 0:
                            in_sec_set = False
                            break
                        print("Security setting updated.")
                elif settings_menu_choices == 4:
                    print("Restore your phone to new by deleting all info")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 7:
            in_call_divert = True
            while in_call_divert:
                print("Call divert")
                call_divert_menu = """
                Press 1 to divert incoming calls
                Press 2 to divert outgoing calls
                Press 3 to block unwanted numbers
                Press 0 to Go Back to Main Menu
                """
                print(call_divert_menu)
                try:
                    call_divert_menu_options = int(input())
                except ValueError:
                    continue

                if call_divert_menu_options == 0:
                    in_call_divert = False
                    break

                if call_divert_menu_options == 1:
                    print("divert calls to your other number, put it here.")
                elif call_divert_menu_options == 2:
                    print("Divert outgoing call, click here to do it")
                elif call_divert_menu_options == 3:
                    print("Your block list is empty, add new numbers")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 8:
            in_games = True
            while in_games:
                print("Games")
                games_menu = """
                Press 1 for Football
                Press 2 for Snake block
                Press 3 for Jumping monkey
                Press 0 to Go Back to Main Menu
                """
                print(games_menu)
                try:
                    games_menu_choices = int(input())
                except ValueError:
                    continue

                if games_menu_choices == 0:
                    in_games = False
                    break

                if games_menu_choices == 1:
                    print("Play PES2025")
                elif games_menu_choices == 2:
                    print("Play Snake block")
                elif games_menu_choices == 3:
                    print("Play jumping monkey")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 9:
            in_calc = True
            while in_calc:
                print("Calculator")
                calculator_menu = """
                Press 1 for scientific calculator
                Press 2 for normal calculator
                Press 3 for Unit converter Options
                Press 4 for Currency converter
                Press 0 to Go Back to Main Menu
                """
                print(calculator_menu)
                try:
                    calculator_menu_options = int(input())
                except ValueError:
                    continue

                if calculator_menu_options == 0:
                    in_calc = False
                    break

                if calculator_menu_options == 1:
                    print("What do you want to calculate today?")
                elif calculator_menu_options == 2:
                    print("Click here to use your normal calculator")
                elif calculator_menu_options == 3:
                    print("Unit conerter options: Length, Area, Volume, Time, Temperature, Weight")
                elif calculator_menu_options == 4:
                    print("Online currency converter")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 10:
            in_reminders = True
            while in_reminders:
                print("Reminders")
                reminders_menu = """
                Press 1 to create tasks to be reminded about
                Press 2 for Reminder settings
                Press 3 to Setup reminder ringing tone
                Press 0 to Go Back to Main Menu
                """
                print(reminders_menu)
                try:
                    reminders_menu_options = int(input())
                except ValueError:
                    continue

                if reminders_menu_options == 0:
                    in_reminders = False
                    break

                if reminders_menu_options == 1:
                    print("What task do you want to be reminded about?.")
                elif reminders_menu_options == 2:
                    print("Change Reminder setting")
                elif reminders_menu_options == 3:
                    print("Change your ringing tone?")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 11:
            in_clock = True
            while in_clock:
                print("Clocks")
                clock_menu = """
                Press 1 to Set Alarm clock
                Press 2 for Clock settings options
                Press 3 for Date settings
                Press 4 to setup Stopwatch
                Press 5 for Countdown timer
                Press 6 for Auto update of date and time
                Press 0 to Go Back to Main Menu
                """
                print(clock_menu)
                try:
                    clock_menu_options = int(input())
                except ValueError:
                    continue

                if clock_menu_options == 0:
                    in_clock = False
                    break

                if clock_menu_options == 1:
                    print("Set Alarm.")
                elif clock_menu_options == 2:
                    print("Change clock settings")
                elif clock_menu_options == 3:
                    print("Change your date?")
                elif clock_menu_options == 4:
                    print("setup stopwatch")
                elif clock_menu_options == 5:
                    print("Setup your timer")
                elif clock_menu_options == 6:
                    print("Auto update your date and time?")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 12:
            in_profiles = True
            while in_profiles:
                print("Profiles")
                profile_menu = """
                Press 1 for Profile 1
                Press 2 for Profile 2
                Press 3 for Profile 3
                Press 0 to Go Back to Main Menu
                """
                print(profile_menu)
                try:
                    profile_menu_options = int(input())
                except ValueError:
                    continue

                if profile_menu_options == 0:
                    in_profiles = False
                    break

                if profile_menu_options == 1:
                    print("Profile 1 options.")
                elif profile_menu_options == 2:
                    print("Profile 2 options")
                elif profile_menu_options == 3:
                    print("Profile 3 options?")
                else:
                    print("Invalid option. Try again.")

        elif phone_book == 13:
            in_sim = True
            while in_sim:
                print("Sim Services")
                simservice_menu = """
                Press 1 to swap your simcard
                Press 2 to Load airtime
                Press 3 to Add password to your simcard
                Press 0 to Go Back to Main Menu
                """
                print(simservice_menu)
                try:
                    simservice_menu_options = int(input())
                except ValueError:
                    continue

                if simservice_menu_options == 0:
                    in_sim = False
                    break

                if simservice_menu_options == 1:
                    print("Swap to get your old phone number.")
                elif simservice_menu_options == 2:
                    print("Buy airtime to get N1000 Bonus")
                elif simservice_menu_options == 3:
                    print("Secure your simcard?")
                else:
                    print("Invalid option. Try again.")

        else:
            print("Invalid main menu option. Please try again.")

 
