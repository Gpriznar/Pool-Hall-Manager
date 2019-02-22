### Title Menu Function ###
title_screen =("""
        **************************************************************************************
        |                                                                                    |
        |                                                                                    |
        |                                 Welcome to the                                     |
        |                             University of Houston's                                |
        |                                   Game Center                                      |
        |                                                                                    |
        |                                                                                    |
        |                                                                                    |
        |                                                                                    |
        |                                                                                    |
        |                                    _......._                                       |
        |                                 .-:::::::::::-.                                    |
        |                               .:::::::::::::::::.                                  |
        |                              :::::::' .-. `:::::::                                 |
        |                             :::::::  :   :  :::::::                                |
        |                            ::::::::  :   :  ::::::::                               |
        |                            :::::::::._`-'_.:::::::::                               |
        |                            :::::::::' .-. `:::::::::                               |
        |                            ::::::::  :   :  ::::::::                               |
        |                             :::::::  :   :  :::::::                                |
        |                              :::::::._`-'_.:::::::                                 |
        |                               `:::::::::::::::::'                                  |
        |                                 `-:::::::::::-'                                    |
        |                                    `'''''''`                                       |
        |                                                                                    |
        |                                                                                    |
        |                      Press "1" to open Pool Hall Application                       |
        |                                                                                    |
        |                      Press "0" to quit Pool Hall Application                       |
        |                                                                                    |
        **************************************************************************************

        Please enter your choice: """)

def title_menu():
    user_input = input(title_screen)


user_input = ""

if user_input == 1:
    pool_table_menu()

elif user_input == 0:
    print("Goodbye")

import pooltable
