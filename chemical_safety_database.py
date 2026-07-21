1#Chemical Safety Database:
#A Python-based chemical information management system that provides:
#Chemical identification by name or formula
# Physical and chemical properties
#Safety classifications and hazard information
#PPE recommendations
#Storage guidelines
#First aid procedures
#Emergency response solutions
#Chemical data is stored in JSON format for easy updating and expansion.
import json
import sys
import os
# Import required modules:
# json -> handles chemical database stored in JSON format
# sys -> allows safe program termination
try:
    file_path = os.path.join(os.path.dirname(__file__), "chemicals.json")
    with open(file_path, "r", encoding="utf-8") as file:
        chemicals =json.load(file)
except FileNotFoundError:
     print("chemicals.json file not found!")
     sys.exit()
except json.JSONDecodeError:
     print("JSON file is corrupted.")
     sys.exit()
# Main navigation interface.
# Allows users to search chemicals, access emergency information,
# or exit the database.    
def main_menu():
     while True:
          print("\n"+"="*40)
          print("chemical safety database-main menu")
          print("\n"+"="*40)
          print("1.Enter chemical name")
          print("2.Enter chemical formula")
          print("3.Emergency response")
          print("4.Exit the Sytem ")
          choice=input("\n select an option (1-4):").strip()
          if choice=="1":
               search_by_name()
          elif choice=="2":
               search_by_formula()
          elif choice=="3":
               emergency_response()
          elif choice=="4":
               print("shutting down safety database")
               sys.exit()
          else:
            print("Invalid option.please choose from (1-4)")
# Search chemical database using user-provided chemical name.
# Search chemical database using molecular formula.
# Formula search loops through all stored chemicals until a match is found.            
def search_by_name():
     name = input("Enter chemical name: ").strip().lower()
     if name in chemicals:
          chemical_menu(name)
     else:
          print("chemical not found!")
    
def search_by_formula():
     formula = input("Enter chemical formula: ").strip().upper()
     for name, data in chemicals.items():
          if data.get("basic_information", {}).get("formula", "").upper() == formula:
               chemical_menu(name)
               return
     print("chemical not found.")
# Displays categorized information options for a selected chemical.
# Users can access different safety and property sections separately.
def chemical_menu(name):
     while True:
          print("\n" + "="*40)
          print(f"Chemical: {name.title()}")
          print(f"Formula: {chemicals[name].get('basic_information', {}).get('formula',"")}")
          print("="*40)
    
          print("1.Basic information")     
          print("2. Physical Properties")
          print("3. Safety Information")
          print("4. PPE")
          print("5. Storage")
          print("6. First Aid")
          print("7. View All Information")
          print("8. Back to Main Menu")
     
          choice = input("Select an option(1-8):")
          if choice=="1":
               basic_information(name)
          elif choice=="2":
               physical_properties(name)
          elif choice=="3":
               safety_information(name)
          elif choice=="4":
               ppe(name)
          elif choice=="5":
               storage(name)
          elif choice=="6":
               first_aid(name)
          elif choice=="7":
               view_all_information(name)
          elif choice=="8":
               break 
          else:
               print("Invalid option.please choose from (1-8)")         
# Displays fundamental identification data of the chemical.
def basic_information(name):
     print("\nBASIC INFORMATION")
     print("Formula:", chemicals[name]["basic_information"]["formula"])
     print("Molar Mass:", chemicals[name]["basic_information"]["molar_mass"])
     print("CAS Number:", chemicals[name]["basic_information"]["cas_number"])
     print("Type:", chemicals[name]["basic_information"]["chemical_type"])
     print("Appearance:", chemicals[name]["basic_information"]["appearance"])
     print("Odor:", chemicals[name]["basic_information"]["odor"])
     print("Color:", chemicals[name]["basic_information"]["color"])
     print("Physical State:", chemicals[name]["basic_information"]["physical_state"])
     print("synonyms:", ", ".join(chemicals[name]["basic_information"]["synonyms"]))
# Displays measurable physical characteristics including:
# density, boiling point, vapor pressure, solubility, and flammability data.
def physical_properties(name):
     print("\nPHYSICAL PROPERTIES")
     data = chemicals[name]["physical_properties"]
     print("Density:", data["density"])
     print("Melting Point:", data["melting_point"])
     print("Boiling Point:", data["boiling_point"])
     print("Freezing Point:", data["freezing_point"])
     print("Vapor Pressure:", data["vapor_pressure"])
     print("Vapor Density:", data["vapor_density"])
     print("Specific Gravity:", data["specific_gravity"])
     print("Water Solubility:", data["solubility_in_water"])
     print("Other Solubility:", data["solubility_in_other_solvents"])
     print("pH:", data["ph"])
     print("Flash Point:", data["flash_point"])
     print("Autoignition Temperature:", data["autoignition_temperature"])
     print("Flammability Limits:", data["flammability_limits"])
     print("Partition Coefficient:", data["partition_coefficient_log_kow"])
     print("Refractive Index:", data["refractive_index"])
     print("Viscosity:", data["viscosity"])
     print("Evaporation Rate:", data["evaporation_rate"])
     print("Decomposition Temperature:", data["decomposition_temperature"])
     print("Electrical Conductivity:", data["electrical_conductivity"])
