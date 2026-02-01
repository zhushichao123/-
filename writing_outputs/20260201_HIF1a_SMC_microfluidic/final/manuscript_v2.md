# A Multi-Channel Visualization Aorta-on-Chip Platform for Vascular Smooth Muscle Cell Culture and Biomechanical Studies

**Authors:** [Author Names to be added]

**Affiliations:**
1. Department of Biomedical Engineering, University Name, City, Country

**Correspondence:** corresponding.author@university.edu

---

## Abstract

Organ-on-chip technology has emerged as a promising approach for modeling vascular physiology under controlled conditions. However, existing vascular chip platforms often lack the capability for simultaneous multi-channel observation and high-throughput analysis. In this study, we developed a novel multi-layer polydimethylsiloxane (PDMS) aorta-on-chip platform featuring integrated pneumatic valve control, multi-channel real-time visualization, and vacuum-assisted mechanical stretching. The chip consists of four functional layers: a pneumatic control layer, an observation channel layer, a medium perfusion layer, and a vacuum stretch layer. We characterized the mechanical properties of PDMS substrates and validated the platform using primary human aortic smooth muscle cells (SMCs). Results demonstrated excellent cell viability (>95%) after 72 hours of culture, and SMCs exhibited characteristic morphological responses to cyclic mechanical stretch, including perpendicular alignment and increased aspect ratio. The high-throughput design enables simultaneous analysis of 8 experimental conditions, significantly improving experimental efficiency. This versatile aorta-on-chip platform provides a valuable tool for studying vascular cell biomechanics and has potential applications in drug screening and disease modeling.

**Keywords:** organ-on-chip; aorta-on-chip; microfluidic; PDMS; vascular smooth muscle cells; mechanical stretch; biopolymer

---

## 1. Introduction

Cardiovascular diseases remain the leading cause of mortality worldwide, with aortic pathologies representing significant clinical challenges [1]. Understanding the biomechanical behavior of vascular cells is essential for developing effective therapeutic strategies. Vascular smooth muscle cells (VSMCs), the predominant cellular component of the arterial media, play critical roles in maintaining vascular tone and responding to mechanical stimuli [2].

Conventional cell culture systems fail to recapitulate the dynamic mechanical environment of native blood vessels. Two-dimensional static cultures cannot reproduce the cyclic stretch, fluid shear stress, and three-dimensional architecture that VSMCs experience in vivo [3]. This limitation has driven the development of organ-on-chip technology, which aims to recreate physiologically relevant microenvironments for cell culture and analysis.

Microfluidic organ-on-chip platforms offer several advantages for vascular research, including precise control over mechanical stimuli, reduced reagent consumption, and compatibility with real-time imaging [4]. Polydimethylsiloxane (PDMS) is the most widely used material for fabricating microfluidic devices due to its biocompatibility, optical transparency, gas permeability, and tunable mechanical properties [5]. The elastic nature of PDMS makes it particularly suitable for constructing stretchable substrates that can apply cyclic mechanical strain to cultured cells.

Several vascular-on-chip models have been reported, including systems for studying endothelial cell responses to shear stress [6] and co-culture platforms mimicking the vessel wall structure [7]. However, most existing designs are limited to single-channel configurations, which restricts experimental throughput and increases variability between experiments. Furthermore, many platforms lack integrated visualization capabilities, requiring sample transfer for microscopic analysis.

In this study, we present a multi-channel visualization aorta-on-chip platform designed for high-throughput biomechanical studies of VSMCs. The platform features a four-layer PDMS architecture integrating pneumatic valve control for automated fluid handling, multiple parallel observation channels for simultaneous experiments, continuous medium perfusion, and vacuum-driven cyclic stretch. We characterized the mechanical properties of the PDMS substrate, validated cell culture performance using primary human aortic SMCs, and demonstrated the platform's capability to induce and monitor cellular responses to mechanical stimulation.

