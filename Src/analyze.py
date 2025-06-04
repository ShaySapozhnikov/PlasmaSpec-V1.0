from utill import clear_screen, REF_Data_dict, models_dict, models_label_dict, model_accuracies, label_to_filename
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from colorama import Fore, Style
from scipy.signal import savgol_filter

def spectrum_similarity(input_df, ref_df, wavelength_tol=0.5, intensity_tol=0.1):
    # (copy your existing spectrum_similarity code here)
    input_waves = input_df['Wavelength (nm)'].values
    input_intens = input_df['Normalized'].values
    ref_waves = ref_df['Wavelength (nm)'].values
    ref_intens = ref_df['Normalized'].values

    match_count = 0
    ref_idx = 0
    ref_len = len(ref_waves)

    for i_wave, i_int in zip(input_waves, input_intens):
        while ref_idx < ref_len and ref_waves[ref_idx] < i_wave - wavelength_tol:
            ref_idx += 1
        candidate_indices = []
        for j in range(ref_idx, min(ref_idx + 5, ref_len)):
            if abs(ref_waves[j] - i_wave) <= wavelength_tol:
                candidate_indices.append(j)
            else:
                if ref_waves[j] - i_wave > wavelength_tol:
                    break
        matched = False
        for cidx in candidate_indices:
            if abs(ref_intens[cidx] - i_int) <= intensity_tol:
                matched = True
                break
        if matched:
            match_count += 1

    similarity = match_count / len(input_waves) if len(input_waves) > 0 else 0
    return similarity


