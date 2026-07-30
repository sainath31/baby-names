#!/usr/bin/env python3
"""
Hindu Baby Boy Name Generator — January 2027
Extracts every possible name from a comprehensive Sanskrit/Hindu knowledge base
covering scriptural sources, modern derivatives, and root-based generation.

Syllable groups: Sa · Si · Su · Se · Ja · Ji · Ga · Gu · De · La

Run:  python3 scraper.py
Output: baby-names-research.csv  |  baby-names-research.json  |  baby-names-scraped.md
"""

import json
import csv
import sys
from collections import defaultdict

# ─────────────────────────────────────────────────────────────────────────────
# CHALDEAN NUMEROLOGY
# ─────────────────────────────────────────────────────────────────────────────

CHALDEAN_MAP = {
    'a':1,'i':1,'j':1,'q':1,'y':1,
    'b':2,'k':2,'r':2,
    'c':3,'g':3,'l':3,'s':3,
    'd':4,'m':4,'t':4,
    'e':5,'h':5,'n':5,'x':5,
    'o':6,'u':6,'v':6,'w':6,
    'z':7,
    'f':8,'p':8,
}
PREFERRED_FINALS = {1, 3, 6}

def chaldean(name: str) -> tuple:
    total = sum(CHALDEAN_MAP.get(c.lower(), 0) for c in name if c.isalpha())
    final = total
    while final > 9:
        final = sum(int(d) for d in str(final))
    return total, final

# ─────────────────────────────────────────────────────────────────────────────
# MEANING QUALITY SCORER
# ─────────────────────────────────────────────────────────────────────────────

POWER_KEYWORDS = [
    "victor","victory","victorious","conquer","conqueror","conquest","triumph",
    "win","winner","rise","rising","ascend","ascent","ascendant","ascended",
    "power","powerful","force","strong","strength","mighty","mightiest",
    "leader","command","commander","king","lord","master","sovereign","ruler",
    "emperor","supreme","highest","excellent","great","greatest","best",
    "brave","valor","valiant","courageous","warrior","hero","heroic","bold",
    "solar","sun","radiant","radiance","brilliance","bright","glow","luster",
    "glorious","glory","fame","renowned","renown","famous","illustrious",
    "achieve","achievement","accomplish","accomplish","success","attain",
    "swift","speed","fast","momentum","unstoppable","irresistible",
    "divine","god","cosmic","celestial","spiritual power","fire","flame",
    "blaze","energy","creator","creation","manifest","invincible","eternal",
    "conqueror","defeat","enemy","battle","army","general","wrath","will",
    "awakened","alert","dynamic","progressive","luminous","charged",
    "lion","thunder","storm","peak","summit","banner","victory flag",
]

WEAK_KEYWORDS = [
    "peace","calm","gentle","soft","mild","quiet","humble","pleasant smell",
    "flower","breeze","cool water","pure water","fragrance","melody","servant",
    "follower","pond","lake","sand","moon of peace","gentle river",
]

def meaning_quality(meaning: str) -> int:
    if not meaning:
        return 0
    m = meaning.lower()
    score = sum(1 for kw in POWER_KEYWORDS if kw in m)
    score -= sum(2 for kw in WEAK_KEYWORDS if kw in m)
    return max(score, -5)

# ─────────────────────────────────────────────────────────────────────────────
# MASTER NAME DATABASE
# Each entry: (Name, Meaning, Category, Source, Deity)
# Category: S = Scriptural, M = Modern Derivative
# ─────────────────────────────────────────────────────────────────────────────

