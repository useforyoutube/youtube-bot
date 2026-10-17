"""KALKI series - Episode 4: Shuka ki Yatra aur Rajkumari Padmavati (~8 min, Hindi). Based on the Kalki Purana
(Padmavati of Simhala, Shiva's boon, the swayamvar, Shuka's message), with dramatized scenes."""
import kalki_seo as ks
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT, STYLE, KALI
from kalki02 import YOUNG
from kalki03 import VOICES as V3, SPEAKERS as S3

SERIES = "कल्कि • भाग 4"
PLAYLIST = "kalki_hi"
HOOK = "राजकुमारी पद्मावती"
HOOK2 = "वो वरदान जो श्राप बन गया"
NEXT = "भाग 5: सिंहल द्वीप और पद्मावती का स्वयंवर"

VOICES = dict(V3, Padmavati=("hi-IN-SwaraNeural", "-8%", "+4Hz", "soft"),
              King=("hi-IN-MadhurNeural", "-12%", "-14Hz", "soft"),
              Queen=("hi-IN-SwaraNeural", "-10%", "-6Hz", "soft"),
              Messenger=("hi-IN-MadhurNeural", "+0%", "-30Hz", "demon"))
SPEAKERS = dict(S3, Padmavati=("पद्मावती", (255, 190, 220)), King=("राजा बृहद्रथ", (240, 210, 150)),
                Queen=("रानी कौमुदी", (255, 200, 170)), Messenger=("असुर दूत", (200, 160, 160)))

PV = "Princess Padmavati, a beautiful young Indian princess with lotus-like eyes, long black hair and gold jewelry"

IMAGES = [
    ("shuka", None), ("kalki_young_face", None), ("padmavati_glimpse", None), ("kali", None), ("kali_smile", None),
    ("vikoka", None), ("horse", None), ("shiva_face", None), ("parvati_face", None), ("flowers_rain", None),
    ("stars_align", None), ("shambhala", None), ("sumati_face", None),
    ("ocean_flight", "a small green parrot flying over a vast ocean at sunrise, endless water, epic wide shot"),
    ("storm_sea", "a small green parrot battling a violent storm over the sea, lightning, huge waves"),
    ("hawk_chase", "a dark demonic hawk with purple glowing eyes chasing a small green parrot through storm clouds"),
    ("simhala_island", "a magnificent island kingdom with white palaces and golden domes rising from a turquoise sea"),
    ("simhala_palace", "a grand ancient Indian palace hall with carved pillars, oil lamps and courtiers"),
    ("king_brihadratha", "an old Indian king with a grey beard and golden crown, worried face, close up, front view"),
    ("queen_kaumudi", "an elegant Indian queen with jewels, tearful worried face, close up, front view"),
    ("padmavati_child", "a little Indian princess girl praying before a shivling with lotus flowers, glowing light"),
    ("padmavati_shiva", PV + " worshipping a shivling with lotus flowers in a palace temple, lamps"),
    ("shiva_boon", "Lord Shiva and Goddess Parvati appearing in divine light before a young princess in a palace "
                   "temple, blessing her"),
    ("padmavati_face", PV + ", gentle sad face, close up, front view, soft moonlight"),
    ("swayamvar_hall", "a grand swayamvar hall with many kings in jeweled clothes on thrones, garlands, a princess "
                       "entering"),
    ("kings_stare", "arrogant Indian kings in jeweled crowns staring greedily in a royal hall"),
    ("kings_transform", "a king transforming into a woman in a burst of magical light in a royal hall, shocked "
                        "courtiers"),
    ("women_attendants", "many royal women in saris standing as attendants behind a princess in a palace, surreal"),
    ("padmavati_cry", PV + " crying alone beside a lotus pond in a moonlit palace garden"),
    ("shuka_garden", "a green parrot landing on a flowering branch near a sad princess in a moonlit palace garden"),
    ("shuka_talk_pv", PV + " talking to a green parrot perched on her hand by a lotus pond, moonlight, magical"),
    ("padmavati_hope", PV + " smiling with hope and tears looking up at the moon, close up, front view"),
    ("necklace", "a princess's hand placing a glowing jeweled necklace into the beak of a green parrot, moonlight"),
    ("shuka_return", "a green parrot flying back over the ocean at dawn carrying a glowing jeweled necklace"),
    ("kalki_receive", YOUNG + " receiving a jeweled necklace from a green parrot in a Himalayan village at evening"),
    ("kali_news", KALI + " listening to a kneeling demon messenger in his dark palace, purple fire, angry"),
    ("kalki_ride_sea", YOUNG + " on a white horse galloping along a beach toward the ocean at sunset, epic"),
]

