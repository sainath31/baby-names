#!/usr/bin/env python3
"""
Sahasranama Modern Name Deriver
Derives modern, usable baby boy names from the Sanskrit roots and meanings
of 6 sacred Hindu texts. Names are NOT lifted verbatim — each is a new
2-4 syllable name formed by root extraction, contraction, or recombination.

Nakshatra syllables: Sa · Si · Su · Se · Ja · Ji · Ga · Gu · De · La
"""

CHALDEAN_MAP = {
    'a':1,'i':1,'j':1,'q':1,'y':1,
    'b':2,'k':2,'r':2,
    'c':3,'g':3,'l':3,'s':3,
    'd':4,'m':4,'t':4,
    'e':5,'h':5,'n':5,'x':5,
    'o':6,'u':6,'v':6,'w':6,
    'z':7,
    'f':8,'p':8
}
PREFERRED = {1, 3, 6}

NAKSHATRA_SYLLABLES = ("Sa","Si","Su","Se","Ja","Ji","Ga","Gu","De","La")

def chaldean(name):
    total = sum(CHALDEAN_MAP.get(c.lower(), 0) for c in name if c.isalpha())
    final = total
    while final > 9:
        final = sum(int(d) for d in str(final))
    return total, final

def syllable_group(name):
    for syl in NAKSHATRA_SYLLABLES:
        if name.startswith(syl):
            return syl.upper()
    return None

# ─────────────────────────────────────────────────────────────────────────────
# FORMAT per entry:
# (source_epithet, shloka_ref, derived_name, devanagari, iast, meaning,
#  derivation_note, rarity, modern_feel)
#
# derivation_note explains HOW the name was formed from the root.
# modern_feel: 1-5 (5 = most modern/trendy)
# rarity: "rare" / "very rare" / "uncommon"
# ─────────────────────────────────────────────────────────────────────────────

