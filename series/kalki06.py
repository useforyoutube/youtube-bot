"""KALKI series - Episode 6: Kikatpur ka Adharmi Raja (~8 min, Hindi). Inspired by the Kalki Purana's war at
Kikatapura; the tyrant king Durmati is a dramatized, fictional character serving Kali."""
import kalki_seo as ks
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT, STYLE, KALI
from kalki02 import YOUNG
from kalki05 import VOICES as V5, SPEAKERS as S5, PV

SERIES = "कल्कि • भाग 6"
PLAYLIST = "kalki_hi"
HOOK = "कीकटपुर का अधर्मी राजा"
HOOK2 = "कल्कि का पहला धर्मयुद्ध"
NEXT = "भाग 7: कोक-विकोक का अंत"

TYRANT = "Durmati, a cruel tyrant king with a black iron crown, red eyes and a scarred face"
VOICES = dict(V5, Durmati=("hi-IN-MadhurNeural", "-6%", "-30Hz", "demon"),
              Villager=("hi-IN-SwaraNeural", "-4%", "-2Hz", "soft"),
              Kavi=("hi-IN-MadhurNeural", "+2%", "+0Hz", "soft"))
SPEAKERS = dict(S5, Durmati=("राजा दुर्मति", (255, 110, 100)), Villager=("एक माँ", (255, 200, 170)),
                Kavi=("कवि", (220, 220, 170)))

IMAGES = [
    ("golden_shambhala", None), ("kalki_young_face", None), ("kalki_smile", None), ("pv_shy", None),
    ("padmavati_face", None), ("kings_freed", None), ("brothers", None), ("horse", None), ("kali", None),
    ("kali_smile", None), ("vikoka", None), ("koka_face", None), ("kalki", None), ("shuka", None),
    ("lightning", None), ("dawn", None), ("flowers_rain", None),
    ("refugees", "ragged Indian villagers, women and children arriving at a golden city gate, exhausted, crying, dusk"),
    ("refugee_mother", "a poor Indian mother holding her child, tearful desperate face, close up, front view"),
    ("kikatpur", "a dark fortress city with black walls and burning watchtowers under a red sky, iron gates"),
    ("durmati_throne", TYRANT + " on an iron throne surrounded by skulls and torches, dark hall"),
    ("durmati_face", TYRANT + ", evil grin, close up face, front view, torchlight"),
    ("slaves", "chained Indian villagers forced to build a dark fortress under whips, smoke, misery"),
    ("temple_burn", "soldiers in black armor burning a small village temple at night, people crying"),
    ("war_council", "a young Indian warrior prince with allied kings and brothers around a war map table, lamps, "
                    "golden palace"),
    ("pv_warrior", PV + " in golden armor holding a bow, determined face, close up, front view"),
    ("army_march", "a righteous army with saffron flags, cavalry and elephants marching through a valley at dawn, "
                   "epic wide shot"),
    ("kikat_army", "a vast army in black armor with red banners lined up before a dark fortress, torches"),
    ("battle_field", "two great armies clashing on a battlefield, saffron flags against black banners, dust and "
                     "arrows, epic"),
    ("kalki_charge", YOUNG + " charging on a radiant white horse with a blazing sword through enemy lines, epic"),
    ("black_magic", TYRANT + " casting dark purple black magic, shadow creatures rising from the ground"),
    ("shadow_beasts", "monstrous shadow beasts with glowing red eyes attacking soldiers on a battlefield"),
    ("agni_astra", "a young warrior releasing a fire arrow that bursts into a giant blazing bird destroying "
                   "shadow beasts"),
    ("duel", YOUNG + " fighting " + TYRANT + " sword to sword in front of a burning fortress gate, sparks"),
    ("durmati_fall", "a tyrant king with a black iron crown falling defeated to his knees, crown rolling on the ground"),
    ("chains_break", "chains breaking off the hands of freed villagers in golden light, joy and tears"),
    ("temple_rebuilt", "villagers relighting lamps in a rebuilt temple at sunrise, conch shells, hope"),
    ("kali_mirror", KALI + " watching a battle in a dark magical mirror, furious"),
]