LINES = [
    ("#", "पिछले भाग में"),
    (["shuka"], "N", "पिछले भाग में... महादेव ने कल्कि को दिया देवदत्त, रत्नजड़ित खड्ग... और सब कुछ जानने वाला तोता शुक।", ""),
    (["padmavati_glimpse"], "N", "और शुक ने सुनाई एक रहस्यमयी राजकुमारी की कहानी... पद्मावती।", ""),
    ("#", "समुद्र के पार"),
    (["kalki_young_face"], "Kalki", "शुक... जाओ सिंहल द्वीप। देखो, पद्मावती के साथ सच में क्या हुआ है।", ""),
    (["shuka"], "Shuka", "जैसी आज्ञा प्रभु... मैं जल्दी लौटूँगा।", ""),
    (["ocean_flight"], "N", "शुक उड़ चला... अनंत समुद्र के ऊपर।", ""),
    (["ocean_flight"], "N", "न कोई किनारा... न कोई पेड़... बस नीला पानी और नीला आसमान।", ""),
    (["ocean_flight"], "N", "दिन में सूरज की तपती धूप... और रात में ठंडी समुद्री हवा।", ""),
    (["shuka"], "Shuka", "थकना मत शुक... प्रभु का काम है। पंखों में चाहे जान न बचे, रुकना नहीं है।", ""),
    (["storm_sea"], "N", "तीसरे दिन... समुद्र में भयानक तूफ़ान उठा।", "thunder"),
    (["hawk_chase"], "N", "और तूफ़ान के बीच से निकला... बैंगनी आँखों वाला एक काला बाज़।", ""),
    (["vikoka"], "N", "वो कोई साधारण बाज़ नहीं था... वो था छलिया विकोक।", ""),
    (["hawk_chase"], "Vikoka", "कहाँ भागेगा छोटे पंछी? कल्कि का संदेशवाहक... आज समुद्र में डूबेगा!", ""),
    (["storm_sea"], "N", "शुक बिजलियों के बीच से उड़ा... लहरों को छूता हुआ...", ""),
    (["shuka"], "Shuka", "हे महादेव... मेरी रक्षा करो!", ""),
    (["storm_sea"], "N", "तभी एक बिजली सीधे बाज़ पर गिरी...", "thunder"),
    (["hawk_chase"], "N", "बाज़ चीख़ता हुआ... समुद्र की लहरों में गिर पड़ा।", ""),
    (["ocean_flight"], "N", "तूफ़ान थम गया... और थका हुआ शुक, लहरों के ऊपर फिर से उड़ने लगा।", ""),
    (["shuka"], "Shuka", "धन्यवाद महादेव... आपने आज फिर अपने भक्त की लाज रख ली।", ""),
    ("#", "सिंहल द्वीप"),
    (["simhala_island"], "N", "और फिर... सुबह की पहली किरण के साथ दिखाई दिया... सिंहल द्वीप।", ""),
    (["simhala_island"], "N", "सफ़ेद महल... सोने के गुंबद... फिर भी पूरे राज्य पर एक उदासी छाई थी।", ""),
    (["simhala_palace"], "N", "राजमहल में राजा बृहद्रथ और रानी कौमुदी... बहुत चिंतित थे।", ""),
    (["simhala_island"], "N", "शुक ने बाज़ार में लोगों की बातें सुनीं... हर कोई एक ही बात कर रहा था।", ""),
    (["simhala_palace"], "N", "हमारी राजकुमारी कितनी सुंदर है... पर कितनी अभागी भी।", ""),
    (["king_brihadratha"], "King", "रानी... हमारी बेटी का क्या होगा? कोई भी उससे विवाह नहीं कर सकता।", ""),
    (["queen_kaumudi"], "Queen", "स्वामी... यह कैसा वरदान है, जो मेरी बच्ची के लिए श्राप बन गया?", ""),
    (["king_brihadratha"], "King", "हमने हर राजा, हर राजकुमार को बुलाया... पर जो भी आया, वो लौटकर नहीं गया।", ""),
    (["queen_kaumudi"], "Queen", "मेरी बच्ची रोज़ महादेव की पूजा करती है... फिर भी उसके भाग्य में यह दुख क्यों?", ""),
    ("#", "पद्मावती का वरदान"),
    (["padmavati_child"], "N", "पद्मावती बचपन से ही... महादेव की परम भक्त थी।", ""),
    (["padmavati_shiva"], "N", "हर दिन वो कमल के फूलों से... शिवलिंग की पूजा करती।", ""),
    (["shiva_boon"], "N", "उसकी भक्ति से प्रसन्न होकर... एक दिन महादेव और माता पार्वती प्रकट हुए।", ""),
    (["shiva_face"], "Shiva", "पुत्री... तुम्हारा विवाह स्वयं भगवान विष्णु से होगा।", ""),
    (["parvati_face"], "Parvati", "और जो भी पुरुष तुम्हें विवाह की इच्छा से देखेगा... वो उसी क्षण स्त्री बन जाएगा।", ""),
    (["padmavati_face"], "N", "पद्मावती उस समय... इस वरदान का अर्थ नहीं समझ पाई।", ""),
    (["padmavati_shiva"], "N", "वो तो बस इतना जानती थी... कि उसके स्वामी स्वयं श्री हरि होंगे।", ""),
    (["padmavati_face"], "N", "और इसी विश्वास के सहारे... वो बड़ी होती गई।", ""),
    ("#", "स्वयंवर"),
    (["swayamvar_hall"], "N", "वर्षों बाद... राजा ने पद्मावती का स्वयंवर रचाया।", ""),
    (["swayamvar_hall"], "N", "दूर-दूर से बड़े-बड़े राजा आए... हीरे-मोतियों से सजे।", ""),
    (["kings_stare"], "N", "जैसे ही पद्मावती सभा में आई... सबकी नज़रें उस पर टिक गईं।", ""),
    (["kings_stare"], "N", "हर राजा के मन में एक ही इच्छा थी... पद्मावती को अपनी रानी बनाना।", ""),
    (["kings_transform"], "N", "और फिर... जो हुआ, उसे देखकर पूरी सभा काँप उठी।", "thunder"),
    (["kings_transform"], "N", "जिस-जिस राजा ने उसे विवाह की इच्छा से देखा... वो स्त्री बन गया!", ""),
    (["women_attendants"], "N", "वे सभी राजा... लज्जा के मारे अपने राज्य नहीं लौटे। वे पद्मावती की दासियाँ बनकर वहीं रह गए।", ""),
    (["padmavati_cry"], "N", "उस दिन के बाद... पद्मावती ने हँसना छोड़ दिया।", ""),
    (["padmavati_cry"], "N", "महल में सब कुछ था... सोना, हीरे, दास-दासियाँ... पर उसके मन में बस सूनापन था।", ""),
    (["padmavati_shiva"], "N", "फिर भी उसने महादेव की पूजा नहीं छोड़ी... एक भी दिन नहीं।", ""),
    (["padmavati_face"], "Padmavati", "हे महादेव... क्या मेरी किस्मत में केवल अकेलापन लिखा है?", ""),
    ("#", "बगीचे में शुक"),
    (["shuka_garden"], "N", "उसी रात... महल के बगीचे में, एक हरा तोता आकर बैठा।", ""),
    (["shuka"], "Shuka", "राजकुमारी... आप इतनी उदास क्यों हैं?", ""),
    (["padmavati_face"], "Padmavati", "एक बोलता हुआ तोता? कौन हो तुम?", ""),
    (["shuka_talk_pv"], "Shuka", "मैं शुक हूँ... और मुझे भेजा है उन्होंने, जिनकी आप वर्षों से प्रतीक्षा कर रही हैं।", ""),
    (["shuka_talk_pv"], "Shuka", "हिमालय के शंभल गाँव में... भगवान विष्णु ने कल्कि के रूप में जन्म लिया है।", ""),
    (["padmavati_face"], "Padmavati", "कल्कि? वो कैसे दिखते हैं शुक? मुझे उनके बारे में सब कुछ बताओ।", ""),
    (["shuka_talk_pv"], "Shuka", "उनकी आँखों में सूरज का तेज है राजकुमारी... और हृदय में चाँद जैसी शीतलता।", ""),
    (["shuka_talk_pv"], "Shuka", "परशुराम उनके गुरु हैं... और महादेव ने स्वयं उन्हें खड्ग और देवदत्त दिया है।", ""),
    (["padmavati_hope"], "N", "यह सुनते ही... पद्मावती की आँखों में चमक लौट आई।", ""),
    (["padmavati_hope"], "Padmavati", "तो महादेव का वचन सच था... मेरे स्वामी आ चुके हैं!", ""),
    (["shuka_talk_pv"], "Shuka", "हाँ राजकुमारी... और केवल वही आपको देख सकते हैं, बिना किसी श्राप के।", ""),
    (["necklace"], "N", "पद्मावती ने अपने गले का रत्नहार उतारा... और शुक को दे दिया।", ""),
    (["padmavati_face"], "Padmavati", "यह मेरे स्वामी को देना... और कहना, पद्मावती उनकी प्रतीक्षा कर रही है।", ""),
    ("#", "शुक की वापसी"),
    (["shuka_return"], "N", "शुक फिर उड़ चला... समुद्र के पार, हिमालय की ओर।", ""),
    (["shambhala"], "N", "कई दिनों बाद... वो शंभल पहुँचा।", ""),
    (["kalki_receive"], "N", "शुक ने रत्नहार कल्कि के हाथों में रखा...", ""),
    (["shuka"], "Shuka", "प्रभु... राजकुमारी पद्मावती ने संदेश भेजा है। वो आपकी प्रतीक्षा कर रही हैं।", ""),
    (["kalki_young_face"], "Kalki", "जिसने महादेव पर इतना विश्वास रखा... उसकी प्रतीक्षा अब और नहीं होगी।", ""),
    (["sumati_face"], "Sumati", "बेटा... समुद्र पार का रास्ता बहुत कठिन है। सावधान रहना।", ""),
    (["kalki_young_face"], "Kalki", "माँ... जहाँ धर्म और भक्ति पुकारे, वहाँ कोई रास्ता कठिन नहीं होता।", ""),
    (["stars_align"], "N", "उस रात आकाश के तारे... फिर एक बार अजीब सी चमक से भर गए।", ""),
    ("#", "कलि की नई चाल"),
    (["kali_news"], "N", "पर दूर अंधकार के महल में... एक असुर दूत घबराया हुआ पहुँचा।", ""),
    (["kali_news"], "Messenger", "महाराज... कल्कि सिंहल द्वीप जाने वाला है। राजकुमारी पद्मावती से विवाह करने!", ""),
    (["kali_smile"], "Kali", "तो विष्णु को अपनी लक्ष्मी मिल गई? हा हा हा...", ""),
    (["kali"], "Kali", "सिंहल के सारे राजाओं को भड़काओ... कल्कि सिंहल तो पहुँचेगा, पर ज़िंदा नहीं लौटेगा!", ""),
    (["kalki_ride_sea"], "N", "अगली सुबह... कल्कि देवदत्त पर सवार होकर... समुद्र की ओर चल पड़े।", ""),
    (["kalki_ride_sea"], "N", "क्या कल्कि पद्मावती का श्राप तोड़ पाएँगे? और सिंहल में कौन सा जाल बिछा है? देखिए अगले भाग में... पद्मावती का स्वयंवर।", ""),
]

