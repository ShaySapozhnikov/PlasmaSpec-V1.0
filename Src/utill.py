import os



#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.abspath(".")
FIRST_RUN_FILE = ".first_run_flag"

def is_first_run():
    return not os.path.exists(FIRST_RUN_FILE)

def set_first_run_complete():
    with open(FIRST_RUN_FILE, "w") as f:
        f.write("This file marks that the tool has already been run.\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

models_dict = {
        "Heavy_metals_model": os.path.join(BASE_DIR, "Models", "Heavy_metals_model", "heavy_metals_rf_classifier.pkl"),
        "light_elements_model": os.path.join(BASE_DIR, "Models", "Light_elements_model", "light_elements_rf_classifier.pkl"),
        "Nonmetals_&_Metalloids": os.path.join(BASE_DIR, "Models", "Nonmetals_&_Metalloids_model", "Nonmetals_&_Metalloids_model.pkl"),
        "Rare_Earth_Elements_model": os.path.join(BASE_DIR, "Models", "Rare_Earth_Elements_model", "Rare_Earth_Elements_model.pkl"),
        "Transition_Metals_model": os.path.join(BASE_DIR, "Models", "Transition_Metals_Model", "Transition_Metals_model.pkl"),
    }

models_label_dict = {
        "Heavy_metals_model_decoder": os.path.join(BASE_DIR, "Models", "Heavy_metals_model", "label_encoder_heavy_metals.pkl"),
        "light_elements_model_decoder": os.path.join(BASE_DIR, "Models", "Light_elements_model", "light_elements_label_encoder.pkl"),
        "Nonmetals_&_Metalloids_model_decoder": os.path.join(BASE_DIR, "Models", "Nonmetals_&_Metalloids_model", "Nonmetals_&_Metalloids_label_encoder.pkl"),
        "Rare_Earth_Elements_model_decoder": os.path.join(BASE_DIR, "Models", "Rare_Earth_Elements_model", "Rare_Earth_Elements_label_encoder.pkl"),
        "Transition_Metals_model_decoder": os.path.join(BASE_DIR, "Models", "Transition_Metals_Model", "Transition_Metals_label_encoder.pkl"),
    }




model_encoder_paths = [
        (models_dict["Heavy_metals_model"], models_label_dict["Heavy_metals_model_decoder"]),
        (models_dict["light_elements_model"], models_label_dict["light_elements_model_decoder"]),
        (models_dict["Nonmetals_&_Metalloids"], models_label_dict["Nonmetals_&_Metalloids_model_decoder"]),
        (models_dict["Rare_Earth_Elements_model"], models_label_dict["Rare_Earth_Elements_model_decoder"]),
        (models_dict["Transition_Metals_model"], models_label_dict["Transition_Metals_model_decoder"]),
    ]




REF_Data_dict = {
        "ref_data_folder": os.path.join(BASE_DIR, "Reference Data", "Data")
    }

label_to_filename = {
    "H_1": "Hydrogen", "H_2": "Hydrogen", "H_3": "Hydrogen",
    "He_1": "Helium", "He_2": "Helium", "He_3": "Helium",
    "Li_1": "Lithium", "Li_2": "Lithium", "Li_3": "Lithium",
    "Be_1": "Beryllium", "Be_2": "Beryllium", "Be_3": "Beryllium",
    "B_1": "Boron", "B_2": "Boron", "B_3": "Boron",
    "C_1": "Carbon", "C_2": "Carbon", "C_3": "Carbon",
    "N_1": "Nitrogen", "N_2": "Nitrogen", "N_3": "Nitrogen",
    "O_1": "Oxygen", "O_2": "Oxygen", "O_3": "Oxygen",
    "F_1": "Fluorine", "F_2": "Fluorine", "F_3": "Fluorine",
    "Ne_1": "Neon", "Ne_2": "Neon", "Ne_3": "Neon",
    "Na_1": "Sodium", "Na_2": "Sodium", "Na_3": "Sodium",
    "Mg_1": "Magnesium", "Mg_2": "Magnesium", "Mg_3": "Magnesium",
    "Al_1": "Aluminum", "Al_2": "Aluminum", "Al_3": "Aluminum",
    "Si_1": "Silicon", "Si_2": "Silicon", "Si_3": "Silicon",
    "P_1": "Phosphorus", "P_2": "Phosphorus", "P_3": "Phosphorus",
    "S_1": "Sulfur", "S_2": "Sulfur", "S_3": "Sulfur",
    "Cl_1": "Chlorine", "Cl_2": "Chlorine", "Cl_3": "Chlorine",
    "Ar_1": "Argon", "Ar_2": "Argon", "Ar_3": "Argon",
    "K_1": "Potassium", "K_2": "Potassium", "K_3": "Potassium",
    "Ca_1": "Calcium", "Ca_2": "Calcium", "Ca_3": "Calcium",
    "Sc_1": "Scandium", "Sc_2": "Scandium", "Sc_3": "Scandium",
    "Ti_1": "Titanium", "Ti_2": "Titanium", "Ti_3": "Titanium",
    "V_1": "Vanadium", "V_2": "Vanadium", "V_3": "Vanadium",
    "Cr_1": "Chromium", "Cr_2": "Chromium", "Cr_3": "Chromium",
    "Mn_1": "Manganese", "Mn_2": "Manganese", "Mn_3": "Manganese",
    "Fe_1": "Iron", "Fe_2": "Iron", "Fe_3": "Iron",
    "Co_1": "Cobalt", "Co_2": "Cobalt", "Co_3": "Cobalt",
    "Ni_1": "Nickel", "Ni_2": "Nickel", "Ni_3": "Nickel",
    "Cu_1": "Copper", "Cu_2": "Copper", "Cu_3": "Copper",
    "Zn_1": "Zinc", "Zn_2": "Zinc", "Zn_3": "Zinc",
    "Ga_1": "Gallium", "Ga_2": "Gallium", "Ga_3": "Gallium",
    "Ge_1": "Germanium", "Ge_2": "Germanium", "Ge_3": "Germanium",
    "As_1": "Arsenic", "As_2": "Arsenic", "As_3": "Arsenic",
    "Se_1": "Selenium", "Se_2": "Selenium", "Se_3": "Selenium",
    "Br_1": "Bromine", "Br_2": "Bromine", "Br_3": "Bromine",
    "Kr_1": "Krypton", "Kr_2": "Krypton", "Kr_3": "Krypton",
    "Rb_1": "Rubidium", "Rb_2": "Rubidium", "Rb_3": "Rubidium",
    "Sr_1": "Strontium", "Sr_2": "Strontium", "Sr_3": "Strontium",
    "Y_1": "Yttrium", "Y_2": "Yttrium", "Y_3": "Yttrium",
    "Zr_1": "Zirconium", "Zr_2": "Zirconium", "Zr_3": "Zirconium",
    "Nb_1": "Niobium", "Nb_2": "Niobium", "Nb_3": "Niobium",
    "Mo_1": "Molybdenum", "Mo_2": "Molybdenum", "Mo_3": "Molybdenum",
    "Tc_1": "Technetium", "Tc_2": "Technetium", "Tc_3": "Technetium",
    "Ru_1": "Ruthenium", "Ru_2": "Ruthenium", "Ru_3": "Ruthenium",
    "Rh_1": "Rhodium", "Rh_2": "Rhodium", "Rh_3": "Rhodium",
    "Pd_1": "Palladium", "Pd_2": "Palladium", "Pd_3": "Palladium",
    "Ag_1": "Silver", "Ag_2": "Silver", "Ag_3": "Silver",
    "Cd_1": "Cadmium", "Cd_2": "Cadmium", "Cd_3": "Cadmium",
    "In_1": "Indium", "In_2": "Indium", "In_3": "Indium",
    "Sn_1": "Tin", "Sn_2": "Tin", "Sn_3": "Tin",
    "Sb_1": "Antimony", "Sb_2": "Antimony", "Sb_3": "Antimony",
    "Te_1": "Tellurium", "Te_2": "Tellurium", "Te_3": "Tellurium",
    "I_1": "Iodine", "I_2": "Iodine", "I_3": "Iodine",
    "Xe_1": "Xenon", "Xe_2": "Xenon", "Xe_3": "Xenon",
    "Cs_1": "Cesium", "Cs_2": "Cesium", "Cs_3": "Cesium",
    "Ba_1": "Barium", "Ba_2": "Barium", "Ba_3": "Barium",
    "La_1": "Lanthanum", "La_2": "Lanthanum", "La_3": "Lanthanum",
    "Ce_1": "Cerium", "Ce_2": "Cerium", "Ce_3": "Cerium",
    "Pr_1": "Praseodymium", "Pr_2": "Praseodymium", "Pr_3": "Praseodymium",
    "Nd_1": "Neodymium", "Nd_2": "Neodymium", "Nd_3": "Neodymium",
    "Pm_1": "Promethium", "Pm_2": "Promethium", "Pm_3": "Promethium",
    "Sm_1": "Samarium", "Sm_2": "Samarium", "Sm_3": "Samarium",
    "Eu_1": "Europium", "Eu_2": "Europium", "Eu_3": "Europium",
    "Gd_1": "Gadolinium", "Gd_2": "Gadolinium", "Gd_3": "Gadolinium",
    "Tb_1": "Terbium", "Tb_2": "Terbium", "Tb_3": "Terbium",
    "Dy_1": "Dysprosium", "Dy_2": "Dysprosium", "Dy_3": "Dysprosium",
    "Ho_1": "Holmium", "Ho_2": "Holmium", "Ho_3": "Holmium",
    "Er_1": "Erbium", "Er_2": "Erbium", "Er_3": "Erbium",
    "Tm_1": "Thulium", "Tm_2": "Thulium", "Tm_3": "Thulium",
    "Yb_1": "Ytterbium", "Yb_2": "Ytterbium", "Yb_3": "Ytterbium",
    "Lu_1": "Lutetium", "Lu_2": "Lutetium", "Lu_3": "Lutetium",
    "Hf_1": "Hafnium", "Hf_2": "Hafnium", "Hf_3": "Hafnium",
    "Ta_1": "Tantalum", "Ta_2": "Tantalum", "Ta_3": "Tantalum",
    "W_1": "Tungsten", "W_2": "Tungsten", "W_3": "Tungsten",
    "Re_1": "Rhenium", "Re_2": "Rhenium", "Re_3": "Rhenium",
    "Os_1": "Osmium", "Os_2": "Osmium", "Os_3": "Osmium",
    "Ir_1": "Iridium", "Ir_2": "Iridium", "Ir_3": "Iridium",
    "Pt_1": "Platinum", "Pt_2": "Platinum", "Pt_3": "Platinum",
    "Au_1": "Gold", "Au_2": "Gold", "Au_3": "Gold",
    "Hg_1": "Mercury", "Hg_2": "Mercury", "Hg_3": "Mercury",
    "Tl_1": "Thallium", "Tl_2": "Thallium", "Tl_3": "Thallium",
    "Pb_1": "Lead", "Pb_2": "Lead", "Pb_3": "Lead",
    "Bi_1": "Bismuth", "Bi_2": "Bismuth", "Bi_3": "Bismuth",
    "Po_1": "Polonium", "Po_2": "Polonium", "Po_3": "Polonium",
    "At_1": "Astatine", "At_2": "Astatine", "At_3": "Astatine",
    "Rn_1": "Radon", "Rn_2": "Radon", "Rn_3": "Radon",
    "Fr_1": "Francium", "Fr_2": "Francium", "Fr_3": "Francium",
    "Ra_1": "Radium", "Ra_2": "Radium", "Ra_3": "Radium",
    "Ac_1": "Actinium", "Ac_2": "Actinium", "Ac_3": "Actinium",
    "Th_1": "Thorium", "Th_2": "Thorium", "Th_3": "Thorium",
    "Pa_1": "Protactinium", "Pa_2": "Protactinium", "Pa_3": "Protactinium",
    "U_1": "Uranium", "U_2": "Uranium", "U_3": "Uranium",
    "Np_1": "Neptunium", "Np_2": "Neptunium", "Np_3": "Neptunium",
    "Pu_1": "Plutonium", "Pu_2": "Plutonium", "Pu_3": "Plutonium",
    "Am_1": "Americium", "Am_2": "Americium", "Am_3": "Americium",
    "Cm_1": "Curium", "Cm_2": "Curium", "Cm_3": "Curium",
    "Bk_1": "Berkelium", "Bk_2": "Berkelium", "Bk_3": "Berkelium",
    "Cf_1": "Californium", "Cf_2": "Californium", "Cf_3": "Californium",
    "Es_1": "Einsteinium", "Es_2": "Einsteinium", "Es_3": "Einsteinium",
    "Fm_1": "Fermium", "Fm_2": "Fermium", "Fm_3": "Fermium",
    "Md_1": "Mendelevium", "Md_2": "Mendelevium", "Md_3": "Mendelevium",
    "No_1": "Nobelium", "No_2": "Nobelium", "No_3": "Nobelium",
    "Lr_1": "Lawrencium", "Lr_2": "Lawrencium", "Lr_3": "Lawrencium",
    "Rf_1": "Rutherfordium", "Rf_2": "Rutherfordium", "Rf_3": "Rutherfordium",
    "Db_1": "Dubnium", "Db_2": "Dubnium", "Db_3": "Dubnium",
    "Sg_1": "Seaborgium", "Sg_2": "Seaborgium", "Sg_3": "Seaborgium",
    "Bh_1": "Bohrium", "Bh_2": "Bohrium", "Bh_3": "Bohrium",
    "Hs_1": "Hassium", "Hs_2": "Hassium", "Hs_3": "Hassium",
    "Mt_1": "Meitnerium", "Mt_2": "Meitnerium", "Mt_3": "Meitnerium",
    "Ds_1": "Darmstadtium", "Ds_2": "Darmstadtium", "Ds_3": "Darmstadtium",
    "Rg_1": "Roentgenium", "Rg_2": "Roentgenium", "Rg_3": "Roentgenium",
    "Cn_1": "Copernicium", "Cn_2": "Copernicium", "Cn_3": "Copernicium",
    "Nh_1": "Nihonium", "Nh_2": "Nihonium", "Nh_3": "Nihonium",
    "Fl_1": "Flerovium", "Fl_2": "Flerovium", "Fl_3": "Flerovium",
    "Mc_1": "Moscovium", "Mc_2": "Moscovium", "Mc_3": "Moscovium",
    "Lv_1": "Livermorium", "Lv_2": "Livermorium", "Lv_3": "Livermorium",
    "Ts_1": "Tennessine", "Ts_2": "Tennessine", "Ts_3": "Tennessine",
    "Og_1": "Oganesson", "Og_2": "Oganesson", "Og_3": "Oganesson"
}



libraries = {
    "pandas": "pandas",
    "numpy": "numpy",
    "joblib": "joblib",
    "matplotlib": "matplotlib",
    "colorama": "colorama",
    "sklearn": "scikit-learn",
    "scipy": "scipy"
    }



ELEMENT_SYMBOLS = {
        "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron",
        "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon",
        "Na": "Sodium", "Mg": "Magnesium", "Al": "Aluminum", "Si": "Silicon", "P": "Phosphorus",
        "S": "Sulfur", "Cl": "Chlorine", "Ar": "Argon", "K": "Potassium", "Ca": "Calcium",
        "Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium", "Mn": "Manganese",
        "Fe": "Iron", "Co": "Cobalt", "Ni": "Nickel", "Cu": "Copper", "Zn": "Zinc",
        "Ga": "Gallium", "Ge": "Germanium", "As": "Arsenic", "Se": "Selenium", "Br": "Bromine",
        "Kr": "Krypton", "Rb": "Rubidium", "Sr": "Strontium", "Y": "Yttrium", "Zr": "Zirconium",
        "Nb": "Niobium", "Mo": "Molybdenum", "Tc": "Technetium", "Ru": "Ruthenium",
        "Rh": "Rhodium", "Pd": "Palladium", "Ag": "Silver", "Cd": "Cadmium", "In": "Indium",
        "Sn": "Tin", "Sb": "Antimony", "Te": "Tellurium", "I": "Iodine", "Xe": "Xenon",
        "Cs": "Cesium", "Ba": "Barium", "La": "Lanthanum", "Ce": "Cerium", "Pr": "Praseodymium",
        "Nd": "Neodymium", "Pm": "Promethium", "Sm": "Samarium", "Eu": "Europium",
        "Gd": "Gadolinium", "Tb": "Terbium", "Dy": "Dysprosium", "Ho": "Holmium", "Er": "Erbium",
        "Tm": "Thulium", "Yb": "Ytterbium", "Lu": "Lutetium", "Hf": "Hafnium", "Ta": "Tantalum",
        "W": "Tungsten", "Re": "Rhenium", "Os": "Osmium", "Ir": "Iridium", "Pt": "Platinum",
        "Au": "Gold", "Hg": "Mercury", "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth",
        "Po": "Polonium", "At": "Astatine", "Rn": "Radon", "Fr": "Francium", "Ra": "Radium",
        "Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium", "U": "Uranium", "Np": "Neptunium",
        "Pu": "Plutonium", "Am": "Americium", "Cm": "Curium", "Bk": "Berkelium",
        "Cf": "Californium", "Es": "Einsteinium", "Fm": "Fermium", "Md": "Mendelevium",
        "No": "Nobelium", "Lr": "Lawrencium", "Rf": "Rutherfordium", "Db": "Dubnium",
        "Sg": "Seaborgium", "Bh": "Bohrium", "Hs": "Hassium", "Mt": "Meitnerium",
        "Ds": "Darmstadtium", "Rg": "Roentgenium", "Cn": "Copernicium", "Nh": "Nihonium",
        "Fl": "Flerovium", "Mc": "Moscovium", "Lv": "Livermorium", "Ts": "Tennessine",
        "Og": "Oganesson"
    }

model_accuracies = {
    'heavy_metals_rf_classifier': 0.97,
    'light_elements_rf_classifier': 0.90,
    'Nonmetals_&_Metalloids_model': 0.91,
    'Rare_Earth_Elements_model': 0.82,
    'Transition_Metals_model': 0.85,
}