# Displays hazard classification, GHS information,
# NFPA/HMIS ratings, toxicity, and environmental risks.
def safety_information(name):
     print("\nSAFETY INFORMATION")
     data = chemicals[name]["safety_information"]
     print("GHS Classification:", data["ghs_classification"])
     print("Signal Word:", data["ghs_signal_word"])
     print("\nHazard Statements:")
     for item in data["hazard_statements"]:
          print("-", item)
     print("\nPrecautionary Statements:")
     for item in data["precautionary_statements"]:
          print("-", item)
     print("\nNFPA Rating")
     print("Health:", data["nfpa_rating"]["health"])
     print("Fire:", data["nfpa_rating"]["fire"])
     print("Reactivity:", data["nfpa_rating"]["reactivity"])
     print("\nHMIS Rating")
     print("Health:", data["hmis_rating"]["health"])
     print("Flammability:", data["hmis_rating"]["flammability"])
     print("Physical Hazard:", data["hmis_rating"]["physical_hazard"])
     print("\nToxicity")
     print("LD50:", data["toxicity"]["ld50"])
     print("LC50:", data["toxicity"]["lc50"])
     print("Corrosive:", data["corrosive"])
     print("Flammable:", data["flammable"])
     print("Oxidizer:", data["oxidizer"])
     print("Reactive:", data["reactive"])
     print("Explosive:", data["explosive"])
     print("Environmental Hazard:", data["environmental_hazard"])
# Provides recommended personal protective equipment
# required for safe chemical handling.
def ppe(name):
     print("\n PPE ")
     data = chemicals[name]["ppe"]
     print("Gloves:", data["gloves"])
     print("Goggles:", data["safety_goggles"])
     print("Face Shield:", data["face_shield"])
     print("Lab Coat:", data["lab_coat"])
     print("Respirator:", data["respirator"])
     print("Safety Shoes:", data["safety_shoes"])
# Shows proper storage conditions and incompatibilities
# to minimize chemical hazards.
def storage(name):
     print("\nSTORAGE")
     data = chemicals[name]["storage"]
     print("Storage Temperature:", data["storage_temperature"])
     print("Keep Away From:")
     for item in data["keep_away_from"]:
          print("-", item)
     print("Storage Class:", data["storage_class"])
     print("Container Type:", data["container_type"])
     print("Ventilation:", data["ventilation_requirement"]) 
     print("HUMIDITY:", data["humidity_requirement"]) 
# Provides immediate response procedures
# for accidental exposure scenarios.                                    
def first_aid(name):
     print("\nFIRST AID")
     data = chemicals[name]["first_aid"]
     print("Skin Contact:", data["skin_contact"])
     print("Eye Contact:", data["eye_contact"])
     print("Inhalation:", data["inhalation"])
     print("Ingestion:", data["ingestion"])
# Provides emergency management information including:
# spill control, firefighting methods, and suitable extinguishing media.
def emergency_information(name):
     if "emergency" not in chemicals[name]:
          print("\nEMERGENCY RESPONSE")
          print("Emergency information is not available.")
          return
     print("\nEMERGENCY RESPONSE")
     data = chemicals[name]["emergency"]
     print("Spill Response:", data["spill_response"])
     print("Fire Fighting Method:", data["fire_fighting_method"])
     print("\nSuitable Extinguishing Media:")
     for item in data["suitable_extinguishing_media"]:
          print("-", item)
     print("\nUnsuitable Extinguishing Media:")
     for item in data["unsuitable_extinguishing_media"]:
           print("-", item)
          
def emergency_response():
     name = input("Enter chemical name: ").strip().lower()
     if name not in chemicals:
          print("chemical not found!")
          return
     emergency_information(name)
# Generates a complete safety report by combining
# all available information categories for a chemical.     
def view_all_information(name):
    basic_information(name)
    physical_properties(name)
    safety_information(name)
    ppe(name)
    storage(name)
    first_aid(name)
    emergency_information(name)
# Start the Chemical Safety Database application.    
main_menu()

