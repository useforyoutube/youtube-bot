"""KALKI series - Episode 2: Parashurama ki Shiksha (~8 min, Hindi). Based on the Kalki Purana
(Kalki's education under Parashurama on Mahendra mountain and the guru dakshina), with dramatized scenes."""
import kalki_seo as ks
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT, VOICES as V1, SPEAKERS as S1, STYLE

SERIES = "कल्कि • भाग 2"
PLAYLIST = "kalki_hi"
HOOK = "परशुराम की शिक्षा"
HOOK2 = "कल्कि का पहला युद्ध"
NEXT = "भाग 3: महादेव का वरदान"

VOICES = dict(V1, Kalki=("hi-IN-MadhurNeural", "-6%", "+6Hz", "soft"),
              Vikoka=("hi-IN-MadhurNeural", "-10%", "-38Hz", "demon"))
SPEAKERS = dict(S1, Kalki=("कल्कि", (255, 225, 120)), Vikoka=("विकोक", (190, 200, 210)))

TEEN = "Kalki, a handsome Indian teenage boy with long black hair tied up, bright divine eyes, saffron dhoti"
YOUNG = "Kalki, a handsome young Indian warrior with long black hair, glowing calm eyes, saffron and gold clothes"
PR = "Parashurama, an ancient warrior sage with matted grey hair and long white beard"

IMAGES = [  # prompt None = reuse from the picture library (earlier episodes)
    ("kali_face", None), ("divine_shield", None), ("parashurama_face", None), ("kalki_leaves", None),
    ("sumati_face", None), ("stars_align", None), ("training", None), ("kali_watch", None), ("kali_smile", None),
    ("demons_flee", None), ("parashurama", None), ("kali", None), ("kali_order", None), ("army", None),
    ("journey_snow", TEEN + " and " + PR + " walking through deep snow on a Himalayan mountain pass, wind, epic wide"),
    ("journey_river", TEEN + " and an old sage crossing a roaring river on a narrow rope bridge, mist, jungle"),
    ("kalki_ask", TEEN + ", close up face, curious eyes, front view, soft mountain light"),
    ("mahendra", "a sacred mountain rising above the clouds with a small hermitage on its peak, golden sunset, epic"),
    ("ashram", "an ancient hermitage on a mountain top with a sacred fire, banyan tree and deer, peaceful morning"),
    ("parashurama_axe", PR + " placing his glowing divine axe on a stone altar beside a sacred fire"),
    ("kalki_meditate", TEEN + " meditating cross-legged on a rock above the clouds at dawn, glowing aura"),
    ("birds_kalki", "birds and deer peacefully gathering around a meditating glowing boy on a mountain top"),
    ("scriptures", "ancient palm-leaf manuscripts glowing with golden sanskrit light in a hermitage, oil lamp"),
    ("teaching", PR + " teaching a teenage boy under a banyan tree, scrolls, beams of sunlight"),
    ("archery", TEEN + " drawing a huge bow, the arrow glowing with fire, mountain cliff at sunrise"),
    ("sword_train", "a teenage Indian boy and an old warrior sage sparring with sword and axe, sparks, misty forest"),
    ("parashurama_smile", PR + " smiling warmly, close up face, front view, golden light"),
    ("horse_riding", TEEN + " riding a wild brown horse at full gallop across a mountain meadow, dust and wind"),
    ("divine_weapons", "glowing celestial weapons floating in a circle above a sacred fire, divine astras, mystic"),
    ("kalki_young_face", YOUNG + ", determined expression, close up face, front view"),
    ("vikoka", "a sly demon general with grey skin, tusks and yellow snake eyes, purple fire, close up face, "
               "front view"),
    ("golden_deer", "a magical golden deer with jeweled antlers glowing in a dark forest near a hermitage"),
    ("parashurama_meditate", PR + " meditating beside a sacred fire suddenly opening his eyes in alarm"),
    ("deer_transform", "a golden deer transforming into a huge grey demon with tusks in a dark forest, purple smoke"),
    ("demon_attack", "a giant grey demon swinging a massive mace at a young Indian warrior in a forest, debris, "
                     "young warrior leaping high to dodge"),
    ("kalki_bow_forest", YOUNG + " drawing a bow in a dark forest, the arrow blazing with blue fire"),
    ("water_arrow", "an arrow turning into a massive torrent of water slamming a giant grey demon backwards through "
                    "trees, forest"),
    ("kalki_bow_guru", "a young Indian warrior bowing and touching the feet of an old sage at a sacred fire, emotional"),
    ("blessing_light", "an old sage blessing a kneeling young warrior with his hand on his head, divine light rays "
                       "from the sky, mountain top"),
    ("kailash_far", "Mount Kailash glowing in the far distance across Himalayan ranges, mystic aura, sunrise"),
]

