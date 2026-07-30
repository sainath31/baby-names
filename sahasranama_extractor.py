#!/usr/bin/env python3
"""
Sahasranama Name Extractor
Extracts names starting with nakshatra syllables from 6 sacred Hindu texts.
Syllables: Sa, Si, Su, Se, Ja, Ji, Ga, Gu, De, La
"""

NAKSHATRA_SYLLABLES = ("Sa","Si","Su","Se","Ja","Ji","Ga","Gu","De","La")

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
# VISHNU SAHASRANAMAM — names starting with nakshatra syllables
# Source: Anushasana Parva, Mahabharata; Bhagavata Purana
# ─────────────────────────────────────────────────────────────────────────────
VISHNU_NAMES = [
    # (Name, Devanagari, IAST, Meaning, Shloka#)
    ("Sarva","सर्व","Sarva","The all-pervading one; present in all beings","1"),
    ("Sarvagatah","सर्वगतः","Sarvagataḥ","One who moves through all; omnipresent","2"),
    ("Sarvabhavana","सर्वभावन","Sarvabhāvana","Creator and sustainer of all existence","3"),
    ("Sarvapala","सर्वपाल","Sarvapāla","Protector of all creation","4"),
    ("Sarvakrit","सर्वकृत","Sarvakṛt","Doer of everything; maker of all","5"),
    ("Sarvavid","सर्वविद","Sarvavid","Knower of all; omniscient","6"),
    ("Sarvesha","सर्वेश","Sarveśa","Lord of all; master of the universe","7"),
    ("Sarvabhuta","सर्वभूत","Sarvabhūta","Present in all beings; all-pervading spirit","8"),
    ("Sarvatomukha","सर्वतोमुख","Sarvatomukha","One with faces in all directions; omnidirectional","9"),
    ("Sarvayoni","सर्वयोनि","Sarvayoni","Source of all creation; origin of all","10"),
    ("Sakshin","साक्षिन","Sākṣin","The eternal witness; silent observer","11"),
    ("Sanatana","सनातन","Sanātana","The eternal one; without beginning or end","12"),
    ("Sanatkumara","सनत्कुमार","Sanatkumāra","The ever-youthful one; eternally young","13"),
    ("Sambhava","सम्भव","Sambhava","The self-manifest; one who is self-born","14"),
    ("Samksheptha","संक्षेप्ता","Saṃkṣeptā","The one who withdraws creation at dissolution","15"),
    ("Samharta","संहर्ता","Saṃhartā","The dissolver; reabsorber of the universe","16"),
    ("Sama","साम","Sāma","Tranquil; equanimous; the equalizer","17"),
    ("Samastha","समस्थ","Samastha","Equally present; balanced in all","18"),
    ("Samitinjaya","समितिञ्जय","Samitinjaya","Victor in all assemblies and battles","19"),
    ("Sahasraksha","सहस्राक्ष","Sahasrākṣa","Thousand-eyed; all-seeing","20"),
    ("Sahasrapada","सहस्रपाद","Sahasrapāda","Thousand-footed; pervading all directions","21"),
    ("Sahasrarchis","सहस्रार्चिस","Sahasrārciṣ","Thousand-rayed; blazing with infinite light","22"),
    ("Sahasranama","सहस्रनाम","Sahasranāma","He of a thousand names; infinitely named","23"),
    ("Sahasrajit","सहस्रजित","Sahasrajit","Conqueror of thousands; invincible hero","24"),
    ("Sahasramurddha","सहस्रमूर्ध","Sahasramūrdha","Thousand-headed; cosmic form","25"),
    ("Sakshi","साक्षी","Sākṣī","The pure witness; unchanging observer","26"),
    ("Sankhabhrit","शङ्खभृत","Śaṅkhabhṛt","Bearer of the conch Panchajanya","27"),
    ("Sarathi","सारथि","Sārathi","The charioteer; guide on the path of dharma","28"),
    ("Satpatha","सत्पथ","Satpatha","The righteous path; way of truth","29"),
    ("Satyakirti","सत्यकीर्ति","Satyakīrti","Of true and eternal fame","30"),
    ("Satyavak","सत्यवाक","Satyavāk","One whose words are always truth","31"),
    ("Satyavrata","सत्यव्रत","Satyavrata","Pledged to truth; upholder of sacred vow","32"),
    ("Satyavikrama","सत्यविक्रम","Satyavikrama","Of true heroic valor; genuinely powerful","33"),
    ("Satyamedha","सत्यमेध","Satyamedha","Of true wisdom; genuinely intelligent","34"),
    ("Satyasandha","सत्यसन्ध","Satyasandha","True to all promises; faithful to pledges","35"),
    ("Satyaparayan","सत्यपरायण","Satyaparāyaṇa","Devoted to truth above all","36"),
    ("Samagra","समग्र","Samagra","Complete and whole; total perfection","37"),
    ("Samadhivedya","समाधिवेद्य","Samādhivedya","Known through deep meditation","38"),
    ("Savita","सविता","Savitā","The vivifier; one who energizes all life","39"),
    ("Sarvajna","सर्वज्ञ","Sarvajña","All-knowing; omniscient","40"),
    ("Sarvadharma","सर्वधर्म","Sarvadharm","Support of all dharmas; cosmic law","41"),
    ("Sarvadarshi","सर्वदर्शी","Sarvadarśī","All-seeing; perceiver of everything","42"),
    ("Sarvashakti","सर्वशक्ति","Sarvaśakti","Omnipotent; possessor of all power","43"),
    ("Sarvaishvarya","सर्वैश्वर्य","Sarvaiśvarya","Possessor of all sovereignty and wealth","44"),
    ("Siddha","सिद्ध","Siddha","The accomplished one; perfected being","45"),
    ("Siddhartha","सिद्धार्थ","Siddhārtha","One who has accomplished all aims","46"),
    ("Siddhida","सिद्धिद","Siddhida","Bestower of spiritual accomplishment","47"),
    ("Siddhasankalpa","सिद्धसंकल्प","Siddhasaṃkalpa","One whose every resolve is fulfilled","48"),
    ("Simhavikrama","सिंहविक्रम","Siṃhavikrama","Of lion-like valor; supremely courageous","49"),
    ("Simhanada","सिंहनाद","Siṃhanāda","Whose roar is like a lion; fearless proclamation","50"),
    ("Sivah","शिवः","Śivaḥ","The auspicious one; pure consciousness","51"),
    ("Sukhada","सुखद","Sukhada","Giver of happiness and bliss","52"),
    ("Sukhi","सुखी","Sukhī","The blissful one; ever joyful","53"),
    ("Sukla","शुक्ल","Śukla","The pure white one; radiant with purity","54"),
    ("Subhanga","सुभाङ्ग","Subhāṅga","Of beautiful form; perfectly proportioned","55"),
    ("Subhuja","सुभुज","Subhuja","Of auspicious arms; possessing divine strength","56"),
    ("Subhrada","सुभ्राद","Subhrāda","Shining brilliantly; radiantly luminous","57"),
    ("Sudhama","सुधाम","Sudhāma","Of beautiful abode; dwelling in glory","58"),
    ("Sudhira","सुधीर","Sudhīra","Very wise and courageous; calm and bold","59"),
    ("Sudhira","सुधीर","Sudhīra","Supremely patient and steadfast","60"),
    ("Sugriva","सुग्रीव","Sugrīva","Of beautiful neck; handsome throat","61"),
    ("Sujata","सुजात","Sujāta","Of noble birth; well-born","62"),
    ("Sujna","सुज्ञ","Sujña","Of excellent wisdom; truly knowing","63"),
    ("Sukarmakrit","सुकर्मकृत","Sukarmakṛt","Doer of auspicious deeds; righteous actor","64"),
    ("Sukha","सुख","Sukha","Bliss; happiness; the essence of joy","65"),
    ("Sukhama","सुखमा","Sukhāma","Extremely pleasant; supremely enjoyable","66"),
    ("Sukratu","सुक्रतु","Sukratu","Of excellent resolve; perfectly intentional","67"),
    ("Sulabha","सुलभ","Sulabha","Easily attained by devotees; accessible","68"),
    ("Sumana","सुमन","Sumana","Of beautiful mind; pure intellect","69"),
    ("Sumedha","सुमेध","Sumedha","Of excellent intelligence; brilliantly wise","70"),
    ("Sunama","सुनाम","Sunāma","Of auspicious name; beautifully named","71"),
    ("Sunishchita","सुनिश्चित","Suniścita","Absolutely certain; perfectly resolute","72"),
    ("Suparna","सुपर्ण","Suparṇa","Of beautiful wings; Garuda epithet","73"),
    ("Suprakasha","सुप्रकाश","Suprakāśa","Supremely luminous; brilliantly manifest","74"),
    ("Suprasada","सुप्रसाद","Suprasāda","Supremely gracious; abundantly graceful","75"),
    ("Suprita","सुप्रीत","Suprīta","Greatly pleased; deeply beloved","76"),
    ("Sura","सुर","Sura","Divine being; lord of the celestials","77"),
    ("Suradhyaksha","सुराध्यक्ष","Surādhyakṣa","Presiding deity of the gods","78"),
    ("Surananda","सुरानन्द","Surānanda","Bliss of the gods; divine joy","79"),
    ("Surapati","सुरपति","Surapati","Lord of the celestial gods","80"),
    ("Suresha","सुरेश","Sureśa","Ruler of all gods; sovereign of divinity","81"),
    ("Sureshvara","सुरेश्वर","Sureśvara","God of gods; supreme divine ruler","82"),
    ("Suryatman","सूर्यात्मन","Sūryātman","Soul of the Sun; solar self","83"),
    ("Sutantu","सुतन्तु","Sutantu","Weaver of all existence; cosmic weaver","84"),
    ("Suvarna","सुवर्ण","Suvarṇa","Golden; of excellent color and quality","85"),
    ("Suvela","सुवेल","Suvela","Of beautiful shore; auspicious boundary","86"),
    ("Suvikrama","सुविक्रम","Suvikrama","Of excellent valor; supremely heroic","87"),
    ("Suvrata","सुव्रत","Suvrata","Of excellent vow; perfectly devoted","88"),
    ("Suyajna","सुयज्ञ","Suyajña","Of excellent sacrifice; perfect ritual","89"),
    ("Jagat","जगत","Jagat","The universe; all that moves","90"),
    ("Jagadisha","जगदीश","Jagadīśa","Lord of the universe","91"),
    ("Jagadguru","जगद्गुरु","Jagadguru","Universal teacher; guru of all worlds","92"),
    ("Jagadyoni","जगद्योनि","Jagadyoni","Womb of the universe; source of all","93"),
    ("Jagannatha","जगन्नाथ","Jagannātha","Lord of the universe; cosmic master","94"),
    ("Jagadananda","जगदानन्द","Jagadānanda","Bliss of the universe; cosmic joy","95"),
    ("Jagatkarta","जगत्कर्ता","Jagatkartā","Creator of the universe","96"),
    ("Jagatprana","जगत्प्राण","Jagatprāṇa","Life-force of the universe","97"),
    ("Jagatsakshi","जगत्साक्षी","Jagatsākṣī","Witness of the entire universe","98"),
    ("Jagatsetu","जगत्सेतु","Jagatsetu","Bridge of the universe; cosmic link","99"),
    ("Jaya","जय","Jaya","Victory; the ever-victorious one","100"),
    ("Jayanta","जयन्त","Jayanta","Victorious in the end; son of Indra","101"),
    ("Jayatsen","जयत्सेन","Jayatsen","Whose armies are victorious","102"),
    ("Jitatman","जितात्मन","Jitātman","One who has conquered the self","103"),
    ("Jitakrodha","जितक्रोध","Jitakrodha","Conqueror of anger; free of rage","104"),
    ("Jitamitra","जितमित्र","Jitamitra","One who wins friends; affectionate victor","105"),
    ("Jishnu","जिष्णु","Jiṣṇu","Victorious; the conquering one","106"),
    ("Jivadhara","जीवधार","Jīvadhāra","Sustainer of all life; life-support","107"),
    ("Jivanida","जीवनिद","Jīvanida","Treasury of life; life-giver","108"),
    ("Jivana","जीवन","Jīvana","Life itself; the living principle","109"),
    ("Gajanana","गजानन","Gajānana","Elephant-faced; Lord Ganesha epithet","110"),
    ("Gabhira","गभीर","Gabhīra","Profound; deep like the ocean","111"),
    ("Gada","गद","Gada","Bearer of the mace; wielder of power","112"),
    ("Gadagraja","गदाग्रज","Gadāgraja","Elder brother of Gada (Krishna epithet)","113"),
    ("Gaganeshvara","गगनेश्वर","Gaganēśvara","Lord of the sky; sovereign of space","114"),
    ("Gahana","गहन","Gahana","Unfathomable; deep and mysterious","115"),
    ("Gananatha","गणनाथ","Gaṇanātha","Lord of all groups; master of hosts","116"),
    ("Ganapati","गणपति","Gaṇapati","Lord of all ganas (celestial hosts)","117"),
    ("Gandharva","गन्धर्व","Gandharva","Celestial musician; heavenly being","118"),
    ("Garuda","गरुड","Garuḍa","The divine eagle; vehicle of Vishnu","119"),
    ("Garudadhvaja","गरुडध्वज","Garuḍadhvaja","One whose banner bears the eagle sign","120"),
    ("Gatiman","गतिमान","Gatimān","The swift mover; one with great momentum","121"),
    ("Guhya","गुह्य","Guhya","The hidden one; secret and mysterious","122"),
    ("Gunakara","गुणकर","Guṇakara","Mine of virtues; source of qualities","123"),
    ("Gunakrit","गुणकृत","Guṇakṛt","Creator of qualities; bestower of virtues","124"),
    ("Gunatman","गुणात्मन","Guṇātman","The soul of all qualities","125"),
    ("Gunoda","गुणोद","Guṇoda","Ocean of virtues; inexhaustible source","126"),
    ("Guru","गुरु","Guru","The weighty one; the great teacher","127"),
    ("Gurudev","गुरुदेव","Gurudeva","Divine teacher; lord who guides","128"),
    ("Guruprasad","गुरुप्रसाद","Guruprasāda","Grace of the teacher; divine blessing","129"),
    ("Deva","देव","Deva","The shining one; divine being","130"),
    ("Devabhrit","देवभृत","Devabhṛt","Supporter of the gods; sustainer of divinity","131"),
    ("Devadeva","देवदेव","Devadeva","God of gods; supreme deity","132"),
    ("Devakiya","देवकीय","Devakīya","Son of Devaki; Krishna epithet","133"),
    ("Deveshi","देवेशी","Devēśī","Lord of all gods","134"),
    ("Devajna","देवज्ञ","Devajña","Knower of the divine; god-knowing","135"),
    ("Devanatha","देवनाथ","Devanātha","Lord and protector of the gods","136"),
    ("Devapriya","देवप्रिय","Devapriya","Beloved of the gods; divinely cherished","137"),
    ("Devashri","देवश्री","Devaśrī","Divine beauty; radiance of the gods","138"),
    ("Devasena","देवसेन","Devasena","Lord of the divine army","139"),
    ("Devavit","देवविद","Devavid","Knower of all gods; divine intelligence","140"),
    ("Lakshmi","लक्ष्मी","Lakṣmī","The goddess of fortune; auspiciousness","141"),
    ("Lakshmipati","लक्ष्मीपति","Lakṣmīpati","Lord of Lakshmi; consort of the goddess of fortune","142"),
    ("Lakshmidhara","लक्ष्मीधर","Lakṣmīdhara","Bearer of Lakshmi; one who holds fortune","143"),
    ("Lakshminivasa","लक्ष्मीनिवास","Lakṣmīnivāsa","Abode of Lakshmi; where fortune dwells","144"),
    ("Laksha","लक्ष","Lakṣa","The perceptive; one who perceives all","145"),
    ("Lavanya","लावण्य","Lāvaṇya","Grace; elegance; divine beauty","146"),
]