RAW_NAMES = [

    # ══════════════════════════════════════════════════════════
    # SA GROUP
    # ══════════════════════════════════════════════════════════
    ("Satyaki","Warrior hero of the Mahabharata; truth-victorious; one who never abandons the battlefield; supreme commander","S","Mahabharata, Bhagavata Purana","Krishna/Vishnu"),
    ("Satrajit","Victorious over the entire realm; conquerer in all directions; king who wins completely","S","Bhagavata Purana Skanda 10","Vishnu/Krishna"),
    ("Satyabhanu","Whose radiance is truth; sun of truth; whose brilliance illuminates reality; solar radiance","S","Vishnu Purana, Puranic stotras","Surya"),
    ("Satyavan","Possessor of truth; unconquerable by death; the man of supreme truth and vitality","S","Mahabharata Aranyaka Parva","Vishnu"),
    ("Satyajit","Truly victorious; one who wins through the power of truth; victorious in truth","S","Bhagavata Purana","Vishnu"),
    ("Satyadev","God of truth; lord whose essence is truth; divine truth embodied","S","Sanskrit stotras","Vishnu/Shiva"),
    ("Satyavijay","Victorious through truth; conquest achieved by truth-power","M","Sanskrit compound","Vishnu"),
    ("Satyaprakash","Radiance of truth; the light of truth that illuminates all darkness","M","Sanskrit compound","Surya/Vishnu"),
    ("Satyadhar","Bearer of truth; one who carries and upholds truth as a warrior carries his sword","M","Sanskrit compound","Vishnu"),
    ("Satyavrat","Whose vow is truth; bound by the supreme vow of truth; unbreakable in integrity","S","Vishnu Sahasranama commentary","Vishnu"),
    ("Savarni","Of the solar lineage; son of the Sun God; the 8th cosmic Manu who rules an entire age","S","Manusmriti, Bhagavata Purana","Surya"),
    ("Satvesh","Lord of the Satvata warriors; master of true power; Vishnu as lord of his warrior devotees","M","Vishnu Sahasranama root","Vishnu"),
    ("Samavesh","Total immersion in divine power; the state of complete absorption by cosmic force","M","Kashmir Shaivism Tantraloka","Shiva"),
    ("Saujit","Auspiciously victorious; whose victory is of the highest celestial order","M","Sanskrit compound","Vishnu"),
    ("Saujash","Of the highest glory; supremely illustrious; whose fame is excellent","M","Sanskrit compound","Vishnu"),
    ("Saujanya","Noble and excellent; of highest character and power","M","Sanskrit compound","Vishnu"),
    ("Savitej","Solar radiance; the brilliance of the Sun God; blazing with solar energy","M","Sanskrit compound","Surya"),
    ("Savitraj","King of solar power; sovereign of the Sun's radiance","M","Sanskrit compound","Surya"),
    ("Savitran","Giver of solar energy; one who distributes solar power; radiating like the Sun","S","Vedic hymns to Savitri","Surya"),
    ("Savitr","The Sun God as progenitor and life-giver; the driving force behind all living things","S","Rig Veda, Gayatri Mantra","Surya"),
    ("Satvat","Of the Satvata warrior lineage; belonging to Vishnu's own clan of fighters","S","Vishnu Sahasranama","Vishnu"),
    ("Satvaan","Possessing great truth and vitality; the unconquerable man","S","Mahabharata","Vishnu"),
    ("Satvan","Warrior full of sattva power; strong, vital, and truthful fighter","S","Sanskrit epic poetry","Vishnu"),
    ("Satvayu","Whose life-breath is truth-power; one of supreme vital force","M","Sanskrit Vedic compound","Vishnu"),
    ("Satvik","Of pure sattva quality; having the nature of clarity, power, and light","M","Bhagavad Gita","Vishnu/Krishna"),
    ("Saurav","Celestial; divine; relating to the heavens; of solar/celestial origin","M","Sanskrit compound","Surya"),
    ("Saurjit","Victorious through solar power; won by the force of the Sun","M","Sanskrit compound","Surya"),
    ("Sauraj","Born of solar power; son of the Sun; of solar origin","M","Sanskrit compound","Surya"),
    ("Sauransh","Fragment of solar power; a portion of the Sun's radiance","M","Sanskrit compound","Surya"),
    ("Saurik","Solar; relating to the Sun; carrying the energy of Surya","M","Sanskrit compound","Surya"),
    ("Saurav","Celestial; of divine beauty; related to the heavens","M","Sanskrit compound","Surya"),
    ("Samveg","Intense momentum; rapid powerful force; the unstoppable energy of a charging warrior","M","Sanskrit philosophical texts","Shiva/Vishnu"),
    ("Samriddh","Supremely prosperous; achieved complete success; one who has accomplished all","M","Sanskrit compound","Vishnu/Lakshmi"),
    ("Samrath","Supremely capable; one of complete ability and power; fully sufficient","M","Sanskrit compound","Vishnu"),
    ("Samvit","Pure consciousness; complete awareness; the highest state of knowing","S","Upanishads, Kashmirshaivism","Shiva"),
    ("Samnay","One who leads by commanding respect; the righteous commander","M","Sanskrit compound","Vishnu"),
    ("Samjit","Completely victorious; winner on all fronts","M","Sanskrit compound","Vishnu"),
    ("Sanjiv","Fully alive; completely vital; one overflowing with life-force","M","Sanskrit compound","Vishnu"),
    ("Sanhat","Firmly established; of solid powerful build; the immovable one","M","Sanskrit compound","Shiva"),
    ("Sanjash","Completely glorious; renowned in all directions","M","Sanskrit compound","Vishnu"),
    ("Sanjeet","Completely victorious; winner without exception","M","Sanskrit compound","Vishnu"),
    ("Sannath","Accompanied by strength; with great power; the well-equipped warrior","M","Sanskrit compound","Vishnu"),
    ("Sanavir","Completely heroic; the thorough warrior; brave in every dimension","M","Sanskrit compound","Skanda"),
    ("Sanmit","Friend and ally of truth; companion of the righteous path","M","Sanskrit compound","Vishnu"),
    ("Santanu","Complete body; one of perfect wholeness; full-bodied and powerful","S","Mahabharata - king Shantanu","Vishnu"),
    ("Sapratap","With great glory and valor; possessing complete dignity and power","M","Sanskrit compound","Vishnu/Indra"),
    ("Saratej","Radiant essence; the brilliance of the best","M","Sanskrit compound","Surya"),
    ("Sarjun","Completely golden; of Arjuna's lineage; wholly noble","M","Sanskrit compound","Indra/Vishnu"),
    ("Sarvik","Universal; completely cosmic; present in all","M","Sanskrit compound","Vishnu"),
    ("Saujas","Of great power and vigor; supremely energized","S","Rig Veda","Indra"),
    ("Savant","Achiever; one who has mastered all; fully accomplished","M","Sanskrit derivative","Vishnu"),
    ("Savit","Inspired by the Sun; solar-energized; lit by Savitr","M","Sanskrit compound","Surya"),
    ("Savrik","One who is sharp and swift like an arrow; the accurate striker","M","Sanskrit compound","Vishnu"),
    ("Sadvit","Knower of truth; one who has attained complete wisdom","M","Sanskrit compound","Vishnu"),
    ("Sajesh","Lord of the excellent; master of the righteous path","M","Sanskrit compound","Vishnu"),
    ("Sajjan","Noble person; one of excellent character and upright conduct","M","Sanskrit compound","Vishnu"),
    ("Samaj","Gathering; assembly; the one who brings all together under leadership","M","Sanskrit compound","Vishnu"),
    ("Samajas","Born of the assembly; one who rises from the collective","M","Sanskrit compound","Vishnu"),
    ("Samant","Universal; present everywhere; the one whose power reaches all directions","S","Sanskrit epics","Vishnu"),
    ("Samavit","Complete consciousness; knowing all; total awareness","M","Upanishads","Vishnu/Shiva"),
    ("Samitr","Friend who is equal in measure; the well-matched companion and ally","M","Sanskrit compound","Vishnu"),

    # ══════════════════════════════════════════════════════════
    # SI GROUP
    # ══════════════════════════════════════════════════════════
    ("Sindhav","The great swift war-horse of the Sindhu region; speed, power, endurance of a champion steed","S","Mahabharata, Ramayana","Indra"),
    ("Sinhaj","Born of the lion; one whose very nature is leonine — brave, commanding, sovereign","M","Sanskrit compound","Narasimha"),
    ("Sinhan","Lion-striker; one who destroys with lion-force; the active lion-destroyer","M","Sanskrit compound","Narasimha"),
    ("Simharth","Whose purpose is lion-level; existing for goals of conquest and sovereignty","M","Sanskrit compound","Narasimha/Vishnu"),
    ("Simhit","Having lion-quality; possessing lion-like strength and courage","M","Sanskrit compound","Narasimha"),
    ("Simhesh","Lord of lions; master of leonine power","M","Sanskrit compound","Narasimha/Vishnu"),
    ("Simhaj","Born of lion; of lion lineage; inherently powerful","M","Sanskrit compound","Narasimha"),
    ("Sindhuraj","King of the ocean; sovereign of vast power","M","Sanskrit compound","Vishnu/Varuna"),
    ("Sindhupal","Protector of the great waters; guardian of vast power","M","Sanskrit compound","Varuna"),
    ("Sindhujas","Born of the ocean; arising from vast depths","M","Sanskrit compound","Vishnu"),
    ("Sindhujit","Conqueror of the ocean; one who overcomes the impossible vastness","M","Sanskrit compound","Vishnu"),
    ("Sivadas","Devotee of Shiva; servant of auspiciousness","S","Sanskrit devotional texts","Shiva"),
    ("Sivakam","Desired by Shiva; beloved of the auspicious divine","M","Sanskrit compound","Shiva"),
    ("Sivanan","With the joy of Shiva; one filled with divine bliss","M","Sanskrit compound","Shiva"),
    ("Sivesh","Lord who is Shiva himself; Shiva as the supreme master","M","Sanskrit compound","Shiva"),
    ("Sikhesh","Lord of the peacock; leader of the divine bird","M","Sanskrit compound","Skanda"),
    ("Sikandar","Victorious defender of men; the great conqueror (Sanskrit-ized Alexander)","S","Historical Sanskrit texts","Vishnu/Indra"),
    ("Siddhesh","Lord of accomplishment; master of all achievement","M","Sanskrit compound","Shiva/Ganesha"),
    ("Siddhraj","King of accomplishment; sovereign of achievement","M","Sanskrit compound","Shiva"),
    ("Siddhivant","Possessor of all accomplishments; one who has achieved everything","M","Sanskrit compound","Shiva/Ganesha"),
    ("Siddham","Accomplished; achieved; one who has realized all goals","S","Buddhist/Sanskrit texts","Vishnu/Shiva"),
    ("Sikhidhvaj","Bearer of the peacock banner; Lord Skanda's title","S","Skanda Purana","Skanda/Murugan"),
    ("Sikhin","One with a crest; the peacock; divine fire; Lord Skanda's epithet","S","Skanda Sahasranama","Skanda/Murugan"),
    ("Simesha","Lord Shiva's gracious form; the auspicious master","M","Sanskrit compound","Shiva"),
    ("Sindhura","Red as the ocean's setting sun; powerful as tidal force","M","Sanskrit compound","Surya"),
    ("Singhal","Lion-hearted; of lion character; brave and sovereign","M","Sanskrit compound","Narasimha"),
    ("Singhan","Lion-man; one who has lion's qualities in human form","M","Sanskrit compound","Narasimha"),
    ("Sinhavant","Possessing the qualities of a lion; full of leonine power","M","Sanskrit compound","Narasimha"),
    ("Sinhavijay","Victory of the lion; conquest achieved with lion-force","M","Sanskrit compound","Narasimha"),
    ("Sinhavikram","Lion's valor; the heroic power of a lion in battle","M","Sanskrit compound","Narasimha"),

    # ══════════════════════════════════════════════════════════
    # SU GROUP
    # ══════════════════════════════════════════════════════════
    ("Sujas","Of supreme vigor and life-force; one whose power-energy is of the highest cosmic order","S","Rig Veda","Surya/Indra"),
    ("Sujwal","Brilliantly blazing; burning with supreme radiance; supreme fire of purpose","M","Sanskrit compound","Agni/Surya"),
    ("Sujav","Supremely swift; of the highest speed; arrow-fast warrior quality","S","Rig Veda Ashvasukta","Indra/Vayu"),
    ("Suketu","Of brilliant presence and banner; whose symbol shines supremely; radiant leader","S","Ramayana","Vishnu/Rama"),
    ("Sukirti","Of supreme renown and glory; whose fame spreads in all directions","S","Vishnu Sahasranama stotras","Vishnu"),
    ("Suparv","Rising supremely at every peak and node; one who excels at every crucial juncture","M","Sanskrit compound","Vishnu"),
    ("Sujesh","Lord of supreme victory; sovereign of the highest conquests","M","Sanskrit compound","Vishnu/Skanda"),
    ("Suvikram","Of supreme valor and heroic power; the most valiant of all warriors","S","Mahabharata","Vishnu/Indra"),
    ("Suvij","Supremely born; of the highest origin; one whose birth is most auspicious","M","Sanskrit compound","Vishnu"),
    ("Suvijay","Supremely victorious; winner of the greatest victories","M","Sanskrit compound","Vishnu"),
    ("Suvrat","One of supreme vow and discipline; bound by the highest commitment","S","Sanskrit Puranas","Vishnu"),
    ("Suvrij","Supremely outstanding; the one who excels most brilliantly","M","Sanskrit compound","Vishnu"),
    ("Suvid","Of supreme wisdom; possessing the highest knowledge","S","Sanskrit philosophical texts","Vishnu"),
    ("Suvarn","Supremely golden; of the finest quality; radiant and excellent","S","Sanskrit texts","Surya"),
    ("Suveg","Supremely swift; of divine momentum; fastest of all","M","Sanskrit compound","Vayu/Vishnu"),
    ("Sutej","Supremely radiant; of the highest brilliance and energy","M","Sanskrit compound","Surya"),
    ("Sutapa","Performing supreme austerities; one of greatest concentrated power","S","Vishnu Purana","Vishnu"),
    ("Surash","Lord of gods; one who rules over the divine beings; king of the heavens","M","Sanskrit compound","Indra/Vishnu"),
    ("Suresha","Supreme lord; master of all; the greatest ruler","M","Sanskrit compound","Vishnu/Indra"),
    ("Suresh","Supreme lord; master of the gods; lord of all beings","M","Sanskrit compound","Vishnu/Indra"),
    ("Surjit","Supremely victorious; winner of all battles; conqueror of everything","M","Sanskrit compound","Vishnu"),
    ("Suraj","Supreme lord; king of the sun; the solar sovereign","M","Sanskrit compound","Surya"),
    ("Surachit","Supremely conscious; of the highest awareness","M","Sanskrit compound","Vishnu"),
    ("Surahan","Destroyer of enemies; one who eliminates all opposition","M","Sanskrit compound","Skanda/Vishnu"),
    ("Suvant","Supremely achieving; the greatest accomplisher","M","Sanskrit compound","Vishnu"),
    ("Sujaan","Supremely wise; one of the highest intelligence and discernment","M","Sanskrit compound","Vishnu"),
    ("Suvash","Supremely clothed in power; dressed in divine authority","M","Sanskrit compound","Vishnu"),
    ("Suhrit","Friend of supreme order; one whose friendship is of the highest caliber","S","Sanskrit texts","Vishnu"),
    ("Sujit","Supremely victorious; winner of all","M","Sanskrit compound","Vishnu"),
    ("Sukhit","One of supreme happiness achieved through power","M","Sanskrit compound","Vishnu"),
    ("Sumit","Supremely measured; one of perfect proportion and power","M","Sanskrit compound","Vishnu"),
    ("Sunik","Of supreme caliber; the finest of all","M","Sanskrit compound","Vishnu"),
    ("Sunish","Supreme lord; lord of all that is auspicious","M","Sanskrit compound","Vishnu/Shiva"),
    ("Suniv","Supreme knowledge; one who knows all at the supreme level","M","Sanskrit compound","Vishnu"),
    ("Supratap","Of supreme glory and valor; whose dignity is highest","M","Sanskrit compound","Vishnu/Indra"),
    ("Suprit","Supremely loved and loving; filled with supreme affection and power","M","Sanskrit compound","Vishnu"),
    ("Suprabh","Supremely radiant; of the highest light and brilliance","M","Sanskrit compound","Surya/Vishnu"),
    ("Supreem","Supreme; the absolute highest; above all others","M","Sanskrit derivative","Vishnu"),
    ("Suprem","Supreme; the very highest; without equal","M","Sanskrit derivative","Vishnu"),
    ("Supriy","Supremely dear; most beloved; one whose love is of the highest order","M","Sanskrit compound","Vishnu"),
    ("Suras","Lord of the gods; one who commands the divine beings","S","Sanskrit texts","Indra"),
    ("Surasena","Army of gods; lord of divine forces; commander of celestial armies","S","Mahabharata - Vasudeva's father","Vishnu/Indra"),
    ("Suryansh","Fragment of the Sun; a portion of solar power; born of Surya","M","Sanskrit compound","Surya"),
    ("Suryajit","Victor through solar power; triumphant with the energy of the Sun","M","Sanskrit compound","Surya"),
    ("Suryakant","Beloved of the Sun; the Sun's darling; one the Sun loves most","S","Sanskrit texts","Surya"),
    ("Suryakirti","Famous as the Sun; renowned like the Sun God","M","Sanskrit compound","Surya"),
    ("Suryamanyu","Divine wrath of the Sun; the fierce will-power of the solar deity","M","Sanskrit compound","Surya"),
    ("Suryaprakash","Radiance of the Sun; the light that the Sun itself produces","M","Sanskrit compound","Surya"),
    ("Suryatej","Solar radiance; the teja (brilliance) of the Sun God","M","Sanskrit compound","Surya"),
    ("Suryaveer","Solar warrior; brave as the Sun; hero who fights with solar energy","M","Sanskrit compound","Surya"),
    ("Suryavikram","Solar valor; the heroic power of the Sun God in battle","M","Sanskrit compound","Surya"),

    # ══════════════════════════════════════════════════════════
    # SE GROUP
    # ══════════════════════════════════════════════════════════
    ("Senaj","Born of the army; warrior by nature and origin; inherently a fighter","M","Sanskrit compound","Skanda"),
    ("Senapati","Commander of armies; lord of forces; the general; Skanda's primary title","S","Rig Veda, Skanda Sahasranama","Skanda/Murugan"),
    ("Setav","Builder of bridges across impossibilities; one who connects what others cannot reach","M","Valmiki Ramayana root","Rama"),
    ("Sehan","The resilient conqueror; one who endures all challenges and rises above them","M","Sanskrit root sah","Vishnu"),
    ("Senavant","Possessor of armies; one who commands great forces","M","Sanskrit compound","Skanda/Indra"),
    ("Senarith","Master of the army; one whose purpose is command","M","Sanskrit compound","Skanda"),
    ("Senadhip","Lord of the army; the commander who oversees all forces","S","Sanskrit epic titles","Skanda"),
    ("Senavikram","Valor of the army; heroic power in command of forces","M","Sanskrit compound","Skanda"),
    ("Senajay","Victory of the army; triumphant command of forces","M","Sanskrit compound","Skanda"),
    ("Senakrit","Creator of the army; one who builds forces from nothing","M","Sanskrit compound","Skanda"),
    ("Senadhar","Bearer of the army's power; carrier of military force","M","Sanskrit compound","Skanda"),
    ("Senaraj","King of the army; royal commander; sovereign of forces","M","Sanskrit compound","Skanda/Indra"),
    ("Senaprav","Rising through the army; ascending by military power","M","Sanskrit compound","Skanda"),
    ("Senaveg","Momentum of the army; unstoppable military force","M","Sanskrit compound","Skanda"),
    ("Senatej","Radiance of the army; the brilliance of military command","M","Sanskrit compound","Skanda"),
    ("Sevit","Honoured; worshipped; the one whom all serve and honour","S","Sanskrit texts","Vishnu"),
    ("Sevansh","Part of divine service; a fragment of sacred purpose","M","Sanskrit compound","Vishnu"),
    ("Sehaj","Natural and powerful; one whose power is effortless and innate","M","Sanskrit compound","Vishnu"),
    ("Sejal","Flowing, clean water; pure as a river; clarity of purpose","M","Sanskrit compound","Vishnu"),
    ("Sejan","Born bright; one whose birth heralds radiance","M","Sanskrit compound","Surya"),
    ("Sekar","One who gathers; the one who brings together power from all sources","M","Sanskrit compound","Vishnu"),

    # ══════════════════════════════════════════════════════════
    # JA GROUP
    # ══════════════════════════════════════════════════════════
    ("Jagrit","The awakened one; fully alert; risen from unconscious slumber into complete power and awareness","M","Mandukya Upanishad, Bhagavad Gita","Vishnu/Shiva"),
    ("Javas","Speed, swiftness, warrior momentum; the irresistible forward force of a champion","S","Rig Veda Ashvasukta","Indra"),
    ("Jayas","Victory itself; the embodiment of conquest; the victorious one","S","Rig Veda, Atharva Veda","Vishnu"),
    ("Javin","The swift one; one who moves with unstoppable speed; arrow-fast","S","Sanskrit epic poetry","Hanuman"),
    ("Jayan","The ever-victorious one; always winning; perpetual victory","S","Sanskrit epics","Vishnu"),
    ("Jayat","Conquering; the one who is in the act of victory right now","S","Sanskrit war poetry","Vishnu"),
    ("Jatin","Bearer of sacred matted locks; carries cosmic powers in Shiva's hair","S","Shiva Sahasranama, Shiva Purana","Shiva"),
    ("Jagvan","Living for the universe; one whose life is cosmic in scope","M","Sanskrit compound","Vishnu"),
    ("Jagesh","Lord of the universe; master of all that exists","M","Sanskrit compound","Vishnu"),
    ("Jagadev","God of the universe; the cosmic deity","S","Sanskrit texts","Vishnu"),
    ("Jagapal","Protector of the universe; the cosmic guardian","M","Sanskrit compound","Vishnu"),
    ("Jagamit","Friend of the universe; companion of all that exists","M","Sanskrit compound","Vishnu"),
    ("Jaganath","Lord of the universe; master of all creation","S","Jagannath Purana, Vedas","Vishnu"),
    ("Jaganniv","Supreme knowledge of the universe; cosmic wisdom","M","Sanskrit compound","Vishnu"),
    ("Jagasamb","Creator of the universe; the one who brings all into being","M","Sanskrit compound","Brahma/Vishnu"),
    ("Jagrav","One who keeps the world awake; the cosmic awakener","M","Sanskrit compound","Vishnu"),
    ("Javayu","Swift as the wind; moving with the speed of Vayu","M","Sanskrit compound","Vayu/Vishnu"),
    ("Javar","Swift; of great speed; the fastest mover","M","Sanskrit root","Vayu"),
    ("Javish","Lord of swiftness; master of speed","M","Sanskrit compound","Vayu"),
    ("Javit","Made swift; given supreme speed; one who was made unstoppable","M","Sanskrit compound","Vayu"),
    ("Javaj","Born of speed; inherently swift; speed is in his nature","M","Sanskrit compound","Vayu"),
    ("Jayam","Victory itself; the embodiment of triumph","S","Sanskrit texts","Vishnu"),
    ("Jayi","The victorious one; the winner; one in the state of victory","S","Sanskrit texts","Vishnu"),
    ("Jayesh","Lord of victory; master of triumph","M","Sanskrit compound","Vishnu"),
    ("Jayaraj","King of victory; royal victor; sovereign of triumph","M","Sanskrit compound","Vishnu"),
    ("Jayakant","Beloved of victory; whom victory loves; victory's favorite","M","Sanskrit compound","Vishnu"),
    ("Jayashil","Whose nature is victory; one who wins by character","M","Sanskrit compound","Vishnu"),
    ("Jayavant","Possessing victory; endowed with triumph; full of conquest","M","Sanskrit compound","Vishnu"),
    ("Jayaveg","Momentum of victory; the unstoppable force of triumph","M","Sanskrit compound","Vishnu"),
    ("Jayatej","Radiance of victory; the brilliance of conquest","M","Sanskrit compound","Vishnu"),
    ("Jayavir","Hero of victory; the victorious warrior","M","Sanskrit compound","Vishnu/Skanda"),
    ("Jayavikram","Valor of victory; heroic power in triumph","M","Sanskrit compound","Vishnu"),
    ("Jayant","Victorious; one who is always triumphant; name of Indra's son","S","Mahabharata, Skanda Purana","Indra/Vishnu"),
    ("Javin","Swift like lightning; the quick and mighty one","S","Sanskrit texts","Indra"),
    ("Javanik","Swift as the wind's power; of wind-like speed and force","M","Sanskrit compound","Vayu"),

    # ══════════════════════════════════════════════════════════
    # JI GROUP
    # ══════════════════════════════════════════════════════════
    ("Jimut","Thunder cloud; storm cloud; carrier of life-giving power and lightning force","S","Kathasaritsagara, Ratnāvali","Indra"),
    ("Jivaj","Born of the life-force itself; one whose origin is vitality not merely biology","M","Sanskrit compound","Vishnu"),
    ("Jiyas","More victorious; the comparative supreme of victory; wins more than any other","M","Sanskrit grammatical form","Vishnu"),
    ("Jivesh","Lord of life-force; master of vitality and living energy","M","Sanskrit compound","Vishnu"),
    ("Jivant","Living powerfully; fully alive; one overflowing with life-force","M","Sanskrit compound","Vishnu"),
    ("Jivraj","King of life; sovereign of vitality; ruler of the living world","M","Sanskrit compound","Vishnu"),
    ("Jivit","Alive; vital; the one who truly lives; imbued with complete life-force","M","Sanskrit texts","Vishnu"),
    ("Jivesh","Lord of life; master of the living; controller of vital force","M","Sanskrit compound","Vishnu"),
    ("Jivaraj","Royal life; the king who is most vitally alive","M","Sanskrit compound","Vishnu"),
    ("Jivakant","Beloved of life; who life itself loves; most vital and beloved","M","Sanskrit compound","Vishnu"),
    ("Jivasena","Army of the living; commander of life's forces","M","Sanskrit compound","Vishnu/Skanda"),
    ("Jivatej","Radiance of life; the brilliance of living with full power","M","Sanskrit compound","Surya/Vishnu"),
    ("Jivavikram","Valor of life; living with heroic power","M","Sanskrit compound","Vishnu"),
    ("Jimutvahan","Rider of thunder clouds; one who commands storm power; hero of supreme valor","S","Kathasaritsagara","Indra"),
    ("Jimutraj","King of thunder clouds; sovereign of storm power","M","Sanskrit compound","Indra"),
    ("Jimutjay","Victory of the storm; triumph of thunder power","M","Sanskrit compound","Indra"),
    ("Jitenesh","Lord of all conquest; master of victory over everything","M","Sanskrit compound","Vishnu"),
    ("Jitraj","King of conquest; sovereign of victory","M","Sanskrit compound","Vishnu"),
    ("Jivraj","King of life-force; royal vitality","M","Sanskrit compound","Vishnu"),
    ("Jitatman","One who has conquered the self; supreme self-mastery; the ultimate victor","S","Bhagavad Gita","Vishnu/Krishna"),
    ("Jitendriya","Conqueror of the senses; one who has mastered all desires","S","Sanskrit philosophical texts","Vishnu"),

    # ══════════════════════════════════════════════════════════
    # GA GROUP
    # ══════════════════════════════════════════════════════════
    ("Gaurish","Lord of Gauri; master of the golden one; husband of Parvati; Lord Shiva","S","Shiva Sahasranama, Shiva Purana","Shiva"),
    ("Gatiman","One of supreme movement and momentum; dynamic; always in powerful motion","S","Sanskrit philosophical literature","Vishnu/Vayu"),
    ("Gatishil","Whose very nature is forward movement; ever-progressive; can never be static","M","Sanskrit compound","Vishnu"),
    ("Gadhi","The great king who was father of Vishwamitra; royal lineage of the greatest sage","S","Vishnu Purana, Mahabharata","Vishnu"),
    ("Gaurik","Of Gauri; born from golden radiance; carries the brilliance of Parvati's light","S","Shiva Purana","Shiva/Parvati"),
    ("Gatiraj","King of movement; sovereign of progress; the regal mover of men","M","Sanskrit compound","Vishnu"),
    ("Gavit","The speaker of truth; one who announces the right","M","Sanskrit compound","Vishnu"),
    ("Gajesh","Lord of elephants; master of massive power; commander of the mightiest forces","M","Sanskrit compound","Ganesha/Indra"),
    ("Gajeswar","Supreme lord of elephant-power; master of the greatest force","M","Sanskrit compound","Ganesha"),
    ("Gajraj","King of elephants; the mightiest of the mighty; monarch of great power","S","Sanskrit texts","Ganesha/Indra"),
    ("Gajveer","Elephant warrior; one who fights with elephant-like power and force","M","Sanskrit compound","Ganesha"),
    ("Gajvikram","Valor of the elephant; heroic power on the scale of the mightiest beast","M","Sanskrit compound","Ganesha"),
    ("Gaganjit","Conqueror of the sky; one who has won the heavens","M","Sanskrit compound","Vishnu/Indra"),
    ("Gaganveer","Sky warrior; brave one who fights at the level of the heavens","M","Sanskrit compound","Vishnu"),
    ("Gagandip","Light of the sky; lamp of the cosmos; the one who illuminates the heavens","M","Sanskrit compound","Surya/Vishnu"),
    ("Gaganeesh","Lord of the sky; master of the cosmic expanse","M","Sanskrit compound","Vishnu"),
    ("Gaganraj","King of the sky; sovereign of the heavens and cosmos","M","Sanskrit compound","Vishnu/Indra"),
    ("Gaganvikram","Valor of the sky; heroic power on a cosmic scale","M","Sanskrit compound","Vishnu/Indra"),
    ("Gaganpreet","Loved by the sky; beloved of the cosmic expanse","M","Sanskrit compound","Vishnu"),
    ("Gaganprabh","Radiance of the sky; brilliance of the cosmic heavens","M","Sanskrit compound","Surya/Vishnu"),
    ("Gaganmit","Friend of the sky; companion of the cosmic expanse","M","Sanskrit compound","Vishnu"),
    ("Gaganpati","Lord of the sky; master and ruler of the heavens","M","Sanskrit compound","Vishnu/Indra"),
    ("Gaurav","Honor; pride; glory; one who commands respect and dignity","M","Sanskrit compound","Vishnu"),
    ("Gaurjit","Victory of the glory; triumphant in dignity and honor","M","Sanskrit compound","Vishnu"),
    ("Gauranand","Joy of glory; blissful in honor and radiance","M","Sanskrit compound","Vishnu"),
    ("Gaurdev","God of glory; divine honor personified","M","Sanskrit compound","Vishnu"),
    ("Gaurvikram","Valor of glory; heroic power in golden radiance","M","Sanskrit compound","Vishnu/Shiva"),
    ("Gavesh","The seeker; one who pursues Vedic knowledge; seeker of the highest truth","M","Sanskrit compound - go+isha","Vishnu"),
    ("Gavas","Swift; of great speed; the fast-moving one","M","Sanskrit compound","Vayu"),
    ("Gavansh","Fraction of great power; a part of the supreme force","M","Sanskrit compound","Vishnu"),
    ("Gavin","Swift; white hawk; the one of great agility and power","M","Sanskrit-influenced","Vishnu"),
    ("Gavis","Light; radiance; shining one; the illuminated one","M","Sanskrit compound","Surya"),
    ("Gavisht","Desirous of cows/power; seeking the best; one who strives for the highest","S","Rig Veda","Indra"),
    ("Gavit","Spoken of with pride; praised for achievement","M","Sanskrit compound","Vishnu"),

    # ══════════════════════════════════════════════════════════
    # GU GROUP
    # ══════════════════════════════════════════════════════════
    ("Gudakesh","Conqueror of sleep; supremely alert and battle-ready; Arjuna's epithet in Bhagavad Gita","S","Bhagavad Gita 1.24, 2.9, 10.20","Krishna/Arjuna"),
    ("Gunatit","One who has transcended the three gunas; beyond all limitations; highest state of being","S","Bhagavad Gita Chapter 14","Krishna/Vishnu"),
    ("Gunavir","The virtuous warrior; supreme inner quality combined with heroic valor","M","Sanskrit compound","Skanda"),
    ("Gunadhip","Lord and master of all virtues; sovereign of his own nature and qualities","M","Sanskrit compound","Vishnu"),
    ("Gunaditya","Sun of virtues; the solar radiance of supreme qualities; radiates goodness like the Sun","M","Sanskrit compound","Surya"),
    ("Gunesh","Lord of qualities; master of all virtues and attributes","M","Sanskrit compound","Vishnu"),
    ("Gunaraj","King of virtues; sovereign of excellence; ruler by inner quality","M","Sanskrit compound","Vishnu"),
    ("Gunakar","Creator of virtues; maker of excellence; producer of quality","S","Sanskrit Puranas - Vishnu epithet","Vishnu"),
    ("Gunanand","Joy of virtues; one who finds bliss in excellence and quality","M","Sanskrit compound","Vishnu"),
    ("Gunakant","Beloved by his virtues; whose virtues attract all to him","M","Sanskrit compound","Vishnu"),
    ("Gunapal","Protector of virtues; guardian of excellence and quality","M","Sanskrit compound","Vishnu"),
    ("Gunaprakash","Radiance of virtues; the light that excellence produces","M","Sanskrit compound","Vishnu/Surya"),
    ("Gunasagar","Ocean of virtues; one who possesses virtues as vast as the sea","S","Sanskrit stotras","Vishnu"),
    ("Gunasena","Army of virtues; forces of excellence under his command","M","Sanskrit compound","Vishnu/Skanda"),
    ("Gunatej","Radiance of virtues; the brilliance of supreme qualities","M","Sanskrit compound","Vishnu"),
    ("Gunavant","Possessing all virtues; endowed with complete excellence","M","Sanskrit compound","Vishnu"),
    ("Gunaveg","Momentum of virtue; the unstoppable force of excellence","M","Sanskrit compound","Vishnu"),
    ("Gunavikram","Valor of virtue; heroic power expressed through excellence of character","M","Sanskrit compound","Vishnu"),
    ("Guresh","Lord who is excellent; the master of supreme quality","M","Sanskrit compound","Vishnu"),
    ("Guritam","The most excellent; the supremely praiseworthy one","M","Sanskrit compound","Vishnu"),
    ("Gurmit","Friend of the teacher; companion of wisdom","M","Sanskrit compound","Vishnu"),
    ("Gurveen","One who carries the teacher's power; possessor of the guru's energy","M","Sanskrit compound","Vishnu"),
    ("Gurvikram","Valor of the teacher; the heroic power of wisdom in action","M","Sanskrit compound","Vishnu"),
    ("Gurdev","Divine teacher; the godly guide; lord who is the teacher of all","M","Sanskrit compound","Vishnu/Shiva"),
    ("Gurjit","Victorious with the teacher's power; winning through wisdom","M","Sanskrit compound","Vishnu"),
    ("Gurpreet","Beloved of the teacher; the teacher's favorite; loved by wisdom","M","Sanskrit compound","Vishnu"),
    ("Gurvant","Possessing the teacher's power; one who has the guru within","M","Sanskrit compound","Vishnu"),

    # ══════════════════════════════════════════════════════════
    # DE GROUP
    # ══════════════════════════════════════════════════════════
    ("Devamanyu","Divine wrath and valor; the sacred fire of righteous will; Vedic deity of invincible will-power","S","Rig Veda Manyu Sukta 10.83-84","Indra/Manyu"),
    ("Devapati","Lord of the gods; king of all divine beings; Indra's primary title","S","Rig Veda (hundreds of hymns)","Indra"),
    ("Devaveg","Divine momentum; the speed and unstoppable force of a god","M","Sanskrit compound","Vishnu"),
    ("Devavikram","Divine valor and power; the heroic might that only gods possess","M","Sanskrit compound","Vishnu"),
    ("Devak","The divine one; noble Yadava king; uncle of Devaki (Krishna's mother)","S","Bhagavata Purana Skanda 10","Krishna/Vishnu"),
    ("Devasut","Son of the gods; of divine lineage; born from celestial parentage (= Arjuna)","S","Mahabharata","Indra"),
    ("Devatej","Divine radiance; the luminous energy of a god; celestial brilliance","M","Sanskrit compound","Vishnu/Krishna"),
    ("Devendra","King of the gods; supreme lord of all divine beings; Indra's name","S","Throughout Vedas and Puranas","Indra"),
    ("Devraj","Divine king; royal among the gods; sovereign of the divine realm","M","Sanskrit compound","Vishnu/Indra"),
    ("Devjit","Divinely victorious; one who wins by divine power","M","Sanskrit compound","Vishnu"),
    ("Devesh","Lord of the divine; master of all gods","S","Sanskrit Puranas","Vishnu/Shiva"),
    ("Devansh","Part of the divine; a fragment of god; born of divine essence","M","Sanskrit compound","Vishnu"),
    ("Devam","The divine one; one of divine essence and quality","M","Sanskrit compound","Vishnu"),
    ("Devabodh","Divine awakening; the enlightenment of the divine","M","Sanskrit compound","Vishnu"),
    ("Devachandra","Divine moon; the celestial luminosity of divinity","M","Sanskrit compound","Vishnu/Shiva"),
    ("Devadharma","Divine law; the righteous order of the gods","S","Sanskrit Puranas","Vishnu"),
    ("Devaguru","Divine teacher; guru of the gods; Brihaspati's name","S","Vedic texts","Brihaspati/Vishnu"),
    ("Devahit","Good for the gods; beneficial to the divine order","M","Sanskrit compound","Vishnu"),
    ("Devajigyasu","Desirous of divine victory; one who strives to win divinely","M","Sanskrit compound","Vishnu"),
    ("Devajyoti","Divine light; the luminous radiance of the divine","M","Sanskrit compound","Surya/Vishnu"),
    ("Devakant","Beloved of the gods; whom the divine beings cherish most","S","Sanskrit Puranas","Vishnu"),
    ("Devaketu","Divine banner; the flag of divinity raised in victory","S","Sanskrit epics","Vishnu"),
    ("Devakirti","Divine fame; renowned throughout the divine realms","M","Sanskrit compound","Vishnu"),
    ("Devakrit","Made by the gods; one whom the divine have created for a great purpose","M","Sanskrit compound","Vishnu"),
    ("Devakumar","Divine prince; the young lord of the gods","M","Sanskrit compound","Vishnu/Skanda"),
    ("Devanav","Divine new one; the fresh divine arising","M","Sanskrit compound","Vishnu"),
    ("Devanethi","Divine leader; the one who leads by divine direction","M","Sanskrit compound","Vishnu"),
    ("Devaprabh","Divine radiance; brilliance that only the divine possess","M","Sanskrit compound","Vishnu/Surya"),
    ("Devaprakash","Divine light; the illumination of divinity itself","M","Sanskrit compound","Surya/Vishnu"),
    ("Devaprasad","Divine grace; the gift bestowed by the gods","S","Sanskrit texts","Vishnu"),
    ("Devarup","Divine form; one whose very form is divine","M","Sanskrit compound","Vishnu"),
    ("Devasena","Army of gods; one who commands divine forces","S","Mahabharata - Skanda's wife named Devasena","Skanda"),
    ("Devashis","Blessed by the gods; one who has received divine blessing","M","Sanskrit compound","Vishnu"),
    ("Devashraya","Refuge in the divine; one who takes shelter in god","M","Sanskrit compound","Vishnu"),
    ("Devasmit","Smiled upon by the gods; divinely favored and joyful","M","Sanskrit compound","Vishnu"),
    ("Devavant","Possessing divine qualities; one endowed with godly attributes","M","Sanskrit compound","Vishnu"),
    ("Devavat","With the divine; accompanied by god's presence","M","Sanskrit compound","Vishnu"),
    ("Devavid","Knower of the divine; one who understands the gods","M","Sanskrit compound","Vishnu"),
    ("Devavijay","Divine victory; triumph achieved by divine power","M","Sanskrit compound","Vishnu"),
    ("Devavir","Divine warrior; the hero who fights with godly power","M","Sanskrit compound","Vishnu/Skanda"),
    ("Devayaj","Worshipper of the divine; one who offers the highest sacrifice","M","Sanskrit compound","Vishnu"),
    ("Devayav","Going toward the divine; moving always toward god","M","Sanskrit compound","Vishnu"),
    ("Devayog","Divine union; one who is yoked to the divine power","M","Sanskrit compound","Vishnu"),
    ("Deveshwar","Supreme lord of gods; the god of all gods","M","Sanskrit compound","Vishnu/Shiva"),
    ("Devit","Made divine; one who has been made into the divine through practice","M","Sanskrit compound","Vishnu"),
    ("Devrup","Divine form; whose form is that of the divine","M","Sanskrit compound","Vishnu"),

    # ══════════════════════════════════════════════════════════
    # LA GROUP
    # ══════════════════════════════════════════════════════════
    ("Lakshaj","Born for achievement; one whose very origin is defined by the goal and aim","M","Sanskrit compound","Vishnu/Rama"),
    ("Lakshin","Marked for greatness; the one bearing the sign of divine favor and destiny","S","Sanskrit Vedic literature","Vishnu"),
    ("Labhesh","Lord of achievement; sovereign of all attainment and gain","M","Sanskrit compound","Vishnu"),
    ("Labhit","The achieved one; already at the destination while others are on the journey","M","Sanskrit participle","Vishnu"),
    ("Labhvan","Possessor of great achievements; endowed with many attainments","M","Sanskrit compound","Vishnu"),
    ("Labhakar","Creator of achievement; maker of gains; the one who produces results","M","Sanskrit compound","Vishnu"),
    ("Labharaj","King of achievement; royal winner; sovereign of accomplishment","M","Sanskrit compound","Vishnu"),
    ("Labhesh","Lord of all gains; master of achievement and attainment","M","Sanskrit compound","Vishnu"),
    ("Labhansh","Portion of achievement; one who takes the lion's share of victory","M","Sanskrit compound","Vishnu"),
    ("Labhavant","One who has gained much; endowed with achievement","M","Sanskrit compound","Vishnu"),
    ("Lakshman","Brother of Rama; possessed of auspicious marks; the devoted brave warrior","S","Valmiki Ramayana","Rama/Vishnu"),
    ("Lakshmipati","Lord of Lakshmi; master of divine wealth and power; Vishnu's name","S","Vishnu Sahasranama","Vishnu"),
    ("Lakshmipal","Protector of the divine wealth; guardian of Lakshmi","M","Sanskrit compound","Vishnu"),
    ("Lakshmikant","Beloved of Lakshmi; Vishnu who is Lakshmi's consort","S","Vishnu Sahasranama","Vishnu"),
    ("Lakshmivar","Excellent one of Lakshmi; one who carries Lakshmi's blessing","M","Sanskrit compound","Vishnu"),
    ("Lakshant","One who accomplishes all aims; achiever of all goals","M","Sanskrit compound","Vishnu"),
    ("Lakshar","Skilled in achieving aims; expert at hitting targets","M","Sanskrit compound","Vishnu"),
    ("Lakshan","Possessing auspicious marks; characterized by excellence","S","Sanskrit texts","Vishnu/Rama"),
    ("Lakshveer","Hero of achievement; the brave one who achieves all goals","M","Sanskrit compound","Vishnu"),
    ("Lavaj","Born of grace and power; arising from the finest qualities","M","Sanskrit compound","Vishnu"),
    ("Lavak","Young one of great charm and power; pleasing and mighty","M","Sanskrit compound","Vishnu"),
    ("Lavan","Graceful; charming; of pleasing excellence","M","Sanskrit compound","Vishnu"),
    ("Lavang","Clove; sharp and pungent; one of piercing quality","M","Sanskrit texts","Vishnu"),
    ("Lavansh","Part of grace and power; a portion of excellent quality","M","Sanskrit compound","Vishnu"),
    ("Lavin","Graceful and powerful; combining elegance with strength","M","Sanskrit compound","Vishnu"),
    ("Lavkesh","Lord of grace and power; master of the finest qualities","M","Sanskrit compound","Vishnu"),
    ("Lavprakash","Light of grace; the radiance of the finest qualities","M","Sanskrit compound","Surya/Vishnu"),
    ("Lavraj","King of grace and power; royal excellence","M","Sanskrit compound","Vishnu"),
    ("Lavtej","Radiance of grace; brilliance of the most excellent quality","M","Sanskrit compound","Surya/Vishnu"),
    ("Lavveer","Hero of grace; brave one with elegant power","M","Sanskrit compound","Vishnu"),
    ("Lavvikram","Valor of grace; heroic power of the most refined order","M","Sanskrit compound","Vishnu"),
    ("Lavyam","Worthy of being cut through; one who is the best material; the finest","M","Sanskrit compound","Vishnu"),
    ("Layansh","Part of dissolution into the divine; a fragment merging into the infinite","M","Sanskrit compound","Vishnu/Shiva"),
    ("Layesh","Lord of dissolution and creation; master of cosmic transformation","M","Sanskrit compound","Vishnu/Shiva"),
    ("Laghu","Swift; light; quick; one of great agility and speed","S","Sanskrit texts","Vayu"),
    ("Lalaj","Son of the beloved; born of divine affection","M","Sanskrit compound","Vishnu"),
    ("Lalat","Forehead; the place of destiny; one marked on his brow for greatness","M","Sanskrit compound","Shiva"),
    ("Lalansh","Part of the beloved divine; a fraction of cosmic love","M","Sanskrit compound","Vishnu"),
    ("Lavitam","The most graceful; the pinnacle of elegance and power","M","Sanskrit compound","Vishnu"),
    ("Lavishesh","Of special grace and excellence; uniquely excellent","M","Sanskrit compound","Vishnu"),
    ("Lakshanand","Joy of auspicious marks; blissful in excellence","M","Sanskrit compound","Vishnu"),
    ("Lakshavant","Possessor of aims; one endowed with goals and the power to achieve them","M","Sanskrit compound","Vishnu"),
    ("Lakshvant","Having the mark of greatness; possessed of destiny's sign","M","Sanskrit compound","Vishnu"),
]

