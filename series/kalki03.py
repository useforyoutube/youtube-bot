"""KALKI series - Episode 3: Mahadev ka Vardan (~8 min, Hindi). Based on the Kalki Purana (Kalki worships Shiva,
receives the horse Devadatta, the parrot Shuka and the jewelled sword), with dramatized scenes."""
import kalki_seo as ks
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT, STYLE
from kalki02 import VOICES as V2, SPEAKERS as S2, YOUNG

SERIES = "कल्कि • भाग 3"
PLAYLIST = "kalki_hi"
HOOK = "महादेव का वरदान"
HOOK2 = "दिव्य खड्ग, देवदत्त और शुक"
NEXT = "भाग 4: शुक की यात्रा और राजकुमारी पद्मावती"

VOICES = dict(V2, Shiva=("hi-IN-MadhurNeural", "-16%", "-26Hz", "divine"),
              Parvati=("hi-IN-SwaraNeural", "-10%", "+0Hz", "divine"),
              Shuka=("hi-IN-SwaraNeural", "+4%", "+38Hz", "soft"))
SPEAKERS = dict(S2, Shiva=("महादेव", (150, 210, 255)), Parvati=("माता पार्वती", (255, 170, 190)),
                Shuka=("शुक", (150, 240, 150)))

IMAGES = [
    ("kalki_young_face", None), ("kailash_far", None), ("shiva", None), ("horse", None), ("kalki", None),
    ("parashurama_face", None), ("shambhala", None), ("sumati_face", None), ("vy_face", None), ("brothers", None),
    ("kali", None), ("kali_smile", None), ("koka_face", None), ("vikoka", None), ("lightning", None),
    ("flowers_rain", None), ("stars_align", None), ("blessing_light", None),
    ("kailash_climb", YOUNG + " climbing an icy slope toward Mount Kailash through a blizzard, epic wide shot"),
    ("shiva_temple", "an ancient Shiva temple with a glowing shivling under a bilva tree in the snow, bells, mist"),
    ("kalki_tapasya", YOUNG + " meditating in deep snow before a shivling, snow covering his shoulders, glowing aura"),
    ("third_eye", "close up of Lord Shiva's third eye opening with blazing white-blue divine light, cosmic"),
    ("shiva_appear", "Lord Shiva and Goddess Parvati appearing in divine light above Mount Kailash with Nandi the "
                     "bull, cosmic sky"),
    ("shiva_face", "Lord Shiva with blue skin, third eye, crescent moon and matted hair, serene smile, close up face, "
                   "front view"),
    ("parvati_face", "Goddess Parvati in a red saree with gold jewelry, kind motherly smile, close up face, "
                     "front view"),
    ("garuda_horse", "Garuda the divine eagle transforming into a radiant white horse in an explosion of golden light"),
    ("shuka", "a wise green parrot with golden glowing eyes perched on a jeweled branch, divine aura"),
    ("sword_close", "a jeweled divine sword glowing with blue-white fire floating in the air, close up, sparks"),
    ("kalki_sword_raise", YOUNG + " raising a glowing jeweled sword to the sky on a mountain peak, lightning"),
    ("ride_first", YOUNG + " riding a radiant white horse galloping across a Himalayan valley at sunrise"),
    ("koka_ambush", "demons ambushing in a narrow mountain pass at night led by a giant red demon with tusks, torches"),
    ("battle_pass", YOUNG + " on a white horse slashing through demons with a blazing sword in a mountain pass, "
                    "sparks"),
    ("koka_cut", "a giant red demon struck down by a blazing sword, explosion of light, dramatic"),
    ("koka_revive", "a grey demon touching a fallen giant red demon with purple magic, the red demon's eyes opening "
                    "again, dark ritual"),
    ("shambhala_return", "villagers welcoming a young warrior on a white horse at a Himalayan village gate with "
                         "flowers and lamps"),
    ("mother_son", "an Indian mother hugging her grown warrior son with tears of joy inside a village hut, oil lamps"),
    ("padmavati_glimpse", "a beautiful Indian princess in a palace garden on an island, sad eyes, lotus pond, "
                          "moonlight"),
]

