
from colorama import Fore, Style
from utill import clear_screen



def show_help():
    from PlasmaSpec import print_menu
    clear_screen()
    print(f'''{Fore.CYAN}{Style.BRIGHT}
    ===============================================================================
                               Help (?) - Version 1.0 Alpha
    -------------------------------------------------------------------------------

    Note: This is a limited prototype, so there may be some bugs or quirks.  
    If you encounter any issues, please submit a report on GitHub and I’ll do my best  
    to address it.  
    – Shay Sapozhnikov

    -------------------------------------------------------------------------------
                               Analyzing Data
    ===============================================================================

    To use the AI model to detect and classify elements from your experiment data,  
    please upload CSV files with **exactly two columns** named:

    - Wavelength (nm)  
    - Intensity

    The tool will automatically normalize your data and reduce noise using a  
    Savitzky Golay filter to optimize classification accuracy.

    -------------------------------------------------------------------------------
                        Viewing an Element’s Spectrum
    ===============================================================================

    To view the spectrum of an element, simply type its correct element symbol.  
    This will display the combined spectral lines for all its ionization states.

    **Example:**  
    Input: `Si` -> Output: Silicon spectrum graph

    -------------------------------------------------------------------------------
                           Future Plans & Updates
    ===============================================================================

    - Decompose spectra of materials and rocks into distinct elemental groups  
    - Generate theoretical compositions of various materials and element mixtures  
    - Add multi-element spectral comparison tools  
    - Export graphs and processed data in multiple formats (CSV, PNG, JSON)  
    - Add element-specific metadata and reference information overlays  
    - Implement custom noise filtering and smoothing options  
    - Support real-time spectrum updates from connected spectrometers  
    - Improve classification model accuracy with user feedback and training data  
    - Add batch processing capabilities for large datasets  
    - Enhance UI with interactive zoom, pan, and annotation features

    =============================================================================== {Style.RESET_ALL}''')

    input(f"\n{Fore.CYAN}Press {Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.CYAN} to return to the main menu...")
    clear_screen()
    print_menu()