LINES = [
    ("#", "पिछले भाग में"),
    (["kali_face"], "N", "पिछले भाग में आपने देखा... कलियुग के अंधकार में, शंभल गाँव में जन्म हुआ भगवान विष्णु के दसवें अवतार... कल्कि का।", ""),
    (["divine_shield"], "N", "बालक कल्कि ने अपने दिव्य तेज से... असुरों को राख कर दिया।", ""),
    (["parashurama_face"], "N", "और फिर आए भगवान परशुराम... कल्कि को अपना शिष्य बनाने।", ""),
    ("#", "महेंद्र पर्वत की ओर"),
    (["kalki_leaves"], "N", "माँ सुमति की आँखों में आँसू थे... पर होंठों पर आशीर्वाद।", ""),
    (["sumati_face"], "Sumati", "जा मेरे लाल... जब लौटना, तो धर्म का सूरज बनकर लौटना।", ""),
    (["journey_snow"], "N", "गुरु और शिष्य... बर्फ़ीले रास्तों पर दिन-रात चलते रहे।", ""),
    (["journey_river"], "N", "नदियाँ लांघीं... जंगल पार किए... पर कल्कि ने एक बार भी थकान की शिकायत नहीं की।", ""),
    (["kalki_ask"], "Kalki", "गुरुदेव... हम कहाँ जा रहे हैं?", ""),
    (["parashurama_face"], "Parashurama", "महेंद्र पर्वत... जहाँ मैंने युगों तक तप किया है। वहीं तुम्हारी शिक्षा होगी।", ""),
    (["mahendra"], "N", "और फिर सामने आया... बादलों को छूता महेंद्र पर्वत।", ""),
    ("#", "आश्रम का पहला पाठ"),
    (["ashram"], "N", "पर्वत की चोटी पर था एक छोटा सा आश्रम... जहाँ हवा में भी मंत्रों की गूँज थी।", ""),
    (["parashurama_axe"], "N", "परशुराम ने अपना फरसा रखा... और कल्कि की ओर देखा।", ""),
    (["parashurama_face"], "Parashurama", "शिक्षा का पहला पाठ... शस्त्र नहीं, संयम है।", ""),
    (["kalki_meditate"], "N", "कल्कि को सबसे पहले... ध्यान करना सिखाया गया।", ""),
    (["kalki_meditate"], "N", "कई दिन बीत गए... कल्कि बिना हिले, बिना कुछ खाए... ध्यान में बैठे रहे।", ""),
    (["birds_kalki"], "N", "आश्रम के पक्षी और हिरण... उनके पास आकर बैठने लगे।", ""),
    (["parashurama_smile"], "Parashurama", "जिसके पास पशु-पक्षी भी निडर होकर बैठें... वही सच्चा योद्धा बनता है।", ""),
    ("#", "वेद और धर्म"),
    (["scriptures"], "N", "फिर शुरू हुई वेदों की शिक्षा... ऋग्वेद, यजुर्वेद, सामवेद... और अथर्ववेद।", ""),
    (["teaching"], "N", "परशुराम ने उन्हें धर्म का असली अर्थ समझाया।", ""),
    (["parashurama_face"], "Parashurama", "धर्म का अर्थ केवल पूजा नहीं है कल्कि... कमज़ोर की रक्षा करना ही सबसे बड़ा धर्म है।", ""),
    (["kalki_ask"], "Kalki", "और अगर कोई राजा ही अधर्मी हो जाए, गुरुदेव?", ""),
    (["parashurama_axe"], "Parashurama", "तो उस राजा को भी... धर्म के आगे झुकना होगा। चाहे उसके लिए युद्ध ही क्यों न करना पड़े।", ""),
    (["stars_align"], "N", "कल्कि उस रात सो नहीं पाए... उन्हें अपने जन्म का उद्देश्य समझ आने लगा था।", ""),
    ("#", "शस्त्र विद्या"),
    (["training"], "N", "फिर आया... शस्त्र विद्या का समय।", ""),
    (["archery"], "N", "धनुष-बाण... जिसमें कल्कि का एक भी तीर निशाना नहीं चूकता था।", ""),
    (["archery"], "N", "एक दिन उन्होंने एक तीर से... पहले चले तीर को बीच से चीर दिया।", ""),
    (["sword_train"], "N", "तलवार और फरसे का अभ्यास... दिन-रात चलता रहा।", ""),
    (["parashurama_face"], "Parashurama", "तेज़ हो... पर तुम्हारे मन में अभी भी दया है। युद्ध में यही दया तुम्हें रोक सकती है।", ""),
    (["kalki_ask"], "Kalki", "गुरुदेव... क्या दया कमज़ोरी है?", ""),
    (["parashurama_smile"], "Parashurama", "नहीं वत्स... दया ही वह कारण है जिसके लिए तुम लड़ोगे। बस उसे अपने हाथ मत बाँधने देना।", ""),
    (["horse_riding"], "N", "घुड़सवारी में तो कल्कि... हवा से बातें करने लगे।", ""),
    (["divine_weapons"], "N", "और फिर परशुराम ने उन्हें सिखाए... दिव्य अस्त्र। आग्नेयास्त्र... वरुणास्त्र... वायव्यास्त्र।", ""),
    (["divine_weapons"], "N", "एक मंत्र पढ़ते ही... तीर आग का पक्षी बन जाता।", ""),
    (["kalki_young_face"], "N", "समय बीतता गया... बालक अब एक तेजस्वी युवक बन चुका था।", ""),
    ("#", "कलि की चाल"),
    (["kali_watch"], "N", "पर दूर अंधकार के महल में... कलि बेचैन था।", ""),
    (["kali_smile"], "Kali", "वो लड़का हर दिन और ताकतवर हो रहा है... उसे अभी रोकना होगा।", ""),
    (["vikoka"], "N", "उसने बुलाया अपने छलिया सेनापति... विकोक को।", ""),
    (["vikoka"], "Vikoka", "महाराज... मैं छल से उसे मारूँगा। वो मुझे पहचान भी नहीं पाएगा।", ""),
    (["golden_deer"], "N", "अगली सुबह... आश्रम के पास एक सुनहरा हिरण दिखाई दिया।", ""),
    (["kalki_young_face"], "N", "इतना सुंदर हिरण... कल्कि ने पहले कभी नहीं देखा था।", ""),
    (["golden_deer"], "N", "हिरण धीरे-धीरे... उन्हें घने जंगल में ले गया।", ""),
    (["parashurama_meditate"], "N", "उधर ध्यान में बैठे परशुराम की आँखें... अचानक खुल गईं।", ""),
    (["parashurama_face"], "Parashurama", "यह हिरण नहीं... छल है! कल्कि!", ""),
    ("#", "पहला युद्ध"),
    (["deer_transform"], "N", "जंगल के बीच पहुँचते ही... हिरण का रूप बदलने लगा।", "thunder"),
    (["vikoka"], "Vikoka", "हा हा हा! आज तेरा अंत निश्चित है... विष्णु के अवतार!", ""),
    (["demon_attack"], "N", "विकोक ने अपनी भारी गदा घुमाई...", ""),
    (["demon_attack"], "N", "पर कल्कि बिजली की तरह उछले... और वार खाली गया।", ""),
    (["kalki_young_face"], "Kalki", "गुरुदेव ने सिखाया है... छल का जवाब धैर्य से देना।", ""),
    (["kalki_bow_forest"], "N", "कल्कि ने धनुष उठाया... और वरुणास्त्र का आवाहन किया।", ""),
    (["water_arrow"], "N", "तीर से निकली... समुद्र जैसी विशाल जलधारा!", "thunder"),
    (["water_arrow"], "N", "विकोक दूर जाकर गिरा... पेड़ टूटकर बिखर गए।", ""),
    (["vikoka"], "Vikoka", "यह... यह तो बस शुरुआत है लड़के! कलि की सेना तुझे ढूँढ लेगी!", ""),
    (["demons_flee"], "N", "और वो काले धुएँ में बदलकर... गायब हो गया।", ""),
    (["parashurama"], "N", "परशुराम दौड़ते हुए वहाँ पहुँचे...", ""),
    (["parashurama_smile"], "Parashurama", "आज तुमने साबित कर दिया... कि तुम तैयार हो रहे हो।", ""),
    (["kalki_young_face"], "Kalki", "पर गुरुदेव... मैंने उसे मारा नहीं। वो भाग गया।", ""),
    (["parashurama_face"], "Parashurama", "विकोक को मारना इतना आसान नहीं है... उसका रहस्य तुम्हें बाद में पता चलेगा।", ""),
    ("#", "गुरु दक्षिणा"),
    (["ashram"], "N", "कई वर्ष बीत गए... और फिर वो दिन आया, जब शिक्षा पूरी हुई।", ""),
    (["kalki_bow_guru"], "N", "कल्कि ने गुरु के चरणों में सिर झुकाया।", ""),
    (["kalki_young_face"], "Kalki", "गुरुदेव... मैं आपको गुरु दक्षिणा में क्या दूँ?", ""),
    (["parashurama_smile"], "Parashurama", "मुझे कुछ नहीं चाहिए वत्स... बस तीन वचन दो।", ""),
    (["parashurama_face"], "Parashurama", "पहला... महादेव की तपस्या करके उनका आशीर्वाद लो।", ""),
    (["parashurama_face"], "Parashurama", "दूसरा... अधर्मी राजाओं को हराकर धर्म का राज स्थापित करो।", ""),
    (["parashurama_axe"], "Parashurama", "और तीसरा... कलि का अंत करो। यही मेरी गुरु दक्षिणा होगी।", ""),
    (["kalki_young_face"], "Kalki", "वचन देता हूँ गुरुदेव... जब तक साँस है, धर्म की रक्षा करूँगा।", ""),
    (["blessing_light"], "N", "परशुराम ने उनके सिर पर हाथ रखा... और आकाश से एक दिव्य प्रकाश उतरा।", "thunder"),
    ("#", "अगला पड़ाव"),
    (["mahendra"], "N", "अगली सुबह... कल्कि महेंद्र पर्वत से नीचे उतरे।", ""),
    (["kailash_far"], "N", "उनकी मंज़िल थी... महादेव का धाम।", ""),
    (["kali"], "N", "पर कलि भी चुप नहीं बैठा था...", ""),
    (["kali_order"], "Kali", "विकोक हार गया? तो अब कोक को जगाओ... और पूरी सेना तैयार करो!", ""),
    (["army"], "N", "क्या महादेव कल्कि को वरदान देंगे? और कलि की नई चाल क्या होगी? देखिए अगले भाग में... महादेव का वरदान।", ""),
]