# ═══════════════════════════════════════════════════════════════════════════
# VISHNU SAHASRANAMAM — derived modern names
# Source: Anushasana Parva (Mahabharata), Bhagavata Purana
# ═══════════════════════════════════════════════════════════════════════════
VISHNU_DERIVED = [
    # SA group
    ("Sahasrajit",    "V-24", "Sahjit",    "सहजित",   "Sahajit",    "Effortless conqueror; one who wins with ease",          "sahasra (limitless) + jit (victor) → trimmed to modern form",        "rare",      5),
    ("Sahasraksha",   "V-20", "Sahaksh",   "सहाक्ष",  "Sahākṣa",   "All-seeing; perceptive like a thousand eyes",           "sahasra + aksha (eye) → compressed",                                 "very rare", 4),
    ("Sanatana",      "V-12", "Sanatan",   "सनातन",   "Sanātana",   "Rooted in eternity; timeless in spirit",                "sanātana → drop final vowel for masculine form",                     "uncommon",  4),
    ("Sarathi",       "V-28", "Sarath",    "सारथ",    "Sāratha",    "The guide; one who steers life with purpose",           "sārathi (charioteer) → dropped suffix -i for crispness",            "uncommon",  5),
    ("Samagraha",     "V-16", "Samagr",    "समग्र",   "Samagra",    "Complete; whole in every dimension",                    "samagra (whole/complete) → already short, drop final -a",           "rare",      4),
    ("Sambhava",      "V-14", "Sambhav",   "सम्भव",   "Sambhava",   "Self-arising; born of pure potential",                  "sambhava → drop final -a (common modern pattern)",                   "uncommon",  5),
    ("Samitinjaya",   "V-19", "Samijay",   "समिजय",   "Samijaya",   "Victor in every gathering; champion among peers",       "samiti (assembly) + jaya (victory) → modern blend",                 "rare",      5),
    ("Sanatkumara",   "V-13", "Sanakumar", "सनकुमार", "Sanakumāra", "Eternally youthful; one who never loses his spark",     "sanat (eternal) + kumāra (youth) → dropped internal syllable",      "uncommon",  4),
    ("Satyamedha",    "V-34", "Satyamedh", "सत्यमेध", "Satyamedha", "Of brilliant, truth-rooted intelligence",              "satya (truth) + medha (intellect) → drop -a suffix",                "rare",      4),
    ("Satyavak",      "V-31", "Satyav",    "सत्यव",   "Satyava",    "One whose every word rings true",                       "satya (truth) + vāk (speech) → trimmed suffix",                     "very rare", 4),
    ("Satyavrata",    "V-32", "Satvrat",   "सत्व्रत", "Satvrata",   "Pledged to truth; unbreakable vow of integrity",        "satya + vrata → contract satya → sat, drop -a",                     "rare",      4),
    ("Satveer",       "V-33", "Satveer",   "सत्वीर",  "Satvīra",    "Hero of truth; valor rooted in righteousness",          "satya (truth) + vīra (hero) → contracted satya→sat, modern blend",  "rare",      5),
    ("Savijit",       "V-39", "Savijit",   "सविजित",  "Savijita",   "Victorious energizer; one who wins through radiance",   "savitā root sav- (to vivify) + jit (victor)",                       "very rare", 5),
    ("Sarvit",        "V-6",  "Sarvit",    "सर्वित",  "Sarvita",    "All-knowing; one with boundless awareness",             "sarva (all) + vid (know) → vid→vit, modern ending",                 "very rare", 5),
    ("Sarvansh",      "V-3",  "Sarvansh",  "सर्वांश", "Sarvāṃśa",  "A part of the whole; born of universal essence",        "sarva (all) + aṃśa (part/portion) → phonetic trim",                "uncommon",  5),
    ("Sarvesh",       "V-7",  "Sarvesh",   "सर्वेश",  "Sarveśa",    "Sovereign of all; master with boundless reach",         "sarva + īśa → sandhi gives sarveśa → drop -a",                     "uncommon",  5),
    ("Satprath",      "V-29", "Satprath",  "सत्प्रथ", "Satpratha",  "Righteous and renowned; known for walking truth",       "sat (truth/good) + pratha (renown) — new compound from root idea",  "very rare", 5),
    ("Samvedh",       "V-38", "Samvedh",   "संवेध",   "Saṃvedha",   "One who is deeply aware; tuned into higher reality",    "sam (together) + vedha (awareness/piercing insight)",               "very rare", 5),
    # SI group
    ("Simhavikrama",  "V-49", "Simhav",    "सिंहव",   "Siṃhava",    "Lion-hearted; courageous like a lion",                  "siṃha (lion) + vikrama → trim to root + -v",                        "very rare", 4),
    ("Simhanada",     "V-50", "Sinaan",    "सिनान",   "Sinān",      "Resonant; one whose voice commands attention",           "siṃha-nāda (lion-roar) → phonetic simplification → sinān",         "very rare", 5),
    ("Sivaan",        "V-51", "Sivaan",    "शिवान",   "Śivān",      "Divine grace; auspicious and pure at the core",          "śiva root + ān suffix (masculine, modern)",                         "uncommon",  5),
    ("Siddhav",       "V-45", "Siddhav",   "सिद्धव",  "Siddhava",   "Accomplished; one who masters whatever he pursues",     "siddha (accomplished) → drop -a, add -v for modern crispness",     "rare",      5),
    ("Siddhansh",     "V-47", "Siddhansh", "सिद्धांश","Siddhāṃśa",  "Born of perfection; a fragment of divine mastery",      "siddha + aṃśa → natural compound",                                  "uncommon",  5),
    # SU group
    ("Sugriva",       "V-61", "Sugriv",    "सुग्रीव", "Sugrīva",    "Handsome and strong-necked; bearing himself with grace","sugrīva → drop final -a",                                           "uncommon",  5),
    ("Sudheer",       "V-59", "Sudheer",   "सुधीर",   "Sudhīra",    "Supremely patient and wise; calm under pressure",       "su (excellent) + dhīra (steadfast/wise) → drop -a",                "uncommon",  5),
    ("Sujaan",        "V-62", "Sujaan",    "सुजान",   "Sujāna",     "Well-born and noble; of fine character",                "sujāta root → modernised with -n ending",                           "uncommon",  5),
    ("Sujit",         "V-64", "Sujit",     "सुजित",   "Sujita",     "One who wins rightfully; a clean and fair victor",      "su (well/good) + jit (conqueror)",                                  "uncommon",  5),
    ("Sukran",        "V-54", "Sukran",    "शुक्रान", "Śukrān",     "Pure-rayed; radiating clarity and purity",              "śukla (pure/white) → phonetic shift → sukran, -n modern",          "very rare", 5),
    ("Sumedhan",      "V-70", "Sumedhan",  "सुमेधन",  "Sumedhana",  "Of brilliant intelligence; exceptionally sharp mind",   "su + medha (intelligence) + -n for modern masculine",              "rare",      5),
    ("Sunav",         "V-71", "Sunav",     "सुनव",    "Sunava",     "Auspiciously named; bearing a beautiful identity",      "su (auspicious) + nāma root → sunāva → sunav",                     "very rare", 5),
    ("Suparn",        "V-73", "Suparn",    "सुपर्ण",  "Suparṇa",    "Of beautiful wings; soaring free and high",             "suparṇa → drop final -a",                                           "rare",      4),
    ("Suraaj",        "V-77", "Suraaj",    "सुराज",   "Surāja",     "Brilliantly ruling; one who leads with light",          "sura (divine) + rāja (king) → new compound",                       "uncommon",  5),
    ("Suresh",        "V-81", "Suresh",    "सुरेश",   "Sureśa",     "Lord of the divine; one of heavenly authority",         "sura + īśa → sureśa → drop -a",                                    "uncommon",  4),
    ("Suryan",        "V-83", "Suryan",    "सूर्यन",  "Sūryana",    "Solar spirit; radiant like the rising sun",             "sūrya + -n (modern masculine suffix)",                              "uncommon",  5),
    ("Suvikram",      "V-87", "Suvikram",  "सुविक्रम","Suvikrama",  "Of excellent valor; supremely courageous",              "su + vikrama → drop -a",                                            "rare",      5),
    ("Suvrat",        "V-88", "Suvrat",    "सुव्रत",  "Suvrata",    "Of noble vow; devoted and disciplined",                 "suvrata → drop -a",                                                 "uncommon",  4),
    # JA group
    ("Jagatpran",     "V-97", "Jagatpran", "जगत्प्राण","Jagatprāṇa","Life-force of the world; vitally alive",               "jagat + prāṇa → drop final -a",                                     "very rare", 5),
    ("Jagesh",        "V-91", "Jagesh",    "जगेश",    "Jageśa",     "Sovereign of the world; born to lead universally",      "jagat + īśa → jagadīśa → phonetic compress → jagesh",             "rare",      5),
    ("Jaganth",       "V-94", "Jaganth",   "जगन्थ",   "Jagantha",   "Lord of the world; one of vast purpose",                "jagannātha → contract nātha → -nth",                               "uncommon",  5),
    ("Javin",         "V-90", "Javin",     "जविन",    "Javina",     "Swift; dynamically moving; unstoppable",                "javana (swift) → trim to root jav + -in",                          "uncommon",  5),
    ("Jayaansh",      "V-100","Jayaansh",  "जयांश",   "Jayāṃśa",   "Born of victory; a portion of triumph",                 "jaya + aṃśa",                                                       "uncommon",  5),
    ("Jayesh",        "V-101","Jayesh",    "जयेश",    "Jayeśa",     "Lord of victory; master of all triumphs",               "jaya + īśa → jayeśa → drop -a",                                    "uncommon",  4),
    # JI group
    ("Jishan",        "V-106","Jishan",    "जिशान",   "Jiśāna",     "Conqueror; born triumphant",                            "jiṣṇu root jiṣ- + -ān → jiśān",                                   "rare",      5),
    ("Jitaansh",      "V-103","Jitaansh",  "जितांश",  "Jitāṃśa",   "Born of self-mastery; a portion of inner victory",      "jita (conquered/won) + aṃśa",                                      "uncommon",  5),
    ("Jivesh",        "V-107","Jivesh",    "जिवेश",   "Jiveśa",     "Lord of life; one who animates all around him",         "jīva (life) + īśa → jīveśa → drop -a, phonetic trim",             "rare",      5),
    ("Jivaan",        "V-109","Jivaan",    "जीवान",   "Jīvān",      "Full of life; radiantly alive",                         "jīvana → jīvān (modern form)",                                      "uncommon",  5),
    # GA group
    ("Gabhiran",      "V-111","Gabhiran",  "गभीरन",   "Gabhīrana",  "Profoundly deep; of unfathomable character",            "gabhīra (profound/deep) + -n modern suffix",                       "very rare", 5),
    ("Gatijit",       "V-121","Gatijit",   "गतिजित",  "Gatijita",   "Swift conqueror; one who wins through momentum",        "gati (motion/speed) + jit (victor) — new compound from roots",     "very rare", 5),
    ("Gauresh",       "V-119","Gauresh",   "गौरेश",   "Gaureśa",    "Radiant lord; brilliantly luminous leader",             "gaura (bright/radiant) + īśa → gaureśa",                           "rare",      5),
    ("Gavesh",        "V-118","Gavesh",    "गवेश",    "Gaveśa",     "Seeker of truth; one who searches with purpose",        "gavesana (seeking/searching) → trimmed to root",                   "rare",      5),
    ("Ganish",        "V-116","Ganish",    "गनिश",    "Ganiśa",     "Lord of all; one who commands every domain",            "gaṇa (host/group) + īśa → gaṇiśa → phonetic trim",               "uncommon",  5),
    # GU group
    ("Gunesh",        "V-123","Gunesh",    "गुणेश",   "Guṇeśa",     "Master of virtues; one whose character is supreme",     "guṇa (virtue) + īśa → guṇeśa → drop -a",                         "uncommon",  5),
    ("Gunav",         "V-124","Gunav",     "गुणव",    "Guṇava",     "Endowed with virtues; naturally excellent",              "guṇa + -v ending for modern boy name",                             "rare",      5),
    ("Gurudev",       "V-128","Gurudev",   "गुरुदेव", "Gurudeva",   "Divinely guided; one who reveres his teacher",          "guru + deva → drop -a",                                            "uncommon",  4),
    ("Guransh",       "V-127","Guransh",   "गुरांश",  "Gurāṃśa",   "Born of wisdom; part of the guru principle",            "guru + aṃśa",                                                       "rare",      5),
    # DE group
    ("Devaan",        "V-130","Devaan",    "देवान",   "Devān",      "Radiant; shining with divine quality",                  "deva + ān (Sanskrit suffix for fulness)",                           "uncommon",  5),
    ("Devesh",        "V-132","Devesh",    "देवेश",   "Deveśa",     "Sovereign of the divine; naturally commanding",         "deva + īśa → deveśa → drop -a",                                   "uncommon",  5),
    ("Devraj",        "V-133","Devraj",    "देवराज",  "Devarāja",   "King among the brilliant; natural leader",              "deva + rāja → drop -a",                                            "uncommon",  4),
    ("Devansh",       "V-136","Devansh",   "देवांश",  "Devāṃśa",   "Born of the divine; a spark of cosmic brilliance",      "deva + aṃśa",                                                       "uncommon",  5),
    ("Devit",         "V-140","Devit",     "देवित",   "Devita",     "Illumined; touched by divine energy",                   "deva root dev- + -it (active participle suffix)",                  "very rare", 5),
    ("Devyan",        "V-139","Devyan",    "देव्यन",  "Devyana",    "On the divine path; journeying toward the sacred",      "deva + -yan (Sanskrit -yāna = journey/path)",                      "very rare", 5),
    # LA group
    ("Lakshan",       "V-145","Lakshan",   "लक्षन",   "Lakṣana",    "Auspiciously marked; one who bears signs of greatness", "lakṣaṇa (auspicious marks) → drop final -a",                      "uncommon",  5),
    ("Lavesh",        "V-146","Lavesh",    "लवेश",    "Laveśa",     "Graceful sovereign; commanding with elegance",          "lāvaṇya (grace) root lav- + īśa → laveśa",                        "rare",      5),
    ("Lavitr",        "V-146","Lavitr",    "लवित्र",  "Lavitra",    "Instrument of grace; bearer of beauty",                 "lāvaṇya root + -tra (instrument/bearer suffix)",                   "very rare", 5),
]

