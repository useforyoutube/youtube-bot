"""KALKI series - Episode 7: Koka-Vikoka ka Ant (~8 min, Hindi). Based on the Kalki Purana (the demon brothers
Koka and Vikoka, protected by Brahma's boon, can only die together - Kalki slays both at once), dramatized."""
import kalki_seo as ks
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT, STYLE, KALI
from kalki02 import YOUNG
from kalki06 import VOICES as V6, SPEAKERS as S6, PV

SERIES = "कल्कि • भाग 7"
PLAYLIST = "kalki_hi"
HOOK = "कोक-विकोक का अंत"
HOOK2 = "वो असुर जो मरकर भी ज़िंदा हो जाते थे"
NEXT = "भाग 8: कलि की बहन दुरुक्ति"

KOKA = "Koka, a giant red-skinned demon with tusks, burning eyes and a huge spear"
VIKOKA = "Vikoka, a sly giant grey-skinned demon with tusks, yellow snake eyes and a massive mace"
VOICES = dict(V6, Durukti=("hi-IN-SwaraNeural", "-12%", "-30Hz", "demon"))
SPEAKERS = dict(S6, Durukti=("दुरुक्ति", (230, 120, 200)))

IMAGES = [
    ("koka_face", None), ("vikoka", None), ("koka_revive", None), ("kalki_young_face", None), ("kalki_smile", None),
    ("pv_warrior", None), ("brothers", None), ("horse", None), ("kalki", None), ("shuka", None), ("brahma", None),
    ("kali", None), ("kali_smile", None), ("kali_mirror", None), ("golden_shambhala", None), ("army_march", None),
    ("flowers_rain", None), ("dawn", None), ("lightning", None),
    ("brahma_boon_past", "Lord Brahma on a lotus granting a glowing boon to two kneeling demon brothers, one red one "
                         "grey, ancient cosmic temple"),
    ("demon_brothers", KOKA + " and " + VIKOKA + " standing together on a burning cliff, demon army behind, epic"),
    ("burning_villages", "demons burning villages at night, people fleeing, smoke and fire across the valley"),
    ("black_valley", "a dark rocky valley with jagged black stones under a stormy sky, two armies facing each other"),
    ("koka_vs_kalki", YOUNG + " on a white horse clashing with " + KOKA + ", sparks, dark valley"),
    ("vikoka_vs_brothers", "three young Indian warrior brothers fighting " + VIKOKA + ", dust and sparks"),
    ("koka_dead", KOKA + " lying defeated on black rocks, his spear broken"),
    ("vikoka_heal", VIKOKA + " touching a fallen red demon with purple magic, reviving him, dark ritual"),
    ("koka_rise", KOKA + " rising again from the ground with purple energy, laughing, terrifying"),
    ("army_tired", "tired wounded Indian soldiers with saffron flags resting at night by campfires, worried"),
    ("war_tent", YOUNG + " and " + PV + " planning in a war tent by lamp light, a green parrot on a map"),
    ("brahma_vision", "a vision of Lord Brahma appearing in golden smoke inside a war tent at night, blessing"),
    ("trap_plan", "warriors herding two giant demons toward each other in a narrow canyon, ropes and arrows"),
    ("pv_arrows", PV + " shooting a rain of golden arrows from a cliff in a canyon, dramatic"),
    ("demons_back", KOKA + " and " + VIKOKA + " forced back to back in a narrow canyon, surrounded"),
    ("devadatta_leap", "a radiant white horse with a young warrior leaping high into the air above two giant "
                       "demons, sword raised, slow motion, light rays"),
    ("one_strike", "a single blazing sword arc slicing through the air in an explosion of golden light between two "
                   "giant demons, epic"),
    ("demons_dust", "two giant demons dissolving into dust and embers together, golden light, canyon"),
    ("victory", "a victorious righteous army raising saffron flags and swords at sunrise in a canyon, cheering"),
    ("durukti", "Durukti, a beautiful but terrifying demon queen with dark purple skin, silver crown and glowing "
                "violet eyes, close up face, front view"),
]

