"""KALKI series - Episode 5: Padmavati ka Swayamvar (~8 min, Hindi). Based on the Kalki Purana (Kalki goes to
Simhala, the kings who had become women are restored, Kalki marries Padmavati, Vishwakarma builds Shambhala),
with dramatized scenes."""
import kalki_seo as ks
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT, STYLE, KALI
from kalki02 import YOUNG
from kalki04 import VOICES as V4, SPEAKERS as S4, PV

SERIES = "कल्कि • भाग 5"
PLAYLIST = "kalki_hi"
HOOK = "पद्मावती का स्वयंवर"
HOOK2 = "क्या टूटेगा श्राप?"
NEXT = "भाग 6: कीकटपुर का अधर्मी राजा"

VOICES = dict(V4, Kshatriya=("hi-IN-MadhurNeural", "+4%", "-10Hz", "soft"),
              Vishwakarma=("hi-IN-MadhurNeural", "-14%", "-18Hz", "divine"))
SPEAKERS = dict(S4, Kshatriya=("एक राजा", (230, 200, 160)), Vishwakarma=("विश्वकर्मा", (255, 200, 120)))

IMAGES = [
    ("kalki_ride_sea", None), ("kalki_young_face", None), ("simhala_island", None), ("simhala_palace", None),
    ("king_brihadratha", None), ("queen_kaumudi", None), ("padmavati_face", None), ("padmavati_hope", None),
    ("women_attendants", None), ("kings_stare", None), ("shuka", None), ("horse", None), ("kali", None),
    ("kali_smile", None), ("flowers_rain", None), ("shambhala", None), ("sumati_face", None), ("vy_face", None),
    ("shiva_face", None), ("koka_face", None), ("vikoka", None), ("army", None),
    ("ocean_ride", YOUNG + " riding a radiant white horse galloping over ocean waves, spray of water, sunrise, "
                  "divine glow"),
    ("simhala_gate", "the giant golden gates of an island kingdom with guards in armor, palm trees, sea behind"),
    ("rival_kings", "a group of angry Indian kings in armor and crowns drawing swords at a palace gate, hostile"),
    ("kings_attack", "many armored kings and soldiers charging at a lone young warrior on a white horse, palace "
                     "courtyard, dust"),
    ("kalki_fight_kings", YOUNG + " on a white horse disarming many armored kings with a glowing sword, swords flying, "
                          "courtyard"),
    ("kings_kneel", "defeated Indian kings kneeling and bowing before a young warrior with a glowing sword, courtyard"),
    ("lotus_garden_meet", YOUNG + " and " + PV + " seeing each other for the first time in a moonlit lotus garden"),
    ("pv_shy", PV + " smiling shyly with tears of joy, close up, front view, moonlight"),
    ("kalki_smile", YOUNG + ", gentle warm smile, close up face, front view, soft golden light"),
    ("curse_break", "many royal women in saris turning back into kings in armor in a burst of golden light, "
                    "magical transformation, palace"),
    ("kings_freed", "joyful Indian kings in crowns folding hands in gratitude toward a glowing young warrior"),
    ("wedding_mandap", "a grand royal Hindu wedding mandap with sacred fire, flowers, golden pillars, island palace"),
    ("wedding_couple", YOUNG + " and " + PV + " in royal wedding attire walking around the sacred fire, flower petals"),
    ("varmala", PV + " placing a flower garland on " + YOUNG + ", wedding hall, joyful crowd"),
    ("ship_return", "a royal ship with golden sails crossing the ocean at sunset carrying a royal couple"),
    ("vishwakarma", "Vishwakarma the divine architect god with a long white beard holding golden building tools, "
                    "glowing, close up face, front view"),
    ("golden_shambhala", "a magnificent golden city with temples and palaces rising in the Himalayan mountains, "
                         "divine light, epic"),
    ("couple_shambhala", "a young royal couple arriving at a golden Himalayan city, villagers celebrating with "
                         "flowers and lamps"),
    ("kali_rage", KALI + " smashing a dark goblet in rage, purple fire, his palace shaking"),
]

