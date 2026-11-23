# Released Model overview

This documents the training/validation species and some standard settings for the released
Helixer models. Five models have been released, four of which are available for auto-selection
via the `--lineage` parameter of `Helixer.py`. Only a random selection of 800 subsequences per
validation species were used for the models land_plant, fungi, vertebrate, invertebrate.

## Table of Contents
1. [land_plant model](#land_plant)
2. [fungi model](#fungi)
3. [vertebrate model](#vertebrate)
4. [invertebrate model](#invertebrate)
5. [mammal model](#mammal)

## Models
### land_plant
Default inference settings when used via `--lineage`:

| --subsequence-length | --overlap-offset | --overlap-core-length |
|:---------------------|:-----------------|:----------------------|
| 64152                | 32076            | 48114                 |

Training/validation species for the selected best model (`land_plant_v0.3_a_0080.h5`):

| Training species          | Phytozome accession | Validation species             | Phytzome accession |
|:--------------------------|:--------------------|:-------------------------------|:-------------------|
| Ananas comosus            | v3                  | Amaranthus hypochondriacus     | v2.1               |
| Arabidopsis thaliana      | TAIR10              | Arabidopsis lyrata             | v2.1               |
| Brachypodium distachyon   | v3.1                | Asparagus officinalis          | V1.1               |
| Cicer arietinum           | v1.0                | Amborella trichopoda           | v1.0               |
| Capsella grandiflora      | v1.1                | Brachypodium hybridum          | v1.1               |
| Chlamydomonas reinhardtii | v5.6                | Brassica oleracea              | v1.0               |
| Capsella rubella          | v1.1                | Brassica rapa                  | v1.3               |
| Eutrema salsugineum       | v1.0                | Beta vulgaris                  | EL10_1.0           |
| Fragaria vesca            | v4.0.a2             | Citrus clementina              | v1.0               |
| Glycine max               | Wm82.a4.v1          | Cinnamomum kanehirae           | v3                 |
| Lotus japonicus           | Lj1.0v1             | Carica papaya                  | ASGPBv0.4          |
| Linum usitatissimum       | v1.0                | Chenopodium quinoa             | v1.0               |
| Musa acuminata            | v1                  | Cucumis sativus                | v1.0               |
| Manihot esculenta         | v8.1                | Citrus sinensis                | v1.1               |
| Mimulus guttatus          | v2.0                | Coccomyxa subellipsoidea C-169 | v2.0               |
| Marchantia polymorpha     | v3.1                | Chromochloris zofingiensis     | v5.2.3.2           |
| Micromonas pusilla        | v3.0                | Dioscorea alata                | v2.1               |
| Medicago truncatula       | Mt4.0v1             | Daucus carota                  | v2.0               |
| Nymphaea colorata         | v1.2                | Dunaliella salina              | v1.0               |
| Ostreococcus lucimarinus  | v2.0                | Eucalyptus grandis             | v2.0               |
| Oryza sativa              | v7.0                | Gossypium raimondii            | v2.1               |
| Oropetium thomaeum        | v1.0                | Glycine soja                   | v1.1               |
| Phaseolus acutifolius     | v1.0                | Helianthus annuus              | r1.2               |
| Prunus persica            | v2.1                | Hordeum vulgare                | r1                 |
| Porphyra umbilicalis      | v1.5                | Kalanchoe fedtschenkoi         | v1.1               |
| Sorghum bicolor           | v3.1.1              | Lupinus albus                  | v1                 |
| Solanum lycopersicum      | ITAG3.2             | Lactuca sativa                 | v5                 |
| Schrenkiella parvula      | v2.2                | Malus domestica                | v1.1               |
| Triticum aestivum         | v2.2                | Micromonas sp. RCC299          | v3.0               |
| Trifolium pratense        | v2                  | Olea europaea                  | v1.0               |
| Volvox carteri            | v2.1                | Panicum hallii                 | v3.2               |
| Zea mays                  | RefGen_V4           | Physcomitrella patens          | v3.3               |
|                           |                     | Populus trichocarpa            | v4.1               |
|                           |                     | Poncirus trifoliata            | v1.3.1             |
|                           |                     | Panicum virgatum               | v5.1               |
|                           |                     | Ricinus communis               | v0.1               |
|                           |                     | Setaria italica                | v2.2               |
|                           |                     | Selaginella moellendorffii     | v1.0               |
|                           |                     | Spirodela polyrhiza            | v2                 |
|                           |                     | Salix purpurea                 | v1.0               |
|                           |                     | Solanum tuberosum              | v4.03              |
|                           |                     | Theobroma cacao                | v2.1               |
|                           |                     | Vigna unguiculata              | v1.2               |
|                           |                     | Vitis vinifera                 | v2.1               |
|                           |                     | Zostera marina                 | v3.1               |


### fungi
Default inference settings when used via `--lineage`:

| --subsequence-length        | --overlap-offset           | --overlap-core-length      |
|:----------------------------|:---------------------------|:---------------------------|
| 21384                       | 10692                      | 16038                      |

Training/validation species for the selected best model (`fungi_v0.3_a_0100.h5`):

| Training species                | NCBI accession                                     | Validation species                    | NCBI accession                                     |
|:--------------------------------|:---------------------------------------------------|:--------------------------------------|:---------------------------------------------------|
| Agaricus bisporus               | GCF_000300575.1_Agabi_varbisH97_2                  | Aaosphaeria arxii                     | GCF_010015735.1_Aaoar1                             |
| Alternaria arborescens          | GCF_004154835.1_ASM415483v1                        | Alternaria atra                       | GCF_907166805.1_ALTATR162                          |
| Alternaria burnsii              | GCF_013036055.1_ASM1303605v1                       | Alternaria rosae                      | GCF_020736505.1_Altro1                             |
| Amorphotheca resinae            | GCF_003019875.1_Amore1                             | Ascochyta rabiei                      | GCF_004011695.1_Arabiei_Me14                       |
| Apiotrichum porosum             | GCF_003942205.1_ASM394220v1                        | Ascoidea rubescens                    | GCF_001661345.1_Ascru1                             |
| Aspergillus alliaceus           | GCF_009176365.1_Aspalli1                           | Aspergillus aculeatinus               | GCF_003184765.1_Aspacu1                            |
| Aspergillus campestris          | GCF_002847485.1_Aspcam1                            | Aspergillus aculeatus                 | GCF_001890905.1_Aspac1                             |
| Aspergillus chevalieri          | GCF_016861735.1_AchevalieriM1_assembly01           | Aspergillus bombycis                  | GCF_001792695.1_ASM179269v1                        |
| Aspergillus clavatus            | GCF_000002715.2_ASM271v1                           | Aspergillus brunneoviolaceus          | GCF_003184695.1_Aspbru1                            |
| Aspergillus homomorphus         | GCF_003184865.1_Asphom1                            | Aspergillus caelatus                  | GCF_009193585.1_Aspcae1                            |
| Aspergillus japonicus           | GCF_003184785.1_Aspjap1                            | Aspergillus candidus                  | GCF_002847045.1_Aspcand1                           |
| Aspergillus luchuensis          | GCF_016861625.1_AkawachiiIFO4308_assembly01        | Aspergillus flavus                    | GCF_014117465.1_ASM1411746v1                       |
| Aspergillus nomiae              | GCF_001204775.2_ASM120477v2                        | Aspergillus fumigatus                 | GCF_000002655.1_ASM265v1                           |
| Aspergillus tanneri             | GCF_003426965.1_ASM342696v1                        | Aspergillus heteromorphus             | GCF_003184545.1_Asphet1                            |
| Aspergillus tubingensis         | GCF_013340325.1_ASM1334032v1                       | Aspergillus ibericus                  | GCF_003184845.1_Aspibe1                            |
| Aspergillus udagawae            | GCF_001078395.1_Aud_assembly02                     | Aspergillus melleus                   | GCF_016097325.1_ASM1609732v1                       |
| Aspergillus uvarum              | GCF_003184745.1_Aspuva1                            | Aspergillus nidulans                  | GCF_000149205.2_ASM14920v2                         |
| Aspergillus viridinutans        | GCF_018404265.1_Aspvir_assembly01                  | Aspergillus novofumigatus             | GCF_002847465.1_Aspnov1                            |
| Aspergillus welwitschiae        | GCF_003344945.1_Aspwel1                            | Aspergillus oryzae                    | GCF_000184455.2_ASM18445v3                         |
| Aureobasidium pullulans         | GCF_000721785.1_Aureobasidium_pullulans_var._pu... | Aspergillus pseudonomiae              | GCF_009193645.1_Asppsen1                           |
| Batrachochytrium dendrobatidis  | GCF_000203795.1_v1.0                               | Aspergillus pseudotamarii             | GCF_009193445.1_Asppset1                           |
| Bipolaris sorokiniana           | GCF_000338995.1_Cocsa1                             | Aspergillus pseudoviridinutans        | GCF_018340605.1_Asppvi_assembly01                  |
| Bipolaris victoriae             | GCF_000527765.1_Cochliobolus_victoriae_v1.0        | Aspergillus ruber                     | GCF_000600275.1_Eurhe1                             |
| Blastomyces dermatitidis        | GCF_000003525.1_BD_ER3_V1                          | Aspergillus sclerotioniger            | GCF_003184525.1_Aspscl1                            |
| Boeremia exigua                 | GCF_020726555.1_Boeex1                             | Aspergillus steynii                   | GCF_002849105.1_Aspste1                            |
| Botrytis cinerea                | GCF_000143535.2_ASM14353v4                         | Aspergillus thermomutatus             | GCF_002237265.1_ASM223726v2                        |
| Botrytis fragariae              | GCF_013461495.1_Bfra_R1V1                          | Aspergillus vadensis                  | GCF_003184925.1_Aspvad1                            |
| Botrytis porri                  | GCF_014898465.1_ASM1489846v1                       | Aspergillus versicolor                | GCF_001890125.1_Aspve1                             |
| Candida auris                   | GCF_002775015.1_Cand_auris_B11221_V1               | Aspergillus wentii                    | GCF_001890725.1_Aspwe1                             |
| Candida haemuloni               | GCF_002926055.2_CanHae_1.0                         | Aureobasidium namibiae                | GCF_000721765.1_Aureobasidium_pullulans_var._na... |
| Candida parapsilosis            | GCF_000182765.1_ASM18276v2                         | Aureobasidium subglaciale             | GCF_000721755.1_Aureobasidium_pullulans_var._su... |
| Candida tropicalis              | GCF_000006335.3_ASM633v3                           | Babjeviella inositovora               | GCF_001661335.1_Babin1                             |
| Capronia epimyces               | GCF_000585565.1_Capr_epim_CBS_606_96_V1            | Bacidia gigantensis                   | GCF_019456465.1_ASM1945646v1                       |
| Ceraceosorus guamensis          | GCF_003144195.1_Cersp1                             | Beauveria bassiana                    | GCF_000280675.1_ASM28067v1                         |
| Chaetomium globosum             | GCF_000143365.1_ASM14336v1                         | Bipolaris maydis                      | GCF_000354255.1_CocheC4_1                          |
| Coccidioides posadasii          | GCF_000151335.2_JCVI-cpa1-1.0                      | Bipolaris oryzae                      | GCF_000523455.1_Cochliobolus_miyabeanus_v1.0       |
| Colletotrichum higginsianum     | GCF_001672515.1_ASM167251v1                        | Blastomyces gilchristii               | GCF_000003855.2_BD_SLH14081_V1                     |
| Coniosporium apollinis          | GCF_000281105.1_Coni_apol_CBS100218_V1             | Brettanomyces nanus                   | GCF_011074865.1_ASM1107486v2                       |
| Cordyceps militaris             | GCF_000225605.1_CmilitarisCM01_v01                 | Candida albicans                      | GCF_000182965.3_ASM18296v3                         |
| Cucurbitaria berberidis         | GCF_010015615.1_Cucbe1                             | Candida dubliniensis                  | GCF_000026945.1_ASM2694v1                          |
| Cutaneotrichosporon oleaginosum | GCF_001027345.1_Triol1                             | Candida orthopsilosis                 | GCF_000315875.1_ASM31587v1                         |
| Cyberlindnera jadinii           | GCF_001661405.1_Cybja1                             | Cantharellus anzutake                 | GCF_015039405.1_Cananz1                            |
| Debaryomyces fabryi             | GCF_001447935.2_debFab1.1                          | Capronia coronata                     | GCF_000585585.1_Capr_coro_CBS_617_96_V1            |
| Diaporthe citri                 | GCF_014595645.1_ASM1459564v1                       | Chaetomium thermophilum               | GCF_000221225.1_CTHT_3.0                           |
| Dichomitus squalens             | GCF_000275845.1_Dichomitus_squalens_v1.0           | Cladophialophora carrionii            | GCF_000365165.1_Clad_carr_CBS_160_54_V1            |
| Diutina rugosa                  | GCF_008704595.1_ASM870459v1                        | Clavispora lusitaniae                 | GCF_000003835.1_ASM383v1                           |
| Drechmeria coniospora           | GCF_001625195.1_ASM162519v1                        | Colletotrichum aenigma                | GCF_013390185.1_ASM1339018v1                       |
| Emericellopsis atlantica        | GCF_019669845.1_AcreTS7_1                          | Colletotrichum fructicola             | GCF_009771025.1_ASM977102v1                        |
| Encephalitozoon cuniculi        | GCF_000091225.1_ASM9122v1                          | Colletotrichum graminicola            | GCF_000149035.1_C_graminicola_M1_001_V1            |
| Endocarpon pusillum             | GCF_000464535.1_EPUS                               | Colletotrichum karsti                 | GCF_011947395.1_ASM1194739v2                       |
| Eremomyces bilateralis          | GCF_010015585.1_Erebi1                             | Colletotrichum siamense               | GCF_013390195.1_ASM1339019v1                       |
| Exophiala aquamarina            | GCF_000709125.1_Exop_aqua_CBS_119918_V1            | Coniophora puteana                    | GCF_000271625.1_Conpu1                             |
| Exophiala oligosperma           | GCF_000835515.1_Exop_olig_CBS72588_V1              | Coprinopsis cinerea                   | GCF_000182895.1_CC3                                |
| Exserohilum turcicum            | GCF_000359705.1_Setospaeria_trucica_Et28A_v1.0     | Cryptococcus amylolentus              | GCF_001720205.1_Cryp_amyl_CBS6039_V3               |
| Filobasidium floriforme         | GCF_021052385.1_Filflo1                            | Cryptococcus neoformans               | GCF_000091045.1_ASM9104v1                          |
| Fomitiporia mediterranea        | GCF_000271605.1_Fomme1                             | Cyphellophora europaea                | GCF_000365145.1_Phia_euro_CBS_101466_V1            |
| Fonsecaea pedrosoi              | GCF_000835455.1_Fons_pedr_CBS_271_37_V1            | Dacryopinax primogenitus              | GCF_000292625.1_Dacryopinax_sp._DJM_731_SSP1_v1.0  |
| Fusarium flagelliforme          | GCF_020744385.1_Fuseq1                             | Diaporthe batatas                     | GCF_019321695.1_ASM1932169v1                       |
| Fusarium fujikuroi              | GCF_900079805.1_Fusarium_fujikuroi_IMI58289_V2     | Diplodia corticola                    | GCF_001883845.1_ASM188384v1                        |
| Fusarium mangiferae             | GCF_900044065.1_Genome_assembly_version_1          | Dothidotthia symphoricarpi            | GCF_010015815.1_Dotsy1                             |
| Fusarium odoratissimum          | GCF_000260195.1_FO_II5_V1                          | Encephalitozoon hellem                | GCF_000277815.2_ASM27781v3                         |
| Fusarium proliferatum           | GCF_900067095.1_F._proliferatum_ET1_version_1      | Encephalitozoon romaleae              | GCF_000280035.1_ASM28003v2                         |
| Fusarium pseudograminearum      | GCF_000303195.2_FP7                                | Eremothecium gossypii                 | GCF_000091025.4_ASM9102v4                          |
| Geosmithia morbida              | GCF_012550715.1_ASM1255071v1                       | Eremothecium sinecaudum               | GCF_001548555.1_ASM154855v1                        |
| Grosmannia clavigera            | GCF_000143105.1_Sanger-454-IlluminaPA_2.0          | Exophiala spinifera                   | GCF_000836115.1_Exop_spin_CBS89968_V1              |
| Heterobasidion irregulare       | GCF_000320585.1_Heterobasidion_irregulare_v2.0     | Exophiala xenobiotica                 | GCF_000835505.1_Exop_xeno_CBS118157_V1             |
| Hyaloscypha bicolor             | GCF_002865645.1_Melbi2                             | Fibroporia radiculosa                 | GCF_000313525.1_ASM31352v1                         |
| Kluyveromyces lactis            | GCF_000002515.2_ASM251v1                           | Fonsecaea erecta                      | GCF_001651985.1_ASM165198v1                        |
| Kwoniella pini                  | GCF_000512605.1_Cryp_pinu_CBS10737_V1              | Fonsecaea monophora                   | GCF_001642475.1_ASM164247v1                        |
| Laetiporus sulphureus           | GCF_001632365.1_Laesu1                             | Fonsecaea nubica                      | GCF_001646965.1_ASM164696v1                        |
| Lentinula edodes                | GCF_021015755.1_Lenedo1                            | Fusarium coffeatum                    | GCF_003316985.1_ASM331698v1                        |
| Letharia columbiana             | GCF_014066305.1_Lecol_v1.0                         | Fusarium oxysporum                    | GCF_000271745.1_FO_FOSC_3_a_V1                     |
| Malassezia sympodialis          | GCF_000349305.1_ASM34930v2                         | Fusarium redolens                     | GCF_020744475.1_Fusre1                             |
| Melampsora larici-populina      | GCF_000204055.1_v1.0                               | Fusarium venenatum                    | GCF_900007375.1_ASM90000737v1                      |
| Metarhizium brunneum            | GCF_000814965.1_MBR_1.0                            | Guyanagaster necrorhizus              | GCF_019112545.1_Guyne1                             |
| Microsporum canis               | GCF_000151145.1_ASM15114v1                         | Hirsutella rhossiliensis              | GCF_020360975.1_ASM2036097v1                       |
| Mixia osmundae                  | GCF_000708205.1_Mixia_osmundae_v1.0                | Histoplasma capsulatum                | GCF_000150115.1_ASM15011v1                         |
| Morchella importuna             | GCF_003444635.1_ASM344463v2                        | Histoplasma mississippiense nom inval | GCF_000149585.1_ASM14958v1                         |
| Morchella sextelata             | GCF_020137385.1_ASM2013738v1                       | Hyphopichia burtonii                  | GCF_001661395.1_Hypbu1                             |
| Mytilinidion resinicola         | GCF_010093595.1_Mytre1                             | Jaminaea rosea                        | GCF_003144245.1_Jamsp1                             |
| Neurospora tetrasperma          | GCF_000213175.1_v2.0                               | Kockovaella imperatae                 | GCF_002102565.1_Kocim1                             |
| Nosema ceranae                  | GCF_000988165.1_ASM98816v1                         | Komagataella phaffii                  | GCF_000027005.1_ASM2700v1                          |
| Ogataea polymorpha              | GCF_001664045.1_Hanpo2                             | Kuraishia capsulata                   | GCF_000576695.1_AUH_PRJEB4427_v1                   |
| Pestalotiopsis fici             | GCF_000516985.1_PFICI                              | Kwoniella bestiolae                   | GCF_000512585.1_Cryp_best_CBS10118_V1              |
| Pneumocystis murina             | GCF_000349005.2_Pneumo_murina_B123_V4              | Kwoniella dejecticola                 | GCF_000512565.1_Cryp_deje_CBS10117_V1              |
| Pochonia chlamydosporia         | GCF_001653235.2_ASM165323v2                        | Kwoniella mangrovensis                | GCF_000507465.1_Kwon_mang_CBS8507_V2               |
| Podospora anserina              | GCF_000226545.1_ASM22654v1                         | Kwoniella shandongensis               | GCF_008629635.1_Kwon_shan_CBS_12478_V1             |
| Postia placenta                 | GCF_002117355.1_PosplRSB12_1                       | Lachancea thermotolerans              | GCF_000142805.1_ASM14280v1                         |
| Pseudogymnoascus destructans    | GCF_001641265.1_ASM164126v1                        | Lasiodiplodia theobromae              | GCF_012971845.1_ASM1297184v1                       |
| Pseudogymnoascus verrucosus     | GCF_001662655.1_ASM166265v1                        | Leptosphaeria maculans                | GCF_000230375.1_ASM23037v1                         |
| Pseudomassariella vexata        | GCF_002105095.1_Pseve2                             | Lindgomyces ingoldianus               | GCF_010093535.1_Linin1                             |
| Pseudozyma hubeiensis           | GCF_000403515.1_ASM40351v1                         | Lodderomyces elongisporus             | GCF_000149685.1_ASM14968v1                         |
| Punctularia strigosozonata      | GCF_000264995.1_Punctularia_strigosozonata_v1.0    | Macroventuria anomochaeta             | GCF_010093625.1_Macan1                             |
| Pyrenophora tritici-repentis    | GCF_000149985.1_ASM14998v1                         | Malassezia globosa                    | GCF_000181695.1_ASM18169v1                         |
| Rhinocladiella mackenziei       | GCF_000835555.1_Rhin_mack_CBS_650_93_V1            | Malassezia pachydermatis              | GCF_001278385.1_MalaPachy                          |
| Rhizophagus irregularis         | GCF_000439145.1_ASM43914v3                         | Meira miltonrushii                    | GCF_003144205.1_Meimi1                             |
| Saccharomyces cerevisiae        | GCF_000146045.2_R64                                | Metarhizium album                     | GCF_000804445.1_MAM_1.0_for_version_1_of_the_Me... |
| Saccharomyces paradoxus         | GCF_002079055.1_ASM207905v1                        | Metschnikowia bicuspidata             | GCF_001664035.1_Metbi1                             |
| Saprochaete ingens              | GCF_902498895.1_sapIngB                            | Meyerozyma guilliermondii             | GCF_000149425.1_ASM14942v1                         |
| Scheffersomyces stipitis        | GCF_000209165.1_ASM20916v1                         | Moesziomyces antarcticus              | GCF_000747765.1_ASM74776v1                         |
| Schizosaccharomyces cryophilus  | GCF_000004155.1_SCY4                               | Mollisia scopiformis                  | GCF_001500285.1_Phisc1                             |
| Schizosaccharomyces japonicus   | GCF_000149845.2_SJ5                                | Mycena indigotica                     | GCF_014461135.1_ASM1446113v1                       |
| Schizosaccharomyces pombe       | GCF_000002945.1_ASM294v2                           | Naumovozyma castellii                 | GCF_000237345.1_ASM23734v1                         |
| Sclerotinia sclerotiorum        | GCF_000146945.2_ASM14694v2                         | Naumovozyma dairenensis               | GCF_000227115.2_ASM22711v2                         |
| Sordaria macrospora             | GCF_000182805.2_ASM18280v2                         | Nematocida parisii                    | GCF_000250985.1_Nema_parisii_ERTm1_V3              |
| Sparassis crispa                | GCF_003851025.1_SCP_1.1                            | Neohortaea acidophila                 | GCF_010093505.1_Horac1                             |
| Spathaspora passalidarum        | GCF_000223485.1_Spathaspora_passalidarum_v2.0      | Ogataea haglerorum                    | GCF_019207285.1_ASM1920728v1                       |
| Sphaerulina musiva              | GCF_000320565.1_Septoria_musiva_SO2202_v1.0        | Ogataea parapolymorpha                | GCF_000187245.1_Hansenula_2                        |
| Spizellomyces punctatus         | GCF_000182565.1_S_punctatus_V1                     | Paraphaeosphaeria sporulosa           | GCF_001642045.1_Parsp1                             |
| Sugiyamaella lignohabitans      | GCF_001640025.1_ASM164002v2                        | Parastagonospora nodorum              | GCF_000146915.1_ASM14691v2                         |
| Suillus clintonianus            | GCF_016758775.1_Suicli1                            | Penicilliopsis zonata                 | GCF_001890105.1_Aspzo1                             |
| Suillus paluster                | GCF_016628075.1_Suipal1                            | Penicillium digitatum                 | GCF_000315645.1_PdigPd1_v1                         |
| Suillus plorans                 | GCF_016647745.1_Suiplo1                            | Penicillium griseofulvum              | GCF_001561935.1_ASM156193v1                        |
| Talaromyces rugulosus           | GCF_013368755.1_ASM1336875v1                       | Penicillium roqueforti                | GCF_015533775.1_ASM1553377v1                       |
| Thermothelomyces thermophilus   | GCF_000226095.1_ASM22609v1                         | Penicillium rubens                    | GCF_000226395.1_PenChr_Nov2007                     |
| Thermothielavioides terrestris  | GCF_000226115.1_ASM22611v1                         | Penicillium solitum                   | GCF_002072235.1_ASM207223v1                        |
| Tilletiaria anomala             | GCF_000711695.1_Tilletiaria_anomala_UBC_951_v1.0   | Phaeoacremonium minimum               | GCF_000392275.1_UCRPA7V03                          |
| Tremella mesenterica            | GCF_000271645.1_Treme1                             | Phycomyces blakesleeanus              | GCF_001638985.1_Phybl2                             |
| Trichoderma reesei              | GCF_000167675.1_v2.0                               | Pichia kudriavzevii                   | GCF_003054445.1_ASM305444v1                        |
| Tuber melanosporum              | GCF_000151645.1_ASM15164v1                         | Pichia membranifaciens                | GCF_001661235.1_Picme2                             |
| Uncinocarpus reesii             | GCF_000003515.1_ASM351v2                           | Pleurotus ostreatus                   | GCF_014466165.1_ASM1446616v1                       |
| Ustilago hordei                 | GCF_900519145.1_Uho2_v1                            | Pneumocystis jirovecii                | GCF_001477535.1_Pneu_jiro_RU7_V2                   |
| Vavraia culicis                 | GCF_000192795.1_Vavr_culi_floridensis_V1           | Protomyces lactucae-debilis           | GCF_002105105.1_Prola1                             |
| Venustampulla echinocandica     | GCF_003357145.1_ASM335714v1                        | Pseudomicrostroma glucosiphilum       | GCF_003144135.1_Rhodsp1                            |
| Wickerhamomyces anomalus        | GCF_001661255.1_Wican1                             | Pseudovirgaria hyperparasitica        | GCF_010093815.1_Psehy1                             |
| Xylona heveae                   | GCF_001619985.1_Xylona_heveae_TC161_v1.0           | Pseudozyma flocculosa                 | GCF_000417875.1_Pflocc_1.0                         |
| Yarrowia lipolytica             | GCF_000002525.2_ASM252v1                           | Pyricularia grisea                    | GCF_004355905.1_ASM435590v1                        |
| Zygosaccharomyces rouxii        | GCF_000026365.1_ASM2636v1                          | Pyricularia oryzae                    | GCF_000002495.2_MG8                                |
|                                 |                                                    | Pyricularia pennisetigena             | GCF_004337985.1_ASM433798v1                        |
|                                 |                                                    | Ramularia collo-cygni                 | GCF_900074925.1_version_1                          |
|                                 |                                                    | Rhodotorula toruloides                | GCF_000320785.1_RHOziaDV1.0                        |
|                                 |                                                    | Saccharomycodes ludwigii              | GCF_020623625.1_UHD_SCDLUD_16                      |
|                                 |                                                    | Saitoella complicata                  | GCF_001661265.1_Saico1                             |
|                                 |                                                    | Scedosporium apiospermum              | GCF_000732125.1_ScApio1.0                          |
|                                 |                                                    | Scheffersomyces spartinae             | GCF_019049425.1_ASM1904942v1                       |
|                                 |                                                    | Schizophyllum commune                 | GCF_000143185.1_v1.0                               |
|                                 |                                                    | Sporisorium graminicola               | GCF_005498985.1_PGRAM_IIB_1.0                      |
|                                 |                                                    | Sporothrix brasiliensis               | GCF_000820605.1_S_brasiliensis_5110_v1             |
|                                 |                                                    | Sporothrix schenckii                  | GCF_000961545.1_S_schenckii_v1                     |
|                                 |                                                    | Stereum hirsutum                      | GCF_000264905.1_Stehi1                             |
|                                 |                                                    | Suillus bovinus                       | GCF_016758785.1_Suibov1                            |
|                                 |                                                    | Suillus discolor                      | GCF_016758755.1_Suidis1                            |
|                                 |                                                    | Suillus subaureus                     | GCF_016647635.1_Suisub1                            |
|                                 |                                                    | Synchytrium microbalum                | GCF_006535985.1_ASM653598v1                        |
|                                 |                                                    | Talaromyces amestolkiae               | GCF_001896365.1_ASM189636v1                        |
|                                 |                                                    | Talaromyces atroroseus                | GCF_001907595.1_ASM190759v1                        |
|                                 |                                                    | Talaromyces marneffei                 | GCF_000001985.1_JCVI-PMFA1-2.0                     |
|                                 |                                                    | Talaromyces stipitatus                | GCF_000003125.1_JCVI-TSTA1-3.0                     |
|                                 |                                                    | Tetrapisispora blattae                | GCF_000315915.1_ASM31591v1                         |
|                                 |                                                    | Thyridium curvatum                    | GCF_004353045.1_ASM435304v1                        |
|                                 |                                                    | Tilletiopsis washingtonensis          | GCF_003144115.1_Tilwa1                             |
|                                 |                                                    | Trametes versicolor                   | GCF_000271585.1_Trametes_versicolor_v1.0           |
|                                 |                                                    | Trichoderma atroviride                | GCF_000171015.1_TRIAT_v2.0                         |
|                                 |                                                    | Trichoderma citrinoviride             | GCF_003025115.1_Trici_v4.0                         |
|                                 |                                                    | Trichoderma gamsii                    | GCF_001481775.2_TGAM01v2                           |
|                                 |                                                    | Trichoderma harzianum                 | GCF_003025095.1_Triha_v1.0                         |
|                                 |                                                    | Trichoderma virens                    | GCF_000170995.1_TRIVI_v2.0                         |
|                                 |                                                    | Trichophyton benhamiae                | GCF_000151125.1_ASM15112v2                         |
|                                 |                                                    | Ustilago maydis                       | GCF_000328475.2_Umaydis521_2.0                     |
|                                 |                                                    | Vanderwaltozyma polyspora             | GCF_000150035.1_ASM15003v1                         |
|                                 |                                                    | Verticillium alfalfae                 | GCF_000150825.1_ASM15082v1                         |
|                                 |                                                    | Verticillium dahliae                  | GCF_000150675.1_ASM15067v2                         |
|                                 |                                                    | Vittaforma corneae                    | GCF_000231115.1_Vitt_corn_V1                       |
|                                 |                                                    | Wallemia ichthyophaga                 | GCF_000400465.1_Wallemia_ichthyophaga_version_1.0  |
|                                 |                                                    | Wallemia mellicola                    | GCF_000263375.1_Wallemia_sebi_v1.0                 |
|                                 |                                                    | Wickerhamiella sorbophila             | GCF_002251995.1_ASM225199v2                        |
|                                 |                                                    | Wickerhamomyces ciferrii              | GCF_000313485.1_ASM31348v1                         |
|                                 |                                                    | Yamadazyma tenuis                     | GCF_000223465.1_Candida_tenuis_v1.0                |
|                                 |                                                    | Zasmidium cellare                     | GCF_010093935.1_Zasce1                             |
|                                 |                                                    | Zymoseptoria tritici                  | GCF_000219625.1_MYCGR_v2.0                         |

### vertebrate
Default inference settings when used via `--lineage`:

| --subsequence-length        | --overlap-offset           | --overlap-core-length      |
|:----------------------------|:---------------------------|:---------------------------|
| 213840                      | 106920                     | 160380                     |

Training/validation species for the selected best model (`vertebrate_v0.3_m_0080.h5`):

| Training species             | NCBI accession                       | Validation species            | NCBI accession                                    |
|:-----------------------------|:-------------------------------------|:------------------------------|:--------------------------------------------------|
| Camelus dromedarius          | GCF_000803125.2_CamDro3              | Acinonyx jubatus              | GCF_003709585.1_Aci_jub_2                         |
| Castor canadensis            | GCF_001984765.1_C.can_genome_v1.0    | Ailuropoda melanoleuca        | GCF_002007445.1_ASM200744v2                       |
| Cavia porcellus              | GCF_000151735.1_Cavpor3.0            | Aotus nancymaae               | GCF_000952055.2_Anan_2.0                          |
| Macaca fascicularis          | GCF_012559485.2_MFA1912RKSv2         | Arvicola amphibius            | GCF_903992535.2_mArvAmp1.2                        |
| Mustela putorius             | GCF_011764305.1_ASM1176430v1.1       | Bison bison                   | GCF_000754665.1_Bison_UMD1.0                      |
| Neogale vison                | GCF_020171115.1_ASM_NN_V1            | Bos indicus                   | GCF_000247795.1_Bos_indicus_1.0                   |
| Neomonachus schauinslandi    | GCF_002201575.2_ASM220157v2          | Bos mutus                     | GCF_000298355.1_BosGru_v2.0                       |
| Odobenus rosmarus            | GCF_000321225.1_Oros_1.0             | Bos taurus                    | GCF_002263795.1_ARS-UCD1.2                        |
| Panthera leo                 | GCF_018350215.1_P.leo_Ple1_pat1.1    | Bubalus bubalis               | GCF_019923935.1_NDDB_SH_1                         |
| Panthera tigris              | GCF_018350195.1_P.tigris_Pti1_mat1.1 | Callithrix jacchus            | GCF_009663435.1_Callithrix_jacchus_cj1700_1.1     |
| Tachyglossus aculeatus       | GCF_015852505.1_mTacAcu1.pri         | Callorhinus ursinus           | GCF_003265705.1_ASM326570v1                       |
| Talpa occidentalis           | GCF_014898055.1_MPIMG_talOcc4        | Canis lupus dingo             | GCF_012295265.1_UNSW_AlpineDingo_1.0              |
| Alligator mississippiensis   | GCF_000281125.3_ASM28112v4           | Canis lupus familiaris        | GCF_014441545.1_ROS_Cfam_1.0                      |
| Antrostomus carolinensis     | GCF_000700745.1_ASM70074v1           | Capra hircus                  | GCF_001704415.1_ARS1                              |
| Calidris pugnax              | GCF_001431845.1_ASM143184v1          | Carlito syrichta              | GCF_000164805.1_Tarsius_syrichta-2.0.1            |
| Chelonoidis abingdonii       | GCF_003597395.1_ASM359739v1          | Cebus imitator                | GCF_001604975.1_Cebus_imitator-1.0                |
| Gouania willdenowi           | GCF_900634775.1_fGouWil2.1           | Ceratotherium simum           | GCF_000283155.1_CerSimSim1.0                      |
| Lacerta agilis               | GCF_009819535.1_rLacAgi1.pri         | Cercocebus atys               | GCF_000955945.1_Caty_1.0                          |
| Leptosomus discolor          | GCF_000691785.1_ASM69178v1           | Cervus elaphus                | GCF_910594005.1_mCerEla1.1                        |
| Myripristis murdjan          | GCF_902150065.1_fMyrMur1.1           | Chinchilla lanigera           | GCF_000276665.1_ChiLan1.0                         |
| Nothoprocta perdicaria       | GCF_003342845.1_notPer1              | Chlorocebus sabaeus           | GCF_015252025.1_Vero_WHO_p1.0                     |
| Oxyura jamaicensis           | GCF_011077185.1_BPBGC_Ojam_1.0       | Chrysochloris asiatica        | GCF_000296735.1_ChrAsi1.0                         |
| Pipra filicauda              | GCF_003945595.2_ASM394559v2          | Colobus angolensis            | GCF_000951035.1_Cang.pa_1.0                       |
| Protobothrops mucrosquamatus | GCF_001527695.2_P.Mucros_1.0         | Cricetulus griseus            | GCF_000223135.1_CriGri_1.0                        |
| Pygocentrus nattereri        | GCF_015220715.1_fPygNat1.pri         | Dasypus novemcinctus          | GCF_000208655.1_Dasnov3.0                         |
| Sander lucioperca            | GCF_008315115.2_SLUC_FBN_1.2         | Delphinapterus leucas         | GCF_002288925.2_ASM228892v3                       |
| Scleropages formosus         | GCF_900964775.1_fSclFor1.1           | Dipodomys ordii               | GCF_000151885.1_Dord_2.0                          |
| Serinus canaria              | GCF_007115625.1_cibio_Scana_2019     | Dromiciops gliroides          | GCF_019393635.1_mDroGli1.pri                      |
| Struthio camelus             | GCF_000698965.1_ASM69896v1           | Echinops telfairi             | GCF_000313985.2_ASM31398v2                        |
| Tachysurus fulvidraco        | GCF_003724035.1_ASM372403v1          | Equus asinus                  | GCF_016077325.2_ASM1607732v2                      |
| Takifugu rubripes            | GCF_901000725.2_fTakRub1.2           | Equus caballus                | GCF_002863925.1_EquCab3.0                         |
|                              |                                      | Erinaceus europaeus           | GCF_000296755.1_EriEur2.0                         |
|                              |                                      | Felis catus                   | GCF_018350175.1_F.catus_Fca126_mat1.0             |
|                              |                                      | Fukomys damarensis            | GCF_012274545.1_DMR_v1.0_HiC                      |
|                              |                                      | Gorilla gorilla               | GCF_008122165.1_Kamilah_GGO_v0                    |
|                              |                                      | Heterocephalus glaber         | GCF_000247695.1_HetGla_female_1.0                 |
|                              |                                      | Hipposideros armiger          | GCF_001890085.1_ASM189008v1                       |
|                              |                                      | Homo sapiens                  | GCF_000001405.39_GRCh38.p13                       |
|                              |                                      | Hyaena hyaena                 | GCF_003009895.1_ASM300989v1                       |
|                              |                                      | Hylobates moloch              | GCF_009828535.2_HMol_V2                           |
|                              |                                      | Ictidomys tridecemlineatus    | GCF_016881025.1_HiC_Itri_2                        |
|                              |                                      | Jaculus jaculus               | GCF_020740685.1_mJacJac1.mat.Y.cur                |
|                              |                                      | Lemur catta                   | GCF_020740605.2_mLemCat1.pri                      |
|                              |                                      | Leptonychotes weddellii       | GCF_000349705.1_LepWed1.0                         |
|                              |                                      | Lipotes vexillifer            | GCF_000442215.1_Lipotes_vexillifer_v1             |
|                              |                                      | Lontra canadensis             | GCF_010015895.1_GSC_riverotter_1.0                |
|                              |                                      | Loxodonta africana            | GCF_000001905.1_Loxafr3.0                         |
|                              |                                      | Lynx canadensis               | GCF_007474595.2_mLynCan4.pri.v2                   |
|                              |                                      | Macaca mulatta                | GCF_003339765.1_Mmul_10                           |
|                              |                                      | Macaca nemestrina             | GCF_000956065.1_Mnem_1.0                          |
|                              |                                      | Mandrillus leucophaeus        | GCF_000951045.1_Mleu.le_1.0                       |
|                              |                                      | Marmota marmota               | GCF_001458135.1_marMar2.1                         |
|                              |                                      | Meles meles                   | GCF_922984935.1_mMelMel3.1_paternal_haplotype     |
|                              |                                      | Meriones unguiculatus         | GCF_002204375.1_MunDraft-v1.0                     |
|                              |                                      | Mesocricetus auratus          | GCF_017639785.1_BCM_Maur_2.0                      |
|                              |                                      | Microcebus murinus            | GCF_000165445.2_Mmur_3.0                          |
|                              |                                      | Microtus ochrogaster          | GCF_000317375.1_MicOch1.0                         |
|                              |                                      | Microtus oregoni              | GCF_018167655.1_Mior012                           |
|                              |                                      | Mirounga leonina              | GCF_011800145.1_KU_Mleo_1.0                       |
|                              |                                      | Monodelphis domestica         | GCF_000002295.2_MonDom5                           |
|                              |                                      | Mus caroli                    | GCF_900094665.1_CAROLI_EIJ_v1.1                   |
|                              |                                      | Mus musculus                  | GCF_000001635.27_GRCm39                           |
|                              |                                      | Mus pahari                    | GCF_900095145.1_PAHARI_EIJ_v1.1                   |
|                              |                                      | Myotis brandtii               | GCF_000412655.1_ASM41265v1                        |
|                              |                                      | Myotis lucifugus              | GCF_000147115.1_Myoluc2.0                         |
|                              |                                      | Myotis myotis                 | GCF_014108235.1_mMyoMyo1.p                        |
|                              |                                      | Nannospalax galili            | GCF_000622305.1_S.galili_v1.0                     |
|                              |                                      | Nomascus leucogenys           | GCF_006542625.1_Asia_NLE_v1                       |
|                              |                                      | Ochotona curzoniae            | GCF_017591425.1_NIBS_Ocur_1.0                     |
|                              |                                      | Ochotona princeps             | GCF_014633375.1_OchPri4.0                         |
|                              |                                      | Octodon degus                 | GCF_000260255.1_OctDeg1.0                         |
|                              |                                      | Orcinus orca                  | GCF_000331955.2_Oorc_1.1                          |
|                              |                                      | Ornithorhynchus anatinus      | GCF_004115215.2_mOrnAna1.pri.v4                   |
|                              |                                      | Oryctolagus cuniculus         | GCF_000003625.3_OryCun2.0                         |
|                              |                                      | Otolemur garnettii            | GCF_000181295.1_OtoGar3                           |
|                              |                                      | Ovis aries                    | GCF_016772045.1_ARS-UI_Ramb_v2.0                  |
|                              |                                      | Pan paniscus                  | GCF_013052645.1_Mhudiblu_PPA_v0                   |
|                              |                                      | Panthera pardus               | GCF_001857705.1_PanPar1.0                         |
|                              |                                      | Pan troglodytes               | GCF_002880755.1_Clint_PTRv2                       |
|                              |                                      | Papio anubis                  | GCF_008728515.1_Panubis1.0                        |
|                              |                                      | Peromyscus maniculatus        | GCF_003704035.1_HU_Pman_2.1.3                     |
|                              |                                      | Phascolarctos cinereus        | GCF_002099425.1_phaCin_unsw_v4.1                  |
|                              |                                      | Phoca vitulina                | GCF_004348235.1_GSC_HSeal_1.0                     |
|                              |                                      | Phocoena sinus                | GCF_008692025.1_mPhoSin1.pri                      |
|                              |                                      | Phyllostomus discolor         | GCF_004126475.2_mPhyDis1.pri.v3                   |
|                              |                                      | Phyllostomus hastatus         | GCF_019186645.2_TTU_PhHast_1.1                    |
|                              |                                      | Piliocolobus tephrosceles     | GCF_002776525.3_ASM277652v3                       |
|                              |                                      | Pipistrellus kuhlii           | GCF_014108245.1_mPipKuh1.p                        |
|                              |                                      | Pongo abelii                  | GCF_002880775.1_Susie_PABv2                       |
|                              |                                      | Propithecus coquereli         | GCF_000956105.1_Pcoq_1.0                          |
|                              |                                      | Pteropus alecto               | GCF_000325575.1_ASM32557v1                        |
|                              |                                      | Pteropus vampyrus             | GCF_000151845.1_Pvam_2.0                          |
|                              |                                      | Puma concolor                 | GCF_003327715.1_PumCon1.0                         |
|                              |                                      | Puma yagouaroundi             | GCF_014898765.1_PumYag                            |
|                              |                                      | Rattus norvegicus             | GCF_015227675.2_mRatBN7.2                         |
|                              |                                      | Rattus rattus                 | GCF_011064425.1_Rrattus_CSIRO_v1                  |
|                              |                                      | Rhinopithecus bieti           | GCF_001698545.1_ASM169854v1                       |
|                              |                                      | Rhinopithecus roxellana       | GCF_007565055.1_ASM756505v1                       |
|                              |                                      | Saimiri boliviensis           | GCF_016699345.1_BCM_Sbol_2.0                      |
|                              |                                      | Sarcophilus harrisii          | GCF_902635505.1_mSarHar1.11                       |
|                              |                                      | Sorex araneus                 | GCF_000181275.1_SorAra2.0                         |
|                              |                                      | Sturnira hondurensis          | GCF_014824575.2_WHU_Shon_v2.1                     |
|                              |                                      | Sus scrofa                    | GCF_000003025.6_Sscrofa11.1                       |
|                              |                                      | Theropithecus gelada          | GCF_003255815.1_Tgel_1.0                          |
|                              |                                      | Tupaia chinensis              | GCF_000334495.1_TupChi_1.0                        |
|                              |                                      | Tursiops truncatus            | GCF_011762595.1_mTurTru1.mat.Y                    |
|                              |                                      | Urocitellus parryii           | GCF_003426925.1_ASM342692v1                       |
|                              |                                      | Ursus americanus              | GCF_020975775.1_gsc_jax_bbear_1.0                 |
|                              |                                      | Ursus arctos                  | GCF_003584765.2_ASM358476v2                       |
|                              |                                      | Ursus maritimus               | GCF_017311325.1_ASM1731132v1                      |
|                              |                                      | Vicugna pacos                 | GCF_000164845.3_VicPac3.1                         |
|                              |                                      | Vombatus ursinus              | GCF_900497805.2_bare-nosed_wombat_genome_assembly |
|                              |                                      | Vulpes vulpes                 | GCF_003160815.1_VulVul2.2                         |
|                              |                                      | Acanthochromis polyacanthus   | GCF_002109545.1_ASM210954v1                       |
|                              |                                      | Acanthopagrus latus           | GCF_904848185.1_fAcaLat1.1                        |
|                              |                                      | Alosa sapidissima             | GCF_018492685.1_fAloSap1.pri                      |
|                              |                                      | Amphiprion ocellaris          | GCF_002776465.1_AmpOce1.0                         |
|                              |                                      | Anabas testudineus            | GCF_900324465.2_fAnaTes1.2                        |
|                              |                                      | Anarrhichthys ocellatus       | GCF_004355925.1_GSC_Weel_1.0                      |
|                              |                                      | Anas platyrhynchos            | GCF_015476345.1_ZJU1.0                            |
|                              |                                      | Anolis carolinensis           | GCF_000090745.1_AnoCar2.0                         |
|                              |                                      | Anser cygnoides               | GCF_000971095.1_AnsCyg_PRJNA183603_v1.0           |
|                              |                                      | Apteryx rowi                  | GCF_003343035.1_aptRow1                           |
|                              |                                      | Aquila chrysaetos             | GCF_900496995.4_bAquChr1.4                        |
|                              |                                      | Archocentrus centrarchus      | GCF_007364275.1_fArcCen1                          |
|                              |                                      | Astatotilapia calliptera      | GCF_900246225.1_fAstCal1.2                        |
|                              |                                      | Astyanax mexicanus            | GCF_000372685.2_Astyanax_mexicanus-2.0            |
|                              |                                      | Athene cunicularia            | GCF_003259725.1_athCun1                           |
|                              |                                      | Austrofundulus limnaeus       | GCF_001266775.1_Austrofundulus_limnaeus-1.0       |
|                              |                                      | Betta splendens               | GCF_900634795.3_fBetSpl5.3                        |
|                              |                                      | Boleophthalmus pectinirostris | GCF_000788275.1_BP.fa                             |
|                              |                                      | Callorhinchus milii           | GCF_018977255.1_IMCB_Cmil_1.0                     |
|                              |                                      | Calypte anna                  | GCF_003957555.1_bCalAnn1_v1.p                     |
|                              |                                      | Camarhynchus parvulus         | GCF_901933205.1_STF_HiC                           |
|                              |                                      | Carassius auratus             | GCF_003368295.1_ASM336829v1                       |
|                              |                                      | Cariama cristata              | GCF_000690535.1_ASM69053v1                        |
|                              |                                      | Catharus ustulatus            | GCF_009819885.2_bCatUst1.pri.v2                   |
|                              |                                      | Centrocercus urophasianus     | GCF_019232065.1_USGS_Curo_1.0                     |
|                              |                                      | Chaetura pelagica             | GCF_000747805.1_ChaPel_1.0                        |
|                              |                                      | Charadrius vociferus          | GCF_000708025.1_ASM70802v2                        |
|                              |                                      | Cheilinus undulatus           | GCF_018320785.1_ASM1832078v1                      |
|                              |                                      | Chiloscyllium plagiosum       | GCF_004010195.1_ASM401019v2                       |
|                              |                                      | Chlamydotis macqueenii        | GCF_000695195.1_ASM69519v1                        |
|                              |                                      | Chrysemys picta               | GCF_000241765.4_Chrysemys_picta_BioNano-3.0.4     |
|                              |                                      | Clupea harengus               | GCF_900700415.2_Ch_v2.0.2                         |
|                              |                                      | Columba livia                 | GCF_000337935.1_Cliv_1.0                          |
|                              |                                      | Corvus moneduloides           | GCF_009650955.1_bCorMon1.pri                      |
|                              |                                      | Cottoperca gobio              | GCF_900634415.1_fCotGob3.1                        |
|                              |                                      | Coturnix japonica             | GCF_001577835.2_Coturnix_japonica_2.1             |
|                              |                                      | Crocodylus porosus            | GCF_001723895.1_CroPor_comp1                      |
|                              |                                      | Cyanistes caeruleus           | GCF_002901205.1_cyaCae2                           |
|                              |                                      | Cyclopterus lumpus            | GCF_009769545.1_fCycLum1.pri                      |
|                              |                                      | Cygnus atratus                | GCF_013377495.1_Cygnus_atratus_primary_v1.0       |
|                              |                                      | Cygnus olor                   | GCF_009769625.2_bCygOlo1.pri.v2                   |
|                              |                                      | Cynoglossus semilaevis        | GCF_000523025.1_Cse_v1.0                          |
|                              |                                      | Cyprinodon tularosa           | GCF_016077235.1_ASM1607723v1                      |
|                              |                                      | Cyprinodon variegatus         | GCF_000732505.1_C_variegatus-1.0                  |
|                              |                                      | Cyprinus carpio               | GCF_018340385.1_ASM1834038v1                      |
|                              |                                      | Danio rerio                   | GCF_000002035.6_GRCz11                            |
|                              |                                      | Denticeps clupeoides          | GCF_900700375.1_fDenClu1.1                        |
|                              |                                      | Dromaius novaehollandiae      | GCF_003342905.1_droNov1                           |
|                              |                                      | Echeneis naucrates            | GCF_900963305.1_fEcheNa1.1                        |
|                              |                                      | Electrophorus electricus      | GCF_013358815.1_fEleEle1.pri                      |
|                              |                                      | Erpetoichthys calabaricus     | GCF_900747795.1_fErpCal1.1                        |
|                              |                                      | Esox lucius                   | GCF_011004845.1_fEsoLuc1.pri                      |
|                              |                                      | Etheostoma spectabile         | GCF_008692095.1_UIUC_Espe_1.0                     |
|                              |                                      | Eurypyga helias               | GCF_000690775.1_ASM69077v1                        |
|                              |                                      | Falco peregrinus              | GCF_000337955.1_F_peregrinus_v1.0                 |
|                              |                                      | Ficedula albicollis           | GCF_000247815.1_FicAlb1.5                         |
|                              |                                      | Fulmarus glacialis            | GCF_000690835.1_ASM69083v1                        |
|                              |                                      | Fundulus heteroclitus         | GCF_011125445.2_MU-UCD_Fhet_4.1                   |
|                              |                                      | Gadus morhua                  | GCF_902167405.1_gadMor3.0                         |
|                              |                                      | Gallus gallus                 | GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b       |
|                              |                                      | Gambusia affinis              | GCF_019740435.1_SWU_Gaff_1.0                      |
|                              |                                      | Gasterosteus aculeatus        | GCF_016920845.1_GAculeatus_UGA_version5           |
|                              |                                      | Gavialis gangeticus           | GCF_001723915.1_GavGan_comp1                      |
|                              |                                      | Geospiza fortis               | GCF_000277835.1_GeoFor_1.0                        |
|                              |                                      | Geotrypetes seraphini         | GCF_902459505.1_aGeoSer1.1                        |
|                              |                                      | Gopherus evgoodei             | GCF_007399415.2_rGopEvg1_v1.p                     |
|                              |                                      | Haliaeetus albicilla          | GCF_000691405.1_ASM69140v1                        |
|                              |                                      | Haplochromis burtoni          | GCF_018398535.1_NCSU_Asbu1                        |
|                              |                                      | Hippocampus comes             | GCF_001891065.1_H_comes_QL1_v1                    |
|                              |                                      | Hippoglossus stenolepis       | GCF_013339905.1_IPHC_HiSten_1.0                   |
|                              |                                      | Hirundo rustica               | GCF_015227805.1_bHirRus1.pri.v2                   |
|                              |                                      | Ictalurus punctatus           | GCF_001660625.1_IpCoco_1.2                        |
|                              |                                      | Kryptolebias marmoratus       | GCF_001649575.2_ASM164957v2                       |
|                              |                                      | Labrus bergylta               | GCF_900080235.1_BallGen_V1                        |
|                              |                                      | Larimichthys crocea           | GCF_000972845.2_L_crocea_2.0                      |
|                              |                                      | Lates calcarifer              | GCF_001640805.1_ASM164080v1                       |
|                              |                                      | Latimeria chalumnae           | GCF_000225785.1_LatCha1                           |
|                              |                                      | Lepidothrix coronata          | GCF_001604755.1_Lepidothrix_coronata-1.0          |
|                              |                                      | Lepisosteus oculatus          | GCF_000242695.1_LepOcu1                           |
|                              |                                      | Lonchura striata              | GCF_005870125.1_lonStrDom2                        |
|                              |                                      | Manacus vitellinus            | GCF_001715985.3_ASM171598v3                       |
|                              |                                      | Mastacembelus armatus         | GCF_900324485.2_fMasArm1.2                        |
|                              |                                      | Mauremys mutica               | GCF_020497125.1_ASM2049712v1                      |
|                              |                                      | Mauremys reevesii             | GCF_016161935.1_ASM1616193v1                      |
|                              |                                      | Maylandia zebra               | GCF_000238955.4_M_zebra_UMD2a                     |
|                              |                                      | Megalops cyprinoides          | GCF_013368585.1_fMegCyp1.pri                      |
|                              |                                      | Melanotaenia boesemani        | GCF_017639745.1_fMelBoe1.pri                      |
|                              |                                      | Meleagris gallopavo           | GCF_000146605.3_Turkey_5.1                        |
|                              |                                      | Melopsittacus undulatus       | GCF_012275295.1_bMelUnd1.mat.Z                    |
|                              |                                      | Mesitornis unicolor           | GCF_000695765.1_ASM69576v1                        |
|                              |                                      | Microcaecilia unicolor        | GCF_901765095.1_aMicUni1.1                        |
|                              |                                      | Micropterus dolomieu          | GCF_021292245.1_ASM2129224v1                      |
|                              |                                      | Micropterus salmoides         | GCF_014851395.1_ASM1485139v1                      |
|                              |                                      | Molothrus ater                | GCF_012460135.1_BPBGC_Mater_1.0                   |
|                              |                                      | Monopterus albus              | GCF_001952655.1_M_albus_1.0                       |
|                              |                                      | Morone saxatilis              | GCF_004916995.1_NCSU_SB_2.0                       |
|                              |                                      | Motacilla alba                | GCF_015832195.1_Motacilla_alba_V1.0_pri           |
|                              |                                      | Nematolebias whitei           | GCF_014905685.2_NemWhi1                           |
|                              |                                      | Neolamprologus brichardi      | GCF_000239395.1_NeoBri1.0                         |
|                              |                                      | Nestor notabilis              | GCF_000696875.1_ASM69687v1                        |
|                              |                                      | Nipponia nippon               | GCF_000708225.1_ASM70822v1                        |
|                              |                                      | Notechis scutatus             | GCF_900518725.1_TS10Xv2-PRI                       |
|                              |                                      | Nothobranchius furzeri        | GCF_001465895.1_Nfu_20140520                      |
|                              |                                      | Numida meleagris              | GCF_002078875.1_NumMel1.0                         |
|                              |                                      | Oncorhynchus keta             | GCF_012931545.1_Oket_V1                           |
|                              |                                      | Oncorhynchus nerka            | GCF_006149115.1_Oner_1.0                          |
|                              |                                      | Oreochromis niloticus         | GCF_001858045.2_O_niloticus_UMD_NMBU              |
|                              |                                      | Oryzias latipes               | GCF_002234675.1_ASM223467v1                       |
|                              |                                      | Oryzias melastigma            | GCF_002922805.2_ASM292280v2                       |
|                              |                                      | Pangasianodon hypophthalmus   | GCF_009078355.1_GENO_Phyp_1.0                     |
|                              |                                      | Pantherophis guttatus         | GCF_001185365.1_UNIGE_PanGut_3.0                  |
|                              |                                      | Parambassis ranga             | GCF_900634625.1_fParRan2.1                        |
|                              |                                      | Paramormyrops kingsleyae      | GCF_002872115.1_PKINGS_0.1                        |
|                              |                                      | Parus major                   | GCF_001522545.3_Parus_major1.1                    |
|                              |                                      | Passer montanus               | GCF_014805655.1_ASM1480565v1                      |
|                              |                                      | Pelecanus crispus             | GCF_000687375.1_ASM68737v1                        |
|                              |                                      | Pelodiscus sinensis           | GCF_000230535.1_PelSin_1.0                        |
|                              |                                      | Perca flavescens              | GCF_004354835.1_PFLA_1.0                          |
|                              |                                      | Perca fluviatilis             | GCF_010015445.1_GENO_Pfluv_1.0                    |
|                              |                                      | Periophthalmus magnuspinnatus | GCF_009829125.1_fPerMag1.pri                      |
|                              |                                      | Petromyzon marinus            | GCF_010993605.1_kPetMar1.pri                      |
|                              |                                      | Phaethon lepturus             | GCF_000687285.1_ASM68728v1                        |
|                              |                                      | Phalacrocorax carbo           | GCF_000708925.1_ASM70892v1                        |
|                              |                                      | Poecilia formosa              | GCF_000485575.1_Poecilia_formosa-5.1.2            |
|                              |                                      | Poecilia latipinna            | GCF_001443285.1_P_latipinna-1.0                   |
|                              |                                      | Poecilia mexicana             | GCF_001443325.1_P_mexicana-1.0                    |
|                              |                                      | Poecilia reticulata           | GCF_000633615.1_Guppy_female_1.0_MT               |
|                              |                                      | Pogona vitticeps              | GCF_900067755.1_pvi1.1                            |
|                              |                                      | Polypterus senegalus          | GCF_016835505.1_ASM1683550v1                      |
|                              |                                      | Protopterus annectens         | GCF_019279795.1_PAN1.0                            |
|                              |                                      | Pseudochaenichthys georgianus | GCF_902827115.1_fPseGeo1.1                        |
|                              |                                      | Pseudopodoces humilis         | GCF_000331425.1_PseHum1.0                         |
|                              |                                      | Pterocles gutturalis          | GCF_000699245.1_ASM69924v1                        |
|                              |                                      | Pundamilia nyererei           | GCF_000239375.1_PunNye1.0                         |
|                              |                                      | Puntigrus tetrazona           | GCF_018831695.1_ASM1883169v1                      |
|                              |                                      | Pygoscelis adeliae            | GCF_000699105.1_ASM69910v1                        |
|                              |                                      | Pyrgilauda ruficollis         | GCF_017590135.1_ASM1759013v1                      |
|                              |                                      | Rana temporaria               | GCF_905171775.1_aRanTem1.1                        |
|                              |                                      | Salarias fasciatus            | GCF_902148845.1_fSalaFa1.1                        |
|                              |                                      | Salmo salar                   | GCF_905237065.1_Ssal_v3.1                         |
|                              |                                      | Salmo trutta                  | GCF_901001165.1_fSalTru1.1                        |
|                              |                                      | Salvelinus namaycush          | GCF_016432855.1_SaNama_1.0                        |
|                              |                                      | Salvelinus sp IW2-2015        | GCF_002910315.2_ASM291031v2                       |
|                              |                                      | Sceloporus undulatus          | GCF_019175285.1_SceUnd_v1.1                       |
|                              |                                      | Scophthalmus maximus          | GCF_013347765.1_ASM1334776v1                      |
|                              |                                      | Scyliorhinus canicula         | GCF_902713615.1_sScyCan1.1                        |
|                              |                                      | Sebastes umbrosus             | GCF_015220745.1_fSebUmb1.pri                      |
|                              |                                      | Seriola dumerili              | GCF_002260705.1_Sdu_1.0                           |
|                              |                                      | Seriola lalandi               | GCF_002814215.1_Sedor1                            |
|                              |                                      | Simochromis diagramma         | GCF_900408965.1_fSimDia1.1                        |
|                              |                                      | Siniperca chuatsi             | GCF_020085105.1_ASM2008510v1                      |
|                              |                                      | Sinocyclocheilus grahami      | GCF_001515645.1_SAMN03320097.WGS_v1.1             |
|                              |                                      | Sinocyclocheilus rhinocerous  | GCF_001515625.1_SAMN03320098_v1.1                 |
|                              |                                      | Solea senegalensis            | GCF_019176455.1_IFAPA_SoseM_1                     |
|                              |                                      | Stegastes partitus            | GCF_000690725.1_Stegastes_partitus-1.0.2          |
|                              |                                      | Sturnus vulgaris              | GCF_001447265.1_Sturnus_vulgaris-1.0              |
|                              |                                      | Taeniopygia guttata           | GCF_003957565.2_bTaeGut1.4.pri                    |
|                              |                                      | Tauraco erythrolophus         | GCF_000709365.1_ASM70936v1                        |
|                              |                                      | Terrapene carolina            | GCF_002925995.2_T_m_triunguis-2.0                 |
|                              |                                      | Thalassophryne amazonica      | GCF_902500255.1_fThaAma1.1                        |
|                              |                                      | Thunnus albacares             | GCF_914725855.1_fThuAlb1.1                        |
|                              |                                      | Thunnus maccoyii              | GCF_910596095.1_fThuMac1.1                        |
|                              |                                      | Tinamus guttatus              | GCF_000705375.1_ASM70537v2                        |
|                              |                                      | Toxotes jaculatrix            | GCF_017976425.1_fToxJac2.pri                      |
|                              |                                      | Trematomus bernacchii         | GCF_902827165.1_fTreBer1.1                        |
|                              |                                      | Varanus komodoensis           | GCF_004798865.1_ASM479886v1                       |
|                              |                                      | Xenopus laevis                | GCF_017654675.1_Xenopus_laevis_v10.1              |
|                              |                                      | Xenopus tropicalis            | GCF_000004195.4_UCB_Xtro_10.0                     |
|                              |                                      | Xiphophorus couchianus        | GCF_001444195.1_X_couchianus-1.0                  |
|                              |                                      | Xiphophorus maculatus         | GCF_002775205.1_X_maculatus-5.0-male              |
|                              |                                      | Zonotrichia albicollis        | GCF_000385455.1_Zonotrichia_albicollis-1.0.1      |

### invertebrate
Default inference settings when used via `--lineage`:

| --subsequence-length        | --overlap-offset           | --overlap-core-length      |
|:----------------------------|:---------------------------|:---------------------------|
| 213840                      | 106920                     | 160380                     |

Training/validation species for the selected best model (`invertebrate_v0.3_m_0100.h5`):

| Training species          | NCBI accession                              | Validation species             | NCBI accession                                     |
|:--------------------------|:--------------------------------------------|:-------------------------------|:---------------------------------------------------|
| Acromyrmex echinatior     | GCF_000204515.1_Aech_3.9                    | Acanthaster planci             | GCF_001949145.1_OKI-Apl_1.0                        |
| Actinia tenebrosa         | GCF_009602425.1_ASM960242v1                 | Acropora millepora             | GCF_013753865.1_Amil_v2.1                          |
| Acyrthosiphon pisum       | GCF_005508785.1_pea_aphid_22Mar2018_4r6ur   | Aedes aegypti                  | GCF_002204515.2_AaegL5.0                           |
| Anopheles albimanus       | GCF_013758885.1_VT_AalbS3_pri_1.0           | Aethina tumida                 | GCF_001937115.1_Atum_1.0                           |
| Anopheles coluzzii        | GCF_016920705.1_AcolMOP1                    | Agrilus planipennis            | GCF_000699045.2_Apla_2.0                           |
| Anopheles stephensi       | GCF_013141755.1_UCI_ANSTEP_V1.0             | Amphibalanus amphitrite        | GCF_019059575.1_NRLGWU_Aamphi_draft                |
| Aphis gossypii            | GCF_004010815.1_ASM401081v1                 | Amphimedon queenslandica       | GCF_000090795.1_v1.0                               |
| Apis mellifera            | GCF_003254395.2_Amel_HAv3.1                 | Amyelois transitella           | GCF_001186105.1_ASM118610v1                        |
| Bemisia tabaci            | GCF_001854935.1_ASM185493v1                 | Anopheles arabiensis           | GCF_016920715.1_AaraD3                             |
| Bicyclus anynana          | GCF_900239965.1_Bicyclus_anynana_v1.2       | Anopheles merus                | GCF_017562075.2_AmerM5.1                           |
| Bombyx mori               | GCF_014905235.1_Bmori_2016v1.0              | Anoplophora glabripennis       | GCF_000390285.2_Agla_2.0                           |
| Bradysia coprophila       | GCF_014529535.1_BU_Bcop_v1                  | Aphidius gifuensis             | GCF_014905175.1_ASM1490517v1                       |
| Brugia malayi             | GCF_000002995.4_B_malayi-4.0                | Apis cerana                    | GCF_001442555.1_ACSNU-2.0                          |
| Caenorhabditis elegans    | GCF_000002985.6_WBcel235                    | Apis florea                    | GCF_000184785.3_Aflo_1.1                           |
| Ceratitis capitata        | GCF_000347755.3_Ccap_2.1                    | Apis laboriosa                 | GCF_014066325.1_ASM1406632v1                       |
| Chelonus insularis        | GCF_013357705.1_ASM1335770v1                | Aplysia californica            | GCF_000002075.1_AplCal3.0                          |
| Ciona intestinalis        | GCF_000224145.3_KH                          | Asterias rubens                | GCF_902459465.1_eAstRub1.3                         |
| Cryptotermes secundus     | GCF_002891405.2_Csec_1.0                    | Atta colombica                 | GCF_001594045.1_Acol1.0                            |
| Daphnia pulicaria         | GCF_021234035.1_SC_F0-13Bv2                 | Bactrocera tryoni              | GCF_016617805.1_CSIRO_BtryS06_freeze2              |
| Dendroctonus ponderosae   | GCF_000355655.1_DendPond_male_1.0           | Belonocnema kinseyi            | GCF_010883055.1_B_treatae_v1                       |
| Dermacentor silvarum      | GCF_013339745.1_ASM1333974v1                | Belonocnema treatae            | GCF_010883055.1_B_treatae_v1                       |
| Diachasma alloeum         | GCF_001412515.2_Dall2.0                     | Biomphalaria glabrata          | GCF_000457365.1_ASM45736v1                         |
| Diuraphis noxia           | GCF_001186385.1_Dnoxia_1.0                  | Bombus bifarius                | GCF_011952205.1_Bbif_JDL3187                       |
| Drosophila biarmipes      | GCF_018148935.1_ASM1814893v1                | Bombus pyrosoma                | GCF_014825855.1_ASM1482585v1                       |
| Drosophila busckii        | GCF_011750605.1_ASM1175060v1                | Bombus terrestris              | GCF_000214255.1_Bter_1.0                           |
| Drosophila elegans        | GCF_018152505.1_ASM1815250v1                | Bombus vancouverensis          | GCF_011952275.1_Bvanc_JDL1245                      |
| Drosophila kikkawai       | GCF_018152535.1_ASM1815253v1                | Bombyx mandarina               | GCF_003987935.1_ASM398793v1                        |
| Drosophila melanogaster   | GCF_000001215.4_Release_6_plus_ISO1_MT      | Caenorhabditis briggsae        | GCF_000004555.2_CB4                                |
| Drosophila navojoa        | GCF_001654015.2_UFRJ_Dnav_4.2               | Camponotus floridanus          | GCF_003227725.1_Cflo_v7.5                          |
| Drosophila rhopaloa       | GCF_018152115.1_ASM1815211v1                | Capsaspora owczarzaki          | GCF_000151315.2_C_owczarzaki_V2                    |
| Drosophila santomea       | GCF_016746245.2_Prin_Dsan_1.1               | Centruroides sculpturatus      | GCF_000671375.1_Cexi_2.0                           |
| Drosophila serrata        | GCF_002093755.1_Dser1.0                     | Cimex lectularius              | GCF_000648675.2_Clec_2.1                           |
| Drosophila simulans       | GCF_016746395.2_Prin_Dsim_3.1               | Coccinella septempunctata      | GCF_907165205.1_icCocSept1.1                       |
| Drosophila teissieri      | GCF_016746235.2_Prin_Dtei_1.1               | Colletes gigas                 | GCF_013123115.1_ASM1312311v1                       |
| Exaiptasia diaphana       | GCF_001417965.1_Aiptasia_genome_1.1         | Contarinia nasturtii           | GCF_009176525.2_AAFC_CNas_1.1                      |
| Fonticula alba            | GCF_000388065.1_Font_alba_ATCC_38817_V2     | Cotesia glomerata              | GCF_020080835.1_MPM_Cglom_v2.3                     |
| Gigantopelta aegis        | GCF_016097555.1_Gae_host_genome             | Crassostrea gigas              | GCF_902806645.1_cgigas_uk_roslin_v1                |
| Haliotis rubra            | GCF_003918875.1_ASM391887v1                 | Daphnia magna                  | GCF_020631705.1_ASM2063170v1.1                     |
| Hermetia illucens         | GCF_905115235.1_iHerIll2.2.curated.20191125 | Dendronephthya gigantea        | GCF_004324835.1_DenGig_1.0                         |
| Ixodes scapularis         | GCF_016920785.2_ASM1692078v2                | Dermatophagoides pteronyssinus | GCF_001901225.1_ASM190122v2                        |
| Leptopilina heterotoma    | GCF_015476425.1_ASM1547642v1                | Diabrotica virgifera           | GCF_003013835.1_Dvir_v2.0                          |
| Lottia gigantea           | GCF_000327385.1_Helro1                      | Diaphorina citri               | GCF_000475195.1_Diaci_psyllid_genome_assembly_v... |
| Lucilia sericata          | GCF_015586225.1_ASM1558622v1                | Drosophila ananassae           | GCF_017639315.1_ASM1763931v2                       |
| Megalopta genalis         | GCF_011865705.1_USU_MGEN_1.2                | Drosophila bipectinata         | GCF_018153845.1_ASM1815384v1                       |
| Melanaphis sacchari       | GCF_002803265.2_SCAv2.0                     | Drosophila erecta              | GCF_003286155.1_DereRS2                            |
| Neodiprion pinetum        | GCF_021155775.1_iyNeoPine1.1                | Drosophila eugracilis          | GCF_018153835.1_ASM1815383v1                       |
| Nylanderia fulva          | GCF_005281655.1_TAMU_Nfulva_1.0             | Drosophila grimshawi           | GCF_018153295.1_ASM1815329v1                       |
| Octopus bimaculoides      | GCF_001194135.1_Octopus_bimaculoides_v2_0   | Drosophila hydei               | GCF_003285905.1_DhydRS2                            |
| Odontomachus brunneus     | GCF_010583005.1_Obru_v1                     | Drosophila innubila            | GCF_004354385.1_UK_Dinn_1.0                        |
| Ooceraea biroi            | GCF_003672135.1_Obir_v5.4                   | Drosophila mauritiana          | GCF_004382145.1_ASM438214v1                        |
| Papilio machaon           | GCF_912999745.1_ilPapMach1.1                | Drosophila miranda             | GCF_003369915.1_D.miranda_PacBio2.1                |
| Parasteatoda tepidariorum | GCF_000365465.3_Ptep_3.0                    | Drosophila mojavensis          | GCF_018153725.1_ASM1815372v1                       |
| Penaeus japonicus         | GCF_017312705.1_Mj_TUMSAT_v1.0              | Drosophila novamexicana        | GCF_003285875.2_DnovRS2.1                          |
| Pieris rapae              | GCF_905147795.1_ilPieRapa1.1                | Drosophila persimilis          | GCF_003286085.1_DperRS2                            |
| Plutella xylostella       | GCF_905116875.1_Haplomerged_assembly        | Drosophila pseudoobscura       | GCF_009870125.1_UCI_Dpse_MV25                      |
| Pogonomyrmex barbatus     | GCF_000187915.1_Pbar_UMD_V03                | Drosophila subobscura          | GCF_008121235.1_UCBerk_Dsub_1.0                    |
| Pomacea canaliculata      | GCF_003073045.1_ASM307304v1                 | Drosophila suzukii             | GCF_013340165.1_LBDM_Dsuz_2.1.pri                  |
| Pseudomyrmex gracilis     | GCF_002006095.1_ASM200609v1                 | Folsomia candida               | GCF_002217175.1_ASM221717v1                        |
| Salpingoeca rosetta       | GCF_000188695.1_Proterospongia_sp_ATCC50818 | Fopius arisanus                | GCF_000806365.1_ASM80636v1                         |
| Thrips palmi              | GCF_012932325.1_TpBJ-2018v1                 | Galendromus occidentalis       | GCF_000255335.1_Mocc_1.0                           |
| Trichoplax adhaerens      | GCF_000150275.1_v1.0                        | Galleria mellonella            | GCF_003640425.2_ASM364042v2                        |
| Varroa destructor         | GCF_002443255.1_Vdes_3.0                    | Glossina fuscipes              | GCF_014805625.1_Yale_Gfus_2                        |
| Vespa crabro              | GCF_910589235.1_iyVesCrab1.2                | Habropoda laboriosa            | GCF_001263275.1_ASM126327v1                        |
| Vespula pensylvanica      | GCF_014466175.1_ASM1446617v1                | Halyomorpha halys              | GCF_000696795.2_Hhal_2.0                           |
| Zootermopsis nevadensis   | GCF_000696155.1_ZooNev1.0                   | Harpegnathos saltator          | GCF_003227715.1_Hsal_v8.5                          |
|                           |                                             | Homalodisca vitripennis        | GCF_021130785.1_UT_GWSS_2.1                        |
|                           |                                             | Homarus americanus             | GCF_018991925.1_GMGI_Hamer_2.0                     |
|                           |                                             | Ischnura elegans               | GCF_921293095.1_ioIscEleg1.1                       |
|                           |                                             | Lepeophtheirus salmonis        | GCF_016086655.3_UVic_Lsal_1.2                      |
|                           |                                             | Leptinotarsa decemlineata      | GCF_000500325.1_Ldec_2.0                           |
|                           |                                             | Linepithema humile             | GCF_000217595.1_Lhum_UMD_V04                       |
|                           |                                             | Lingula anatina                | GCF_001039355.2_LinAna2.0                          |
|                           |                                             | Loa loa                        | GCF_000183805.2_Loa_loa_V3.1                       |
|                           |                                             | Manduca sexta                  | GCF_014839805.1_JHU_Msex_v1.0                      |
|                           |                                             | Maniola jurtina                | GCF_905333055.1_ilManJurt1.1                       |
|                           |                                             | Megachile rotundata            | GCF_000220905.1_MROT_1.0                           |
|                           |                                             | Melitaea cinxia                | GCF_905220565.1_ilMelCinx1.1                       |
|                           |                                             | Mercenaria mercenaria          | GCF_014805675.1_ASM1480567v1.1                     |
|                           |                                             | Microplitis demolitor          | GCF_000572035.2_Mdem2                              |
|                           |                                             | Monosiga brevicollis           | GCF_000002865.3_V1.0                               |
|                           |                                             | Musca domestica                | GCF_000371365.1_Musca_domestica-2.0.2              |
|                           |                                             | Myzus persicae                 | GCF_001856785.1_MPER_G0061.0                       |
|                           |                                             | Nasonia vitripennis            | GCF_009193385.2_Nvit_psr_1.1                       |
|                           |                                             | Necator americanus             | GCF_000507365.1_N_americanus_v1                    |
|                           |                                             | Nematostella vectensis         | GCF_000209225.1_ASM20922v1                         |
|                           |                                             | Neodiprion fabricii            | GCF_021155785.1_iyNeoFabr1.1                       |
|                           |                                             | Neodiprion lecontei            | GCF_021901455.1_iyNeoLeco1.1                       |
|                           |                                             | Neodiprion virginiana          | GCF_021901495.1_iyNeoVirg1.1                       |
|                           |                                             | Nicrophorus vespilloides       | GCF_001412225.1_Nicve_v1.0                         |
|                           |                                             | Nilaparvata lugens             | GCF_014356525.1_ASM1435652v1                       |
|                           |                                             | Nomia melanderi                | GCF_003710045.1_USU_Nmel_1.2                       |
|                           |                                             | Octopus sinensis               | GCF_006345805.1_ASM634580v1                        |
|                           |                                             | Octopus vulgaris               | GCF_006345805.1_ASM634580v1                        |
|                           |                                             | Orbicella faveolata            | GCF_002042975.1_ofav_dov_v1                        |
|                           |                                             | Orussus abietinus              | GCF_000612105.2_Oabi_2.0                           |
|                           |                                             | Osmia bicornis                 | GCF_907164935.1_iOsmBic2.1                         |
|                           |                                             | Osmia lignaria                 | GCF_012274295.1_USDA_OLig_1.0                      |
|                           |                                             | Ostrinia furnacalis            | GCF_004193835.1_ASM419383v1                        |
|                           |                                             | Papilio polytes                | GCF_000836215.1_Ppol_1.0                           |
|                           |                                             | Papilio xuthus                 | GCF_000836235.1_Pxut_1.0                           |
|                           |                                             | Pararge aegeria                | GCF_905163445.1_ilParAegt1.1                       |
|                           |                                             | Patiria miniata                | GCF_015706575.1_ASM1570657v1                       |
|                           |                                             | Pecten maximus                 | GCF_902652985.1_xPecMax1.1                         |
|                           |                                             | Penaeus monodon                | GCF_015228065.1_NSTDA_Pmon_1                       |
|                           |                                             | Photinus pyralis               | GCF_008802855.1_Ppyr1.3                            |
|                           |                                             | Pieris brassicae               | GCF_905147105.1_ilPieBrab1.1                       |
|                           |                                             | Pocillopora damicornis         | GCF_003704095.1_ASM370409v1                        |
|                           |                                             | Polistes canadensis            | GCF_001313835.1_ASM131383v1                        |
|                           |                                             | Pollicipes pollicipes          | GCF_011947565.2_Ppol_2                             |
|                           |                                             | Portunus trituberculatus       | GCF_017591435.1_ASM1759143v1                       |
|                           |                                             | Rhagoletis zephyria            | GCF_001687245.1_Rhagoletis_zephyria_1.0            |
|                           |                                             | Rhipicephalus microplus        | GCF_013339725.1_ASM1333972v1                       |
|                           |                                             | Rhipicephalus sanguineus       | GCF_013339695.1_ASM1333969v1                       |
|                           |                                             | Saccoglossus kowalevskii       | GCF_000003605.2_Skow_1.1                           |
|                           |                                             | Scaptodrosophila lebanonensis  | GCF_003285725.1_SlebRS2                            |
|                           |                                             | Schistosoma haematobium        | GCF_000699445.2_SchHae_2.0                         |
|                           |                                             | Sitophilus oryzae              | GCF_002938485.1_Soryzae_2.0                        |
|                           |                                             | Solenopsis invicta             | GCF_016802725.1_UNIL_Sinv_3.0                      |
|                           |                                             | Sphaeroforma arctica           | GCF_001186125.1_Spha_arctica_JP610_V1              |
|                           |                                             | Spodoptera frugiperda          | GCF_011064685.1_ZJU_Sfru_1.0                       |
|                           |                                             | Spodoptera litura              | GCF_002706865.1_ASM270686v1                        |
|                           |                                             | Stegodyphus dumicola           | GCF_010614865.1_ASM1061486v1                       |
|                           |                                             | Stomoxys calcitrans            | GCF_001015335.1_Stomoxys_calcitrans-1.0.1          |
|                           |                                             | Strongylocentrotus purpuratus  | GCF_000002235.5_Spur_5.0                           |
|                           |                                             | Stylophora pistillata          | GCF_002571385.1_Stylophora_pistillata_v1           |
|                           |                                             | Tetranychus urticae            | GCF_000239435.1_ASM23943v1                         |
|                           |                                             | Trachymyrmex septentrionalis   | GCF_001594115.1_Tsep1.0                            |
|                           |                                             | Tribolium madens               | GCF_015345945.1_Tmad_KSU_1.1                       |
|                           |                                             | Trichinella spiralis           | GCF_000181795.1_Trichinella_spiralis-3.7.1         |
|                           |                                             | Varroa jacobsoni               | GCF_002532875.1_vjacob_1.0                         |
|                           |                                             | Venturia canescens             | GCF_019457755.1_ASM1945775v1                       |
|                           |                                             | Vespa mandarinia               | GCF_014083535.2_V.mandarinia_Nanaimo_p1.0          |
|                           |                                             | Vollenhovia emeryi             | GCF_000949405.1_V.emery_V1.0                       |
|                           |                                             | Xenia sp Carnegie-2017         | GCF_021976095.1_XeniaSp_v1                         |
|                           |                                             | Zerene cesonia                 | GCF_012273895.1_Zerene_cesonia_1.1                 |
|                           |                                             | Zeugodacus cucurbitae          | GCF_000806345.1_ASM80634v1                         |

### mammal
(not available via auto-selection or fetch, but can be downloaded from Zenodo: https://zenodo.org/records/17850139
as the model was not extensively trained/tested)

Recommended inference settings when used via `--model-filepath`:

| --subsequence-length        | --overlap-offset           | --overlap-core-length      |
|:----------------------------|:---------------------------|:---------------------------|
| 213840                      | 106920                     | 160380                     |

Training/validation species for the selected best model (`mammal_v0.3_a_0100.h5`); the
entire validation species were used, not just a random set of samples:

| Training species           | NCBI accession                     | Validation species | NCBI accession            |
|:---------------------------|:-----------------------------------|:-------------------|:--------------------------|
| Aotus nancymaae            | GCF_000952055.2_Anan_2.0           | Panthera pardus    | GCF_001857705.1_PanPar1.0 |
| Canis lupus familiaris     | GCF_000002285.3_CanFam3.1          | Rattus norvegicus  | GCF_000001895.5_Rnor_6.0  |
| Cavia porcellus            | GCF_000151735.1_Cavpor3.0          |                    |                           |
| Cebus imitator             | GCF_001604975.1_Cebus_imitator-1.0 |                    |                           |
| Ceratotherium simum        | GCF_000283155.1_CerSimSim1.0       |                    |                           |
| Chinchilla lanigera        | GCF_000276665.1_ChiLan1.0          |                    |                           |
| Condylura cristata         | GCF_000260355.1_ConCri1.0          |                    |                           |
| Desmodus rotundus          | GCF_022682495.1_HLdesRot8A         |                    |                           |
| Dipodomys ordii            | GCF_000151885.1_Dord_2.0           |                    |                           |
| Enhydra lutris             | GCF_002288905.1_ASM228890v2        |                    |                           |
| Eptesicus fuscus           | GCF_000308155.1_EptFus1.0          |                    |                           |
| Equus caballus             | GCF_000002305.2_EquCab2.0          |                    |                           |
| Heterocephalus glaber      | GCF_000247695.1_HetGla_female_1.0  |                    |                           |
| Ictidomys tridecemlineatus | GCF_000236235.1_SpeTri2.0          |                    |                           |
| Jaculus jaculus            | GCF_000280705.1_JacJac1.0          |                    |                           |
| Loxodonta africana         | GCF_000001905.1_Loxafr3.0          |                    |                           |
| Marmota marmota            | GCF_001458135.1_marMar2.1          |                    |                           |
| Microcebus murinus         | GCF_000165445.2_Mmur_3.0           |                    |                           |
| Microtus ochrogaster       | GCF_000317375.1_MicOch1.0          |                    |                           |
| Mus musculus               | GCF_000001635.26_GRCm38.p6         |                    |                           |
| Mus pahari                 | GCF_900095145.1_PAHARI_EIJ_v1.1    |                    |                           |
| Neomonachus schauinslandi  | GCF_002201575.2_ASM220157v2        |                    |                           |
| Ochotona princeps          | GCF_000292845.1_OchPri3.0          |                    |                           |
| Octodon degus              | GCF_000260255.1_OctDeg1.0          |                    |                           |
| Odobenus rosmarus          | GCF_000321225.1_Oros_1.0           |                    |                           |
| Otolemur garnettii         | GCF_000181295.1_OtoGar3            |                    |                           |
| Puma concolor              | GCF_003327715.1_PumCon1.0          |                    |                           |
| Saimiri boliviensis        | GCF_000235385.1_SaiBol1.0          |                    |                           |
| Sorex araneus              | GCF_000181275.1_SorAra2.0          |                    |                           |
| Trichechus manatus         | GCF_000243295.1_TriManLat1.0       |                    |                           |