LINES = [
    ("#", "पिछले भाग में"),
    (["kalki_young_face"], "N", "पिछले भाग में... परशुराम से शिक्षा पाकर कल्कि एक महान योद्धा बन चुके थे।", ""),
    (["blessing_light"], "N", "गुरु दक्षिणा में उन्होंने तीन वचन दिए... और पहला वचन था... महादेव का आशीर्वाद।", ""),
    ("#", "कैलाश की ओर"),
    (["kailash_far"], "N", "दूर क्षितिज पर चमक रहा था... कैलाश पर्वत।", ""),
    (["kailash_climb"], "N", "बर्फ़ीले तूफ़ान... जमी हुई चट्टानें... पर कल्कि रुके नहीं।", ""),
    (["kailash_climb"], "N", "कई बार पैर फिसले... हाथ बर्फ़ से सुन्न हो गए...", ""),
    (["kalki_young_face"], "Kalki", "गुरुदेव का पहला वचन... मुझे हर हाल में पूरा करना है।", ""),
    (["shiva_temple"], "N", "कैलाश की तलहटी में मिला एक प्राचीन शिव मंदिर... बेल के पेड़ के नीचे।", ""),
    (["kalki_young_face"], "Kalki", "हे महादेव... मैं यहीं बैठूँगा, जब तक आप दर्शन नहीं देते।", ""),
    (["shuka"], "N", "कहते हैं... महादेव भोले हैं, पर उनकी परीक्षा उतनी ही कठिन होती है।", ""),
    ("#", "कठोर तपस्या"),
    (["kalki_tapasya"], "N", "कल्कि ध्यान में बैठ गए... ॐ नमः शिवाय।", ""),
    (["kalki_tapasya"], "N", "दिन बीते... महीने बीते... बर्फ़ उनके कंधों पर जमती रही।", ""),
    (["stars_align"], "N", "पर उनका ध्यान... एक पल के लिए भी नहीं टूटा।", ""),
    (["sumati_face"], "N", "दूर शंभल में माँ सुमति... हर रात बेटे के लिए दीया जलातीं।", ""),
    (["sumati_face"], "Sumati", "हे महादेव... मेरे बच्चे की रक्षा करना।", ""),
    (["kali"], "N", "उधर कलि को भी खबर लग गई...", ""),
    (["kali_smile"], "Kali", "महादेव से वरदान माँग रहा है? तपस्या तोड़ो उसकी... किसी भी तरह!", ""),
    (["lightning"], "N", "कैलाश पर काले तूफ़ान उठे... बिजलियाँ गिरीं...", "thunder"),
    (["kalki_tapasya"], "N", "पर कल्कि की तपस्या के तेज़ के आगे... तूफ़ान भी शांत हो गया।", ""),
    (["kalki_tapasya"], "N", "कलि की हर चाल... उस ध्यान की अग्नि में जलकर राख हो गई।", ""),
    ("#", "महादेव के दर्शन"),
    (["third_eye"], "N", "और फिर एक रात... आकाश में एक नेत्र खुला।", "thunder"),
    (["shiva_appear"], "N", "भगवान शिव और माता पार्वती... नंदी के साथ प्रकट हुए।", ""),
    (["shiva_face"], "Shiva", "उठो कल्कि... तुम्हारी तपस्या से मैं प्रसन्न हूँ।", ""),
    (["kalki_young_face"], "Kalki", "हे महादेव... मुझे कलि का अंत करने की शक्ति दीजिए।", ""),
    (["parvati_face"], "Parvati", "पुत्र... शक्ति तो तुम्हारे भीतर ही है। हम तुम्हें बस उसके साधन देंगे।", ""),
    (["shiva_face"], "Shiva", "कलि से युद्ध केवल बल से नहीं जीता जाएगा... उसके लिए गति, ज्ञान और तेज, तीनों चाहिए।", ""),
    ("#", "तीन दिव्य उपहार"),
    (["shiva_face"], "Shiva", "पहला उपहार... देवदत्त।", ""),
    (["garuda_horse"], "N", "गरुड़ देव ने अपना रूप बदला... और बन गए एक दिव्य सफ़ेद घोड़ा।", ""),
    (["horse"], "N", "देवदत्त... जो हवा से तेज़ दौड़ता था... और जिसे कोई अस्त्र छू नहीं सकता था।", ""),
    (["shiva_face"], "Shiva", "दूसरा उपहार... शुक।", ""),
    (["shuka"], "N", "एक हरा तोता... जो भूत, भविष्य और वर्तमान... सब जानता था।", ""),
    (["shuka"], "N", "कहते हैं... शुक ने ही वेदों को सबसे पहले सुना था।", ""),
    (["shuka"], "Shuka", "प्रणाम प्रभु... आज से मैं आपकी आँख और कान बनूँगा।", ""),
    (["shiva"], "Shiva", "और तीसरा उपहार... यह रत्नजड़ित खड्ग।", ""),
    (["sword_close"], "N", "एक ऐसी तलवार... जिसकी चमक से अंधकार भी काँप उठे।", ""),
    (["kalki_sword_raise"], "N", "कल्कि ने जैसे ही खड्ग उठाया... आकाश गरज उठा।", "thunder"),
    (["kalki_young_face"], "Kalki", "हे महादेव... यह खड्ग केवल धर्म की रक्षा के लिए उठेगा। यह मेरा वचन है।", ""),
    (["shiva_face"], "Shiva", "जाओ कल्कि... धर्म की स्थापना करो। मेरा आशीर्वाद सदा तुम्हारे साथ है।", ""),
    (["flowers_rain"], "N", "देवताओं ने फूल बरसाए... और महादेव अंतर्ध्यान हो गए।", ""),
    ("#", "पहली सवारी"),
    (["ride_first"], "N", "कल्कि देवदत्त पर सवार हुए... और घर की ओर चल पड़े।", ""),
    (["ride_first"], "N", "पहाड़, नदियाँ, जंगल... सब पलक झपकते पीछे छूटने लगे।", ""),
    (["horse"], "N", "देवदत्त के खुरों से चिंगारियाँ निकलतीं... और हवा उसके पीछे छूट जाती।", ""),
    (["kalki_young_face"], "Kalki", "देवदत्त... तुम सच में गरुड़ जितने तेज़ हो।", ""),
    (["shuka"], "Shuka", "प्रभु... सावधान! आगे घाटी में कोई छिपा है।", ""),
    ("#", "कोक का हमला"),
    (["koka_ambush"], "N", "घाटी में घात लगाए बैठा था... कलि का सबसे क्रूर सेनापति, कोक।", ""),
    (["koka_face"], "Koka", "विकोक भाग गया था... पर मैं नहीं भागूँगा! आज तेरा सिर कलि के चरणों में होगा!", ""),
    (["koka_ambush"], "N", "हज़ारों असुर... चारों ओर से टूट पड़े।", ""),
    (["battle_pass"], "N", "पर देवदत्त पर सवार कल्कि... तूफ़ान बन गए।", ""),
    (["battle_pass"], "N", "रत्नजड़ित खड्ग चमका... और असुर कटते चले गए।", ""),
    (["koka_face"], "Koka", "असंभव! एक मनुष्य... इतना शक्तिशाली कैसे?", ""),
    (["kalki_young_face"], "Kalki", "मैं अकेला नहीं हूँ कोक... मेरे साथ महादेव का आशीर्वाद है।", ""),
    (["battle_pass"], "N", "देवदत्त ने हवा में छलांग लगाई... और कल्कि सीधे कोक के सामने पहुँच गए।", ""),
    (["koka_cut"], "N", "आख़िरी वार कोक पर हुआ... और वो धरती पर गिर पड़ा।", "thunder"),
    (["kalki_young_face"], "Kalki", "जा... कलि से कहना, उसका समय पूरा हो रहा है।", ""),
    ("#", "कोक-विकोक का रहस्य"),
    (["vikoka"], "N", "पर तभी... अंधेरे से निकला विकोक।", ""),
    (["koka_revive"], "N", "उसने कोक के शरीर को छुआ... और कोक की आँखें फिर से खुल गईं!", "thunder"),
    (["shuka"], "Shuka", "प्रभु! यही इनका रहस्य है... जब तक दोनों में से एक ज़िंदा है, दूसरा मर नहीं सकता!", ""),
    (["koka_face"], "Koka", "हा हा हा! हमें कोई नहीं मार सकता... फिर मिलेंगे, अवतार!", ""),
    (["kalki_young_face"], "N", "दोनों असुर अंधेरे में गायब हो गए... और कल्कि सोच में पड़ गए।", ""),
    (["kalki_young_face"], "Kalki", "दोनों को... एक साथ मारना होगा।", ""),
    (["shuka"], "Shuka", "पर प्रभु... उसके लिए सही समय आने तक प्रतीक्षा करनी होगी।", ""),
    ("#", "घर वापसी"),
    (["shambhala_return"], "N", "कई वर्षों बाद... कल्कि शंभल लौटे।", ""),
    (["shambhala_return"], "N", "पूरा गाँव फूल और दीये लेकर... उनके स्वागत में खड़ा था।", ""),
    (["mother_son"], "N", "माँ सुमति ने बेटे को गले लगा लिया...", ""),
    (["mother_son"], "N", "वर्षों की प्रतीक्षा... आँसुओं में बह निकली।", ""),
    (["sumati_face"], "Sumati", "मेरा लाल... सच में धर्म का सूरज बनकर लौटा है।", ""),
    (["vy_face"], "Vishnuyasha", "आज मेरा जीवन सफल हो गया बेटा।", ""),
    (["brothers"], "N", "भाई कवि, प्राज्ञ और सुमंत्रक भी... ख़ुशी से झूम उठे।", ""),
    (["shambhala"], "N", "उस रात शंभल में... वर्षों बाद उत्सव मना।", ""),
    (["kalki_young_face"], "N", "पर कल्कि जानते थे... यह शांति कुछ ही दिनों की है।", ""),
    ("#", "शुक की कहानी"),
    (["shuka"], "N", "उस रात... शुक ने कल्कि को एक कहानी सुनाई।", ""),
    (["shuka"], "Shuka", "प्रभु... समुद्र के पार सिंहल द्वीप पर एक राजकुमारी है... पद्मावती।", ""),
    (["padmavati_glimpse"], "Shuka", "वो महादेव की परम भक्त है... पर उसे एक ऐसा वरदान मिला है, जो श्राप बन गया है।", ""),
    (["padmavati_glimpse"], "Shuka", "जो भी पुरुष उसे विवाह की इच्छा से देखता है... वो स्त्री बन जाता है!", ""),
    (["kalki_young_face"], "Kalki", "क्या? ऐसा कैसा वरदान?", ""),
    (["padmavati_glimpse"], "N", "कौन है पद्मावती? और क्या है उसके वरदान का रहस्य? देखिए अगले भाग में... शुक की यात्रा।", ""),
]