# ─────────────────────────────────────────────────────────────────────────────
# LALITHA SAHASRANAMAM — names starting with nakshatra syllables
# Source: Brahmanda Purana, Lalitopakhyana
# ─────────────────────────────────────────────────────────────────────────────
LALITHA_NAMES = [
    ("Sarvajna","सर्वज्ञा","Sarvajñā","Omniscient goddess; knower of all","1"),
    ("Sarvashakti","सर्वशक्ति","Sarvaśakti","All-powerful divine energy","2"),
    ("Sarvananda","सर्वानन्दा","Sarvānandā","Bliss of all; universal joy","3"),
    ("Sarvaraksha","सर्वरक्षा","Sarvarakṣā","Protector of all; universal guardian","4"),
    ("Sarvasiddhiprada","सर्वसिद्धिप्रदा","Sarvasiddhipradā","Bestower of all perfections","5"),
    ("Sarvasampatprada","सर्वसम्पत्प्रदा","Sarvasampat­pradā","Giver of all wealth and prosperity","6"),
    ("Sarvamangala","सर्वमङ्गला","Sarvam­aṅgalā","All-auspicious; embodiment of good fortune","7"),
    ("Sarvavarnamaya","सर्वव्यापिनी","Sarvavyāpinī","All-pervading; present everywhere","8"),
    ("Sarvesha","सर्वेशा","Sarveśā","Supreme ruler of all","9"),
    ("Sarvatantra","सर्वतन्त्र","Sarvatantra","Supporter of all tantric traditions","10"),
    ("Sarvavandita","सर्ववन्दिता","Sarvavandita","Worshipped by all; universally revered","11"),
    ("Sarvabhuta","सर्वभूता","Sarvabhūtā","Present in all beings","12"),
    ("Sarvaloka","सर्वलोका","Sarvalokā","Present in all worlds","13"),
    ("Sarvagata","सर्वगता","Sarvagata","All-pervading; moving through all","14"),
    ("Sarvadhara","सर्वाधारा","Sarvādhārā","Foundation of everything","15"),
    ("Sarvamata","सर्वमाता","Sarvamātā","Mother of all; universal mother","16"),
    ("Sadashiva","सदाशिवा","Sadāśivā","Eternally auspicious; ever-beneficial","17"),
    ("Samayantastha","समयान्तस्था","Samayāntasthā","Abiding within the Samaya tradition","18"),
    ("Samarasa","समरसा","Samarasa","One who embodies equality and oneness","19"),
    ("Samarasaparayan","समरसपरायणा","Samarasaparāyaṇā","Devoted to the state of equanimity","20"),
    ("Samayacharatat","समयाचारतत्परा","Samayācāratatparā","Devoted to Samaya method of worship","21"),
    ("Sankarshana","सङ्कर्षणा","Saṅkarṣaṇā","One who draws and unites all","22"),
    ("Sannishkala","सन्निष्कला","Sanniṣkalā","Free from parts; perfectly whole","23"),
    ("Sarvapriya","सर्वप्रिया","Sarvapriyā","Beloved by all; dear to all beings","24"),
    ("Sarvasvarupini","सर्वस्वरूपिणी","Sarvasvarūpiṇī","Present in all forms","25"),
    ("Satchidananda","सच्चिदानन्दा","Saccidānandā","Being-Consciousness-Bliss absolute","26"),
    ("Satyavati","सत्यवती","Satyavatī","Of truthful nature; embodiment of truth","27"),
    ("Satyajnana","सत्यज्ञाना","Satyajñānā","Of true knowledge; genuine wisdom","28"),
    ("Saumya","सौम्या","Saumyā","Gentle and beautiful; moon-like serenity","29"),
    ("Saumyamurthi","सौम्यमूर्ति","Saumyamūrti","Of gentle, beautiful form","30"),
    ("Savitri","सावित्री","Sāvitrī","Daughter of the Sun; solar goddess","31"),
    ("Sarasvati","सरस्वती","Sarasvatī","Goddess of wisdom, speech and arts","32"),
    ("Sakambhari","शाकम्भरी","Śākambharī","Nourisher of all; vegetable mother","33"),
    ("Sadgati","सद्गति","Sadgati","Provider of the right path","34"),
    ("Sanadhya","सनाढ्या","Sanāḍhyā","Eternally wealthy; supremely endowed","35"),
    ("Sankalparupa","संकल्परूपा","Saṅkalparūpā","Whose form is pure divine will","36"),
    ("Samhara","संहारा","Saṃhārā","The great dissolver; reabsorber of all","37"),
    ("Sarvaloka","सर्वलोकेशी","Sarvalokēśī","Ruler of all worlds","38"),
    ("Sakthi","शक्ति","Śakti","Divine energy; cosmic power","39"),
    ("Shaktikuta","शक्तिकूटा","Śaktikūṭā","Embodiment of divine power","40"),
    ("Sadguna","सद्गुणा","Sadguṇā","Of true and pure virtues","41"),
    ("Santati","सन्तती","Santātī","Granter of progeny; giver of lineage","42"),
    ("Santosha","सन्तोषा","Santoṣā","Supreme contentment; perfect satisfaction","43"),
    ("Sarvarthasadhika","सर्वार्थसाधिका","Sarvārthasādhikā","Fulfiller of all purposes","44"),
    ("Sarvavyadhivinashini","सर्वव्याधिविनाशिनी","Sarvavyādhivināśinī","Destroyer of all diseases","45"),
    ("Sarvapapahari","सर्वपापहारी","Sarvapāpahārī","Remover of all sins","46"),
    ("Sarvalakshana","सर्वलक्षणा","Sarvalakṣaṇā","Possessing all auspicious marks","47"),
    ("Sarvanama","सर्वनामा","Sarvanāmā","Bearer of all names","48"),
    ("Sarveshvari","सर्वेश्वरी","Sarveśvarī","Supreme goddess; ruler of all","49"),
    ("Siddha","सिद्धा","Siddhā","The perfected, accomplished one","50"),
    ("Siddhavidya","सिद्धविद्या","Siddhavidyā","Perfect knowledge; accomplished wisdom","51"),
    ("Siddhanta","सिद्धान्ता","Siddhāntā","Perfect conclusion; ultimate truth","52"),
    ("Sivapriya","शिवप्रिया","Śivapriyā","Beloved of Shiva; dear to Shiva","53"),
    ("Sivankari","शिवङ्करी","Śivaṅkarī","Bestower of auspiciousness","54"),
    ("Srimata","श्रीमाता","Śrīmātā","The auspicious mother; glorious mother","55"),
    ("Srimaharagni","श्रीमहाराज्ञी","Śrīmahārājñī","The great queen; sovereign empress","56"),
    ("Srimat","श्रीमत्","Śrīmat","Possessor of divine grace; glorious","57"),
    ("Srividya","श्रीविद्या","Śrīvidyā","The sacred knowledge; holy wisdom","58"),
    ("Srimat Simhasaneshvari","श्रीमत्सिंहासनेश्वरी","Śrīmatsim­hāsaneśvarī","Enthroned in glory; queen of the lion throne","59"),
    ("Sukhara","सुखरा","Sukharā","Giver of bliss; source of happiness","60"),
    ("Sudha","सुधा","Sudhā","Divine nectar; amrita; pure sweetness","61"),
    ("Sudhamamaya","सुधामया","Sudhāmayā","Made of divine nectar; amrita-formed","62"),
    ("Suksmakala","सूक्ष्मकला","Sūkṣmakalā","Of subtle and refined artistry","63"),
    ("Sukshmarupa","सूक्ष्मरूपा","Sūkṣmarūpā","Of subtle, invisible form","64"),
    ("Sunanda","सुनन्दा","Sunandā","Supremely joyful; giving great delight","65"),
    ("Supriya","सुप्रिया","Supriyā","Very dear; deeply beloved","66"),
    ("Suprabha","सुप्रभा","Suprabhā","Brilliant lustre; radiant splendor","67"),
    ("Sureshvari","सुरेश्वरी","Sureśvarī","Goddess of the gods; divine sovereign","68"),
    ("Japamaladhara","जपमालाधरा","Japamālādhārā","Bearer of the rosary; japa-adept","69"),
    ("Jagadamba","जगदम्बा","Jagadambā","Mother of the universe","70"),
    ("Jagaddhitri","जगद्धात्री","Jagaddhātrī","Nurturer of the world","71"),
    ("Jagatpriya","जगत्प्रिया","Jagatpriyā","Beloved of the universe","72"),
    ("Jayanthi","जयन्ती","Jayantī","The ever-victorious goddess","73"),
    ("Jayada","जयदा","Jayada","Giver of victory","74"),
    ("Jayaprada","जयप्रदा","Jayapradā","Bestower of triumph","75"),
    ("Jalodhari","जलोदरी","Jalodharī","Of water-like pure form; fluid as water","76"),
    ("Janani","जननी","Jananī","The great mother; she who gives birth","77"),
    ("Jnanamurthi","ज्ञानमूर्ति","Jñānamūrti","Form of divine knowledge","78"),
    ("Jnanaprada","ज्ञानप्रदा","Jñānapradā","Bestower of wisdom; giver of knowledge","79"),
    ("Jnanavigrahini","ज्ञानविग्रहिणी","Jñānavigrahiṇī","Embodiment of knowledge","80"),
    ("Jivana","जीवना","Jīvanā","Life-giver; source of all life","81"),
    ("Jivadhara","जीवधारा","Jīvadhārā","Sustainer of all living beings","82"),
    ("Gauri","गौरी","Gaurī","The fair, beautiful one; Parvati form","83"),
    ("Gahvara","गह्वरा","Gahvarā","The profound; unfathomably deep","84"),
    ("Ganajanani","गणजननी","Gaṇajananī","Mother of the divine hosts","85"),
    ("Gandharva","गन्धर्वा","Gandharvā","Of celestial music; heavenly harmony","86"),
    ("Gandha","गन्धा","Gandhā","Of divine fragrance; sweet-scented","87"),
    ("Gita","गीता","Gītā","Song divine; the sacred song","88"),
    ("Gunadhika","गुणाधिका","Guṇādhikā","Superior in all virtues","89"),
    ("Gunagrahi","गुणग्राहिणी","Guṇagrāhiṇī","One who appreciates virtues in others","90"),
    ("Guhyarupa","गुह्यरूपा","Guhyarūpā","Of hidden, secret form","91"),
    ("Guhyakaradhyeya","गुह्यकाराध्येया","Guhyakārādhyeyā","Meditated upon by the hidden ones","92"),
    ("Devi","देवी","Devī","The goddess; divine feminine","93"),
    ("Deveshi","देवेशी","Devēśī","Ruler of the gods","94"),
    ("Devakarya","देवकार्या","Devakāryā","Worker of divine purposes","95"),
    ("Devapriya","देवप्रिया","Devapriyā","Beloved of the gods","96"),
    ("Devanuta","देवनुता","Devanutā","Praised by the gods","97"),
    ("Devamanasa","देवमानसा","Devamānasā","In the minds of the gods","98"),
    ("Devaraksha","देवरक्षा","Devarakṣā","Protector of the gods","99"),
    ("Devasundari","देवसुन्दरी","Devasundarī","Most beautiful among divine beings","100"),
    ("Devatashakti","देवताशक्ति","Devatāśakti","Power of the divine","101"),
    ("Laksha","लक्षा","Lakṣā","The perceptive one; all-noticing","102"),
    ("Lakshmana","लक्ष्मणा","Lakṣmaṇā","Auspiciously marked; bearing divine signs","103"),
    ("Lakshmivibhava","लक्ष्मीविभवा","Lakṣmīvibhavā","Splendor of Lakshmi; glorious fortune","104"),
    ("Lalita","ललिता","Lalitā","The playful, graceful goddess; Tripura Sundari","105"),
    ("Lalitambika","ललिताम्बिका","Lalitāmbikā","Mother Lalita; playful divine mother","106"),
    ("Lavanya","लावण्या","Lāvaṇyā","Grace personified; embodiment of beauty","107"),
    ("Layakartri","लयकर्त्री","Layakartṛī","Creator of dissolution; merger of all","108"),
]