LINES = [
    ("#", "पिछले भाग में"),
    (["padmavati_face"], "N", "पिछले भाग में... कल्कि और पद्मावती का विवाह हुआ, और शंभल बन गया सोने का नगर।", ""),
    (["kali"], "N", "पर कलि ने अपने सबसे वफ़ादार राजा को आदेश दे दिया था... कीकटपुर के दुर्मति को।", ""),
    ("#", "शंभल के द्वार पर"),
    (["golden_shambhala"], "N", "एक शाम... शंभल के सुनहरे द्वार पर कुछ लोग आकर गिर पड़े।", ""),
    (["refugees"], "N", "फटे कपड़े... ख़ाली पेट... और आँखों में डर।", ""),
    (["refugee_mother"], "Villager", "बचा लीजिए प्रभु... हम कीकटपुर से भागकर आए हैं।", ""),
    (["kalki_young_face"], "Kalki", "डरिए मत माँ... यहाँ आप सुरक्षित हैं। बताइए, क्या हुआ?", ""),
    (["refugee_mother"], "Villager", "हम सात दिन से भूखे-प्यासे चल रहे हैं... रास्ते में कितने ही लोग गिर गए।", ""),
    (["padmavati_face"], "N", "पद्मावती ने तुरंत उनके लिए भोजन और वस्त्र मँगवाए।", ""),
    (["refugee_mother"], "Villager", "राजा दुर्मति ने पूजा पर रोक लगा दी है... मंदिर जला दिए हैं...", ""),
    (["refugee_mother"], "Villager", "और जो उसका विरोध करता है... उसे ज़ंजीरों में बाँधकर क़िले बनवाता है।", ""),
    (["kalki_young_face"], "N", "कल्कि की मुट्ठियाँ भिंच गईं... आँखों में आग जल उठी।", ""),
    (["kalki_young_face"], "Kalki", "गुरुदेव का दूसरा वचन... अधर्मी राजाओं को हराना। उसका समय आ गया है।", ""),
    ("#", "कीकटपुर का अंधकार"),
    (["kikatpur"], "N", "कीकटपुर... काली दीवारों का नगर, जहाँ सूरज भी डरकर उगता था।", ""),
    (["durmati_throne"], "N", "और उसके लोहे के सिंहासन पर बैठा था... राजा दुर्मति।", ""),
    (["durmati_face"], "Durmati", "इस राज्य में केवल एक भगवान है... कलि! और उसका सेवक... मैं!", ""),
    (["slaves"], "N", "हज़ारों लोग ज़ंजीरों में बँधे... दिन-रात पत्थर ढोते।", ""),
    (["slaves"], "N", "बच्चों से भी काम करवाया जाता... और जो गिर जाता, उसे कोड़े पड़ते।", ""),
    (["temple_burn"], "N", "जहाँ भी कोई दीया जलाता... वहाँ उसके सैनिक आग लगा देते।", ""),
    (["durmati_throne"], "N", "कहते हैं... दुर्मति ने कलि से काली विद्या सीखी थी। रात में वो छायाओं से बातें करता था।", ""),
    (["durmati_face"], "Durmati", "सुना है शंभल में कोई अवतार पैदा हुआ है? उसे भी ज़ंजीरों में देखना चाहता हूँ।", ""),
    ("#", "युद्ध की सभा"),
    (["war_council"], "N", "शंभल के राजमहल में... युद्ध की सभा बैठी।", ""),
    (["kings_freed"], "N", "वो राजा भी आए... जिन्हें कल्कि ने सिंहल में श्राप से मुक्त किया था।", ""),
    (["brothers"], "Kavi", "भैया... हम तीनों भाई भी आपके साथ लड़ेंगे।", ""),
    (["pv_warrior"], "Padmavati", "और मैं भी, स्वामी। लक्ष्मी केवल धन नहीं... शक्ति भी है।", ""),
    (["kalki_smile"], "Kalki", "तो चलो... अधर्म के अंधकार में धर्म का पहला दीया जलाने।", ""),
    (["kalki_young_face"], "Kalki", "पर याद रखना... हम बदला लेने नहीं, मुक्ति दिलाने जा रहे हैं। किसी निर्दोष का खून नहीं बहेगा।", ""),
    (["army_march"], "N", "अगली सुबह... भगवा ध्वजों वाली सेना कीकटपुर की ओर चल पड़ी।", ""),
    (["army_march"], "N", "रास्ते के गाँवों में लोग... फूल और दीये लेकर सेना का स्वागत करने लगे।", ""),
    (["army_march"], "N", "बहुत से युवक भी... तलवारें उठाकर सेना में शामिल हो गए।", ""),
    (["shuka"], "Shuka", "प्रभु... दुर्मति के पास काली विद्या है। सावधान रहना।", ""),
    ("#", "धर्मयुद्ध"),
    (["kikat_army"], "N", "कीकटपुर के बाहर... काले कवच वाली विशाल सेना खड़ी थी।", ""),
    (["kalki_young_face"], "Kalki", "दुर्मति! बंदियों को छोड़ दो... और युद्ध टल जाएगा।", ""),
    (["durmati_face"], "Durmati", "एक गाँव का लड़का... मुझसे युद्ध करेगा? हमला करो!", ""),
    (["battle_field"], "N", "दोनों सेनाएँ... आँधी की तरह टकराईं।", "thunder"),
    (["battle_field"], "N", "तलवारों की खनक... घोड़ों की हिनहिनाहट... और धूल का तूफ़ान।", ""),
    (["kalki_charge"], "N", "देवदत्त पर सवार कल्कि... दुश्मन की पंक्तियाँ चीरते हुए आगे बढ़े।", ""),
    (["pv_warrior"], "N", "पद्मावती के तीर... एक भी निशाना नहीं चूकते थे।", ""),
    (["brothers"], "N", "कवि, प्राज्ञ और सुमंत्रक... तीनों भाई कंधे से कंधा मिलाकर लड़ रहे थे।", ""),
    (["battle_field"], "N", "धीरे-धीरे... काले कवच वाली सेना पीछे हटने लगी।", ""),
    ("#", "काली विद्या"),
    (["black_magic"], "N", "हार देखकर दुर्मति ने... अपनी काली विद्या जगाई।", "thunder"),
    (["shadow_beasts"], "N", "धरती फटी... और उसमें से निकले छाया के राक्षस।", ""),
    (["shadow_beasts"], "N", "तलवारें उनके आर-पार निकल जातीं... उन्हें कोई अस्त्र नहीं काट पा रहा था।", ""),
    (["shadow_beasts"], "N", "सैनिक डरकर पीछे हटने लगे... धर्म की सेना बिखरने लगी।", ""),
    (["shuka"], "Shuka", "प्रभु! ये छायाएँ हैं... इन्हें केवल अग्नि का प्रकाश मिटा सकता है!", ""),
    (["kalki_young_face"], "Kalki", "अंधकार को तलवार नहीं... प्रकाश हराता है!", ""),
    (["agni_astra"], "N", "कल्कि ने आग्नेयास्त्र छोड़ा... और आकाश में एक आग का पक्षी उड़ चला!", "thunder"),
    (["agni_astra"], "N", "उसकी रोशनी में... छाया के राक्षस भाप बनकर उड़ गए।", ""),
    ("#", "आमना-सामना"),
    (["duel"], "N", "आख़िर में... कल्कि और दुर्मति आमने-सामने थे।", ""),
    (["durmati_face"], "Durmati", "कलि ने मुझे अमर होने का वचन दिया है!", ""),
    (["kalki_young_face"], "Kalki", "कलि का वचन... उसके झूठ जितना ही खोखला है।", ""),
    (["duel"], "N", "तलवारें टकराईं... चिंगारियाँ उड़ीं...", ""),
    (["duel"], "N", "दुर्मति हर वार के साथ... काली विद्या की लपटें छोड़ता।", ""),
    (["kalki_young_face"], "N", "पर कल्कि का मन शांत था... जैसे गुरु परशुराम ने सिखाया था।", ""),
    (["durmati_fall"], "N", "एक ही वार में... दुर्मति का लोहे का मुकुट धूल में जा गिरा।", "thunder"),
    (["durmati_fall"], "Durmati", "कलि... मेरी रक्षा करो! कलि!", ""),
    (["kali_mirror"], "N", "पर कलि ने... अपने सेवक की ओर देखा तक नहीं।", ""),
    (["kalki_young_face"], "Kalki", "देखा दुर्मति? अधर्म अपने सेवकों को भी नहीं बचाता।", ""),
    (["durmati_fall"], "N", "दुर्मति ने हथियार डाल दिए... और उसे बंदी बना लिया गया।", ""),
    ("#", "मुक्ति"),
    (["chains_break"], "N", "उसी पल... हज़ारों लोगों की ज़ंजीरें टूट गईं।", ""),
    (["chains_break"], "N", "माँएँ अपने बच्चों से मिलीं... बूढ़ों की आँखों में आँसू थे।", ""),
    (["temple_rebuilt"], "N", "जले हुए मंदिरों में... वर्षों बाद फिर से दीये जले।", ""),
    (["refugee_mother"], "Villager", "जय श्री कल्कि! आज हमें हमारा धर्म वापस मिल गया।", ""),
    (["dawn"], "N", "कीकटपुर पर... पहली बार सुनहरी सुबह हुई।", ""),
    ("#", "अगला तूफ़ान"),
    (["kali_mirror"], "Kali", "दुर्मति गया... कोई बात नहीं। अब असली खेल शुरू होगा।", ""),
    (["koka_face"], "N", "कलि ने अपने दो अमर सेनापतियों को... आख़िरी आदेश दिया।", ""),
    (["vikoka"], "Vikoka", "इस बार हम दोनों साथ लड़ेंगे... और हमें कोई नहीं मार सकता!", ""),
    (["kalki"], "N", "क्या कल्कि उन असुरों को हरा पाएँगे, जो मरकर भी ज़िंदा हो जाते हैं? देखिए अगले भाग में... कोक-विकोक का अंत।", ""),
]