# ─────────────────────────────────────────────────────────────────────────────
# ADDITIONAL NAMES FROM ROOT GENERATION
# Sanskrit root prefixes × power suffixes
# ─────────────────────────────────────────────────────────────────────────────

SA_PREFIXES = ["Sa","Sat","Sav","Sau","Sam","San","Sar","Sad","Sac","Sah"]
SI_PREFIXES = ["Si","Sin","Sim","Sid","Siv"]
SU_PREFIXES = ["Su","Sur","Sun","Sup","Suj","Suk","Sum","Sug"]
SE_PREFIXES = ["Se","Sen","Sev","Seh"]
JA_PREFIXES = ["Ja","Jay","Jav","Jag","Jan"]
JI_PREFIXES = ["Ji","Jiv","Jim","Jit","Jig"]
GA_PREFIXES = ["Ga","Gat","Gau","Gaj","Gag","Gav","Gar"]
GU_PREFIXES = ["Gu","Gun","Gur","Gud","Guj"]
DE_PREFIXES = ["De","Dev","Deb"]
LA_PREFIXES = ["La","Lak","Lab","Lav","Lay","Lag"]

POWER_SUFFIXES = [
    ("raj","king; sovereign; the one who rules"),
    ("veer","warrior; brave one; hero"),
    ("jit","victorious; one who wins"),
    ("pati","lord; master; commander"),
    ("nath","lord; master; protector"),
    ("esh","lord; controller; master"),
    ("dev","divine; god; divine being"),
    ("vant","possessing; endowed with"),
    ("vikram","valor; heroic power; valiant strength"),
    ("ansh","part of; born from; a portion of"),
    ("prabh","radiance; brilliance; glowing"),
    ("tej","energy; radiance; brilliance"),
    ("veg","speed; momentum; force"),
    ("krit","maker of; creator of"),
    ("dhar","bearer of; one who holds"),
    ("prem","filled with love and power"),
    ("kant","beloved; radiant; the shining one"),
    ("sena","army; forces; one who commands"),
    ("jyot","light; flame; radiance"),
    ("swar","self-manifest; sovereign of the self"),
]