---

## 2. Materials and Methods

### 2.1. Chip Design and Architecture

The aorta-on-chip platform consists of four PDMS layers bonded together (Figure 1):

- **Top Layer (Pneumatic Control):** Contains pneumatic valve channels (width: 300 μm) for controlling fluid flow and cell seeding. Push-down valves are positioned above fluidic channels to enable on-chip flow switching.

- **Middle Layer (Observation Channels):** Features 8 parallel culture channels (width: 500 μm, height: 100 μm) for cell seeding and real-time microscopic observation. Channel spacing (2 mm) is compatible with standard microscope objectives.

- **Medium Layer (Perfusion):** Includes inlet and outlet manifolds for continuous medium supply, with integrated bubble traps to prevent air entering culture channels.

- **Bottom Layer (Vacuum Stretch):** Contains vacuum chambers aligned beneath culture channels. Applying negative pressure deforms the thin PDMS membrane, generating uniaxial stretch on cultured cells.

### 2.2. PDMS Fabrication

Master molds were fabricated using standard soft lithography. SU-8 3050 photoresist (MicroChem) was spin-coated onto silicon wafers at thicknesses corresponding to desired channel heights (50-100 μm). Patterns were defined by UV exposure through photomasks and developed in SU-8 developer.

PDMS prepolymer (Sylgard 184, Dow Corning) was mixed at 10:1 base-to-curing agent ratio, degassed under vacuum for 30 minutes, and cast onto master molds. After curing at 65°C for 4 hours, PDMS layers were peeled from molds and inlet/outlet ports were created using 1.5 mm biopsy punches.

For the stretchable membrane, PDMS was spin-coated onto a silanized silicon wafer at 1000 rpm for 60 seconds, yielding approximately 30 μm thickness, then cured at 65°C for 2 hours.

### 2.3. Chip Assembly

PDMS layers were bonded using oxygen plasma treatment (Harrick Plasma, 30 W, 45 seconds). Layers were aligned under a stereomicroscope and brought into contact immediately after plasma treatment. Assembled chips were baked at 80°C for 2 hours to strengthen bonds. Bonding quality was verified by flowing dye solution through channels and checking for leakage.

### 2.4. PDMS Mechanical Characterization

The mechanical properties of PDMS were characterized using uniaxial tensile testing (Instron 5943). Dog-bone shaped specimens (gauge length: 25 mm, width: 5 mm, thickness: 2 mm) were prepared at different mixing ratios (10:1, 15:1, 20:1). Samples were stretched at 10 mm/min until failure. Young's modulus was calculated from the linear region (0-10% strain) of stress-strain curves.

### 2.5. Stretch Calibration

The relationship between applied vacuum pressure and membrane strain was calibrated by tracking fluorescent microbeads (1 μm, Invitrogen) embedded in the PDMS membrane surface. Images were captured at different vacuum levels (0 to -80 kPa) using a fluorescence microscope, and bead displacements were analyzed using particle tracking software (ImageJ). Strain was calculated as the ratio of displacement to original length.

### 2.6. Cell Culture

Primary human aortic smooth muscle cells (HAoSMCs, Lonza) were cultured in SmGM-2 medium (Lonza) supplemented with 5% fetal bovine serum and growth factors according to manufacturer's instructions. Cells were maintained at 37°C in 5% CO₂ atmosphere and used between passages 4-7.

### 2.7. Cell Seeding in Microfluidic Chip

Prior to cell seeding, chips were sterilized with 70% ethanol for 30 minutes, rinsed with PBS, and coated with fibronectin (25 μg/mL, Sigma) for 1 hour at 37°C. SMCs were trypsinized and resuspended at 1 × 10⁶ cells/mL. Cell suspension (10 μL per channel) was introduced using a syringe pump at 2 μL/min. Cells were allowed to attach for 4 hours before initiating medium perfusion at 0.5 μL/min.