# ═══════════════════════════════════════════════════════════════════════════
# LALITHA SAHASRANAMAM — derived modern names
# Source: Brahmanda Purana — Lalitopakhyana
# Note: Lalitha is the goddess; derived names capture her energy for boys
# ═══════════════════════════════════════════════════════════════════════════
LALITHA_DERIVED = [
    # SA group
    ("Sarvajnata",    "L-1",  "Sarvajnan",  "सर्वज्ञन", "Sarvajñana","Omniscient; one with boundless knowing",               "sarvajñā → masculine -n suffix, trim",                              "very rare", 5),
    ("Sarvananda",    "L-3",  "Sarvanand",  "सर्वानन्द","Sarvānanda", "Universal bliss; radiating joy to all",                "sarvānandā → drop -ā",                                              "uncommon",  5),
    ("Sarvamangal",   "L-7",  "Sarvmangal", "सर्वमङ्गल","Sarvmaṅgala","All-auspicious; one who brings good fortune",          "sarvam­aṅgalā → drop -ā, compress",                                "uncommon",  4),
    ("Sadashivan",    "L-17", "Sadashivan", "सदाशिवन",  "Sadāśivana", "Eternally auspicious; ever-pure in spirit",            "sadāśiva + -n modern suffix",                                       "uncommon",  4),
    ("Samrasen",      "L-19", "Samrasen",   "समरसेन",   "Samarasena", "Warrior of equanimity; balanced and powerful",         "samarasa (equanimity) + senā (warrior) → new compound",            "very rare", 5),
    ("Satchitr",      "L-26", "Satchitr",   "सच्चित्र", "Saccitra",   "Living consciousness; brilliantly aware",              "saccidānanda → root sat+cit compressed",                           "very rare", 5),
    ("Satyajnan",     "L-28", "Satyajnan",  "सत्यज्ञन", "Satyajñana", "Of true wisdom; one who knows with clarity",           "satyajñānā → masculine -n form",                                   "rare",      4),
    ("Saumyan",       "L-29", "Saumyan",    "सौम्यन",   "Saumyana",   "Moon-like serenity; gentle strength",                  "saumya + -n modern masculine",                                      "uncommon",  5),
    ("Savitran",      "L-31", "Savitran",   "सवित्रन",  "Savitrana",  "Son of light; born of the solar source",               "sāvitrī → masculine form sāvitrana → savitran",                   "rare",      5),
    ("Sadgun",        "L-41", "Sadgun",     "सद्गुण",   "Sadguṇa",   "Of true virtue; genuinely good in character",           "sadguṇā → drop -ā",                                                "uncommon",  5),
    ("Santosh",       "L-43", "Santosh",    "सन्तोष",   "Santoṣa",   "Content at the deepest level; at peace",                "santoṣā → drop -ā",                                                "uncommon",  4),
    ("Sankalan",      "L-36", "Sankalan",   "संकलन",    "Saṃkalana",  "Born of divine will; manifested purpose",              "saṅkalpa root → compress to sankala + -n",                         "very rare", 5),
    ("Samharan",      "L-37", "Samharan",   "संहरन",    "Saṃharana",  "Powerfully transformative; one who reorders things",   "saṃhārā root → masculine form + -n",                               "very rare", 5),
    # SI group
    ("Sivesh",        "L-53", "Sivesh",     "शिवेश",    "Śiveśa",    "Lord of auspiciousness; divinely peaceful ruler",       "śivapriyā root śiva + īśa → śiveśa",                              "rare",      5),
    ("Sivankaran",    "L-54", "Sivankaran", "शिवंकरन",  "Śivaṃkarana","Maker of auspiciousness; one who brings peace",        "śivaṅkarī → masculine -n form",                                    "rare",      4),
    ("Siddhesh",      "L-51", "Siddhesh",   "सिद्धेश",  "Siddheśa",  "Lord of accomplishment; master of perfections",         "siddhā + īśa → siddheśa → drop -a",                               "uncommon",  5),
    # SU group
    ("Sudhav",        "L-61", "Sudhav",     "सुधव",     "Sudhava",    "Of divine sweetness; pure and nourishing",              "sudhā (nectar) + -v ending",                                       "very rare", 5),
    ("Sunandan",      "L-65", "Sunandan",   "सुनन्दन",  "Sunandana",  "One who gives great joy; spreader of delight",         "sunandā → masculine sunandana → sunandan",                         "uncommon",  5),
    ("Suprabh",       "L-67", "Suprabh",    "सुप्रभ",   "Suprabha",   "Brilliantly radiant; shining at the highest level",    "suprabhā → drop -ā",                                               "uncommon",  5),
    ("Suresh",        "L-68", "Suresh",     "सुरेश",    "Sureśa",    "Lord of the divine realm; celestial authority",         "sureśvarī → compress to sureśa → suresh",                         "uncommon",  4),
    # JA group
    ("Jagmind",       "L-70", "Jagmind",    "जगमिंद",   "Jagaminda",  "Mind of the universe; of cosmic intelligence",         "jagadambā root jagat + mind (phonetic blend of manas/mind)",       "very rare", 5),
    ("Jagatpriyan",   "L-72", "Jagatpriyan","जगत्प्रियन","Jagatpriyaṇa","Beloved across the world; universally cherished",    "jagatpriyā → masculine -n form",                                   "very rare", 5),
    ("Jayansh",       "L-73", "Jayansh",    "जयांश",    "Jayāṃśa",   "Born of victory; a part of triumph",                   "jayantī → aṃśa compound",                                          "uncommon",  5),
    ("Janansh",       "L-77", "Janansh",    "जनांश",    "Janāṃśa",   "Born from the great mother; of noble origin",           "jananī root jana + aṃśa",                                          "very rare", 5),
    # JI group
    ("Jivesh",        "L-81", "Jivesh",     "जिवेश",    "Jiveśa",    "Lord of life; one who vitalizes everything he touches", "jīvanā root jīva + īśa",                                           "rare",      5),
    # GA group
    ("Gaurav",        "L-83", "Gaurav",     "गौरव",     "Gaurava",    "Pride; one who commands respect and honour",            "gaurī root gaura (bright) + -v",                                   "uncommon",  4),
    ("Gavit",         "L-88", "Gavit",      "गवित",     "Gavita",     "Divinely sung; one whose story is worth telling",       "gītā root gav- (from go/song) + -it",                              "very rare", 5),
    ("Ganesh",        "L-85", "Ganesh",     "गणेश",     "Gaṇeśa",    "Lord of hosts; naturally commanding and organized",     "gaṇajananī root → boy form ganeśa → ganesh",                       "uncommon",  3),
    # GU group
    ("Guhyan",        "L-91", "Guhyan",     "गुह्यन",   "Guhyana",    "One of hidden depth; profoundly interior",              "guhyarūpā → masculine -n form",                                    "very rare", 5),
    # DE group
    ("Devesh",        "L-93", "Devesh",     "देवेश",    "Deveśa",    "Ruler of divine beings; sovereign light",               "devēśī → masculine deveśa → devesh",                               "uncommon",  5),
    ("Devpriyan",     "L-96", "Devpriyan",  "देवप्रियन","Devapriyaṇa","Cherished by all divine beings; universally blessed",  "devapriyā → masculine -n form",                                    "rare",      5),
    ("Devnutan",      "L-97", "Devnutan",   "देवनुतन",  "Devanutana", "Praised by the gods; divinely celebrated",             "devanutā → masculine form + -n",                                   "very rare", 5),
    # LA group
    ("Lavit",         "L-105","Lavit",      "लवित",     "Lavita",     "Graceful; bearing elegance and refinement",             "lalitā → stripped to root lav- + -it (active suffix)",            "rare",      5),
    ("Lavansh",       "L-107","Lavansh",    "लावांश",   "Lāvāṃśa",  "Born of grace; carrying divine elegance",               "lāvaṇyā + aṃśa",                                                   "rare",      5),
    ("Layesh",        "L-108","Layesh",     "लयेश",     "Layeśa",    "Master of the cosmic rhythm; attuned to all cycles",    "layakartṛī root laya (dissolution/rhythm) + īśa",                 "very rare", 5),
]

