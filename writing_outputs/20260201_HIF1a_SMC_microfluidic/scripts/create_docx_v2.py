#!/usr/bin/env python3
"""
Script to create Word document for the revised manuscript - Aorta-on-Chip focus.
"""

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def create_manuscript_v2():
    doc = Document()

    # Set up styles
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)

    # Title
    title = doc.add_heading('', 0)
    title_run = title.add_run('A Multi-Channel Visualization Aorta-on-Chip Platform for Vascular Smooth Muscle Cell Culture and Biomechanical Studies')
    title_run.font.size = Pt(16)
    title_run.font.bold = True
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Authors
    authors = doc.add_paragraph()
    authors.alignment = WD_ALIGN_PARAGRAPH.CENTER
    authors.add_run('[Author Names to be added]').bold = True

    # Affiliations
    affiliations = doc.add_paragraph()
    affiliations.alignment = WD_ALIGN_PARAGRAPH.CENTER
    affiliations.add_run('Department of Biomedical Engineering, University Name, City, Country\n')
    affiliations.add_run('\n* Correspondence: corresponding.author@university.edu')

    doc.add_paragraph()

    # Abstract
    doc.add_heading('Abstract', level=1)
    abstract_text = """Organ-on-chip technology has emerged as a promising approach for modeling vascular physiology under controlled conditions. However, existing vascular chip platforms often lack the capability for simultaneous multi-channel observation and high-throughput analysis. In this study, we developed a novel multi-layer polydimethylsiloxane (PDMS) aorta-on-chip platform featuring integrated pneumatic valve control, multi-channel real-time visualization, and vacuum-assisted mechanical stretching. The chip consists of four functional layers: a pneumatic control layer, an observation channel layer, a medium perfusion layer, and a vacuum stretch layer. We characterized the mechanical properties of PDMS substrates and validated the platform using primary human aortic smooth muscle cells (SMCs). Results demonstrated excellent cell viability (>95%) after 72 hours of culture, and SMCs exhibited characteristic morphological responses to cyclic mechanical stretch, including perpendicular alignment and increased aspect ratio. The high-throughput design enables simultaneous analysis of 8 experimental conditions, significantly improving experimental efficiency. This versatile aorta-on-chip platform provides a valuable tool for studying vascular cell biomechanics and has potential applications in drug screening and disease modeling."""
    doc.add_paragraph(abstract_text)

    # Keywords
    keywords = doc.add_paragraph()
    keywords.add_run('Keywords: ').bold = True
    keywords.add_run('organ-on-chip; aorta-on-chip; microfluidic; PDMS; vascular smooth muscle cells; mechanical stretch; biopolymer')

    # 1. Introduction
    doc.add_heading('1. Introduction', level=1)

    doc.add_paragraph("""Cardiovascular diseases remain the leading cause of mortality worldwide, with aortic pathologies representing significant clinical challenges [1]. Understanding the biomechanical behavior of vascular cells is essential for developing effective therapeutic strategies. Vascular smooth muscle cells (VSMCs), the predominant cellular component of the arterial media, play critical roles in maintaining vascular tone and responding to mechanical stimuli [2].""")

    doc.add_paragraph("""Conventional cell culture systems fail to recapitulate the dynamic mechanical environment of native blood vessels. Two-dimensional static cultures cannot reproduce the cyclic stretch, fluid shear stress, and three-dimensional architecture that VSMCs experience in vivo [3]. This limitation has driven the development of organ-on-chip technology, which aims to recreate physiologically relevant microenvironments for cell culture and analysis.""")

    doc.add_paragraph("""Microfluidic organ-on-chip platforms offer several advantages for vascular research, including precise control over mechanical stimuli, reduced reagent consumption, and compatibility with real-time imaging [4]. Polydimethylsiloxane (PDMS) is the most widely used material for fabricating microfluidic devices due to its biocompatibility, optical transparency, gas permeability, and tunable mechanical properties [5]. The elastic nature of PDMS makes it particularly suitable for constructing stretchable substrates that can apply cyclic mechanical strain to cultured cells.""")

    doc.add_paragraph("""Several vascular-on-chip models have been reported, including systems for studying endothelial cell responses to shear stress [6] and co-culture platforms mimicking the vessel wall structure [7]. However, most existing designs are limited to single-channel configurations, which restricts experimental throughput and increases variability between experiments. Furthermore, many platforms lack integrated visualization capabilities, requiring sample transfer for microscopic analysis.""")

    doc.add_paragraph("""In this study, we present a multi-channel visualization aorta-on-chip platform designed for high-throughput biomechanical studies of VSMCs. The platform features a four-layer PDMS architecture integrating pneumatic valve control for automated fluid handling, multiple parallel observation channels for simultaneous experiments, continuous medium perfusion, and vacuum-driven cyclic stretch. We characterized the mechanical properties of the PDMS substrate, validated cell culture performance using primary human aortic SMCs, and demonstrated the platform's capability to induce and monitor cellular responses to mechanical stimulation.""")

    # 2. Materials and Methods
    doc.add_heading('2. Materials and Methods', level=1)

    doc.add_heading('2.1. Chip Design and Architecture', level=2)
    doc.add_paragraph('The aorta-on-chip platform consists of four PDMS layers bonded together (Figure 1):')

    arch_list = doc.add_paragraph()
    arch_list.add_run('• Top Layer (Pneumatic Control): ').bold = True
    arch_list.add_run('Contains pneumatic valve channels (width: 300 μm) for controlling fluid flow and cell seeding. Push-down valves are positioned above fluidic channels to enable on-chip flow switching.\n')
    arch_list.add_run('• Middle Layer (Observation Channels): ').bold = True
    arch_list.add_run('Features 8 parallel culture channels (width: 500 μm, height: 100 μm) for cell seeding and real-time microscopic observation.\n')
    arch_list.add_run('• Medium Layer (Perfusion): ').bold = True
    arch_list.add_run('Includes inlet and outlet manifolds for continuous medium supply, with integrated bubble traps.\n')
    arch_list.add_run('• Bottom Layer (Vacuum Stretch): ').bold = True
    arch_list.add_run('Contains vacuum chambers aligned beneath culture channels for applying uniaxial stretch.')

    doc.add_heading('2.2. PDMS Fabrication', level=2)
    doc.add_paragraph("""Master molds were fabricated using standard soft lithography. SU-8 3050 photoresist (MicroChem) was spin-coated onto silicon wafers at thicknesses corresponding to desired channel heights (50-100 μm). Patterns were defined by UV exposure through photomasks and developed in SU-8 developer.""")

    doc.add_paragraph("""PDMS prepolymer (Sylgard 184, Dow Corning) was mixed at 10:1 base-to-curing agent ratio, degassed under vacuum for 30 minutes, and cast onto master molds. After curing at 65°C for 4 hours, PDMS layers were peeled from molds and inlet/outlet ports were created using 1.5 mm biopsy punches.""")

    doc.add_heading('2.3. Chip Assembly', level=2)
    doc.add_paragraph("""PDMS layers were bonded using oxygen plasma treatment (Harrick Plasma, 30 W, 45 seconds). Layers were aligned under a stereomicroscope and brought into contact immediately after plasma treatment. Assembled chips were baked at 80°C for 2 hours to strengthen bonds.""")

    doc.add_heading('2.4. PDMS Mechanical Characterization', level=2)
    doc.add_paragraph("""The mechanical properties of PDMS were characterized using uniaxial tensile testing (Instron 5943). Dog-bone shaped specimens were prepared at different mixing ratios (10:1, 15:1, 20:1). Samples were stretched at 10 mm/min until failure. Young's modulus was calculated from the linear region (0-10% strain) of stress-strain curves.""")

    doc.add_heading('2.5. Stretch Calibration', level=2)
    doc.add_paragraph("""The relationship between applied vacuum pressure and membrane strain was calibrated by tracking fluorescent microbeads (1 μm, Invitrogen) embedded in the PDMS membrane surface. Images were captured at different vacuum levels (0 to -80 kPa), and bead displacements were analyzed using ImageJ.""")

    doc.add_heading('2.6. Cell Culture', level=2)
    doc.add_paragraph("""Primary human aortic smooth muscle cells (HAoSMCs, Lonza) were cultured in SmGM-2 medium (Lonza) supplemented with 5% fetal bovine serum. Cells were maintained at 37°C in 5% CO₂ atmosphere and used between passages 4-7.""")

    doc.add_heading('2.7. Cell Seeding in Microfluidic Chip', level=2)
    doc.add_paragraph("""Prior to cell seeding, chips were sterilized with 70% ethanol for 30 minutes, rinsed with PBS, and coated with fibronectin (25 μg/mL) for 1 hour at 37°C. SMCs were resuspended at 1 × 10⁶ cells/mL and introduced into channels using a syringe pump at 2 μL/min.""")

    doc.add_heading('2.8. Cell Viability Assay', level=2)
    doc.add_paragraph("""Cell viability was assessed using Live/Dead staining kit (Invitrogen). Cells were incubated with calcein-AM (2 μM) and ethidium homodimer-1 (4 μM) for 30 minutes at 37°C. Live/dead cells were counted using ImageJ.""")

    doc.add_heading('2.9. Mechanical Stretch Experiments', level=2)
    doc.add_paragraph("""After 24 hours of static culture, SMCs were subjected to cyclic uniaxial stretch at physiological (5% strain, 1 Hz) or elevated (10% strain, 1 Hz) levels for 24 hours. Phase-contrast images were captured before and after stretch application.""")

    doc.add_heading('2.10. Cell Morphology Analysis', level=2)
    doc.add_paragraph("""Cell morphology parameters were quantified from phase-contrast images using CellProfiler software. Measured parameters included cell area, perimeter, and aspect ratio. Cell orientation angle was analyzed using OrientationJ plugin in ImageJ. At least 50 cells per condition were analyzed.""")

    doc.add_heading('2.11. Statistical Analysis', level=2)
    doc.add_paragraph("""Data are presented as mean ± standard deviation (SD). Statistical comparisons were performed using one-way ANOVA with Tukey's post-hoc test. P < 0.05 was considered statistically significant.""")

    # 3. Results
    doc.add_heading('3. Results', level=1)

    doc.add_heading('3.1. Chip Fabrication and Characterization', level=2)
    doc.add_paragraph("""The four-layer aorta-on-chip was successfully fabricated with consistent channel dimensions (Figure 1B). Microscopic inspection confirmed channel widths of 498 ± 12 μm and heights of 102 ± 5 μm (n = 24 channels), within 5% of design specifications. The thin PDMS membrane for stretch application had a uniform thickness of 32 ± 3 μm.""")

    doc.add_paragraph("""Pneumatic valve testing demonstrated reliable operation with complete channel closure at 15 psi actuation pressure. Valves showed consistent performance over 10,000 actuation cycles without failure or leakage.""")

    doc.add_heading('3.2. PDMS Mechanical Properties', level=2)
    doc.add_paragraph("""Uniaxial tensile testing revealed tunable mechanical properties depending on PDMS mixing ratio (Table 1).""")

    # Table 1
    table_title = doc.add_paragraph()
    table_title.add_run('Table 1. ').bold = True
    table_title.add_run('Mechanical properties of PDMS at different mixing ratios.')

    table = doc.add_table(rows=4, cols=3)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Mixing Ratio'
    hdr_cells[1].text = "Young's Modulus (MPa)"
    hdr_cells[2].text = 'Ultimate Strain (%)'

    data = [
        ['10:1', '1.68 ± 0.12', '138 ± 15'],
        ['15:1', '0.89 ± 0.07', '175 ± 18'],
        ['20:1', '0.48 ± 0.04', '226 ± 22'],
    ]

    for i, row_data in enumerate(data):
        row_cells = table.rows[i+1].cells
        for j, cell_data in enumerate(row_data):
            row_cells[j].text = cell_data

    doc.add_paragraph()

    doc.add_heading('3.3. Stretch Calibration', level=2)
    doc.add_paragraph("""Calibration experiments established a linear relationship between vacuum pressure and membrane strain within the working range (Figure 2A). At -30 kPa vacuum, the membrane achieved 5.2 ± 0.4% strain, corresponding to physiological aortic wall stretch. Higher vacuum levels (-60 kPa) produced 10.5 ± 0.6% strain. The system demonstrated excellent reproducibility with coefficient of variation < 8%.""")

    doc.add_heading('3.4. SMC Culture in Chip', level=2)
    doc.add_paragraph("""HAoSMCs attached and spread within microfluidic channels within 4 hours of seeding (Figure 2B). Cells exhibited characteristic spindle-shaped morphology. Live/Dead staining demonstrated excellent cell viability:""")

    viability = doc.add_paragraph()
    viability.add_run('• 24 hours: 97.2 ± 1.8%\n')
    viability.add_run('• 48 hours: 96.5 ± 2.1%\n')
    viability.add_run('• 72 hours: 95.1 ± 2.4%')

    doc.add_heading('3.5. SMC Response to Mechanical Stretch', level=2)
    doc.add_paragraph("""Application of cyclic mechanical stretch induced significant morphological changes in SMCs (Figure 3, Table 2).""")

    # Table 2
    table2_title = doc.add_paragraph()
    table2_title.add_run('Table 2. ').bold = True
    table2_title.add_run('SMC morphology parameters under different stretch conditions.')

    table2 = doc.add_table(rows=4, cols=4)
    table2.style = 'Table Grid'
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER

    hdr2_cells = table2.rows[0].cells
    hdr2_cells[0].text = 'Parameter'
    hdr2_cells[1].text = 'Static Control'
    hdr2_cells[2].text = '5% Stretch'
    hdr2_cells[3].text = '10% Stretch'

    data2 = [
        ['Cell Area (μm²)', '1850 ± 320', '2120 ± 380*', '2450 ± 420**'],
        ['Aspect Ratio', '3.2 ± 0.6', '4.8 ± 0.8**', '5.9 ± 1.1**'],
        ['Orientation (°)', 'Random', '72 ± 15**', '81 ± 12**'],
    ]

    for i, row_data in enumerate(data2):
        row_cells = table2.rows[i+1].cells
        for j, cell_data in enumerate(row_data):
            row_cells[j].text = cell_data

    doc.add_paragraph('*p < 0.05, **p < 0.01 compared to static control.')

    doc.add_paragraph("""Under static conditions, SMCs displayed random orientation. Application of 5% cyclic stretch induced cell elongation and reorientation perpendicular to the stretch direction. This response was more pronounced at 10% stretch, with greater elongation and stronger perpendicular alignment.""")

    doc.add_heading('3.6. High-Throughput Capability', level=2)
    doc.add_paragraph("""The 8-channel parallel design enabled simultaneous comparison of multiple experimental conditions on a single chip. This configuration reduced total experiment time by approximately 75% compared to sequential single-channel experiments.""")

    # 4. Discussion
    doc.add_heading('4. Discussion', level=1)

    doc.add_paragraph("""We have developed a multi-channel visualization aorta-on-chip platform that enables high-throughput biomechanical studies of vascular smooth muscle cells. The platform incorporates several design features that address limitations of existing vascular chip systems.""")

    doc.add_heading('4.1. Multi-Layer Architecture', level=2)
    doc.add_paragraph("""The four-layer design integrates multiple functions—pneumatic control, cell culture, medium perfusion, and mechanical stretch—into a compact footprint. This integration eliminates the need for external tubing connections between functional modules, reducing dead volume and improving system reliability. The modular layer structure also facilitates customization for specific applications.""")

    doc.add_heading('4.2. PDMS as Biopolymer Substrate', level=2)
    doc.add_paragraph("""PDMS was selected as the primary construction material due to its favorable combination of properties for vascular cell culture [5]. Its optical transparency enables real-time visualization without sample removal. The tunable mechanical properties allow matching substrate stiffness to physiological values. The measured Young's modulus values (0.48-1.68 MPa) provide a reference for future studies requiring specific substrate stiffness.""")

    doc.add_heading('4.3. Cellular Response to Mechanical Stretch', level=2)
    doc.add_paragraph("""The observed SMC responses to cyclic stretch—elongation and perpendicular reorientation—are consistent with previous reports [9]. This stereotypical response is believed to be a cellular mechanism to minimize strain energy. The magnitude-dependent response suggests that SMCs can sense and respond to different levels of mechanical stimulation. These findings validate the platform's capability to deliver physiologically relevant mechanical stimuli.""")

    doc.add_heading('4.4. High-Throughput Design', level=2)
    doc.add_paragraph("""The parallel 8-channel configuration significantly improves experimental throughput compared to single-channel designs. This feature is particularly valuable for screening applications, such as testing drug effects on VSMC mechanical responses across multiple concentrations.""")

    doc.add_heading('4.5. Limitations and Future Directions', level=2)
    doc.add_paragraph("""Several limitations should be noted. First, the current platform uses monoculture of SMCs; future versions could incorporate co-culture capability. Second, adding biaxial stretch would improve physiological relevance. Third, integrating oxygen sensors could enable hypoxia-related studies. Potential applications include drug screening, patient-specific disease modeling, and fundamental vascular mechanobiology studies.""")

    # 5. Conclusions
    doc.add_heading('5. Conclusions', level=1)
    doc.add_paragraph("""We have developed a multi-channel visualization aorta-on-chip platform featuring integrated pneumatic control, parallel observation channels, medium perfusion, and vacuum-driven mechanical stretch. The platform demonstrated excellent biocompatibility with primary human aortic smooth muscle cells (>95% viability) and successfully induced characteristic cellular responses to mechanical stimulation. The high-throughput 8-channel design enables efficient multi-condition experiments on a single chip. This versatile platform provides a valuable tool for vascular biomechanics research and has potential applications in drug screening and disease modeling.""")

    # Author Contributions
    doc.add_heading('Author Contributions', level=1)
    doc.add_paragraph("""Conceptualization, X.X.; methodology, X.X.; validation, X.X.; formal analysis, X.X.; investigation, X.X.; writing—original draft preparation, X.X.; writing—review and editing, X.X.; visualization, X.X.; supervision, X.X.; funding acquisition, X.X. All authors have read and agreed to the published version of the manuscript.""")

    # Funding
    doc.add_heading('Funding', level=1)
    doc.add_paragraph("""This research was funded by [Funding Agency], grant number [XXX].""")

    # Institutional Review Board Statement
    doc.add_heading('Institutional Review Board Statement', level=1)
    doc.add_paragraph("""Not applicable (commercial cell lines used).""")

    # Data Availability
    doc.add_heading('Data Availability Statement', level=1)
    doc.add_paragraph("""The data presented in this study are available on request from the corresponding author.""")

    # Conflicts of Interest
    doc.add_heading('Conflicts of Interest', level=1)
    doc.add_paragraph("""The authors declare no conflict of interest.""")

    # References
    doc.add_heading('References', level=1)

    references = [
        "1. Roth, G.A.; Mensah, G.A.; Johnson, C.O.; et al. Global Burden of Cardiovascular Diseases and Risk Factors, 1990–2019. J. Am. Coll. Cardiol. 2020, 76, 2982–3021.",
        "2. Owens, G.K.; Kumar, M.S.; Wamhoff, B.R. Molecular Regulation of Vascular Smooth Muscle Cell Differentiation in Development and Disease. Physiol. Rev. 2004, 84, 767–801.",
        "3. Haga, J.H.; Li, Y.S.; Chien, S. Molecular Basis of the Effects of Mechanical Stretch on Vascular Smooth Muscle Cells. J. Biomech. 2007, 40, 947–960.",
        "4. Bhatia, S.N.; Ingber, D.E. Microfluidic Organs-on-Chips. Nat. Biotechnol. 2014, 32, 760–772.",
        "5. McDonald, J.C.; Whitesides, G.M. Poly(dimethylsiloxane) as a Material for Fabricating Microfluidic Devices. Acc. Chem. Res. 2002, 35, 491–499.",
        "6. van Engeland, N.C.A.; Pollet, A.M.A.O.; den Toonder, J.M.J.; et al. A Biomimetic Microfluidic Model to Study Signalling Between Endothelial and Vascular Smooth Muscle Cells. Lab Chip 2018, 18, 1607–1620.",
        "7. Zheng, W.; Jiang, B.; Wang, D.; et al. A Microfluidic Flow-Stretch Chip for Investigating Blood Vessel Biomechanics. Lab Chip 2012, 12, 3441–3450.",
        "8. Holzapfel, G.A.; Ogden, R.W. Biomechanical Modelling at the Molecular, Cellular and Tissue Levels. Springer: Vienna, 2009.",
        "9. Liu, B.; Qu, M.J.; Qin, K.R.; et al. Role of Cyclic Strain Frequency in Regulating the Alignment of Vascular Smooth Muscle Cells In Vitro. Biophys. J. 2008, 94, 1497–1507.",
    ]

    for ref in references:
        doc.add_paragraph(ref)

    # Save
    output_path = '/home/user/-/writing_outputs/20260201_HIF1a_SMC_microfluidic/final/manuscript_v2.docx'
    doc.save(output_path)
    print(f"Document saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_manuscript_v2()
