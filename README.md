# Dodge Ram Service Manual - Consolidated Documentation

## Overview

This directory contains the complete 1998-1999 Dodge Ram Service Manual converted from scanned PDFs to markdown format. The structure has been optimized for efficient LLM reference and navigation.

**Stats:**
- **Total Chapters:** 43
- **Total Pages:** 2,261 markdown files
- **Total Size:** 63 MB
- **Images:** Co-located with markdown files

## Directory Structure

```
service_manual/
├── INDEX.md                          # Master index - START HERE
├── README.md                         # This file
│
├── 00_Introduction/                  # 16 pages
├── 0_Lubrication_and_Maintenance/    # 33 pages (28 base + 5 supplement)
├── 2_Suspension/                     # 26 pages
├── 3_Differential_and_Driveline/     # 155 pages
├── 5_Brakes/                         # 56 pages
├── 6_Clutch/                         # 17 pages
├── 7_Cooling_System/                 # 89 pages (includes supplement)
├── 8A_Battery/                       # 18 pages
├── 8B_Starting_Systems/              # 12 pages
├── 8C_Charging_System/               # 12 pages (includes supplement)
├── 8D_Ignition_System/               # 29 pages
├── 8E_Insturment_Panel_Systems/      # 37 pages
├── 8F_Audio_Systems/                 # 11 pages
├── 8G_Horn_Systems/                  # 4 pages
├── 8H_Vehicle_Speed_Control_System/  # 16 pages (includes supplement)
├── 8J_Turn_Signal_and_Hazard_Systems/# 6 pages
├── 8K_Wiper_and_Washer_Systems/      # 12 pages
├── 8L_Lamps/                         # 18 pages
├── 8M_Passive_Restraint_Systems/     # 17 pages
├── 8N_Electrically_Heated_Systems/   # 3 pages
├── 8p_Power_Door_Locks/              # 8 pages
├── 8Q_Vehicle_Theft_Security_Systems/# 5 pages
├── 8R_Power_Seat_Systems/            # 5 pages
├── 8S_Power_Window_Systems/          # 4 pages
├── 8T_Power_Mirror_Systems/          # 5 pages
├── 8U_Chime_Buzzer_Warning_Systems/  # 6 pages
├── 8V_Overhead_Console_Systems/      # 8 pages
├── 8W_Wiring_Diagrams_indexes/       # 28 pages - Searchable YAML indexes
├── 8W_01_GENERAL_INFORMATION/        # 14 pages - Wire codes, symbols
├── 8W_Wiring_Diagrams/               # 59 pages - Additional diagrams
├── 8W_Wiring_Diagrams_sections/      # 298 pages - All 27 wiring sections
├── 9_Engine/                         # 299 pages (all batches merged)
├── 11_Exhaust_System_and_Intake_Manifold/ # 37 pages (includes supplement)
├── 13_Frame_and_Bumpers/             # 10 pages
├── 14_Fuel_System/                   # 134 pages
├── 19_Steering/                      # 30 pages
├── 21_Transmission_and_Transfer_Case/ # 410 pages
├── 22_Tires_and_Wheels/              # 11 pages
├── 23_Body/                          # 67 pages
├── 24_Heating_and_Air_Conditioning/  # 48 pages
├── 25_Emission_Control_Systems/      # 42 pages (includes supplement)
├── Body_Shop_Manual/                 # 118 pages
└── 99_Index/                         # 28 pages - Original manual index
```

## How to Use

### For Humans

1. **Start with INDEX.md** - Contains links to all chapters
2. **Each chapter has _CHAPTER_INDEX.md** - Quick navigation within chapters
3. **Images are embedded** - Figures are in the same directory as markdown files
4. **Page numbers match PDF** - Original page numbering preserved

### For LLMs