LINES = [
    ("#", "पिछले भाग में"),
    (["kalki"], "N", "पिछले भाग में... कल्कि ने कीकटपुर के अत्याचारी राजा को हराकर हज़ारों लोगों को मुक्त कराया।", ""),
    (["demon_brothers"], "N", "पर अब सामने थे... कलि के दो अमर सेनापति। कोक और विकोक।", ""),
    ("#", "ब्रह्मा का वरदान"),
    (["brahma_boon_past"], "N", "युगों पहले... इन दोनों भाइयों ने ब्रह्मा जी की घोर तपस्या की थी।", ""),
    (["brahma"], "Brahma", "माँगो वत्स... क्या वरदान चाहिए?", ""),
    (["koka_face"], "Koka", "हमें अमरता चाहिए प्रभु!", ""),
    (["brahma"], "Brahma", "अमरता किसी को नहीं मिलती... पर मैं यह वर देता हूँ।", ""),
    (["brahma"], "Brahma", "जब तक तुम दोनों में से एक भी जीवित रहेगा... दूसरे को कोई नहीं मार पाएगा।", ""),
    (["demon_brothers"], "N", "बस... तभी से ये दोनों भाई, अजेय बन गए।", ""),
    (["demon_brothers"], "N", "देवताओं से लेकर राजाओं तक... किसी में इन्हें हराने का साहस नहीं था।", ""),
    (["kali_smile"], "N", "और कलि ने इन्हें बना लिया... अपना दाहिना और बायाँ हाथ।", ""),
    ("#", "आतंक"),
    (["burning_villages"], "N", "कलि के आदेश पर... कोक और विकोक ने गाँव के गाँव जला दिए।", ""),
    (["burning_villages"], "N", "उनका एक ही संदेश था... कल्कि सामने आए, वरना पूरा देश जलेगा।", ""),
    (["vikoka"], "Vikoka", "कहाँ छिपा है वो अवतार? आ... और देख, कलि के सेनापति क्या होते हैं!", ""),
    (["kalki_young_face"], "Kalki", "बहुत हुआ... अब इनका अंत होगा।", ""),
    (["shuka"], "Shuka", "प्रभु... याद है? ये दोनों एक-दूसरे को ज़िंदा कर देते हैं।", ""),
    (["kalki_young_face"], "Kalki", "याद है शुक... पर हर ताले की एक चाबी होती है। हम उसे ढूँढ लेंगे।", ""),
    (["army_march"], "N", "धर्म की सेना... एक बार फिर निकल पड़ी।", ""),
    ("#", "काली घाटी का युद्ध"),
    (["black_valley"], "N", "काली चट्टानों की घाटी में... दोनों सेनाएँ आमने-सामने थीं।", ""),
    (["demon_brothers"], "Koka", "पिछली बार तू बच गया था... इस बार नहीं!", ""),
    (["koka_vs_kalki"], "N", "कल्कि और कोक भिड़ गए...", "thunder"),
    (["vikoka_vs_brothers"], "N", "और विकोक से लड़ रहे थे... कल्कि के तीनों भाई।", ""),
    (["vikoka_vs_brothers"], "N", "विकोक की गदा से धरती काँपती... पर तीनों भाई डटे रहे।", ""),
    (["koka_vs_kalki"], "N", "भाले और खड्ग की टक्कर से... चट्टानें फटने लगीं।", ""),
    (["koka_dead"], "N", "एक भयानक वार... और कोक धरती पर गिर पड़ा।", "thunder"),
    (["kalki_young_face"], "N", "पर कल्कि जानते थे... यह अंत नहीं है।", ""),
    (["vikoka_heal"], "N", "विकोक दौड़ता हुआ आया... और कोक के शरीर को छुआ।", ""),
    (["koka_rise"], "N", "कोक फिर उठ खड़ा हुआ... पहले से भी ज़्यादा भयानक!", ""),
    (["koka_rise"], "Koka", "हा हा हा! कितनी बार मारेगा? हम मरकर भी लौट आते हैं!", ""),
    (["vikoka_vs_brothers"], "N", "पूरा दिन यही चलता रहा... एक गिरता, दूसरा उसे ज़िंदा कर देता।", ""),
    (["koka_dead"], "N", "कल्कि ने कोक को तीन बार गिराया... और तीनों बार वो लौट आया।", ""),
    (["lightning"], "N", "सूरज ढलने लगा... और युद्ध का कोई अंत नहीं दिख रहा था।", ""),
    ("#", "युद्ध की रात"),
    (["army_tired"], "N", "रात हुई... धर्म की सेना थक चुकी थी। बहुत से सैनिक घायल थे।", ""),
    (["war_tent"], "N", "तंबू में कल्कि, पद्मावती और शुक... चिंता में डूबे थे।", ""),
    (["kalki_young_face"], "Kalki", "हम उनमें से एक को मारते हैं... तो दूसरा उसे बचा लेता है। दोनों को एक साथ कैसे मारें?", ""),
    (["pv_warrior"], "Padmavati", "स्वामी... ऐसे तो यह युद्ध कभी ख़त्म नहीं होगा।", ""),
    (["shuka"], "Shuka", "प्रभु... ब्रह्मा जी के वरदान में ही इसका उत्तर छिपा है।", ""),
    (["brahma_vision"], "N", "तभी तंबू में एक सुनहरा धुआँ उठा... और ब्रह्मा जी प्रकट हुए।", "thunder"),
    (["brahma"], "Brahma", "कल्कि... मेरे वरदान का अर्थ समझो। एक के रहते दूसरा नहीं मरेगा...", ""),
    (["brahma"], "Brahma", "पर अगर दोनों एक ही पल में मरें... तो कोई किसी को नहीं बचा पाएगा।", ""),
    (["kalki_smile"], "Kalki", "एक ही पल में... एक ही वार से। धन्यवाद पितामह।", ""),
    ("#", "जाल"),
    (["trap_plan"], "N", "अगली सुबह... कल्कि ने एक योजना बनाई।", ""),
    (["trap_plan"], "N", "भाइयों और राजाओं ने... दोनों असुरों को एक तंग घाटी की ओर धकेलना शुरू किया।", ""),
    (["pv_arrows"], "N", "पहाड़ी पर खड़ी पद्मावती ने... तीरों की बारिश कर दी।", ""),
    (["demons_back"], "N", "तीरों से बचते-बचते... कोक और विकोक, पीठ से पीठ सटाकर खड़े हो गए।", ""),
    (["demons_back"], "Vikoka", "भाई... ये हमें घेर रहे हैं!", ""),
    (["brothers"], "N", "कल्कि के भाइयों ने रस्सियाँ और भाले लेकर... घाटी के दोनों रास्ते बंद कर दिए।", ""),
    (["koka_face"], "Koka", "डर मत... हमें कोई नहीं मार सकता!", ""),
    ("#", "एक वार"),
    (["horse"], "N", "तभी... आकाश में एक सफ़ेद चमक दिखी।", ""),
    (["devadatta_leap"], "N", "देवदत्त ने आकाश में छलांग लगाई... और कल्कि ने खड्ग उठाया।", "thunder"),
    (["kalki_young_face"], "Kalki", "जय महादेव!", ""),
    (["one_strike"], "N", "एक ही वार... एक ही पल...", "thunder"),
    (["demons_dust"], "N", "और कोक-विकोक... दोनों एक साथ धूल बनकर बिखर गए।", ""),
    (["demons_dust"], "N", "इस बार... कोई किसी को बचाने वाला नहीं बचा था।", ""),
    ("#", "विजय"),
    (["victory"], "N", "पूरी घाटी जयकारों से गूँज उठी... जय श्री कल्कि!", ""),
    (["brothers"], "N", "भाई कवि ने दौड़कर कल्कि को गले लगा लिया।", ""),
    (["victory"], "N", "जिन असुरों से देवता भी डरते थे... आज उनका अंत हो चुका था।", ""),
    (["flowers_rain"], "N", "आकाश से देवताओं ने फूल बरसाए...", ""),
    (["pv_warrior"], "Padmavati", "आपने कर दिखाया स्वामी!", ""),
    (["kalki_smile"], "Kalki", "यह हम सबकी जीत है देवी... और ब्रह्मा जी के ज्ञान की।", ""),
    (["dawn"], "N", "बर्बाद हुए गाँवों में... फिर से जीवन लौटने लगा।", ""),
    ("#", "कलि की नई चाल"),
    (["kali_mirror"], "N", "पर अंधकार के महल में... कलि का दर्पण चटक गया।", "thunder"),
    (["kali"], "Kali", "मेरे सबसे शक्तिशाली सेनापति... एक वार में?", ""),
    (["kali_smile"], "Kali", "तो अब... मेरी बहन को जगाने का समय आ गया है।", ""),
    (["durukti"], "N", "अंधेरे से निकली एक स्त्री... बैंगनी आँखें, चाँदी का मुकुट...", ""),
    (["durukti"], "Durukti", "भैया... तलवार से नहीं, मैं उसे उसके अपनों से हराऊँगी।", ""),
    (["golden_shambhala"], "N", "कौन है दुरुक्ति? और शंभल पर कौन सा संकट आने वाला है? देखिए अगले भाग में।", ""),
]