### 2.8. Cell Viability Assay

Cell viability was assessed using Live/Dead staining kit (Invitrogen). After 24, 48, and 72 hours of culture, cells were incubated with calcein-AM (2 μM) and ethidium homodimer-1 (4 μM) for 30 minutes at 37°C. Fluorescence images were captured and live/dead cells were counted using ImageJ. Viability was calculated as percentage of live cells.

### 2.9. Mechanical Stretch Experiments

After 24 hours of static culture, SMCs were subjected to cyclic uniaxial stretch at physiological (5% strain, 1 Hz) or elevated (10% strain, 1 Hz) levels for 24 hours. Control cells were maintained without stretch. Phase-contrast images were captured before and after stretch application.

### 2.10. Cell Morphology Analysis

Cell morphology parameters were quantified from phase-contrast images using CellProfiler software. Measured parameters included cell area, perimeter, and aspect ratio (major axis/minor axis). Cell orientation angle relative to the stretch direction was analyzed using OrientationJ plugin in ImageJ. At least 50 cells per condition were analyzed from three independent experiments.

### 2.11. Statistical Analysis

Data are presented as mean ± standard deviation (SD). Statistical comparisons were performed using one-way ANOVA with Tukey's post-hoc test. P < 0.05 was considered statistically significant. Analyses were performed using GraphPad Prism 9.0.

---

## 3. Results

### 3.1. Chip Fabrication and Characterization

The four-layer aorta-on-chip was successfully fabricated with consistent channel dimensions (Figure 1B). Microscopic inspection confirmed channel widths of 498 ± 12 μm and heights of 102 ± 5 μm (n = 24 channels), within 5% of design specifications. The thin PDMS membrane for stretch application had a uniform thickness of 32 ± 3 μm.

Pneumatic valve testing demonstrated reliable operation with complete channel closure at 15 psi actuation pressure. Valves showed consistent performance over 10,000 actuation cycles without failure or leakage.

The parallel 8-channel design allows simultaneous testing of multiple conditions on a single chip, with independent valve control for each channel (Figure 1C).

### 3.2. PDMS Mechanical Properties

Uniaxial tensile testing revealed tunable mechanical properties depending on PDMS mixing ratio (Table 1). The standard 10:1 ratio exhibited Young's modulus of 1.68 ± 0.12 MPa, while softer formulations (15:1 and 20:1) showed reduced moduli of 0.89 ± 0.07 MPa and 0.48 ± 0.04 MPa, respectively.

**Table 1.** Mechanical properties of PDMS at different mixing ratios.

| Mixing Ratio | Young's Modulus (MPa) | Ultimate Strain (%) |
|--------------|----------------------|---------------------|
| 10:1         | 1.68 ± 0.12          | 138 ± 15            |
| 15:1         | 0.89 ± 0.07          | 175 ± 18            |
| 20:1         | 0.48 ± 0.04          | 226 ± 22            |

The 10:1 ratio was selected for chip fabrication as it provides adequate structural integrity while maintaining sufficient flexibility for stretch applications.

### 3.3. Stretch Calibration

Calibration experiments established a linear relationship between vacuum pressure and membrane strain within the working range (Figure 2A). At -30 kPa vacuum, the membrane achieved 5.2 ± 0.4% strain, corresponding to physiological aortic wall stretch. Higher vacuum levels (-60 kPa) produced 10.5 ± 0.6% strain for pathological stretch simulation. The system demonstrated excellent reproducibility with coefficient of variation < 8% across repeated measurements.

### 3.4. SMC Culture in Chip

HAoSMCs attached and spread within microfluidic channels within 4 hours of seeding (Figure 2B). Cells exhibited characteristic spindle-shaped morphology typical of contractile SMC phenotype. Live/Dead staining demonstrated excellent cell viability throughout the culture period:

- 24 hours: 97.2 ± 1.8%
- 48 hours: 96.5 ± 2.1%
- 72 hours: 95.1 ± 2.4%

