
from colorama import Fore, Style
from view import view_element_spectra
from analyze import analyze_sample_spectra
from help import show_help
from setup import setup_tool
from utill import is_first_run,set_first_run_complete,clear_screen







def print_menu():
    print(f'''{Fore.CYAN}{Style.BRIGHT}
==============================================================================
         Plasma Spectrum CLI Tool - Analyze and Match Your Sample Spectra!
------------------------------------------------------------------------------
                          By Shay Sapozhnikov
                          Version 1.0 Alpha
==============================================================================
1) Analyze Sample Spectra
2) View an Element's Spectra
3) Help (?)
4) Setup
5) Exit
==============================================================================
{Style.RESET_ALL}''')


def main():
    
    #clear_screen()
    if is_first_run():

        print(f'''{Fore.CYAN}{Style.BRIGHT}
==============================================================================
Welcome! It seems this is your first time running the Plasma Spectrum CLI Tool.
Please proceed to Setup so I can ensure your tool is correctly configured to run 
as intended.

— shay    
==============================================================================
{Style.RESET_ALL}''')
        set_first_run_complete()

    print(f'''{Fore.CYAN}{Style.BRIGHT}
==============================================================================
         Plasma Spectrum CLI Tool - Analyze and Match Your Sample Spectra!
------------------------------------------------------------------------------
                          By Shay Sapozhnikov
                          Version 1.0 Alpha
==============================================================================
1) Analyze Sample Spectra
2) View an Element's Spectra
3) Help (?)
4) Setup
5) Exit
==============================================================================
{Style.RESET_ALL}''')

    while True:
        user_option = input("--> ").strip()

        if user_option == "1":
            analyze_sample_spectra()
        elif user_option == "2":
            view_element_spectra()
        elif user_option == "3":
            show_help()
        elif user_option == "4":
            setup_tool()
        elif user_option == "5":
            print("Exiting Plasma Spectrum CLI Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