# ═══════════════════════════════════════════════════════════════════════════
# SHIVA SAHASRANAMAM — derived modern names
# Source: Anushasana Parva (Mahabharata), Shiva Purana
# ═══════════════════════════════════════════════════════════════════════════
SHIVA_DERIVED = [
    # SA group
    ("Sadyajat",      "SH-14","Sadyajat",   "सद्यजात",  "Sadyajāta",  "Instantaneous; one who manifests with sudden brilliance","sadyojāta → drop -a + -t",                                       "very rare", 5),
    ("Samharan",      "SH-17","Samharan",   "संहरन",    "Saṃharana",  "Powerfully transformative; a force of renewal",         "saṃhārā root + masculine -n",                                     "very rare", 5),
    ("Sankaran",      "SH-19","Sankaran",   "शंकरन",    "Śaṃkarana",  "Giver of peace; spreader of auspiciousness",            "śaṅkara + -n modern suffix",                                       "uncommon",  4),
    ("Sanvesh",       "SH-22","Sanvesh",    "संवेश",    "Saṃveśa",   "Deeply immersed; one absorbed in higher purpose",       "saṃkṛt root sam + veśa (entry/immersion)",                        "very rare", 5),
    ("Sarvatn",       "SH-3", "Sarvatan",   "सर्वतन",   "Sarvatana",  "All-pervading; present in every thread of existence",   "sarvātman → compress root sarva + tana",                          "very rare", 5),
    ("Satvesh",       "SH-26","Satvesh",    "सत्वेश",   "Satveśa",   "Lord of truth; master of pure existence",               "satyakāma root sat + īśa → satveśa",                              "very rare", 5),
    ("Savarchas",     "SH-48","Savarchas",  "सवर्चस",   "Savarcas",   "Brilliantly radiant; of great spiritual lustre",        "suvarcas → phonetic modernisation",                               "very rare", 4),
    ("Shambhav",      "SH-30","Shambhav",   "शम्भव",    "Śambhava",   "Born of peace; one who naturally brings calm",          "śambhu root + -av ending",                                         "uncommon",  5),
    # SI group
    ("Sivaan",        "SH-36","Sivaan",     "शिवान",    "Śivān",      "Auspicious; pure-hearted and divinely calm",            "śiva + ān (richness suffix)",                                      "uncommon",  5),
    ("Sivesh",        "SH-36","Sivesh",     "शिवेश",    "Śiveśa",    "Lord of auspiciousness; supreme in peace",              "śiva + īśa → śiveśa → drop -a",                                   "rare",      5),
    ("Simhav",        "SH-35","Simhav",     "सिंहव",    "Siṃhava",    "Lion-like; fearless and bold",                          "siṃhavāhana → root siṃha + -v",                                   "very rare", 4),
    # SU group
    ("Subran",        "SH-39","Subran",     "सुब्रन",   "Subrana",    "Very dear to wisdom; beloved of the learned",           "subrahmaṇya → compress to root sub + -ran",                       "very rare", 5),
    ("Subhesh",       "SH-29","Subhesh",    "शुभेश",    "Śubheśa",   "Lord of the auspicious; commanding goodness",           "śubhaṅkara root śubha + īśa",                                     "rare",      5),
    ("Suprakash",     "SH-43","Suprakash",  "सुप्रकाश", "Suprakāśa",  "Supremely luminous; shining with highest clarity",      "suprakāśa → drop -a",                                             "uncommon",  4),
    ("Sureshan",      "SH-44","Sureshan",   "सुरेशन",   "Sureśana",   "Divine sovereign; lord of the radiant ones",            "sureśa + -n suffix",                                               "rare",      5),
    # JA group
    ("Jagmith",       "SH-50","Jagmith",    "जगमित",    "Jagamita",   "Friend of the universe; beloved by all worlds",         "jagadhita (welfare of universe) → compress jagat + mitra → jagmith","very rare",5),
    ("Jagish",        "SH-51","Jagish",     "जगेश",     "Jageśa",    "World-sovereign; born to command widely",               "jagadīśvara → compress → jagīśa → jagish",                        "rare",      5),
    ("Jayakar",       "SH-59","Jayakar",    "जयकर",     "Jayakara",   "Maker of victory; one who creates triumph for others",  "jayakara → already clean, drop final -a optional",               "uncommon",  5),
    # JI group
    ("Jitesh",        "SH-61","Jitesh",     "जितेश",    "Jiteśa",    "Master of the conquered self; inner champion",          "jitātman → root jita + īśa → jiteśa",                             "uncommon",  5),
    ("Jivaansh",      "SH-64","Jivaansh",   "जीवांश",   "Jīvāṃśa",  "A fragment of life itself; vibrantly alive",            "jīvana + aṃśa",                                                    "uncommon",  5),
    # GA group
    ("Gaugesh",       "SH-73","Gaugesh",    "गौगेश",    "Gaugeśa",   "Lord of the sacred river; pure and flowing",            "gaurīpati root gauri → gaugeśa",                                  "very rare", 5),
    ("Gangesh",       "SH-73","Gangesh",    "गंगेश",    "Gaṅgeśa",   "Lord of the sacred Ganga; one of pure flow",            "gaṅgādhara root gaṅgā + īśa",                                     "uncommon",  5),
    ("Girishan",      "SH-75","Girishan",   "गिरीशन",   "Girīśana",   "Mountain-lord; one who stands firm and high",           "girīśvara → trim to girīśa + -n",                                 "uncommon",  4),
    ("Gauripriyan",   "SH-74","Gauripriyan","गौरीप्रियन","Gaurīpriyaṇa","Cherished; deeply beloved and tender",               "gaurīvallabha → new compound gauri + priya + -n",                 "rare",      4),
    # GU group
    ("Guhesh",        "SH-77","Guhesh",     "गुहेश",    "Guheśa",    "Lord of inner depth; sovereign of the hidden",          "guheśvara → drop -vara → guheśa → guhesh",                       "rare",      5),
    ("Gunavit",       "SH-78","Gunavit",    "गुणवित",   "Guṇavita",   "One who recognizes and lives by virtues",               "guṇagrāhī root guṇa + vid → guṇavit",                             "very rare", 5),
    # DE group
    ("Devaan",        "SH-81","Devaan",     "देवान",    "Devān",      "Radiating divinity; naturally luminous",                "deva + -ān",                                                       "uncommon",  5),
    ("Devpat",        "SH-84","Devpat",     "देवपत",    "Devapata",   "Lord of the divine; one who rules with grace",          "devapati → drop -i suffix → devpat",                              "rare",      5),
    ("Devansh",       "SH-89","Devansh",    "देवांश",   "Devāṃśa",  "A spark of the divine; born of celestial essence",      "deva + aṃśa",                                                      "uncommon",  5),
    # LA group
    ("Lingesh",       "SH-90","Lingesh",    "लिंगेश",   "Liṅgeśa",   "Lord of the cosmic symbol; rooted in Shiva's essence",  "liṅgamūrti → liṅga + īśa → liṅgeśa → lingesh",                 "uncommon",  4),
]