def analyze_sample_spectra():
    from PlasmaSpec import print_menu
    clear_screen()
    print(f'''{Fore.CYAN}{Style.BRIGHT}
================================================================================
                            Analyze Sample Spectra
--------------------------------------------------------------------------------
''')

    file_path = input("Please enter the spectrum CSV file path: ")

    if not os.path.exists(file_path):
        print(f"{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} The file '{file_path}' does not exist.\n")
        return

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} An error occurred while reading the file:\n{e}\n")
        return

    required_columns = ['Wavelength (nm)', 'Intensity']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} Missing required column(s): {', '.join(missing_columns)}\n")
        return

    # Data cleaning and normalization
    df_clean = df.dropna(subset=["Wavelength (nm)", "Intensity"])
    df_clean.sort_values("Wavelength (nm)", inplace=True)
    df_clean["Intensity"] = df_clean["Intensity"].interpolate(method='linear')
    df_clean.dropna(subset=["Intensity"], inplace=True)

    if len(df_clean) > 11:
        df_clean["Denoised"] = savgol_filter(df_clean["Intensity"], window_length=11, polyorder=2)
    else:
        df_clean["Denoised"] = df_clean["Intensity"]

    denoised = df_clean["Denoised"]
    if denoised.max() != denoised.min():
        df_clean["Normalized"] = (denoised - denoised.min()) / (denoised.max() - denoised.min())
    else:
        df_clean["Normalized"] = np.ones(len(denoised))

    print("===============================================================================")
    print(f"Processed {len(df_clean)} data points")
    print("Analyzing spectrum ....")
    print("===============================================================================")

    # Save the processed CSV temporarily or overwrite original for use in prediction
    temp_processed_file = os.path.join(os.getcwd(), "temp_processed_input.csv")
    df_clean.to_csv(temp_processed_file, index=False)

    # Prediction and plotting logic (like your predict_and_plot_reference function)
    try:
        new_data = pd.read_csv(temp_processed_file)
    except Exception as e:
        print(f"{Fore.RED}Error reading processed file: {e}{Style.RESET_ALL}")
        return

    new_data = new_data.rename(columns={"Normalized Intensity": "Normalized"})
    X_new = new_data[['Normalized', 'Wavelength (nm)']]
    first_sample = X_new.iloc[[0]]

    print(f"\n{Fore.CYAN}- Plasma spectrum Sample identification V 1.0 Demo -{Style.RESET_ALL}")
    print(f"{Fore.CYAN}--------Made by Shay Sapozhnikov-{Style.RESET_ALL}")
    print("\nTop Predictions from Each Model (Top 3 weighted by accuracy):")
    print("---------------------------------")

    model_encoder_paths = [
        (models_dict["Heavy_metals_model"], models_label_dict["Heavy_metals_model_decoder"]),
        (models_dict["light_elements_model"], models_label_dict["light_elements_model_decoder"]),
        (models_dict["Nonmetals_&_Metalloids"], models_label_dict["Nonmetals_&_Metalloids_model_decoder"]),
        (models_dict["Rare_Earth_Elements_model"], models_label_dict["Rare_Earth_Elements_model_decoder"]),
        (models_dict["Transition_Metals_model"], models_label_dict["Transition_Metals_model_decoder"]),
    ]

    all_label_preds = []

    for model_path, encoder_path in model_encoder_paths:
        model_name = os.path.basename(model_path).replace('.pkl', '')
        accuracy = model_accuracies.get(model_name, 0.9)

        try:
            model = joblib.load(model_path)
            label_encoder = joblib.load(encoder_path)
        except Exception as e:
            print(f"Failed to load model or encoder from {model_path}: {e}")
            continue

        probs = model.predict_proba(first_sample)[0]
        top3_idx = np.argsort(probs)[-3:][::-1]
        top3_labels = label_encoder.inverse_transform(top3_idx)
        top3_probs = probs[top3_idx]

        for label, prob in zip(top3_labels, top3_probs):
            weighted_prob = prob * accuracy

            similarity = 0
            element_name = label_to_filename.get(label)
            if element_name:
                ref_path = os.path.join(REF_Data_dict['ref_data_folder'], f"{element_name}.csv")
                if os.path.exists(ref_path):
                    try:
                        ref_data = pd.read_csv(ref_path)
                        similarity = spectrum_similarity(new_data, ref_data)
                    except Exception as e:
                        print(f"Error loading reference data for similarity: {e}")

            combined_score = weighted_prob * similarity

            all_label_preds.append({
                'label': label,
                'model_name': model_name,
                'raw_prob': prob,
                'accuracy': accuracy,
                'weighted_prob': weighted_prob,
                'similarity': similarity,
                'combined_score': combined_score
            })

            print(f"{model_name}: {label} ({prob * 100:.2f}%), accuracy: {accuracy*100:.1f}%, weighted score: {weighted_prob * 100:.2f}%, similarity: {similarity:.3f}, combined score: {combined_score:.3f}")

    if not all_label_preds:
        print(f"{Fore.RED}No predictions could be made.{Style.RESET_ALL}")
        return

    best_pred = max(all_label_preds, key=lambda x: x['combined_score'])
    best_label = best_pred['label']
    best_model_name = best_pred['model_name']
    best_weighted_prob = best_pred['weighted_prob']
    best_similarity = best_pred['similarity']
    best_raw_prob = best_pred['raw_prob']
    best_accuracy = best_pred['accuracy']

    print(f"\n{Fore.GREEN} Best prediction overall:{Style.RESET_ALL}")
    print(f"Model: {best_model_name}, Label: {best_label}")
    print(f"Raw prob: {best_raw_prob * 100:.2f}%, Accuracy: {best_accuracy * 100:.1f}%, Weighted prob: {best_weighted_prob * 100:.2f}%")
    print(f"Similarity with ref spectrum: {best_similarity:.3f}, Combined score: {best_pred['combined_score']:.3f}")

    # Reload best model and encoder for plotting top 3 predictions
    best_model_path = None
    best_encoder_path = None
    for model_path, encoder_path in model_encoder_paths:
        if os.path.basename(model_path).replace('.pkl', '') == best_model_name:
            best_model_path = model_path
            best_encoder_path = encoder_path
            break

    if best_model_path and best_encoder_path:
        best_model = joblib.load(best_model_path)
        best_encoder = joblib.load(best_encoder_path)
        best_probs = best_model.predict_proba(first_sample)[0]
        top3_idx = np.argsort(best_probs)[-3:][::-1]
        top3_labels = best_encoder.inverse_transform(top3_idx)
        top3_probs = best_probs[top3_idx]
    else:
        print("Error: Could not reload best model for plotting top 3 predictions.")
        top3_labels, top3_probs = [], []

    plt.figure(figsize=(10, 5))
    plt.plot(new_data['Wavelength (nm)'], new_data['Normalized'], label='Input Sample', color='blue')

    element_name = label_to_filename.get(best_label, None)
    if element_name:
        ref_path = os.path.join(REF_Data_dict['ref_data_folder'], f"{element_name}.csv")
        if os.path.exists(ref_path):
            try:
                ref_data = pd.read_csv(ref_path)
                plt.plot(ref_data['Wavelength (nm)'], ref_data['Normalized'],
                         label=f'Reference: {element_name}', color='red', alpha=0.4, linewidth=2)
            except Exception as e:
                print(f"Error loading reference data: {e}")
        else:
            print(f"Reference spectrum not found at {ref_path}")
    else:
        print(f"No reference mapping found for label '{best_label}'")

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Normalized Intensity')
    plt.title(f'Input Sample vs Reference Spectrum of {best_label}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    colors = ['green', 'orange', 'gray']
    plt.bar(top3_labels, top3_probs, color=colors[:len(top3_labels)])
    plt.ylabel('Probability')
    plt.title('Top 3 Predictions (Best Model)')
    plt.ylim(0, 1)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    input(f"\n{Fore.CYAN}Press {Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.CYAN} to return to the main menu...")
    clear_screen()
    print_menu()