TALK = {"kali_face": ("Kali", 528, 812, 140, 170, 42)}
MUSIC_PLAN = [(0.0, "Echoes of Time v2.mp3", 0.0), ("journey_snow", "Ossuary 6 - Air.mp3", 30.0),
              ("training", "Heroic Age.mp3", 0.0), ("kali_watch", "Darkest Child.mp3", 0.0),
              ("deer_transform", "Volatile Reaction.mp3", 0.0), ("ashram", "Echoes of Time v2.mp3", 120.0),
              ("blessing_light", "Echoes of Time v2.mp3", 229.0), ("kali", "Five Armies.mp3", 0.0)]
MUSIC_CREDIT = ('"Echoes of Time v2", "Ossuary 6 - Air", "Heroic Age", "Darkest Child", "Volatile Reaction", '
                '"Five Armies" - Kevin MacLeod (incompetech.com). Licensed under Creative Commons: By Attribution 4.0 '
                "License (CC BY 4.0)")

THUMB = dict(image="water_arrow", zoom=1.0, pany=0.0,
             text=[("कल्कि का पहला युद्ध!", 140, (255, 214, 60), 150), ("परशुराम की शिक्षा", 100, (255, 255, 255), 290)])

SEO = dict(
    title="कल्कि का पहला युद्ध! 🔥 परशुराम की शिक्षा | Kalki Avatar Full Story | Kalki Puran भाग 2",
    description=ks.description(
        "भगवान परशुराम ने कल्कि को कैसे शिक्षा दी? कल्कि का पहला युद्ध किससे हुआ? Kalki Puran की पूरी कहानी, भाग 2।",
        "महेंद्र पर्वत पर भगवान परशुराम कल्कि को ध्यान, वेद, धर्म, धनुर्विद्या और दिव्य अस्त्रों की शिक्षा देते हैं। "
        "पर कलि अपने छलिया सेनापति विकोक को सुनहरे हिरण के रूप में भेजता है... और जंगल में होता है कल्कि का पहला "
        "युद्ध! अंत में परशुराम गुरु दक्षिणा में माँगते हैं तीन वचन।",
        "Kalki's training under Lord Parashurama on Mahendra mountain - meditation, the Vedas, archery and divine "
        "astras - and his first battle against Kali's demon general Vikoka. Part 2 of our cinematic Kalki series.", 2),
    tags=ks.tags(["parashurama", "kalki parashurama", "kalki training", "kalki first battle", "vikoka",
                  "guru dakshina", "परशुराम", "कल्कि की शिक्षा"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "golden_deer", "to": "demons_flee"}, hook="सुनहरा हिरण... या असुर?", hook2=SERIES,
         music=[(0.0, "Volatile Reaction.mp3", 0.0)],
         seo=dict(title="सुनहरा हिरण निकला असुर! 😱 कल्कि का पहला युद्ध #shorts #kalki #kalkiavatar",
                  description=ks.short_description("कलि ने विकोक को सुनहरे हिरण के रूप में भेजा... पर कल्कि ने "
                                                   "वरुणास्त्र चला दिया! देखिए कल्कि का पहला युद्ध।"),
                  tags=ks.tags(["kalki first battle", "vikoka", "golden deer", "shorts", "kalki shorts"]),
                  categoryId="24")),
    dict(**{"from": "kalki_bow_guru", "to": "blessing_light"}, hook="परशुराम ने माँगे 3 वचन", hook2=SERIES,
         music=[(0.0, "Echoes of Time v2.mp3", 200.0)],
         seo=dict(title="परशुराम ने कल्कि से गुरु दक्षिणा में क्या माँगा? 🙏 #shorts #kalki #parashurama",
                  description=ks.short_description("शिक्षा पूरी होने पर परशुराम ने कल्कि से गुरु दक्षिणा में "
                                                   "माँगे तीन वचन... तीसरा वचन था कलि का अंत!"),
                  tags=ks.tags(["parashurama", "guru dakshina", "kalki parashurama", "shorts", "kalki shorts"]),
                  categoryId="24")),
]