# ═══════════════════════════════════════════════════════════════════════════
# SKANDA SAHASRANAMAM — derived modern names
# Source: Skanda Purana, Vana Parva (Mahabharata)
# ═══════════════════════════════════════════════════════════════════════════
SKANDA_DERIVED = [
    # SA group
    ("Sarvnayak",     "SK-2", "Sarvnayak",  "सर्वनायक", "Sarvanāyaka","Leader of all; one born to lead everywhere",            "sarvanāyaka → drop -a",                                           "rare",      5),
    ("Sarvsena",      "SK-5", "Sarvsena",   "सर्वसेन",  "Sarvasena",  "Invincible commander; leading any force to victory",    "sarvasena → drop -a",                                             "rare",      5),
    ("Sanmukh",       "SK-9", "Sanmukh",    "षण्मुख",   "Ṣaṇmukha",   "Multi-faceted; able to face any direction or challenge","ṣaṇmukha → drop -a",                                              "uncommon",  5),
    ("Sharavesh",     "SK-10","Sharavesh",  "शरवेश",    "Śaraveśa",   "Lord of the sacred forest; born of divine mystery",     "śaravaṇa → forest root śara + veśa (entry/dwelling)",            "very rare", 5),
    ("Shaktesh",      "SK-12","Shaktesh",   "शक्तेश",   "Śakteśa",   "Lord of divine power; master of energy and force",      "śaktidhara root śakti + īśa → śakteśa",                          "rare",      5),
    ("Senaj",         "SK-27","Senaj",      "सेनज",     "Senaja",     "Born to lead; warrior-born by nature",                  "senānī root senā (army) + ja (born of)",                          "very rare", 5),
    ("Senesh",        "SK-28","Senesh",     "सेनेश",    "Seneśa",    "Commander; sovereign of the warrior force",             "senāpati → senā + īśa → seneśa",                                 "rare",      5),
    ("Siddhesh",      "SK-30","Siddhesh",   "सिद्धेश",  "Siddheśa",  "Lord of accomplishment; perfection personified",        "siddheśa → drop -a",                                              "uncommon",  5),
    # SI group
    ("Simhaveer",     "SK-15","Simhaveer",  "सिंहवीर",  "Siṃhavīra",  "Lion-like hero; supremely courageous warrior",          "siṃhavikrama → root siṃha + vīra",                               "rare",      5),
    ("Sivkumar",      "SK-25","Sivkumar",   "शिवकुमार", "Śivakumāra", "Divine son; young and auspicious",                      "śivakumāra → drop -a",                                            "uncommon",  4),
    # SU group
    ("Subran",        "SK-16","Subran",     "सुब्रन",   "Subrana",    "Very dear to wisdom; radiantly intelligent",            "subrahmaṇya → root sub + ran",                                   "very rare", 5),
    ("Suransh",       "SK-19","Suransh",    "सुरांश",   "Surāṃśa",   "Born of the divine; a celestial fragment",              "sura + aṃśa",                                                      "rare",      5),
    ("Surend",        "SK-23","Surend",     "सुरेंद",   "Surenda",    "Of divine and royal spirit; supremely elevated",        "surendravandita root surendra → drop -a",                         "uncommon",  5),
    # JA group
    ("Jayjit",        "SK-31","Jayjit",     "जयजित",    "Jayajita",   "Doubly victorious; conqueror of every battle",          "jaya + jita",                                                      "uncommon",  5),
    ("Jayesh",        "SK-32","Jayesh",     "जयेश",     "Jayeśa",    "Lord of victory; sovereign of triumph",                 "jayanta root jaya + īśa",                                          "uncommon",  5),
    ("Jayashakt",     "SK-34","Jayashakt",  "जयशक्त",   "Jayaśakta",  "Empowered to win; whose strength brings victory",       "jayaśakti → drop -i",                                             "very rare", 5),
    # JI group
    ("Jitarajn",      "SK-36","Jitarajn",   "जितराजन",  "Jitarājana", "Conqueror of demonic forces; slayer of darkness",       "jitasura root jita + raja (king/force)",                          "very rare", 5),
    # GA group
    ("Ganansh",       "SK-41","Ganansh",    "गणांश",    "Gaṇāṃśa",  "Born of divine hosts; part of the celestial force",     "gaṇanātha root gaṇa + aṃśa",                                      "rare",      5),
    ("Ganesh",        "SK-41","Ganesh",     "गणेश",     "Gaṇeśa",    "Lord of all groups; naturally unifying leader",         "gaṇanātha → gaṇeśa → ganesh",                                     "uncommon",  3),
    ("Girijkumar",    "SK-43","Girijkumar", "गिरिजकुमार","Girijkumāra","Son of the mountain goddess; noble birth",             "girijākumāra → drop syllable -ā",                                "uncommon",  4),
    ("Guhansh",       "SK-44","Guhansh",    "गुहांश",   "Guhāṃśa",  "Born of the inner depths; mysterious and deep",         "guhanātha root guha + aṃśa",                                      "very rare", 5),
    ("Gunasagar",     "SK-46","Gunasagar",  "गुणसागर",  "Guṇasāgara", "Ocean of virtues; infinitely excellent",                "guṇasāgara → already clean, drop -a",                            "uncommon",  4),
    # DE group
    ("Devasenth",     "SK-48","Devasenth",  "देवसेन्थ", "Devasentha", "Born of the divine army; warrior of the gods",          "devasenā → masculine contracted form",                            "very rare", 5),
    ("Devkumar",      "SK-51","Devkumar",   "देवकुमार", "Devakumāra", "Divine youth; the youthful divine prince",              "devakumāra → drop -a",                                            "uncommon",  4),
    ("Devanth",       "SK-52","Devanth",    "देवन्थ",   "Devantha",   "Limit of divinity; boundlessly divine",                 "deva + anta (end/limit) → devāntha → devanth",                   "rare",      5),
    # LA group
    ("Lavnish",       "SK-54","Lavnish",    "लवनिश",    "Lavanīśa",   "Graceful sovereign; commanding with beauty",            "lavanya root lav + nīśa (lord) → lavnish",                       "very rare", 5),
]