LINES = [
    ("#", "पिछले भाग में"),
    (["padmavati_face"], "N", "पिछले भाग में... शुक ने सिंहल द्वीप की राजकुमारी पद्मावती का रहस्य जाना।", ""),
    (["women_attendants"], "N", "महादेव के वरदान से... जो भी राजा उसे विवाह की इच्छा से देखता, वो स्त्री बन जाता।", ""),
    (["kalki_ride_sea"], "N", "और अब... कल्कि स्वयं सिंहल की ओर चल पड़े थे।", ""),
    (["sumati_face"], "N", "माँ सुमति ने विदा करते समय... उनके माथे पर तिलक लगाया था।", ""),
    (["shuka"], "N", "और शुक उनके कंधे पर बैठा... रास्ता दिखा रहा था।", ""),
    ("#", "समुद्र पर दौड़", ),
    (["ocean_ride"], "N", "समुद्र के किनारे पहुँचकर... कल्कि एक पल को रुके।", ""),
    (["kalki_young_face"], "Kalki", "देवदत्त... क्या तुम समुद्र पार कर सकते हो?", ""),
    (["horse"], "N", "देवदत्त हिनहिनाया... और लहरों पर दौड़ पड़ा!", "thunder"),
    (["ocean_ride"], "N", "उसके खुर पानी को छूते... पर डूबते नहीं। जैसे समुद्र स्वयं रास्ता दे रहा हो।", ""),
    (["shuka"], "Shuka", "प्रभु... समुद्र देव भी आपका सम्मान कर रहे हैं।", ""),
    (["ocean_ride"], "N", "मछुआरों ने अपनी नावों से यह दृश्य देखा... और हाथ जोड़कर खड़े हो गए।", ""),
    (["kalki_young_face"], "Kalki", "यह मेरी शक्ति नहीं शुक... यह महादेव का आशीर्वाद है।", ""),
    ("#", "सिंहल का द्वार"),
    (["simhala_island"], "N", "और फिर सामने आया... सिंहल द्वीप।", ""),
    (["simhala_gate"], "N", "पर महल के द्वार पर... कुछ ठीक नहीं था।", ""),
    (["rival_kings"], "N", "कलि के बहकावे में आकर... कई राजा तलवारें लेकर खड़े थे।", ""),
    (["kali_smile"], "N", "रातों-रात कलि ने उनके कानों में ज़हर घोला था... कि एक परदेसी उनकी राजकुमारी छीनने आ रहा है।", ""),
    (["rival_kings"], "Kshatriya", "रुक जा परदेसी! पद्मावती पर पहला अधिकार हमारा है। लौट जा, वरना यहीं मरेगा!", ""),
    (["kalki_young_face"], "Kalki", "मैं युद्ध करने नहीं आया... पर अगर धर्म का रास्ता रोकोगे, तो पीछे भी नहीं हटूँगा।", ""),
    ("#", "द्वार पर युद्ध"),
    (["kings_attack"], "N", "राजाओं ने एक साथ हमला कर दिया...", "thunder"),
    (["kings_attack"], "N", "भाले... तलवारें... तीरों की बौछार...", ""),
    (["horse"], "N", "पर देवदत्त ऐसे घूमा... जैसे हवा का बवंडर।", ""),
    (["kalki_fight_kings"], "N", "पर कल्कि ने किसी का खून नहीं बहाया।", ""),
    (["kalki_fight_kings"], "N", "रत्नजड़ित खड्ग चमकता... और एक-एक करके सबकी तलवारें हवा में उड़ जातीं।", ""),
    (["kings_kneel"], "N", "कुछ ही पलों में... सारे राजा घुटनों पर थे।", ""),
    (["kings_kneel"], "Kshatriya", "क्षमा... हम समझ गए। आप कोई साधारण योद्धा नहीं हैं।", ""),
    (["kalki_young_face"], "Kalki", "उठिए राजन... दोषी आप नहीं, आपके मन में बैठा कलि है।", ""),
    (["kings_kneel"], "N", "राजाओं को पहली बार लगा... जैसे उनके मन से कोई काला बादल हट गया हो।", ""),
    ("#", "पहली भेंट"),
    (["simhala_palace"], "N", "राजा बृहद्रथ ने आदर से कल्कि का स्वागत किया...", ""),
    (["king_brihadratha"], "King", "युवक... तुम जानते हो, पद्मावती को देखने वाला हर पुरुष स्त्री बन जाता है?", ""),
    (["kalki_young_face"], "Kalki", "जानता हूँ राजन... पर महादेव का वचन कभी गलत नहीं होता।", ""),
    (["king_brihadratha"], "King", "मैंने बहुत से राजाओं को स्त्री बनते देखा है... मैं तुम्हें खोना नहीं चाहता।", ""),
    (["kalki_young_face"], "Kalki", "राजन... जो पद्मावती को केवल रूप से नहीं, उसकी भक्ति से देखेगा, उस पर यह वरदान नहीं चलेगा।", ""),
    (["lotus_garden_meet"], "N", "उस शाम... कमल के बगीचे में... पद्मावती और कल्कि ने पहली बार एक-दूसरे को देखा।", ""),
    (["padmavati_face"], "N", "पूरा महल साँस रोककर देख रहा था... क्या होगा?", ""),
    (["kalki_smile"], "N", "पर... कुछ नहीं हुआ। कल्कि वैसे ही खड़े रहे... मुस्कुराते हुए।", ""),
    (["pv_shy"], "Padmavati", "तो... तो आप ही हैं... जिनकी मैं वर्षों से प्रतीक्षा कर रही थी।", ""),
    (["kalki_smile"], "Kalki", "और आप ही हैं... जिनकी भक्ति ने मुझे यहाँ तक खींच लाया, देवी।", ""),
    (["queen_kaumudi"], "Queen", "महादेव... आपने मेरी बच्ची की सुन ली!", ""),
    (["king_brihadratha"], "King", "यह... यह चमत्कार है! महादेव का वचन पूरा हुआ!", ""),
    (["pv_shy"], "N", "पद्मावती की आँखों से आँसू बह निकले... पर इस बार, ख़ुशी के।", ""),
    ("#", "श्राप का अंत"),
    (["women_attendants"], "N", "उसी रात... वे सारे राजा, जो स्त्री बन गए थे, कल्कि के पास आए।", ""),
    (["women_attendants"], "Kshatriya", "प्रभु... हमें क्षमा करें। हम अपना रूप वापस चाहते हैं।", ""),
    (["kalki_young_face"], "Kalki", "आपका पाप केवल एक पल की इच्छा थी... उसका दंड आपने भोग लिया।", ""),
    (["curse_break"], "N", "कल्कि ने उन्हें आशीर्वाद दिया... और एक सुनहरा प्रकाश फैल गया।", "thunder"),
    (["curse_break"], "N", "एक-एक करके... सब अपने असली रूप में लौट आए!", ""),
    (["kings_freed"], "Kshatriya", "जय हो प्रभु! आज से हम सब धर्म के लिए आपके साथ लड़ेंगे।", ""),
    (["kalki_smile"], "N", "उस रात कल्कि को... अपनी पहली सेना मिल गई।", ""),
    ("#", "विवाह"),
    (["wedding_mandap"], "N", "कुछ दिनों बाद... सिंहल में भव्य विवाह की तैयारी हुई।", ""),
    (["simhala_island"], "N", "पूरा सिंहल दीयों और फूलों से सज गया... ढोल-नगाड़े बजने लगे।", ""),
    (["simhala_palace"], "N", "दूर-दूर से ऋषि-मुनि... आशीर्वाद देने आए।", ""),
    (["varmala"], "N", "पद्मावती ने कल्कि के गले में... वरमाला डाली।", ""),
    (["wedding_couple"], "N", "अग्नि के सात फेरे... और श्री हरि और लक्ष्मी का मिलन।", ""),
    (["flowers_rain"], "N", "आकाश से देवताओं ने... फूल बरसाए।", ""),
    (["shiva_face"], "N", "कहते हैं... उस दिन कैलाश पर महादेव भी मुस्कुराए थे।", ""),
    (["queen_kaumudi"], "Queen", "जा बेटी... अपने स्वामी के साथ सुखी रहना।", ""),
    ("#", "स्वर्ण शंभल"),
    (["ship_return"], "N", "कल्कि और पद्मावती... सोने के पालों वाले जहाज़ से शंभल लौटे।", ""),
    (["vishwakarma"], "N", "और उनके स्वागत के लिए... देवताओं ने भेजा विश्वकर्मा को।", ""),
    (["vishwakarma"], "Vishwakarma", "प्रभु... आपका शंभल अब एक साधारण गाँव नहीं रहेगा।", ""),
    (["golden_shambhala"], "N", "एक ही रात में... शंभल सोने के महलों और मंदिरों से भर गया।", "thunder"),
    (["couple_shambhala"], "N", "पूरा गाँव... अब एक दिव्य नगर बन चुका था।", ""),
    (["golden_shambhala"], "N", "सोने की सड़कें... रत्नों से जड़े मंदिर... और हर घर में दीया।", ""),
    (["sumati_face"], "Sumati", "आओ बेटी... यह घर अब तुम्हारा है।", ""),
    (["vy_face"], "Vishnuyasha", "आज मेरा कुल धन्य हो गया।", ""),
    ("#", "कलि का क्रोध"),
    (["kali_rage"], "N", "पर दूर अंधकार के महल में...", ""),
    (["kali_rage"], "Kali", "मेरे भड़काए राजा... उसी की सेना बन गए? बहुत हुआ!", ""),
    (["koka_face"], "Kali", "कोक! विकोक! अब छल नहीं... अब सीधा युद्ध होगा!", ""),
    (["vikoka"], "Vikoka", "आदेश दीजिए महाराज... कीकटपुर का राजा हमारा भक्त है। वहीं से शुरुआत करेंगे।", ""),
    (["army"], "N", "कीकटपुर का अधर्मी राजा कौन है? और कल्कि का पहला धर्मयुद्ध कैसा होगा? देखिए अगले भाग में।", ""),
]