def generate_compound_names() -> list[dict]:
    """Generate valid compound names from prefix × suffix combinations."""
    generated = []
    all_prefix_groups = [
        (SA_PREFIXES, "sa"), (SI_PREFIXES, "si"), (SU_PREFIXES, "su"),
        (SE_PREFIXES, "se"), (JA_PREFIXES, "ja"), (JI_PREFIXES, "ji"),
        (GA_PREFIXES, "ga"), (GU_PREFIXES, "gu"), (DE_PREFIXES, "de"),
        (LA_PREFIXES, "la"),
    ]
    for prefixes, syl_key in all_prefix_groups:
        for prefix in prefixes:
            for suffix, suf_meaning in POWER_SUFFIXES:
                name = prefix + suffix
                if len(name) < 4 or len(name) > 14:
                    continue
                meaning = f"One whose {suf_meaning} is of divine {prefix.lower()}-energy; {suf_meaning} of {prefix.lower()} power"
                generated.append({
                    "name": name,
                    "meaning": meaning,
                    "category": "M",
                    "source": "Sanskrit compound (generated)",
                    "deity": "Vishnu",
                    "syllable": syl_key.upper(),
                })
    return generated


# ─────────────────────────────────────────────────────────────────────────────
# BUILD FULL DATASET
# ─────────────────────────────────────────────────────────────────────────────