TALK = {}
MUSIC_PLAN = [(0.0, "Lightless Dawn.mp3", 0.0), ("refugees", "Echoes of Time v2.mp3", 0.0),
              ("kikatpur", "Darkest Child.mp3", 0.0), ("war_council", "Heroic Age.mp3", 0.0),
              ("kikat_army", "Volatile Reaction.mp3", 0.0), ("black_magic", "Darkest Child.mp3", 90.0),
              ("agni_astra", "Five Armies.mp3", 0.0), ("chains_break", "Echoes of Time v2.mp3", 229.0),
              ("kali_mirror", "Lightless Dawn.mp3", 120.0)]
MUSIC_CREDIT = ('"Lightless Dawn", "Echoes of Time v2", "Darkest Child", "Heroic Age", "Volatile Reaction", '
                '"Five Armies" - Kevin MacLeod (incompetech.com). Licensed under Creative Commons: By Attribution 4.0 '
                "License (CC BY 4.0)")

THUMB = dict(image="kalki_charge", zoom=1.0, pany=0.0,
             text=[("कल्कि का पहला धर्मयुद्ध!", 130, (255, 214, 60), 150), ("काली विद्या vs आग्नेयास्त्र", 90,
                                                                         (255, 255, 255), 280)])

SEO = dict(
    title="कल्कि का पहला धर्मयुद्ध! ⚔️ काली विद्या vs आग्नेयास्त्र | Kalki vs Kali | Kalki Puran भाग 6",
    description=ks.description(
        "कल्कि का पहला धर्मयुद्ध किससे हुआ? कलि के सेवक राजा ने काली विद्या से क्या किया? Kalki Puran से प्रेरित "
        "कहानी, भाग 6।",
        "कीकटपुर के अत्याचारी राजा दुर्मति ने मंदिर जला दिए और लोगों को ज़ंजीरों में बाँध दिया। शरणार्थियों की पुकार "
        "पर कल्कि, पद्मावती, उनके भाई और मुक्त हुए राजा धर्मयुद्ध के लिए निकलते हैं। काली विद्या के छाया राक्षस, "
        "आग्नेयास्त्र का आग का पक्षी, और दुर्मति से आमना-सामना!",
        "Kalki's first war for dharma against the tyrant king of Kikatapura, a servant of Kali, and his shadow "
        "sorcery. Part 6 of our cinematic Kalki series.", 6),
    tags=ks.tags(["kalki first war", "kikatpur", "kalki war", "kalki padmavati", "agneyastra", "धर्मयुद्ध",
                  "कल्कि युद्ध"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "black_magic", "to": "agni_astra"}, hook="तलवार नहीं, प्रकाश!", hook2=SERIES,
         music=[(0.0, "Five Armies.mp3", 0.0)],
         seo=dict(title="काली विद्या के राक्षस vs कल्कि का आग्नेयास्त्र 🔥 #shorts #kalki #kalkiavatar",
                  description=ks.short_description("छाया के राक्षसों को कोई तलवार नहीं काट पा रही थी... तब "
                                                   "कल्कि ने छोड़ा आग्नेयास्त्र!"),
                  tags=ks.tags(["kalki war", "agneyastra", "shorts", "kalki shorts"]), categoryId="24")),
]