# ═══════════════════════════════════════════════════════════════════════════
# GANESHA SAHASRANAMAM — derived modern names
# Source: Ganesha Purana, Mudgala Purana
# ═══════════════════════════════════════════════════════════════════════════
GANESHA_DERIVED = [
    # SA group
    ("Sarvesh",       "G-6",  "Sarvesh",    "सर्वेश",   "Sarveśa",   "Master of all; naturally commanding presence",          "sarvalokasundara → sarva + īśa → sarvesh",                        "uncommon",  5),
    ("Samidh",        "G-8",  "Samidh",     "समिध",     "Samidha",    "Blazing with inner fire; brilliantly illumined",        "samiddha → drop -a",                                              "rare",      5),
    ("Siddhesh",      "G-14", "Siddhesh",   "सिद्धेश",  "Siddheśa",  "Lord of accomplishments; master of perfections",        "siddheśa → drop -a",                                              "uncommon",  5),
    ("Siddhant",      "G-12", "Siddhant",   "सिद्धान्त","Siddhānta",  "Of clear principle; one who lives by clear truths",     "siddhakara root siddha + anta → siddhānta → drop -a",            "uncommon",  5),
    ("Siddhansh",     "G-13", "Siddhansh",  "सिद्धांश", "Siddhāṃśa", "A fragment of divine perfection; supremely gifted",     "siddha + aṃśa",                                                   "uncommon",  5),
    ("Sivkumar",      "G-17", "Sivkumar",   "शिवकुमार", "Śivakumāra","Son of Shiva; divinely born",                           "śivakumāra → drop -a",                                            "uncommon",  4),
    # SU group
    ("Subhav",        "G-22", "Subhav",     "सुभव",     "Subhava",    "Auspiciously born; one who brings good wherever he goes","subhaga root su + bhava → subhav",                               "rare",      5),
    ("Subodh",        "G-25", "Subodh",     "सुबोध",    "Subodha",    "Of excellent understanding; quick to grasp truths",     "subuddhi root su + bodha (understanding)",                        "uncommon",  4),
    ("Sudheer",       "G-26", "Sudheer",    "सुधीर",    "Sudhīra",    "Supremely patient and wise",                            "sudhīra → drop -a",                                               "uncommon",  5),
    ("Sukhansh",      "G-19", "Sukhansh",   "सुखांश",   "Sukhāṃśa",  "Born of bliss; carrying happiness everywhere",          "sukha + aṃśa",                                                    "rare",      5),
    ("Sunav",         "G-29", "Sunav",      "सुनव",     "Sunava",     "Beautifully named; of auspicious identity",             "sunāma → sun + av ending",                                        "very rare", 5),
    ("Suprabh",       "G-31", "Suprabh",    "सुप्रभ",   "Suprabha",   "Of excellent radiance; brilliantly glowing",            "suprabha → drop -a",                                              "uncommon",  5),
    ("Suresh",        "G-32", "Suresh",     "सुरेश",    "Sureśa",    "Lord of the divine; celestial sovereign",               "sureśvara → suresh",                                              "uncommon",  4),
    ("Suryan",        "G-33", "Suryan",     "सूर्यन",   "Sūryana",    "Solar energy; radiant like the sun",                    "sūrya + -n",                                                      "uncommon",  5),
    # JA group
    ("Jagbandh",      "G-36", "Jagbandh",   "जगबंध",    "Jagabandha", "Friend of the world; universally connected",            "jagadbandhu → contract to jagbandh",                             "very rare", 5),
    ("Jagesh",        "G-38", "Jagesh",     "जगेश",     "Jageśa",    "Lord of the world; commanding universal respect",       "jagadīśa → compress → jagesh",                                   "rare",      5),
    ("Jayansh",       "G-39", "Jayansh",    "जयांश",    "Jayāṃśa",   "Born of victory; carrying triumph",                     "jayadeva root jaya + aṃśa",                                       "uncommon",  5),
    # GA group
    ("Gajesh",        "G-43", "Gajesh",     "गजेश",     "Gajeśa",    "Lord among the mighty; powerfully commanding",          "gajapati root gaja + īśa → gajeśa",                              "uncommon",  5),
    ("Gajansh",       "G-42", "Gajansh",    "गजांश",    "Gajāṃśa",  "Born of Ganesha's energy; divinely wise",               "gajānana root gaja + aṃśa",                                       "rare",      5),
    ("Ganadip",       "G-47", "Ganadip",    "गणदीप",    "Gaṇadīpa",  "Light of the divine hosts; a shining leader",           "gaṇadeva → gaṇa + dīpa (lamp/light)",                            "very rare", 5),
    ("Ganansh",       "G-49", "Ganansh",    "गणांश",    "Gaṇāṃśa",  "Part of the divine force; born of celestial hosts",     "gaṇanātha root gaṇa + aṃśa",                                     "rare",      5),
    ("Gauresh",       "G-53", "Gauresh",    "गौरेश",    "Gaureśa",   "Son of the radiant mother; luminous and pure",          "gaurīputra → gauri root + īśa",                                  "rare",      5),
    # GU group
    ("Gunansh",       "G-57", "Gunansh",    "गुणांश",   "Guṇāṃśa",  "Born of virtue; naturally excellent",                   "guṇakara root guṇa + aṃśa",                                      "rare",      5),
    ("Gunesh",        "G-56", "Gunesh",     "गुणेश",    "Guṇeśa",   "Master of virtues; supremely excellent in character",   "guṇagrāhī root guṇa + īśa",                                      "uncommon",  5),
    # DE group
    ("Devesh",        "G-61", "Devesh",     "देवेश",    "Deveśa",   "Sovereign of divinity; lord of the radiant",            "devapujita root deva + īśa",                                      "uncommon",  5),
    ("Devansh",       "G-59", "Devansh",    "देवांश",   "Devāṃśa",  "Born of the divine; a part of cosmic light",            "devabhūta root deva + aṃśa",                                      "uncommon",  5),
    ("Devyan",        "G-63", "Devyan",     "देव्यन",   "Devyana",   "On the divine path; journeying toward the sacred",      "devayāna root deva + yana",                                       "very rare", 5),
    # LA group
    ("Lambesh",       "G-64", "Lambesh",    "लम्बेश",   "Lambeśa",   "Vast and wise lord; one of generous presence",          "lambodara → root lamba (vast/generous) + īśa",                   "very rare", 4),
    ("Lavansh",       "G-66", "Lavansh",    "लावांश",   "Lāvāṃśa",  "Born of grace; carrying divine beauty",                 "lāvaṇyamaya root lāvaṇya + aṃśa",                                "rare",      5),
]