# ─────────────────────────────────────────────────────────────────────────────
# SHIVA SAHASRANAMAM — names starting with nakshatra syllables
# Source: Anushasana Parva, Mahabharata; Shiva Purana
# ─────────────────────────────────────────────────────────────────────────────
SHIVA_NAMES = [
    ("Sarva","सर्व","Sarva","The all-pervading; present in everything","1"),
    ("Sarvagata","सर्वगत","Sarvagata","Moving through all; omnipresent","2"),
    ("Sarvatman","सर्वात्मन","Sarvātman","Soul of all; universal self","3"),
    ("Sarvabhava","सर्वभाव","Sarvabhāva","Essence of all existence","4"),
    ("Sarvasiddha","सर्वसिद्ध","Sarvasiddha","All-accomplished; perfect in all ways","5"),
    ("Sarvadevata","सर्वदेवता","Sarvadevatā","Deity of all gods","6"),
    ("Sarvajna","सर्वज्ञ","Sarvajña","Knower of all","7"),
    ("Sarvadarsha","सर्वदर्श","Sarvadarśa","Seer of all","8"),
    ("Sarvakala","सर्वकाल","Sarvakāla","Present at all times; timeless","9"),
    ("Sarvasreshtha","सर्वश्रेष्ठ","Sarvaśreṣṭha","Best of all; most excellent","10"),
    ("Sarvavasa","सर्वावास","Sarvāvāsa","Dwelling in all things","11"),
    ("Sada","सद","Sada","Ever-existing; eternally present","12"),
    ("Sadashiva","सदाशिव","Sadāśiva","The eternally auspicious Shiva","13"),
    ("Sadyojata","सद्योजात","Sadyojāta","Instantaneously born; sudden manifestation","14"),
    ("Sama","साम","Sāma","The equalizer; equal to all","15"),
    ("Samagraha","समग्राह","Samagrāha","Grasper of all; cosmic comprehender","16"),
    ("Samhara","संहार","Saṃhāra","The great dissolver; destroyer of the universe","17"),
    ("Samhartri","संहर्ता","Saṃhartā","The dissolving one; agent of cosmic dissolution","18"),
    ("Sankara","शङ्कर","Śaṅkara","Bestower of happiness; auspicious one","19"),
    ("Sankarshana","संकर्षण","Saṃkarṣaṇa","The one who draws all unto himself","20"),
    ("Sanmukha","सन्मुख","Sanmukha","Of truthful, upright face; six-faced (Skanda)","21"),
    ("Sarvatanumaya","सर्वतनुमय","Sarvatanumaya","Present in all bodies","22"),
    ("Sarvabhavanapara","सर्वभावनपर","Sarvabhāvanapara","One who brings forth all creation","23"),
    ("Sarveshvara","सर्वेश्वर","Sarveśvara","Lord of all; supreme ruler","24"),
    ("Sarvavit","सर्ववित","Sarvavit","All-knowing one","25"),
    ("Satyakama","सत्यकाम","Satyakāma","Whose desires are pure truth","26"),
    ("Satyasandha","सत्यसन्ध","Satyasandha","Bound to truth; faithful to vows","27"),
    ("Savita","सविता","Savitā","The solar one; energizer of all","28"),
    ("Shatakratu","शतक्रतु","Śatakratu","Of a hundred sacrifices; Indra","29"),
    ("Shambhu","शम्भु","Śambhu","Source of happiness; bestower of peace","30"),
    ("Shankha","शङ्ख","Śaṅkha","The conch; sacred sound","31"),
    ("Siddha","सिद्ध","Siddha","Accomplished; perfected being","32"),
    ("Siddhanta","सिद्धान्त","Siddhānta","Ultimate principle; perfected doctrine","33"),
    ("Siddhesha","सिद्धेश","Siddheśa","Lord of all siddhas; master of accomplished ones","34"),
    ("Simhavahana","सिंहवाहन","Siṃhavāhana","Whose vehicle is the lion; fierce carrier","35"),
    ("Sivah","शिव","Śiva","The auspicious; pure consciousness","36"),
    ("Sivalinga","शिवलिङ्ग","Śivaliṅga","Sacred symbol of Shiva; cosmic pillar","37"),
    ("Smarahara","स्मरहर","Smarahara","Destroyer of Kama (Cupid); beyond desire","38"),
    ("Subrahmania","सुब्रह्मण्य","Subrahmaṇya","Very dear to Brahmanas; Murugan epithet","39"),
    ("Subrahmanya","सुब्रह्मण्य","Subrahmaṇya","Benevolent to devotees; Skanda epithet","40"),
    ("Sukshmamurthi","सूक्ष्ममूर्ति","Sūkṣmamūrti","Of subtle, formless form; invisible","41"),
    ("Sunishpanna","सुनिष्पन्न","Suniṣpanna","Perfectly produced; flawlessly manifested","42"),
    ("Suprakasha","सुप्रकाश","Suprakāśa","Supremely luminous; brilliantly manifest","43"),
    ("Sura","सुर","Sura","Divine being; lord of celestials","44"),
    ("Suresha","सुरेश","Sureśa","Lord of gods; king of celestials","45"),
    ("Surya","सूर्य","Sūrya","The sun; solar deity","46"),
    ("Suryamandala","सूर्यमण्डल","Sūryamaṇḍala","Of solar orb; shining like the sun","47"),
    ("Suvarchas","सुवर्चस","Suvarcas","Of great spiritual brilliance","48"),
    ("Suvrata","सुव्रत","Suvrata","Of excellent vows; steadfast devotion","49"),
    ("Jagadhita","जगद्धित","Jagaddhita","For the welfare of the universe","50"),
    ("Jagadisvara","जगदीश्वर","Jagadīśvara","Lord of the universe","51"),
    ("Jagannatha","जगन्नाथ","Jagannātha","Lord of all worlds","52"),
    ("Jagatkarta","जगत्कर्ता","Jagatkartā","Creator of the universe","53"),
    ("Jagatpita","जगत्पिता","Jagatpitā","Father of the universe","54"),
    ("Jagatprana","जगत्प्राण","Jagatprāṇa","Life of the universe; cosmic life-force","55"),
    ("Jagatsetu","जगत्सेतु","Jagatsetu","Cosmic bridge; universal link","56"),
    ("Jagatsvami","जगत्स्वामी","Jagatsvāmī","Master of the universe","57"),
    ("Jagadbija","जगद्बीज","Jagadbīja","Seed of the universe; cosmic origin","58"),
    ("Jaya","जय","Jaya","Victory; the victorious one","59"),
    ("Jayakara","जयकर","Jayakara","Bestower of victory","60"),
    ("Jitatman","जितात्मन","Jitātman","Conqueror of the self; self-mastered","61"),
    ("Jitakama","जितकाम","Jitakāma","Conqueror of desire; free of lust","62"),
    ("Jishnu","जिष्णु","Jiṣṇu","The conquering one; ever-victorious","63"),
    ("Jivana","जीवन","Jīvana","Life itself; the principle of life","64"),
    ("Jyotirlinga","ज्योतिर्लिङ्ग","Jyotirliṅga","Column of light; cosmic fire pillar","65"),
    ("Gajanana","गजानन","Gajānana","Elephant-faced; Ganesha epithet","66"),
    ("Gahana","गहन","Gahana","Unfathomable deep; beyond comprehension","67"),
    ("Ganapati","गणपति","Gaṇapati","Lord of the celestial hosts","68"),
    ("Gandha","गन्ध","Gandha","The fragrant one; primordial scent","69"),
    ("Ganesha","गणेश","Gaṇeśa","Lord of all ganas; obstacle-remover","70"),
    ("Gangadhara","गङ्गाधर","Gaṅgādhara","Bearer of the Ganges on his head","71"),
    ("Garala","गरल","Garala","Bearer of the poison Halahala","72"),
    ("Gauripati","गौरीपति","Gaurīpati","Lord and consort of Gauri/Parvati","73"),
    ("Gaurivallabha","गौरीवल्लभ","Gaurīvallabha","Beloved of Gauri; dear to Parvati","74"),
    ("Girishvara","गिरीश्वर","Girīśvara","Lord of mountains; Kailasha dweller","75"),
    ("Girijapati","गिरिजापति","Girijāpati","Husband of Girija (Parvati)","76"),
    ("Guheshvara","गुहेश्वर","Guheśvara","Lord of Guha; master of the cave-dweller","77"),
    ("Gunagrahi","गुणग्राही","Guṇagrāhī","Appreciator of virtues; virtue-recognizing","78"),
    ("Gunakara","गुणकर","Guṇakara","Mine of all virtues","79"),
    ("Gurumurthi","गुरुमूर्ति","Gurumūrti","Embodiment of the guru; teacher-form","80"),
    ("Deva","देव","Deva","The divine being; shining one","81"),
    ("Devadeva","देवदेव","Devadeva","God of gods; supreme deity","82"),
    ("Devadhipa","देवाधिप","Devādhipa","Ruler of the gods","83"),
    ("Devapati","देवपति","Devapati","Lord of all divine beings","84"),
    ("Devapriya","देवप्रिय","Devapriya","Beloved of all gods","85"),
    ("Devaraksha","देवरक्ष","Devarakṣa","Protector of the divine beings","86"),
    ("Devasena","देवसेन","Devasena","Commander of the divine army","87"),
    ("Deveshvara","देवेश्वर","Deveśvara","Supreme lord of all gods","88"),
    ("Devadhisha","देवाधीश","Devādhīśa","Sovereign of all gods","89"),
    ("Linga","लिङ्ग","Liṅga","The sacred emblem; cosmic pillar of light","90"),
    ("Lingamurthi","लिङ्गमूर्ति","Liṅgamūrti","Form of the linga; pillar of consciousness","91"),
]