TALK = {}
MUSIC_PLAN = [(0.0, "Echoes of Time v2.mp3", 0.0), ("ocean_ride", "Heroic Age.mp3", 0.0),
              ("rival_kings", "Darkest Child.mp3", 30.0), ("kings_attack", "Volatile Reaction.mp3", 0.0),
              ("simhala_palace", "Ossuary 6 - Air.mp3", 30.0), ("curse_break", "Echoes of Time v2.mp3", 229.0),
              ("wedding_mandap", "Lord of the Land.mp3", 0.0), ("kali_rage", "Five Armies.mp3", 0.0)]
MUSIC_CREDIT = ('"Echoes of Time v2", "Heroic Age", "Darkest Child", "Volatile Reaction", "Ossuary 6 - Air", '
                '"Lord of the Land", "Five Armies" - Kevin MacLeod (incompetech.com). Licensed under Creative Commons: '
                "By Attribution 4.0 License (CC BY 4.0)")

THUMB = dict(image="lotus_garden_meet", zoom=1.0, pany=0.0,
             text=[("श्राप टूट गया!", 150, (255, 214, 60), 150), ("कल्कि और पद्मावती", 100, (255, 255, 255), 290)])

SEO = dict(
    title="कल्कि और पद्मावती का विवाह 💍 कैसे टूटा श्राप? | Kalki Avatar Full Story | Kalki Puran भाग 5",
    description=ks.description(
        "कल्कि और पद्मावती का विवाह कैसे हुआ? पद्मावती का श्राप कैसे टूटा? Kalki Puran की पूरी कहानी, भाग 5।",
        "कल्कि देवदत्त पर सवार होकर समुद्र पार सिंहल पहुँचते हैं। कलि के बहकाए राजा रास्ता रोकते हैं, पर कल्कि बिना "
        "खून बहाए उन्हें हरा देते हैं। फिर कमल के बगीचे में पद्मावती से पहली भेंट... स्त्री बने राजाओं का श्राप टूटता है, "
        "भव्य विवाह होता है, और विश्वकर्मा शंभल को सोने का नगर बना देते हैं।",
        "Kalki crosses the ocean to Simhala, defeats the kings incited by Kali without bloodshed, frees the cursed kings "
        "and marries Padmavati; Vishwakarma turns Shambhala into a golden city. Part 5 of our cinematic Kalki series.", 5),
    tags=ks.tags(["kalki padmavati", "kalki padmavati vivah", "padmavati", "kalki wife", "simhala", "vishwakarma",
                  "पद्मावती", "कल्कि विवाह"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "lotus_garden_meet", "to": "queen_kaumudi"}, hook="देखते ही क्या हुआ?", hook2=SERIES,
         music=[(0.0, "Ossuary 6 - Air.mp3", 30.0)],
         seo=dict(title="जिसे देखते ही राजा स्त्री बन जाते थे... कल्कि ने देखा तो? 😱 #shorts #kalki #padmavati",
                  description=ks.short_description("पद्मावती को देखने वाला हर पुरुष स्त्री बन जाता था... पर जब "
                                                   "कल्कि ने उन्हें देखा, तो जो हुआ उसे देखकर पूरा महल हैरान रह गया!"),
                  tags=ks.tags(["kalki padmavati", "padmavati", "shorts", "kalki shorts"]), categoryId="24")),
]