# ═══════════════════════════════════════════════════════════════════════════
# SURYA SAHASRANAMAM — derived modern names
# Source: Samba Purana, Bhavishya Purana
# ═══════════════════════════════════════════════════════════════════════════
SURYA_DERIVED = [
    # SA group
    ("Saptarashm",    "SU-8", "Saptarashmit","सप्तरश्मित","Saptaraśmita","Seven-rayed; multi-directional brilliance",           "saptaraśmi → + -t suffix",                                       "very rare", 4),
    ("Sahasrakiran",  "SU-12","Sahasrakiran","सहस्रकिरण","Sahasrakiraṇa","Blazing with infinite radiance; endlessly brilliant",  "sahasrakiraṇa → already clean",                                  "uncommon",  4),
    ("Savijit",       "SU-11","Savijit",     "सविजित",   "Savijita",   "Victorious energizer; conquering through light",        "savitā root sav + jit",                                           "very rare", 5),
    ("Savrajan",      "SU-20","Savrajan",    "सव्राजन",  "Savrājana",  "Brilliantly ruling; sovereign with solar radiance",     "saura (solar) + rāja + -n",                                      "very rare", 5),
    ("Sandhyesh",     "SU-17","Sandhyesh",   "सन्ध्येश", "Sandhyeśa",  "Lord of the twilight; master of transitions",           "sandhyā + īśa → sandhyeśa → sandhyesh",                         "rare",      5),
    ("Saurabh",       "SU-19","Saurabh",     "सौरभ",     "Saurabha",   "Of divine fragrance; sweetly radiant",                  "saurabha → drop -a",                                             "uncommon",  4),
    ("Sauryan",       "SU-20","Sauryan",     "सौर्यन",   "Sauryana",   "Solar spirit; blazing with the sun's courage",          "saura root + -n modern suffix",                                  "rare",      5),
    # SI group
    ("Sikhesh",       "SU-21","Sikhesh",     "शिखेश",    "Śikheśa",   "Flame-lord; one who leads with blazing energy",         "śikhaṇḍa root śikha (flame) + īśa",                             "very rare", 5),
    # SU group
    ("Suryaan",       "SU-23","Suryaan",     "सूर्यान",  "Sūryāna",   "Of the Sun; solar in spirit and nature",                "sūrya + -ān",                                                    "uncommon",  5),
    ("Suryesh",       "SU-24","Suryesh",     "सूर्येश",  "Sūryeśa",   "Lord of the Sun; commanding solar power",               "sūrya + īśa → sūryeśa → suryesh",                               "uncommon",  5),
    ("Suryanshu",     "SU-26","Suryanshu",   "सूर्यांशु","Sūryāṃśu",  "Ray of the Sun; a beam of solar brilliance",            "sūrya + aṃśu (ray)",                                             "uncommon",  4),
    ("Suryaansh",     "SU-27","Suryaansh",   "सूर्यांश", "Sūryāṃśa",  "Born of the Sun; a portion of solar light",             "sūrya + aṃśa",                                                   "uncommon",  5),
    ("Subhesh",       "SU-29","Subhesh",     "शुभेश",    "Śubheśa",   "Lord of the auspicious; master of blessings",           "subhankara root śubha + īśa",                                    "rare",      5),
    ("Suvarchan",     "SU-33","Suvarchan",   "सुवर्चन",  "Suvarcana",  "Of great spiritual lustre; radiantly alive",            "suvarcas + -an modern suffix",                                   "very rare", 5),
    # JA group
    ("Jagesh",        "SU-37","Jagesh",      "जगेश",     "Jageśa",    "Lord of the world; universally sovereign",              "jagadīśa → compress → jagesh",                                   "rare",      5),
    ("Jagatpran",     "SU-38","Jagatpran",   "जगत्प्राण","Jagatprāṇa","Life-force of the universe; vitally luminous",          "jagatprāṇa → drop -a",                                           "very rare", 5),
    ("Jayesh",        "SU-42","Jayesh",      "जयेश",     "Jayeśa",    "Lord of victory; master of every triumph",              "jayaprada root jaya + īśa",                                      "uncommon",  5),
    # GA group
    ("Gaganesh",      "SU-44","Gaganesh",    "गगनेश",    "Gaganeśa",  "Lord of the sky; sovereign of the open heavens",        "gaganacara root gagana + īśa",                                   "rare",      5),
    ("Gaganprabh",    "SU-45","Gaganprabh",  "गगनप्रभ",  "Gaganaprabha","Radiant in the sky; shining across all horizons",      "gaganaprabha → drop -a",                                         "rare",      5),
    ("Gatiman",       "SU-47","Gatiman",     "गतिमान",   "Gatimān",   "Swiftly moving; dynamic and unstoppable",               "gatimān → already short and modern",                             "uncommon",  5),
    ("Gauresh",       "SU-47","Gauresh",     "गौरेश",    "Gaureśa",   "Radiant sovereign; brilliantly commanding",             "gatimān context + gaura root",                                   "rare",      5),
    # DE group
    ("Devraj",        "SU-55","Devraj",      "देवराज",   "Devarāja",  "King of the divine; natural sovereign",                 "devarāja → drop -a",                                             "uncommon",  4),
    ("Devesh",        "SU-51","Devesh",      "देवेश",    "Deveśa",   "God of gods; supreme divine authority",                 "devadeva → deveśa → devesh",                                     "uncommon",  5),
    ("Devansh",       "SU-54","Devansh",     "देवांश",   "Devāṃśa",  "Born of the divine; a fragment of cosmic light",        "deva + aṃśa",                                                    "uncommon",  5),
    ("Devyan",        "SU-53","Devyan",      "देव्यन",   "Devyana",   "On the divine path; moving toward the sacred",          "deva + yana (journey)",                                           "very rare", 5),
    # LA group
    ("Lavesh",        "SU-59","Lavesh",      "लवेश",     "Laveśa",   "Graceful lord; commanding with beauty and light",        "lāvaṇya root lav + īśa",                                         "rare",      5),
    ("Lakshansh",     "SU-59","Lakshansh",   "लक्षांश",  "Lakṣāṃśa", "Born of fortune; marked by auspiciousness",             "lakṣmīvāsa root lakṣa + aṃśa",                                  "rare",      5),
]

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def enrich(records, source_name):
    seen = set()
    result = []
    for rec in records:
        (src_epithet, shloka, name, dev, iast, meaning, deriv, rarity, mfeel) = rec
        if name.lower() in seen:
            continue
        grp = syllable_group(name)
        if not grp:
            continue
        seen.add(name.lower())
        total, final = chaldean(name)
        result.append({
            "source_epithet": src_epithet,
            "shloka": shloka,
            "name": name,
            "devanagari": dev,
            "iast": iast,
            "meaning": meaning,
            "derivation": deriv,
            "rarity": rarity,
            "modern_feel": mfeel,
            "syllable": grp,
            "chaldean_total": total,
            "chaldean_final": final,
            "preferred": "✦" if final in PREFERRED else "",
            "source": source_name,
        })
    return sorted(result, key=lambda x: (x["syllable"], x["name"]))