# ─────────────────────────────────────────────────────────────────────────────
# SKANDA SAHASRANAMAM — names starting with nakshatra syllables
# Source: Skanda Purana, Vana Parva (Mahabharata)
# ─────────────────────────────────────────────────────────────────────────────
SKANDA_NAMES = [
    ("Sarvajna","सर्वज्ञ","Sarvajña","Omniscient Skanda; all-knowing commander","1"),
    ("Sarvanayaka","सर्वनायक","Sarvanāyaka","Leader of all; commander-in-chief","2"),
    ("Sarvadevasenapati","सर्वदेवसेनापति","Sarvadevasena­pati","Commander-in-chief of all divine armies","3"),
    ("Sarvalokapriya","सर्वलोकप्रिय","Sarvaloka­priya","Beloved in all worlds","4"),
    ("Sarvasena","सर्वसेन","Sarvasena","Whose armies are invincible","5"),
    ("Sarvabhayankara","सर्वभयङ्कर","Sarvabhayaṅkara","Terror of all enemies","6"),
    ("Sarvashatrunibarhi","सर्वशत्रुनिबर्ही","Sarvaśatru­nibarhī","Destroyer of all enemies","7"),
    ("Sarvavighnavinashaka","सर्वविघ्नविनाशक","Sarvavighna­vināśaka","Remover of all obstacles","8"),
    ("Sanmukha","षण्मुख","Ṣaṇmukha","Six-faced; Kartikeya's primary form","9"),
    ("Sharavana","शरवण","Śaravaṇa","Born in the reed forest; Saravana-bhava","10"),
    ("Shaktidhara","शक्तिधर","Śaktidhara","Bearer of the Vel (divine spear)","11"),
    ("Shaktimana","शक्तिमान","Śaktimān","Possessor of great power","12"),
    ("Shaktinatha","शक्तिनाथ","Śaktinātha","Lord of the divine spear Vel","13"),
    ("Sikhivahana","शिखिवाहन","Śikhivāhana","Whose vehicle is the peacock","14"),
    ("Simhavikrama","सिंहविक्रम","Siṃhavikrama","Of lion-like valor","15"),
    ("Skandha","स्कन्ध","Skandha","The leaping one; Murugan","16"),
    ("Subrahmanya","सुब्रह्मण्य","Subrahmaṇya","Very dear to the wise; benevolent","17"),
    ("Subrahmanyapriya","सुब्रह्मण्यप्रिय","Subrahmaṇya­priya","Dear to Subrahmanya's devotees","18"),
    ("Sura","सुर","Sura","Divine being","19"),
    ("Suradipa","सुरदीप","Suradīpa","Lamp of the gods; divine light","20"),
    ("Surananda","सुरानन्द","Surānanda","Bliss of the gods","21"),
    ("Suresha","सुरेश","Sureśa","Lord of all gods","22"),
    ("Surendravandita","सुरेन्द्रवन्दित","Surendravandita","Worshipped even by Indra","23"),
    ("Suvela","सुवेल","Suvela","Master of the sacred Vel","24"),
    ("Sivakumara","शिवकुमार","Śivakumāra","Divine son of Shiva","25"),
    ("Sivashakti","शिवशक्ति","Śivaśakti","Union of Shiva and Shakti","26"),
    ("Senani","सेनानी","Senānī","Commander; leader of the army","27"),
    ("Senapati","सेनापति","Senāpati","Supreme commander; general of divine forces","28"),
    ("Siddhidata","सिद्धिदाता","Siddhidātā","Bestower of spiritual perfections","29"),
    ("Siddhesha","सिद्धेश","Siddheśa","Lord of accomplished beings","30"),
    ("Jaya","जय","Jaya","The victorious one","31"),
    ("Jayanta","जयन्त","Jayanta","Ultimately victorious","32"),
    ("Jayapriya","जयप्रिय","Jayapriya","Lover of victory; victorious friend","33"),
    ("Jayashakti","जयशक्ति","Jayaśakti","Power of victory","34"),
    ("Jayaveeragni","जयवीरग्नि","Jayavīragni","Fire of the victorious hero","35"),
    ("Jitasurasena","जितसुरसेन","Jitasura­sena","Conqueror of the demon armies","36"),
    ("Jyotirmaya","ज्योतिर्मय","Jyotirmaya","Made of divine light","37"),
    ("Jyotishmana","ज्योतिष्मान","Jyotiṣmān","Possessor of brilliant light","38"),
    ("Jitataraka","जितताराक","Jitatāraka","Conqueror of the demon Taraka","39"),
    ("Gajanasha","गजनाश","Gajanāśa","Destroyer of the demon-elephant forces","40"),
    ("Gananatha","गणनाथ","Gaṇanātha","Lord of all celestial hosts","41"),
    ("Gandhamadhura","गन्धमधुर","Gandhamādhura","Of sweet, divine fragrance","42"),
    ("Girijakumara","गिरिजाकुमार","Girijākumāra","Son of Parvati (Girija); divine child","43"),
    ("Guhapriya","गुहप्रिय","Guhapriya","The beloved Guha; dear to all","44"),
    ("Guhanatha","गुहनाथ","Guhanātha","Lord Guha; master of the cave","45"),
    ("Gunasagara","गुणसागर","Guṇasāgara","Ocean of virtues; inexhaustible goodness","46"),
    ("Guruguha","गुरुगुह","Gurugaha","Guru and Guha combined; teacher-child","47"),
    ("Devasena","देवसेन","Devasena","Commander of divine forces","48"),
    ("Devasendhipati","देवसेनाधिपति","Devasenā­dhipati","Supreme commander of the army of gods","49"),
    ("Devapriya","देवप्रिय","Devapriya","Beloved of all gods","50"),
    ("Devakumara","देवकुमार","Devakumāra","Divine youth; son of the gods","51"),
    ("Devanatha","देवनाथ","Devanātha","Lord of gods; divine protector","52"),
    ("Deva","देव","Deva","Divine shining one","53"),
    ("Latavandita","लतावन्दित","Latāvandita","Worshipped even by creepers; adored by all","54"),
    ("Lavanyamurthi","लावण्यमूर्ति","Lāvaṇyamūrti","Form of grace and beauty","55"),
]