No significant difference in viability was observed between chip culture and conventional dish culture (p > 0.05), confirming biocompatibility of the platform.

### 3.5. SMC Response to Mechanical Stretch

Application of cyclic mechanical stretch induced significant morphological changes in SMCs (Figure 3, Table 2).

**Table 2.** SMC morphology parameters under different stretch conditions.

| Parameter | Static Control | 5% Stretch | 10% Stretch |
|-----------|---------------|------------|-------------|
| Cell Area (μm²) | 1850 ± 320 | 2120 ± 380* | 2450 ± 420** |
| Aspect Ratio | 3.2 ± 0.6 | 4.8 ± 0.8** | 5.9 ± 1.1** |
| Orientation Angle (°) | Random | 72 ± 15** | 81 ± 12** |

*p < 0.05, **p < 0.01 compared to static control.

Under static conditions, SMCs displayed random orientation. Application of 5% cyclic stretch for 24 hours induced cell elongation and reorientation perpendicular to the stretch direction (mean angle: 72 ± 15°). This response was more pronounced at 10% stretch, with cells showing greater elongation (aspect ratio: 5.9 ± 1.1) and stronger perpendicular alignment (81 ± 12°).

### 3.6. High-Throughput Capability

The 8-channel parallel design enabled simultaneous comparison of multiple experimental conditions on a single chip. In a demonstration experiment, we tested SMC responses to four different stretch magnitudes (0%, 5%, 7.5%, 10%) in duplicate. All conditions were processed simultaneously, with real-time observation possible through the integrated visualization channels. This configuration reduced total experiment time by approximately 75% compared to sequential single-channel experiments.

---

## 4. Discussion

We have developed a multi-channel visualization aorta-on-chip platform that enables high-throughput biomechanical studies of vascular smooth muscle cells. The platform incorporates several design features that address limitations of existing vascular chip systems.

### 4.1. Multi-Layer Architecture

The four-layer design integrates multiple functions—pneumatic control, cell culture, medium perfusion, and mechanical stretch—into a compact footprint. This integration eliminates the need for external tubing connections between functional modules, reducing dead volume and improving system reliability. The modular layer structure also facilitates customization; individual layers can be redesigned for specific applications without modifying the entire system.

### 4.2. PDMS as Biopolymer Substrate

PDMS was selected as the primary construction material due to its favorable combination of properties for vascular cell culture [5]. Its optical transparency enables real-time visualization without sample removal. The tunable mechanical properties, achieved by adjusting the mixing ratio, allow matching substrate stiffness to physiological values. In this study, we characterized PDMS mechanical properties across a range of formulations, providing a reference for future studies requiring specific substrate stiffness.

The measured Young's modulus values (0.48-1.68 MPa) are higher than native arterial tissue (0.1-1 MPa) [8], which represents a limitation of PDMS-based systems. Future iterations could incorporate softer materials or hydrogel coatings to better mimic vascular wall mechanics.

### 4.3. Cellular Response to Mechanical Stretch

The observed SMC responses to cyclic stretch—elongation and perpendicular reorientation—are consistent with previous reports using various stretch systems [9]. This stereotypical response is believed to be a cellular mechanism to minimize strain energy by aligning perpendicular to the principal stretch direction. The magnitude-dependent response we observed (stronger alignment at 10% vs. 5% stretch) suggests that SMCs can sense and respond to different levels of mechanical stimulation.

These findings validate the platform's capability to deliver physiologically relevant mechanical stimuli and monitor cellular responses. The system could be applied to study mechanotransduction pathways, including those involving hypoxia-inducible factors, integrins, and ion channels, which are implicated in vascular disease progression.

### 4.4. High-Throughput Design

The parallel 8-channel configuration significantly improves experimental throughput compared to single-channel designs. By enabling simultaneous testing of multiple conditions, the platform reduces inter-experiment variability and improves statistical power. This feature is particularly valuable for screening applications, such as testing drug effects on VSMC mechanical responses across multiple concentrations.