TALK = {}
MUSIC_PLAN = [(0.0, "Lord of the Land.mp3", 0.0), ("storm_sea", "Volatile Reaction.mp3", 0.0),
              ("simhala_island", "Echoes of Time v2.mp3", 30.0), ("padmavati_child", "Ossuary 6 - Air.mp3", 30.0),
              ("swayamvar_hall", "Darkest Child.mp3", 0.0), ("shuka_garden", "Echoes of Time v2.mp3", 120.0),
              ("kali_news", "Darkest Child.mp3", 60.0), ("kalki_ride_sea", "Five Armies.mp3", 0.0)]
MUSIC_CREDIT = ('"Lord of the Land", "Volatile Reaction", "Echoes of Time v2", "Ossuary 6 - Air", "Darkest Child", '
                '"Five Armies" - Kevin MacLeod (incompetech.com). Licensed under Creative Commons: By Attribution 4.0 '
                "License (CC BY 4.0)")

THUMB = dict(image="kings_transform", zoom=1.0, pany=0.0,
             text=[("राजा बन गए स्त्री!", 140, (255, 214, 60), 150), ("पद्मावती का रहस्य", 100, (255, 255, 255), 290)])

SEO = dict(
    title="पद्मावती को देखते ही राजा स्त्री क्यों बन गए? 😱 कल्कि और पद्मावती | Kalki Puran भाग 4",
    description=ks.description(
        "कल्कि की पत्नी पद्मावती कौन थीं? उन्हें देखते ही राजा स्त्री क्यों बन जाते थे? Kalki Puran की पूरी कहानी, भाग 4।",
        "तोता शुक समुद्र पार सिंहल द्वीप पहुँचता है, जहाँ राजकुमारी पद्मावती को महादेव का एक ऐसा वरदान मिला है जो "
        "श्राप बन गया: जो भी पुरुष उसे विवाह की इच्छा से देखे, वो स्त्री बन जाए! स्वयंवर में सारे राजा स्त्री बन "
        "गए... फिर शुक ने पद्मावती को कल्कि के बारे में बताया।",
        "Who was Padmavati, the wife of Kalki? Shuka the parrot flies across the ocean to the island of Simhala, "
        "where princess Padmavati's boon from Lord Shiva has turned every king at her swayamvar into a woman. "
        "Part 4 of our cinematic Kalki series.", 4),
    tags=ks.tags(["padmavati", "kalki padmavati", "kalki wife", "simhala dweep", "shuka parrot", "padmavati swayamvar",
                  "पद्मावती", "कल्कि की पत्नी"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "swayamvar_hall", "to": "women_attendants"}, hook="राजा बन गए स्त्री!", hook2=SERIES,
         music=[(0.0, "Darkest Child.mp3", 0.0)],
         seo=dict(title="इस राजकुमारी को देखते ही राजा स्त्री बन जाते थे 😱 #shorts #kalki #padmavati",
                  description=ks.short_description("राजकुमारी पद्मावती के स्वयंवर में जो भी राजा उसे विवाह की "
                                                   "इच्छा से देखता... वो स्त्री बन जाता! क्या था यह वरदान?"),
                  tags=ks.tags(["padmavati", "padmavati swayamvar", "kalki wife", "shorts", "kalki shorts"]),
                  categoryId="24")),
    dict(**{"from": "storm_sea", "to": "hawk_chase", "to_last": True}, hook="तोते के पीछे असुर बाज़!", hook2=SERIES,
         music=[(0.0, "Volatile Reaction.mp3", 0.0)],
         seo=dict(title="कल्कि के तोते शुक पर असुर बाज़ का हमला! 🦅 #shorts #kalki #kalkiavatar",
                  description=ks.short_description("समुद्र के बीच तूफ़ान... और शुक के पीछे विकोक, एक काले बाज़ "
                                                   "के रूप में! फिर महादेव ने जो किया..."),
                  tags=ks.tags(["shuka parrot", "vikoka", "kalki puran", "shorts", "kalki shorts"]), categoryId="24")),
]