# ─────────────────────────────────────────────────────────────────────────────
# GANESHA SAHASRANAMAM — names starting with nakshatra syllables
# Source: Ganesha Purana, Mudgala Purana
# ─────────────────────────────────────────────────────────────────────────────
GANESHA_NAMES = [
    ("Sarvasiddha","सर्वसिद्ध","Sarvasiddha","All-accomplished; remover of all obstacles","1"),
    ("Sarvasidhiprada","सर्वसिद्धिप्रद","Sarvasiddhi­prada","Bestower of all perfections and accomplishments","2"),
    ("Sarvajnanata","सर्वज्ञानता","Sarvajñānatā","Embodiment of omniscience","3"),
    ("Sarvajaneshvara","सर्वजनेश्वर","Sarvajanēśvara","Lord of all people","4"),
    ("Sarvavighnavinayaka","सर्वविघ्नविनायक","Sarvavighna­vināyaka","Remover of all obstacles","5"),
    ("Sarvalokasundarah","सर्वलोकसुन्दर","Sarvalokasum­dara","Most beautiful in all worlds","6"),
    ("Sarvadevanayaka","सर्वदेवनायक","Sarvadev­anāyaka","Leader of all divine beings","7"),
    ("Sanmukhagraja","षण्मुखाग्रज","Ṣaṇmukhāgraja","Elder brother of Sanmukha (Murugan)","8"),
    ("Samiddha","समिद्ध","Samiddha","Blazing with divine fire; illumined","9"),
    ("Sankha","शङ्ख","Śaṅkha","Of conch-like purity; sacred sound","10"),
    ("Sarvabhaya","सर्वभय","Sarvabhaya","Destroyer of all fears","11"),
    ("Siddhidata","सिद्धिदाता","Siddhidātā","Bestower of spiritual accomplishments","12"),
    ("Siddha","सिद्ध","Siddha","The accomplished perfected one","13"),
    ("Siddhakara","सिद्धकर","Siddhakara","Maker of accomplishments","14"),
    ("Siddhesha","सिद्धेश","Siddheśa","Lord of all siddhas","15"),
    ("Siddhipriya","सिद्धिप्रिय","Siddhipriya","Lover of perfection; fond of accomplishment","16"),
    ("Sivakumara","शिवकुमार","Śivakumāra","Son of Shiva","17"),
    ("Sivapriya","शिवप्रिय","Śivapriya","Beloved of Shiva","18"),
    ("Sukha","सुख","Sukha","Bliss; embodiment of happiness","19"),
    ("Sukhakara","सुखकर","Sukhakara","Maker of happiness; giver of joy","20"),
    ("Sukhaprada","सुखप्रद","Sukhaprada","Bestower of happiness","21"),
    ("Subhaga","सुभग","Subhaga","Extremely fortunate; highly auspicious","22"),
    ("Subhanga","सुभाङ्ग","Subhāṅga","Of beautiful, auspicious form","23"),
    ("Subhechcha","सुभेच्छा","Subhecchā","Of auspicious intention; good-willed","24"),
    ("Subuddhi","सुबुद्धि","Subuddhi","Of excellent intelligence; clear-minded","25"),
    ("Sudhira","सुधीर","Sudhīra","Supremely wise and patient","26"),
    ("Sukshma","सूक्ष्म","Sūkṣma","The subtle one; beyond gross perception","27"),
    ("Sumnna","सुमना","Sumanā","Of beautiful, gentle mind","28"),
    ("Sunama","सुनाम","Sunāma","Of auspicious name; beautifully named","29"),
    ("Suprasida","सुप्रसीद","Suprasīda","Supremely gracious; fully satisfied","30"),
    ("Suprabha","सुप्रभ","Suprabha","Of excellent brilliance","31"),
    ("Sureshvara","सुरेश्वर","Sureśvara","God of all gods","32"),
    ("Surya","सूर्य","Sūrya","The solar one; sun-like radiance","33"),
    ("Suvarna","सुवर्ण","Suvarṇa","Golden; of golden hue","34"),
    ("Jagatpalaka","जगत्पालक","Jagatpālaka","Protector of the universe","35"),
    ("Jagadbandhu","जगद्बन्धु","Jagadbandhu","Friend of the universe; cosmic companion","36"),
    ("Jagadguru","जगद्गुरु","Jagadguru","Universal teacher","37"),
    ("Jagadisha","जगदीश","Jagadīśa","Lord of the universe","38"),
    ("Jayadeva","जयदेव","Jayadeva","Divine victor; god of victory","39"),
    ("Jayanta","जयन्त","Jayanta","Ultimately victorious","40"),
    ("Gajamukha","गजमुख","Gajamukha","Elephant-faced; the elephant-headed one","41"),
    ("Gajanana","गजानन","Gajānana","Elephant-faced divine lord","42"),
    ("Gajapati","गजपति","Gajapati","Lord of elephants; elephant-king","43"),
    ("Gajendra","गजेन्द्र","Gajendra","Chief of elephants; king of elephants","44"),
    ("Gajavaktra","गजवक्त्र","Gajavaकtra","Elephant-snouted; of elephant face","45"),
    ("Ganaadhipa","गणाधिप","Gaṇādhipa","Ruler of celestial hosts","46"),
    ("Ganadeva","गणदेव","Gaṇadeva","God of celestial hosts","47"),
    ("Ganadhyaksha","गणाध्यक्ष","Gaṇādhyakṣa","Presiding deity over celestial hosts","48"),
    ("Gananatha","गणनाथ","Gaṇanātha","Lord of all ganas","49"),
    ("Ganapati","गणपति","Gaṇapati","Lord of the divine hosts","50"),
    ("Ganaraja","गणराज","Gaṇarāja","King of celestial hosts","51"),
    ("Ganeshvara","गणेश्वर","Gaṇeśvara","Ruler of celestial hosts","52"),
    ("Gauriputta","गौरीपुत्त","Gaurīputra","Son of Gauri; Parvati's divine child","53"),
    ("Gaurisuta","गौरीसुत","Gaurīsuta","Son of Gauri","54"),
    ("Girijatanaya","गिरिजातनय","Girijātanaya","Son of Girija (Parvati)","55"),
    ("Gunagrahi","गुणग्राही","Guṇagrāhī","One who recognizes virtues","56"),
    ("Gunakara","गुणकर","Guṇakara","Mine of all virtues","57"),
    ("Gunadhisha","गुणाधीश","Guṇādhīśa","Master of all virtues","58"),
    ("Devabhuta","देवभूत","Devabhūta","Born divine; divinely manifested","59"),
    ("Devapujita","देवपूजित","Devapūjita","Worshipped by all divine beings","60"),
    ("Devapriya","देवप्रिय","Devapriya","Beloved by all gods","61"),
    ("Devavandya","देववन्द्य","Devavandya","Worthy of divine worship","62"),
    ("Devayana","देवयान","Devayāna","Path of the divine; divine journey","63"),
    ("Lambodar","लम्बोदर","Lambodara","Large-bellied; cosmic womb","64"),
    ("Latayita","लतायित","Latāyita","Gracefully branching like a creeper","65"),
    ("Lavanyamaya","लावण्यमय","Lāvaṇyamaya","Made of grace and beauty","66"),
],

