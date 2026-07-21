# Chemical Safety Database:
Python-based command-line application for managing chemical safety information.
This project is designed to help students and laboratory personnel quickly access important information. This project enables users to search chemicals by name or molecular formula and access comprehensive database like physical properties, hazard classifications, personal protective equipment (PPE), storage guidelines, first aid procedures, and emergency response information.

The application stores all chemical records in a JSON database, making it simple to maintain, expand, and customize without modifying the program's source code.

##Overview
Chemical safety information is essential in laboratories, educational institutions, and industrial environments. This project was developed to provide a centralized and user-friendly system for retrieving important chemical data quickly and efficiently.
Instead of searching through multiple documents or Safety Data Sheets (SDS), users can access essential information through a structured menu-driven interface.


## Features
- Search chemicals by **chemical name**
- Search chemicals by **chemical formula**
- View detailed chemical information
- Physical and chemical properties
- GHS hazard classification
-Personal Protective Equipment (PPE) recommendations
- Storage guidelines
- First aid procedures
-Emergency response information
- chemical data stored in **JSON** for easy expansion
-Error handling for missing or corrupted database files

##Project Structure
Chemical-Safety-Database/
│
├── chemical_safety_database.py
├── chemicals.json
├── README.md

##Technologies Used

- Python 3
- JSON
- Command Line Interface (CLI)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Chemical-Safety-Database.git
```

### 2. Navigate to the project folder

```bash
cd Chemical-Safety-Database
```

### 3. Run the program

```bash
python chemical_safety_database.py
```

---
##code structure:
## Main Menu
====================================
CHEMICAL SAFETY DATABASE
====================================

1. Enter Chemical Name
2. Enter Chemical Formula
3. Emergency Response
4. Exit

## Information Available
For every chemical stored in the database, the application can display:
    
1)Basic Information:
●Chemical Name
●Molecular Formula
●Molar Mass
●CAS Number
●Chemical Type
●Appearance
●Color
●Odor
●Physical State
2)Physical Properties:
●Density
●Melting Point
●Boiling Point
●Freezing Point
●Vapor Pressure
●Vapor Density
●Specific Gravity
●Water Solubility
●Other Solubility
●ph
●Flash Point
●Autoignition Temperature
●Flammability Limits
●Partition Coefficient (Log Kow)
●Refractive Index
●Viscosity
●Evaporation Rate
●Decomposition Temperature
●Electrical Conductivity
3)Safety Information:
●GHS Classification
●Signal Word
●Hazard Statements
●Precautionary Statements
●NFPA Rating
●HMIS Rating
●Toxicity Information
●Corrosive Status
●Flammability
●Oxidizing Property
●Reactivity
●Explosive Property
●Environmental Hazard
4)Personal Protective Equipment (PPE):
●Protective Gloves
●Safety Goggles
●Face Shield
●Lab Coat
●Respirator
●Safety Shoes
5)Storage Guidelines:
●Storage Temperature
●Storage Class
●Container Type
●Ventilation Requirements
●Incompatible Chemicals
●First Aid Procedures
●Skin Contact
●Eye Contact
●Inhalation
●Ingestion
6)Emergency Response:
●Spill Response
●Fire Fighting Method
●Suitable Extinguishing Media
●Unsuitable Extinguishing Media

##Chemical Database
All chemical information is stored in a structured JSON file.
Example:
{
  "hydrochloric acid": {
    "formula": "HCl",
    "molar_mass": "36.46 g/mol",
    "...": "..."
  }
}
Adding new chemicals only requires inserting another JSON object that follows the existing data structure.

## Future Improvements

- Export reports as PDF or TXT
- Search using partial names
- Search by CAS Number
- Chemical categories
- Colorized terminal output
- Graphical User Interface (GUI)
- Web version using Flask or Django


##Learning Objectives

This project demonstrates:

- Python programming
- JSON file handling
- Exception handling
- Functions
- Dictionaries and nested data structures
- Menu-driven applications
- Modular programming
- Chemical safety information management


##Author

**SHAKIBA BINTE ISLAM**