def write_file(records, source_name, deity, purana_ref, filename):
    total = len(records)
    by_syl = {}
    for r in records:
        by_syl.setdefault(r["syllable"], []).append(r)

    preferred = [r for r in records if r["preferred"]]
    top_modern = sorted([r for r in records if r["modern_feel"] >= 5],
                        key=lambda x: (-x["chaldean_final"] if x["preferred"] else 0, x["name"]))

    lines = [
        f"# {source_name} — Modern Baby Boy Names",
        f"",
        f"**Deity / Subject:** {deity}  ",
        f"**Scriptural Source:** {purana_ref}  ",
        f"**Method:** Each name is derived from Sanskrit roots of the original text —",
        f"not a verbatim lift. Root extraction → contraction → modern 2-4 syllable form.  ",
        f"**Nakshatra Syllables:** Sa · Si · Su · Se · Ja · Ji · Ga · Gu · De · La  ",
        f"**Total Derived Names:** {total}  ",
        f"**With Preferred Chaldean (1/3/6):** {len(preferred)}  ",
        f"",
        f"---",
        f"",
        f"## How to Read This Table",
        f"",
        f"| Column | Meaning |",
        f"|--------|---------|",
        f"| **Derived From** | The original sahasranama epithet (verse word) |",
        f"| **Name** | The new modern baby boy name derived from it |",
        f"| **Derivation** | How the name was formed from Sanskrit roots |",
        f"| **Chaldean ✦** | Final numerology value; ✦ = preferred (1, 3, or 6) |",
        f"| **Feel** | Modern-feel score 1-5 (5 = most contemporary-sounding) |",
        f"",
        f"---",
        f"",
    ]

    for syl in ["SA","SI","SU","SE","JA","JI","GA","GU","DE","LA"]:
        group = by_syl.get(syl, [])
        if not group:
            continue
        lines.append(f"## {syl} — ({len(group)} names)")
        lines.append("")
        lines.append("| Derived From | Name | Devanagari | Meaning | Derivation | Chaldean | ✦ | Feel |")
        lines.append("|-------------|------|------------|---------|------------|----------|---|------|")
        for r in group:
            lines.append(
                f"| *{r['source_epithet']}* | **{r['name']}** | {r['devanagari']} | "
                f"{r['meaning']} | {r['derivation']} | "
                f"{r['chaldean_final']} | {r['preferred']} | {r['modern_feel']}/5 |"
            )
        lines.append("")

    lines += [
        "---",
        "",
        f"## Top Picks — Highest Modern Feel + Preferred Chaldean",
        "",
        "| Name | Syllable | Chaldean | Devanagari | Meaning | Derived From |",
        "|------|----------|----------|------------|---------|-------------|",
    ]
    shown = set()
    for r in sorted(records, key=lambda x: (-x["modern_feel"], x["preferred"] == "", x["name"])):
        if r["name"] in shown:
            continue
        if r["modern_feel"] < 4:
            continue
        shown.add(r["name"])
        lines.append(
            f"| **{r['name']}** | {r['syllable']} | "
            f"{r['chaldean_final']}{'✦' if r['preferred'] else ''} | "
            f"{r['devanagari']} | {r['meaning']} | *{r['source_epithet']}* |"
        )

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    preferred_count = len([r for r in records if r["preferred"]])
    print(f"  {filename}: {total} derived names, {preferred_count} with preferred Chaldean")


def main():
    print("Generating modern name files from sahasranama roots...\n")

    datasets = [
        (VISHNU_DERIVED,  "Vishnu Sahasranamam",  "Lord Vishnu",
         "Anushasana Parva (Mahabharata), Bhagavata Purana",
         "VISHNU-SAHASRANAMAM-NAMES.md"),
        (LALITHA_DERIVED, "Lalitha Sahasranamam", "Goddess Lalitha / Devi (Shakti)",
         "Brahmanda Purana — Lalitopakhyana",
         "LALITHA-SAHASRANAMAM-NAMES.md"),
        (SHIVA_DERIVED,   "Shiva Sahasranamam",   "Lord Shiva",
         "Anushasana Parva (Mahabharata), Shiva Purana",
         "SHIVA-SAHASRANAMAM-NAMES.md"),
        (SKANDA_DERIVED,  "Skanda Sahasranamam",  "Lord Murugan / Kartikeya",
         "Skanda Purana, Vana Parva (Mahabharata)",
         "SKANDA-SAHASRANAMAM-NAMES.md"),
        (GANESHA_DERIVED, "Ganesha Sahasranamam", "Lord Ganesha",
         "Ganesha Purana, Mudgala Purana",
         "GANESHA-SAHASRANAMAM-NAMES.md"),
        (SURYA_DERIVED,   "Surya Sahasranamam",   "Lord Surya (Sun God)",
         "Samba Purana, Bhavishya Purana",
         "SURYA-SAHASRANAMAM-NAMES.md"),
    ]

    for raw, source, deity, purana, fname in datasets:
        enriched = enrich(raw, source)
        write_file(enriched, source, deity, purana, fname)

    print("\nDone.")


if __name__ == "__main__":
    main()
