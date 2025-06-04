import os
import importlib
from utill import clear_screen,libraries,models_dict, models_label_dict,REF_Data_dict,BASE_DIR
from colorama import Fore, Style,init

def setup_tool():
    from PlasmaSpec import print_menu

    init(autoreset=True)
    clear_screen()

    print("=" * 78)
    print(f"{Fore.CYAN}{Style.BRIGHT} Checking Required Libraries{Style.RESET_ALL}")
    print("=" * 78)



    missing_libs = []
    for lib in libraries:
        try:
            importlib.import_module(lib)
            print(f"{Fore.GREEN} {lib} is installed.")
        except ImportError:
            print(f"{Fore.RED} {lib} is NOT installed.")
            missing_libs.append(lib)

    if missing_libs:
        print(f"\n{Fore.RED}{Style.BRIGHT}Setup Failed: Missing Libraries\n")
        print(f"{Fore.YELLOW}Please install them using the following commands:")
        for lib in missing_libs:
            print(f"  pip install {lib}")
    else:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}All required libraries are installed!")

    print("\n" + "=" * 78)
    print(f"{Fore.CYAN}{Style.BRIGHT}  Checking Required File Paths{Style.RESET_ALL}")
    print("=" * 78)
    
    combined_dicts = {
        **{f"Model: {k}": v for k, v in models_dict.items()},
        **{f"Label: {k}": v for k, v in models_label_dict.items()},
        **{f"Ref: {k}": v for k, v in REF_Data_dict.items()},
    }

    missing_files = []

    print(f"{'Name':45} {'Exists':7} {'Is File':8} {'Valid':6} Path")
    print("-" * 120)

    for name, path in combined_dicts.items():
        exists = os.path.exists(path)
        is_file = os.path.isfile(path)
        is_dir = os.path.isdir(path)
        valid = exists and (is_file or is_dir)

        color = Fore.GREEN if valid else Fore.RED
        exists_col = f"{Fore.GREEN}Yes" if exists else f"{Fore.RED}No "
        is_file_col = f"{Fore.GREEN}Yes" if is_file else f"{Fore.RED}No "
        valid_col = f"{Fore.GREEN}Yes" if valid else f"{Fore.RED}No "

        print(f"{name:45} {exists_col:7} {is_file_col:8} {valid_col:6} {Style.RESET_ALL}{path}")

        if not valid:
            missing_files.append((name, path))

    print("=" * 120)

    if not missing_files:
        print(f"\n{Fore.GREEN}{Style.BRIGHT} All required model, label, and reference files are present you are ready to Go!")
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}  Missing or invalid files detected:")
        for name, path in missing_files:
            print(f"   - {name:45} → {path}")
    
    input(f"\n{Fore.CYAN}Press {Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.CYAN} to return to the main menu...")
    clear_screen()
    print_menu()