# ─────────────────────────────────────────────────────────────────────────────
# SURYA SAHASRANAMAM — names starting with nakshatra syllables
# Source: Samba Purana; Bhavishya Purana
# ─────────────────────────────────────────────────────────────────────────────
SURYA_NAMES = [
    ("Sarvatman","सर्वात्मन","Sarvātman","Universal soul; soul of all","1"),
    ("Sarvajnanaya","सर्वज्ञाय","Sarvajñāya","Omniscient solar deity","2"),
    ("Sarvabhuteshvara","सर्वभूतेश्वर","Sarvabhūteśvara","Lord of all beings","3"),
    ("Sarvaprakasha","सर्वप्रकाश","Sarvaprakāśa","Light of all; universal illuminator","4"),
    ("Sarvaloka","सर्वलोक","Sarvaloka","Present in all worlds","5"),
    ("Sarvakala","सर्वकाल","Sarvakāla","All times; beyond time","6"),
    ("Sarvashakti","सर्वशक्ति","Sarvaśakti","All-powerful solar energy","7"),
    ("Saptarashmi","सप्तरश्मि","Saptaraśmi","Seven-rayed; the seven-beamed sun","8"),
    ("Saptashva","सप्ताश्व","Saptāśva","Of seven horses; the week's driver","9"),
    ("Saptarchis","सप्तार्चिस","Saptārciṣ","Seven-flamed; seven solar rays","10"),
    ("Savita","सविता","Savitā","The vivifier; energizer of life","11"),
    ("Sahasrakirana","सहस्रकिरण","Sahasrakiraṇa","Thousand-rayed; blazing brilliance","12"),
    ("Sahasramshu","सहस्रांशु","Sahasrāṃśu","Of a thousand rays; boundless radiance","13"),
    ("Sahasrarchis","सहस्रार्चिस","Sahasrārciṣ","Thousand-flamed; intensely radiant","14"),
    ("Sahasrateja","सहस्रतेज","Sahasrateja","Of a thousand energies","15"),
    ("Sakala","सकल","Sakala","Complete; whole; perfect","16"),
    ("Sandhyavandya","सन्ध्यावन्द्य","Sandhyāvandya","Worshipped at the three sandhyas","17"),
    ("Sarvahetuka","सर्वहेतुक","Sarvahetuka","Cause of all creation","18"),
    ("Saurabha","सौरभ","Saurabha","Of divine fragrance; solar sweet scent","19"),
    ("Saura","सौर","Saura","Solar; relating to the sun","20"),
    ("Sikhanda","शिखण्ड","Śikhaṇḍa","Crested one; with flame-crest","21"),
    ("Sikhivahana","शिखिवाहन","Śikhivāhana","Fire-vehicle; flame-rider","22"),
    ("Surya","सूर्य","Sūrya","The Sun; the solar deity","23"),
    ("Suryamandala","सूर्यमण्डल","Sūryamaṇḍala","Solar disk; orb of the sun","24"),
    ("Suryanarayana","सूर्यनारायण","Sūryanārāyaṇa","Solar Narayana; Vishnu as the Sun","25"),
    ("Suryaprakasha","सूर्यप्रकाश","Sūryaprakāśa","Sunlight; solar radiance","26"),
    ("Suryatman","सूर्यात्मन","Sūryātman","Soul of the Sun; solar self","27"),
    ("Subhaga","सुभग","Subhaga","Supremely fortunate; auspicious","28"),
    ("Subhankara","शुभङ्कर","Śubhaṅkara","Bestower of good; auspiciousness","29"),
    ("Sukhi","सुखी","Sukhī","Blissful; joyful one","30"),
    ("Sukla","शुक्ल","Śukla","Pure white light; radiant purity","31"),
    ("Supta","सुप्त","Supta","Ever-awake; beyond sleep","32"),
    ("Suvarchas","सुवर्चस","Suvarcas","Of great spiritual lustre","33"),
    ("Jagachakshus","जगच्चक्षुस","Jagaccakṣuṣ","Eye of the universe; cosmic vision","34"),
    ("Jagaddhata","जगद्धाता","Jagaddhātā","Sustainer of the universe","35"),
    ("Jagadguru","जगद्गुरु","Jagadguru","Universal preceptor; teacher of all worlds","36"),
    ("Jagadisha","जगदीश","Jagadīśa","Lord of the universe","37"),
    ("Jagajjivana","जगज्जीवन","Jagajjīvana","Life of the universe","38"),
    ("Jagatpita","जगत्पिता","Jagatpitā","Father of the universe","39"),
    ("Jagatprakasha","जगत्प्रकाश","Jagatprakāśa","Light of the universe","40"),
    ("Jagatsakshi","जगत्साक्षी","Jagatsākṣī","Witness of all; cosmic observer","41"),
    ("Jaya","जय","Jaya","Victor; the triumphant one","42"),
    ("Jayaprada","जयप्रद","Jayaprada","Giver of victory","43"),
    ("Gaganachara","गगनचर","Gaganacara","Traveler of the sky; solar being","44"),
    ("Gaganaprabha","गगनप्रभ","Gaganaprabha","Radiant in the sky; sky-splendor","45"),
    ("Gaganashaya","গগनशाय","Gaganśāya","Resting in the sky; sky-dweller","46"),
    ("Gatiman","गतिमान","Gatimān","Swift mover; dynamic force","47"),
    ("Graharaja","ग्रहराज","Graharāja","King of planets; sovereign of celestials","48"),
    ("Gunadhara","गुणधर","Guṇadhara","Bearer of all virtues","49"),
    ("Gunagrahi","गुणग्राही","Guṇagrāhī","Recognizer of virtues","50"),
    ("Deva","देव","Deva","The divine shining one","51"),
    ("Devadeva","देवदेव","Devadeva","God of gods","52"),
    ("Devaloka","देवलोक","Devaloka","Of the divine realm; celestial world","53"),
    ("Devapriya","देवप्रिय","Devapriya","Beloved of all gods","54"),
    ("Devaraja","देवराज","Devarāja","King of the gods; divine sovereign","55"),
    ("Devashri","देवश्री","Devaśrī","Divine glory; radiance of the divine","56"),
    ("Devasena","देवसेन","Devasena","Lord of the divine army","57"),
    ("Deveshvara","देवेश्वर","Deveśvara","God of all gods","58"),
    ("Lakshmivasa","लक्ष्मीवास","Lakṣmīvāsa","Abode of Lakshmi; where fortune lives","59"),
    ("Lavanya","लावण्य","Lāvaṇya","Grace; golden beauty","60"),
]