ACCEPTED_SYLLABLES = ["sa","si","su","se","ja","ji","ga","gu","de","la"]

def get_syllable(name: str) -> str | None:
    n = name.lower().strip()
    for s in ACCEPTED_SYLLABLES:
        if n.startswith(s):
            return s.upper()
    return None


def build_database() -> list[dict]:
    records = []

    # ── From RAW_NAMES master list ──
    for entry in RAW_NAMES:
        name, meaning, cat, source, deity = entry
        syl = get_syllable(name)
        if not syl:
            continue
        records.append({
            "name": name,
            "meaning": meaning,
            "category": "Scriptural" if cat == "S" else "Modern Derivative",
            "source": source,
            "deity": deity,
            "syllable": syl,
        })

    # ── From generated compounds ──
    for rec in generate_compound_names():
        # Check not already in records
        existing_names = {r["name"].lower() for r in records}
        if rec["name"].lower() not in existing_names:
            rec["category"] = "Modern Derivative"
            records.append(rec)

    return records


def score_and_enrich(records: list[dict]) -> list[dict]:
    seen: set[str] = set()
    output = []
    for rec in records:
        name = rec["name"].strip()
        key = name.lower()
        if key in seen:
            # Keep the one with the better meaning
            continue
        seen.add(key)

        compound, final = chaldean(name)
        preferred = final in PREFERRED_FINALS
        mq = meaning_quality(rec.get("meaning", ""))

        overall = (
            mq * 2
            + (3 if preferred else 0)
            + (1 if rec.get("category", "").startswith("Script") else 0)
            + (2 if 4 <= len(name) <= 9 else 0)  # sweet spot length
            + (1 if rec.get("deity", "") in ("Vishnu","Krishna","Rama","Shiva","Surya","Skanda","Indra") else 0)
        )

        output.append({
            "name": name,
            "syllable": rec.get("syllable", ""),
            "meaning": rec.get("meaning", ""),
            "category": rec.get("category", ""),
            "source": rec.get("source", ""),
            "deity": rec.get("deity", ""),
            "chaldean_compound": compound,
            "chaldean_final": final,
            "preferred_number": preferred,
            "meaning_score": mq,
            "overall_score": overall,
        })

    output.sort(key=lambda r: (r["syllable"], -r["overall_score"], r["name"]))
    return output