**Best Practices:**
- Reference the master `INDEX.md` first to find relevant chapters
- Use relative paths: `service_manual/Chapter/_CHAPTER_INDEX.md`
- Page files follow pattern: `page_N_Title.md`
- Images use pattern: `page_N_fig_M.jpg`
- Wiring diagrams use pattern: `8W-XX-Y.md` where XX=section, Y=diagram number

**Quick Reference Paths:**
```
Engine specs:           9_Engine/_CHAPTER_INDEX.md
Wiring diagrams:        8W_Wiring_Diagrams_sections/_CHAPTER_INDEX.md
Wiring reference data:  8W_01_GENERAL_INFORMATION/_CHAPTER_INDEX.md
Searchable indexes:     8W_Wiring_Diagrams_indexes/_CHAPTER_INDEX.md
Torque specs:           [Search within relevant chapter]
Diagnostic procedures:  [Chapter specific - see INDEX.md]
```

**Search Strategy:**
1. Check `INDEX.md` for chapter organization
2. Read `_CHAPTER_INDEX.md` in relevant chapter
3. Access specific pages using relative paths
4. Images are co-located with their pages

## Special Sections

### Wiring Diagrams (8W_*)
- **8W_01_GENERAL_INFORMATION/** - Wire color codes, circuit functions, symbols
- **8W_Wiring_Diagrams_indexes/** - YAML indexes for fuses, connectors, components, grounds, splices
- **8W_Wiring_Diagrams_sections/** - All 27 wiring sections with structured YAML frontmatter:
  - AIRBAG SYSTEM
  - AIR CONDITIONING/HEATER
  - ALL-WHEEL ANTI-LOCK BRAKES
  - AUDIO SYSTEM
  - CHARGING SYSTEM
  - COMPONENT INDEX
  - CONNECTOR LOCATIONS/PIN-OUTS
  - FRONT LIGHTING
  - FUEL/IGNITION SYSTEMS
  - GROUND DISTRIBUTION
  - HORN/CIGAR LIGHTER/POWER OUTLET
  - INSTRUMENT CLUSTER
  - INTERIOR LIGHTING
  - JUNCTION BLOCK
  - OVERHEAD CONSOLE
  - POWER DISTRIBUTION
  - POWER WINDOWS
  - REAR WHEEL ANTI-LOCK BRAKES
  - SPLICE INFORMATION/LOCATIONS
  - STARTING SYSTEM
  - TURN SIGNALS
  - VEHICLE SPEED CONTROL
  - VEHICLE THEFT SECURITY SYSTEM
  - WIPERS

### Engine Chapter (9_Engine/)
Contains all 299 pages from the complete engine service manual including:
- General information and service procedures
- Gasoline engines (3.9L, 5.2L, 5.9L, 8.0L V10)
- Diesel engine (5.9L Cummins)
- Diagnosis and testing procedures
- Removal and installation procedures
- Specifications and torque values

## File Naming Conventions

- **Chapters:** `NN_Chapter_Name/` where NN is chapter number
- **Pages:** `page_N_Title.md` where N is page number
- **Figures:** `page_N_fig_M.jpg` where M is figure number
- **Diagrams:** `8W-XX-Y.md` where XX=section, Y=diagram
- **Indexes:** `_CHAPTER_INDEX.md` in each chapter directory

## Conversion Pipeline

Files were processed through a 6-stage pipeline:
1. Page extraction from PDF
2. Surya OCR (text, layout, tables)
3. AI-assisted text review and correction
4. Figure extraction from layout detection
5. AI-assisted figure verification
6. Markdown assembly with figure links

**Quality Notes:**
- All pages reviewed by Claude API for accuracy
- Tables validated and restructured
- Figures verified and captioned
- OCR errors corrected
- Original page numbers preserved

## Source Information

**Original:** 1998-1999 Dodge Ram Factory Service Manual
**Format:** Scanned PDF → Markdown conversion
**Processing:** PDF-to-Markdown pipeline with Surya OCR + Claude API review
**Date Generated:** 2025

---

*For technical details on the conversion process, see CLAUDE.md in the project root.*