TALK = {}
MUSIC_PLAN = [(0.0, "Echoes of Time v2.mp3", 0.0), ("kailash_climb", "Lightless Dawn.mp3", 60.0),
              ("third_eye", "Echoes of Time v2.mp3", 229.0), ("ride_first", "Heroic Age.mp3", 0.0),
              ("koka_ambush", "Volatile Reaction.mp3", 0.0), ("vikoka", "Darkest Child.mp3", 0.0),
              ("shambhala_return", "Ossuary 6 - Air.mp3", 30.0), ("padmavati_glimpse", "Lord of the Land.mp3", 0.0)]
MUSIC_CREDIT = ('"Echoes of Time v2", "Lightless Dawn", "Heroic Age", "Volatile Reaction", "Darkest Child", '
                '"Ossuary 6 - Air", "Lord of the Land" - Kevin MacLeod (incompetech.com). Licensed under Creative '
                "Commons: By Attribution 4.0 License (CC BY 4.0)")

THUMB = dict(image="shiva_face", zoom=1.0, pany=0.0,
             text=[("महादेव का वरदान!", 140, (255, 214, 60), 150), ("कल्कि को मिले 3 दिव्य उपहार", 90, (255, 255, 255), 285)])

SEO = dict(
    title="महादेव ने कल्कि को क्या वरदान दिया? 🔱 देवदत्त, शुक और दिव्य खड्ग | Kalki Avatar | Kalki Puran भाग 3",
    description=ks.description(
        "महादेव ने कल्कि को क्या वरदान दिया? कल्कि का घोड़ा देवदत्त, तोता शुक और रत्नजड़ित खड्ग कहाँ से आए? "
        "Kalki Puran की पूरी कहानी, भाग 3।",
        "कैलाश पर कल्कि की कठोर तपस्या... भगवान शिव और माता पार्वती के दर्शन... और तीन दिव्य उपहार: गरुड़ से बना "
        "सफ़ेद घोड़ा देवदत्त, सब कुछ जानने वाला तोता शुक, और रत्नजड़ित खड्ग। फिर घाटी में कोक का हमला, और खुलता है "
        "कोक-विकोक का रहस्य!",
        "Kalki's penance at Mount Kailash, the blessings of Lord Shiva and Goddess Parvati - the white horse Devadatta, "
        "the all-knowing parrot Shuka and the jewelled sword - and the secret of the demons Koka and Vikoka. "
        "Part 3 of our cinematic Kalki series.", 3),
    tags=ks.tags(["kalki mahadev", "shiva kalki", "devadatta horse", "kalki sword", "shuka parrot", "koka vikoka",
                  "महादेव का वरदान", "देवदत्त"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "shiva_face", "to": "kalki_sword_raise"}, hook="महादेव के 3 उपहार", hook2=SERIES,
         music=[(0.0, "Echoes of Time v2.mp3", 215.0)],
         seo=dict(title="महादेव ने कल्कि को दिए 3 दिव्य उपहार 🔱 #shorts #kalki #mahadev",
                  description=ks.short_description("कैलाश पर तपस्या से प्रसन्न होकर महादेव ने कल्कि को दिए: "
                                                   "घोड़ा देवदत्त, तोता शुक और रत्नजड़ित खड्ग!"),
                  tags=ks.tags(["kalki mahadev", "devadatta", "shuka", "shorts", "kalki shorts"]), categoryId="24")),
    dict(**{"from": "vikoka", "to": "kalki_young_face"}, hook="ये असुर मर क्यों नहीं सकते?", hook2=SERIES,
         music=[(0.0, "Darkest Child.mp3", 0.0)],
         seo=dict(title="कोक-विकोक: वो असुर जो मरकर भी ज़िंदा हो जाते थे 😱 #shorts #kalki #kalkipuran",
                  description=ks.short_description("कल्कि ने कोक को मार गिराया... पर विकोक के छूते ही वो फिर "
                                                   "ज़िंदा हो गया! क्या है कोक-विकोक का रहस्य?"),
                  tags=ks.tags(["koka vikoka", "kalki puran", "shorts", "kalki shorts"]), categoryId="24")),
]