TALK = {}
MUSIC_PLAN = [(0.0, "Darkest Child.mp3", 0.0), ("brahma_boon_past", "Lightless Dawn.mp3", 60.0),
              ("burning_villages", "Darkest Child.mp3", 120.0), ("black_valley", "Volatile Reaction.mp3", 0.0),
              ("army_tired", "Echoes of Time v2.mp3", 0.0), ("trap_plan", "Heroic Age.mp3", 0.0),
              ("devadatta_leap", "Echoes of Time v2.mp3", 229.0), ("victory", "Five Armies.mp3", 60.0),
              ("kali_mirror", "Lightless Dawn.mp3", 120.0)]
MUSIC_CREDIT = ('"Darkest Child", "Lightless Dawn", "Volatile Reaction", "Echoes of Time v2", "Heroic Age", '
                '"Five Armies" - Kevin MacLeod (incompetech.com). Licensed under Creative Commons: By Attribution 4.0 '
                "License (CC BY 4.0)")

THUMB = dict(image="demon_brothers", zoom=1.0, pany=0.0,
             text=[("मरकर भी ज़िंदा!", 150, (255, 214, 60), 150), ("कोक-विकोक का अंत", 100, (255, 255, 255), 290)])

SEO = dict(
    title="वो असुर जो मरकर भी ज़िंदा हो जाते थे 😱 कोक-विकोक का अंत | Kalki vs Kali | Kalki Puran भाग 7",
    description=ks.description(
        "कोक और विकोक कौन थे? ब्रह्मा जी के वरदान से ये असुर मरकर भी ज़िंदा क्यों हो जाते थे? कल्कि ने इन्हें कैसे "
        "मारा? Kalki Puran की पूरी कहानी, भाग 7।",
        "ब्रह्मा जी के वरदान से कोक और विकोक अजेय थे: एक के रहते दूसरा मर नहीं सकता था। काली घाटी के युद्ध में "
        "कल्कि बार-बार कोक को गिराते हैं, पर विकोक उसे फिर ज़िंदा कर देता है। फिर ब्रह्मा जी बताते हैं रहस्य... "
        "और देवदत्त की छलांग के साथ एक ही वार में दोनों का अंत!",
        "Koka and Vikoka, the demon brothers who could only die together by Brahma's boon, and how Kalki slew both "
        "with a single strike. Part 7 of our cinematic Kalki series.", 7),
    tags=ks.tags(["koka vikoka", "koka vikoka vadh", "kalki koka vikoka", "brahma boon", "kalki war",
                  "कोक विकोक", "कल्कि युद्ध"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "devadatta_leap", "to": "demons_dust", "to_last": True}, hook="एक वार, दो असुर!", hook2=SERIES,
         music=[(0.0, "Echoes of Time v2.mp3", 222.0)],
         seo=dict(title="एक ही वार में दो अमर असुरों का अंत! ⚔️ कल्कि #shorts #kalki #kalkipuran",
                  description=ks.short_description("कोक-विकोक को कोई नहीं मार सकता था... जब तक दोनों एक साथ न "
                                                   "मरें। तब कल्कि ने देवदत्त पर आकाश में छलांग लगाई..."),
                  tags=ks.tags(["koka vikoka", "kalki war", "shorts", "kalki shorts"]), categoryId="24")),
]