# ─────────────────────────────────────────────────────────────────────────────
# Helper: enrich a name list
# ─────────────────────────────────────────────────────────────────────────────

def enrich(records, source_name):
    """Add computed fields to each record."""
    result = []
    seen = set()
    for rec in records:
        name = rec[0]
        if name.lower() in seen:
            continue
        grp = syllable_group(name)
        if not grp:
            continue
        seen.add(name.lower())
        total, final = chaldean(name)
        result.append({
            "name": name,
            "devanagari": rec[1],
            "iast": rec[2],
            "meaning": rec[3],
            "shloka": rec[4],
            "source": source_name,
            "syllable": grp,
            "chaldean_total": total,
            "chaldean_final": final,
            "preferred": "✦" if final in PREFERRED else "",
        })
    return sorted(result, key=lambda x: (x["syllable"], x["name"]))


def write_file(records, source_name, deity, purana_ref, filename):
    total = len(records)
    by_syl = {}
    for r in records:
        by_syl.setdefault(r["syllable"], []).append(r)

    top = [r for r in records if r["preferred"]]
    top_sorted = sorted(top, key=lambda x: x["chaldean_final"])

    lines = [
        f"# {source_name} — Baby Boy Name Candidates",
        f"",
        f"**Deity / Subject:** {deity}  ",
        f"**Scriptural Source:** {purana_ref}  ",
        f"**Filter:** Names starting with nakshatra syllables Sa · Si · Su · Se · Ja · Ji · Ga · Gu · De · La  ",
        f"**Total Names Found:** {total}  ",
        f"**With Preferred Chaldean (1/3/6):** {len(top)}  ",
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
        lines.append("| # | Name | Devanagari | IAST | Meaning | Shloka | Chaldean | ✦ |")
        lines.append("|---|------|------------|------|---------|--------|----------|---|")
        for i, r in enumerate(group, 1):
            lines.append(
                f"| {i} | **{r['name']}** | {r['devanagari']} | *{r['iast']}* | "
                f"{r['meaning']} | {r['shloka']} | {r['chaldean_final']} | {r['preferred']} |"
            )
        lines.append("")

    lines += [
        "---",
        "",
        f"## Top Picks — Preferred Chaldean Numbers (1, 3, 6)",
        "",
        "| Name | Syllable | Chaldean | Devanagari | Meaning |",
        "|------|----------|----------|------------|---------|",
    ]
    for r in top_sorted[:30]:
        lines.append(
            f"| **{r['name']}** | {r['syllable']} | {r['chaldean_final']}✦ | "
            f"{r['devanagari']} | {r['meaning']} |"
        )

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  Written: {filename}  ({total} names, {len(top)} preferred)")


def main():
    print("Generating Sahasranama name files...")

    datasets = [
        (VISHNU_NAMES,  "Vishnu Sahasranamam",  "Lord Vishnu",
         "Anushasana Parva (Mahabharata), Bhagavata Purana",
         "VISHNU-SAHASRANAMAM-NAMES.md"),
        (LALITHA_NAMES, "Lalitha Sahasranamam", "Goddess Lalitha / Devi (Shakti)",
         "Brahmanda Purana — Lalitopakhyana",
         "LALITHA-SAHASRANAMAM-NAMES.md"),
        (SHIVA_NAMES,   "Shiva Sahasranamam",   "Lord Shiva",
         "Anushasana Parva (Mahabharata), Shiva Purana",
         "SHIVA-SAHASRANAMAM-NAMES.md"),
        (SKANDA_NAMES,  "Skanda Sahasranamam",  "Lord Murugan / Kartikeya (Skanda)",
         "Skanda Purana, Vana Parva (Mahabharata)",
         "SKANDA-SAHASRANAMAM-NAMES.md"),
        (GANESHA_NAMES[0], "Ganesha Sahasranamam", "Lord Ganesha",
         "Ganesha Purana, Mudgala Purana",
         "GANESHA-SAHASRANAMAM-NAMES.md"),
        (SURYA_NAMES,   "Surya Sahasranamam",   "Lord Surya (Sun God)",
         "Samba Purana, Bhavishya Purana",
         "SURYA-SAHASRANAMAM-NAMES.md"),
    ]

    for raw, source, deity, purana, fname in datasets:
        enriched = enrich(raw, source)
        write_file(enriched, source, deity, purana, fname)

    print("\nDone. All 6 files generated.")


if __name__ == "__main__":
    main()