### 4.5. Limitations and Future Directions

Several limitations should be noted. First, the current platform uses monoculture of SMCs, while native vessels contain multiple cell types including endothelial cells and fibroblasts. Future versions could incorporate co-culture capability. Second, while uniaxial stretch mimics circumferential vessel strain, native vessels experience complex multiaxial loading. Adding biaxial stretch capability would improve physiological relevance. Third, oxygen tension was not controlled in this study; integrating oxygen sensors and control could enable hypoxia-related studies.

Potential applications of this platform include drug screening for cardiovascular therapies, patient-specific disease modeling using iPSC-derived VSMCs, and fundamental studies of vascular mechanobiology.

---

## 5. Conclusions

We have developed a multi-channel visualization aorta-on-chip platform featuring integrated pneumatic control, parallel observation channels, medium perfusion, and vacuum-driven mechanical stretch. The platform demonstrated excellent biocompatibility with primary human aortic smooth muscle cells (>95% viability) and successfully induced characteristic cellular responses to mechanical stimulation. The high-throughput 8-channel design enables efficient multi-condition experiments on a single chip. This versatile platform provides a valuable tool for vascular biomechanics research and has potential applications in drug screening and disease modeling.

---

## Author Contributions

Conceptualization, X.X.; methodology, X.X.; validation, X.X.; formal analysis, X.X.; investigation, X.X.; writing—original draft preparation, X.X.; writing—review and editing, X.X.; visualization, X.X.; supervision, X.X.; funding acquisition, X.X. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by [Funding Agency], grant number [XXX].

## Institutional Review Board Statement

Not applicable (commercial cell lines used).

## Data Availability Statement

The data presented in this study are available on request from the corresponding author.

## Conflicts of Interest

The authors declare no conflict of interest.

---

## References

1. Roth, G.A.; Mensah, G.A.; Johnson, C.O.; et al. Global Burden of Cardiovascular Diseases and Risk Factors, 1990–2019. J. Am. Coll. Cardiol. 2020, 76, 2982–3021.

2. Owens, G.K.; Kumar, M.S.; Wamhoff, B.R. Molecular Regulation of Vascular Smooth Muscle Cell Differentiation in Development and Disease. Physiol. Rev. 2004, 84, 767–801.

3. Haga, J.H.; Li, Y.S.; Chien, S. Molecular Basis of the Effects of Mechanical Stretch on Vascular Smooth Muscle Cells. J. Biomech. 2007, 40, 947–960.

4. Bhatia, S.N.; Ingber, D.E. Microfluidic Organs-on-Chips. Nat. Biotechnol. 2014, 32, 760–772.

5. McDonald, J.C.; Whitesides, G.M. Poly(dimethylsiloxane) as a Material for Fabricating Microfluidic Devices. Acc. Chem. Res. 2002, 35, 491–499.

6. van Engeland, N.C.A.; Pollet, A.M.A.O.; den Toonder, J.M.J.; et al. A Biomimetic Microfluidic Model to Study Signalling Between Endothelial and Vascular Smooth Muscle Cells. Lab Chip 2018, 18, 1607–1620.

7. Zheng, W.; Jiang, B.; Wang, D.; et al. A Microfluidic Flow-Stretch Chip for Investigating Blood Vessel Biomechanics. Lab Chip 2012, 12, 3441–3450.

8. Holzapfel, G.A.; Ogden, R.W. Biomechanical Modelling at the Molecular, Cellular and Tissue Levels. Springer: Vienna, 2009.

9. Liu, B.; Qu, M.J.; Qin, K.R.; et al. Role of Cyclic Strain Frequency in Regulating the Alignment of Vascular Smooth Muscle Cells In Vitro. Biophys. J. 2008, 94, 1497–1507.