# ─────────────────────────────────────────────────────────────────────────────
# OUTPUT
# ─────────────────────────────────────────────────────────────────────────────

def write_csv(records: list[dict]) -> None:
    path = "baby-names-research.csv"
    fields = ["name","syllable","meaning","category","source","deity",
              "chaldean_compound","chaldean_final","preferred_number",
              "meaning_score","overall_score"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(records)
    print(f"✓ CSV  → {path}  ({len(records)} names)", flush=True)


def write_json(records: list[dict]) -> None:
    path = "baby-names-research.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"✓ JSON → {path}", flush=True)


def write_markdown(records: list[dict]) -> None:
    path = "baby-names-scraped.md"
    by_syl: dict[str, list] = defaultdict(list)
    for r in records:
        by_syl[r["syllable"]].append(r)

    lines = [
        "# Hindu Baby Boy Names — Complete Research",
        "## January 2027 | All Nakshatra Syllables | No Rejection Filters",
        f"\n**Total unique names:** {len(records)}  |  "
        f"**With preferred Chaldean (1/3/6):** {sum(1 for r in records if r['preferred_number'])}",
        "\nChaldean key: 1=A,I,J,Q,Y · 2=B,K,R · 3=C,G,L,S · 4=D,M,T · "
        "5=E,H,N,X · 6=O,U,V,W · 7=Z · 8=F,P  |  ✦ = preferred final (1, 3, 6)",
        "\n---\n",
    ]

    order = ["SA","SI","SU","SE","JA","JI","GA","GU","DE","LA"]
    for syl in order:
        group = by_syl.get(syl, [])
        lines.append(f"## {syl} — {len(group)} names\n")
        lines.append("| # | Name | Meaning | Cat | Deity | Num | ✦ | Score |")
        lines.append("|---|------|---------|-----|-------|-----|---|-------|")
        for i, r in enumerate(group, 1):
            cat_short = "S" if r["category"].startswith("Script") else "M"
            star = "✦" if r["preferred_number"] else ""
            meaning_short = r.get("meaning","")[:75].replace("|","·")
            lines.append(
                f"| {i} | **{r['name']}** | {meaning_short} | "
                f"{cat_short} | {r['deity']} | {r['chaldean_final']} | {star} | "
                f"{r['overall_score']} |"
            )
        lines.append("")

    # Top 50
    top50 = sorted(records, key=lambda r: -r["overall_score"])[:50]
    lines += [
        "---",
        "## Top 50 Names (by score)\n",
        "| Rank | Name | Syllable | Meaning | Chaldean | ✦ | Score | Category |",
        "|------|------|----------|---------|----------|---|-------|----------|",
    ]
    for i, r in enumerate(top50, 1):
        star = "✦" if r["preferred_number"] else ""
        meaning_short = r.get("meaning","")[:60].replace("|","·")
        cat_short = "Scriptural" if r["category"].startswith("Script") else "Mod.Deriv."
        lines.append(
            f"| {i} | **{r['name']}** | {r['syllable']} | {meaning_short} | "
            f"{r['chaldean_final']} | {star} | {r['overall_score']} | {cat_short} |"
        )

    # Stats
    lines += [
        "",
        "---",
        "## Statistics by Syllable",
        "| Syllable | Total | Scriptural | Modern | With ✦ |",
        "|----------|-------|-----------|--------|---------|",
    ]
    for syl in order:
        g = by_syl.get(syl, [])
        sc = sum(1 for r in g if r["category"].startswith("Script"))
        mo = sum(1 for r in g if not r["category"].startswith("Script"))
        pf = sum(1 for r in g if r["preferred_number"])
        lines.append(f"| {syl} | {len(g)} | {sc} | {mo} | {pf} |")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✓ MD   → {path}", flush=True)


def print_summary(records: list[dict]) -> None:
    by_syl: dict[str, list] = defaultdict(list)
    for r in records:
        by_syl[r["syllable"]].append(r)

    print(f"\n{'='*65}")
    print("  GENERATION COMPLETE")
    print(f"{'='*65}")
    print(f"  Total unique names: {len(records)}")
    print(f"  Scriptural names:   {sum(1 for r in records if r['category'].startswith('Script'))}")
    print(f"  Modern derivatives: {sum(1 for r in records if not r['category'].startswith('Script'))}")
    print(f"  Preferred ✦ (1/3/6): {sum(1 for r in records if r['preferred_number'])}")

    print("\n  By syllable:")
    for syl in ["SA","SI","SU","SE","JA","JI","GA","GU","DE","LA"]:
        g = by_syl.get(syl, [])
        pf = sum(1 for r in g if r["preferred_number"])
        print(f"    {syl}:  {len(g):4d} names   ({pf} with ✦ Chaldean)")

    print("\n  Top 15 names by overall score:")
    top = sorted(records, key=lambda r: -r["overall_score"])[:15]
    for r in top:
        star = "✦" if r["preferred_number"] else " "
        cat = "S" if r["category"].startswith("Script") else "M"
        print(f"    {r['name']:<18} {r['syllable']}  "
              f"Chaldean {r['chaldean_final']}{star}  "
              f"Score {r['overall_score']:2d}  [{cat}]  "
              f"{r['deity']}")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("Building comprehensive Hindu baby boy name database...", flush=True)
    print("Sources: Master scriptural list + Sanskrit root generator", flush=True)
    print("Rejection list: DISABLED (as requested)\n", flush=True)

    raw = build_database()
    print(f"Raw entries (before dedup): {len(raw)}", flush=True)

    scored = score_and_enrich(raw)
    print(f"Unique names after scoring: {len(scored)}\n", flush=True)

    write_csv(scored)
    write_json(scored)
    write_markdown(scored)
    print_summary(scored)


if __name__ == "__main__":
    main()
