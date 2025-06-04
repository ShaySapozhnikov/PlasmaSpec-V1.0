import os
from utill import clear_screen,ELEMENT_SYMBOLS,BASE_DIR
from colorama import Fore, Style
import pandas as pd
import matplotlib.pyplot as plt

def view_element_spectra():
    from PlasmaSpec import print_menu
    spectrum_ref_folder = os.path.join(BASE_DIR, "Reference Data", "Data")
    clear_screen()
    print(f'''{Fore.CYAN}{Style.BRIGHT}
    ===============================================================================
                               View an Element's Spectra
    -------------------------------------------------------------------------------





    ''')
    if not os.path.exists(spectrum_ref_folder):
        print(f"{Fore.RED}ERROR: Reference Data folder not found at {spectrum_ref_folder}")
        return

    element_symbol = input("Enter Element Symbol (e.g. Si, Fe): ").capitalize().strip()
    print(f"DEBUG: User input = {element_symbol}")

    if element_symbol not in ELEMENT_SYMBOLS:
        print(f"{Fore.RED}ERROR: '{element_symbol}' is not a valid symbol.")
        input(f"\n{Fore.CYAN}Press {Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.CYAN} to return to the main menu...")
        clear_screen()
        print_menu()
        return

    element_name = ELEMENT_SYMBOLS[element_symbol]
    #print(f"DEBUG: Full element name = {element_name}")

    file_path = os.path.join(spectrum_ref_folder, f"{element_name}.csv")
    #print(f"DEBUG: Looking for file = {file_path}")

    if not os.path.exists(file_path):
        print(f"{Fore.RED}ERROR: No spectrum CSV found for '{element_name}' at: {file_path}")
        input(f"\n{Fore.CYAN}Press {Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.CYAN} to return to the main menu...")
        clear_screen()
        print_menu()
        return

    try:
        df = pd.read_csv(file_path)
        #print(f"DEBUG: CSV loaded successfully. Rows = {len(df)}")

        if 'Wavelength (nm)' not in df.columns or 'Normalized' not in df.columns:
            print(f"{Fore.RED}ERROR: CSV file missing required columns.")
            input(f"\n{Fore.CYAN}Press {Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.CYAN} to return to the main menu...")
            clear_screen()
            print_menu()
            return

        print("Plotting data...")
        plt.plot(df['Wavelength (nm)'], df['Normalized'])
        plt.title(f"{element_name} Spectrum")
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Intensity - Normalized")
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"{Fore.RED}ERROR: Failed to load or plot data: {e}")
    
    input(f"\n{Fore.CYAN}Press {Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.CYAN} to return to the main menu...")
    clear_screen()
    print_menu()