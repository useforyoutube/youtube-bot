"""KALKI series - Episode 1: Kalki ka Janm (~9 min, Hindi). Cinematic story based on the Kalki Purana and
Puranic belief. Render: python myth_images.py kalki01 && python cine.py kalki01 && python cine.py kalki01 --short 0"""

SERIES = "कल्कि • भाग 1"
HOOK = "कल्कि का जन्म"
HOOK2 = "कलियुग के अंत की शुरुआत"
NEXT = "भाग 2: कल्कि की शिक्षा और महादेव का वरदान"
DISCLAIMER = ("यह वीडियो कल्कि पुराण और पौराणिक मान्यताओं पर आधारित एक सिनेमैटिक प्रस्तुति है। "
              "इसमें कुछ दृश्य कल्पना पर आधारित हैं। किसी की धार्मिक भावनाओं को ठेस पहुँचाना हमारा उद्देश्य नहीं है।")
DISCLAIMER_SHORT = "पौराणिक कथा पर आधारित सिनेमैटिक प्रस्तुति"

VOICES = {   # speaker: (voice, rate, pitch, effect)
    "N": ("hi-IN-MadhurNeural", "-14%", "-12Hz", "narrator"),
    "Kali": ("hi-IN-MadhurNeural", "-22%", "-48Hz", "demon"),
    "Koka": ("hi-IN-MadhurNeural", "-12%", "-34Hz", "demon"),
    "Bhudevi": ("hi-IN-SwaraNeural", "-12%", "-6Hz", "divine"),
    "Brahma": ("hi-IN-MadhurNeural", "-16%", "-20Hz", "divine"),
    "Vishnu": ("hi-IN-MadhurNeural", "-12%", "-4Hz", "divine"),
    "Sumati": ("hi-IN-SwaraNeural", "-10%", "-4Hz", "soft"),
    "Vishnuyasha": ("hi-IN-MadhurNeural", "-8%", "+2Hz", "soft"),
    "Rishi": ("hi-IN-MadhurNeural", "-18%", "-22Hz", "divine"),
    "Parashurama": ("hi-IN-MadhurNeural", "-14%", "-28Hz", "divine"),
}
SPEAKERS = {"Kali": ("कलि", (200, 140, 255)), "Koka": ("कोक", (255, 120, 110)), "Bhudevi": ("धरती माता", (170, 230, 170)),
            "Brahma": ("ब्रह्मा", (255, 210, 140)), "Vishnu": ("श्री विष्णु", (140, 200, 255)),
            "Sumati": ("सुमति", (255, 200, 150)), "Vishnuyasha": ("विष्णुयश", (240, 220, 180)),
            "Rishi": ("ऋषि", (255, 230, 170)), "Parashurama": ("परशुराम", (255, 170, 120))}

STYLE = (", epic cinematic movie still, Indian mythology, photorealistic, dramatic volumetric lighting, highly "
         "detailed, 8k, subject centered, no text, no letters, no watermark")
SUMATI = "Sumati, a young Indian woman with long black hair, red bindi and a simple saffron saree"
VY = "Vishnuyasha, a gentle middle-aged Indian brahmin priest with short black beard, tilak, white dhoti, sacred thread"
KALI = "Kali, a dark demon king with black skin, glowing purple eyes and a black horned crown"

IMAGES = [
    ("yugas", "four giant glowing cosmic wheels of time in space representing the four yugas, golden silver bronze "
              "and black, galaxy"),
    ("bull_four", "a radiant white divine bull standing strong on four legs in a golden heavenly meadow, Satyuga"),
    ("bull_one", "a wounded white bull struggling to stand on one leg in a dark ruined wasteland, storm, sorrow"),
    ("kali_rise", KALI + " rising out of black smoke and fire from the earth, arms spread, terrifying"),
    ("kali", "a dark demon king with glowing purple eyes sitting on a black throne of skulls, purple fire, cosmic "
             "darkness, terrifying"),
    ("corrupt_king", "a greedy fat Indian king on a golden throne laughing while starving poor people beg below, "
                     "dark palace"),
    ("broken_family", "an old Indian couple crying outside the closed door of their house at night, rain, "
                      "abandoned by their son"),
    ("temple_ruin", "an abandoned ruined Hindu temple with extinguished lamps, cobwebs, cold dark interior"),
    ("burning", "a burning ancient Indian city at night under a blood red sky, ash falling, ruined temples, Kaliyug"),
    ("bhudevi_cow", "a sad glowing white divine cow with tears walking up a staircase of clouds toward a golden "
                    "heavenly palace"),
    ("bhudevi", "Bhudevi the earth goddess, a beautiful Indian goddess with green saree and flower crown, tears in "
                "her eyes, front view face"),
    ("brahma", "Lord Brahma with four faces and white beard sitting on a giant pink lotus, holding vedas, golden "
               "cosmic light, front face looking at viewer"),
    ("devas_journey", "a procession of radiant Hindu gods walking across clouds toward a glowing cosmic milk ocean"),
    ("kshirsagar", "Lord Vishnu with blue skin reclining on the giant coiled serpent Sheshnaag on the cosmic milk "
                   "ocean, goddess Lakshmi at his feet, divine light"),
    ("devas_pray", "many Hindu gods with folded hands praying together on clouds, golden light rays"),
    ("vishnu_awake", "Lord Vishnu with blue skin and golden crown opening his eyes, calm divine face, close up, "
                     "front view"),
    ("vishnu_glow", "Lord Vishnu standing with four arms holding conch, chakra, mace and lotus, blazing divine light "
                    "behind him, cosmic"),
    ("vishnu_promise", "Lord Vishnu raising his hand in blessing, sudarshan chakra spinning with fire above his finger, "
                       "galaxy behind"),
    ("devas_joy", "Hindu gods with tears of joy and hope looking up at a bright divine light in the sky"),
    ("himalaya_wide", "majestic snowy Himalayan mountain peaks above the clouds at golden sunrise, epic wide shot"),
    ("shambhala", "a hidden glowing village in the Himalayan mountains, small stone temples with golden light, snow "
                  "peaks, sacred and peaceful, night"),
    ("village_life", "peaceful Himalayan village morning, villagers doing aarti and chanting outside small stone "
                     "temples, prayer flags, warm light"),
    ("vishnuyasha", VY + ", doing a fire ritual (havan) at dawn in a small courtyard"),
    ("sumati_pray", SUMATI + ", praying with folded hands in front of a small oil lamp at a home shrine"),
    ("sumati_face", SUMATI + ", close up portrait praying, eyes looking up with hope, warm lamp light, front view"),
    ("dream", SUMATI + " sleeping peacefully while a golden divine light descends from the sky into her, magical"),
    ("sumati_wake", SUMATI + " sitting up at night in wonder, close up face, front view, moonlight"),
    ("vy_face", VY + ", close up portrait smiling with tears of joy, front view, oil lamp light"),
    ("vaishakh_night", "a magical spring night in the Himalayas, full moon, blossoming trees, glowing fireflies"),
    ("stars_align", "stars aligning in a bright line across the night sky above Himalayan peaks, celestial event"),
    ("hut_light", "golden divine light bursting out of the windows of a small village hut at night in the "
                  "Himalayas"),
    ("birth_light", "a newborn baby surrounded by a soft golden aura in the arms of a midwife inside a hut, lamps"),
    ("baby", "close up of a newborn baby's tiny feet glowing with golden divine light on a cloth, sacred atmosphere"),
    ("mother", "a young Indian mother in a simple saree holding a newborn baby that glows with soft divine golden "
               "light, inside a small village hut, oil lamps, tears of joy"),
    ("flowers_rain", "flower petals raining from a glowing sky over a Himalayan village at night, gods faintly "
                     "visible in the clouds"),
    ("conch_bells", "temple bells and conch shells glowing and ringing by themselves in a village temple at night"),
    ("villagers_bow", "village people in shawls gathering in wonder outside a glowing hut at night, lanterns"),
    ("lightning", "massive lightning striking over Himalayan mountain peaks, dark storm clouds, divine energy"),
    ("kali_throne2", KALI + " gripping his skull throne as it cracks, purple lightning, rage"),
    ("kali_face", "extreme close up of a dark demonic face with glowing purple eyes filled with fear and rage, "
                  "purple smoke"),
    ("koka_vikoka", "two giant demon brothers with red skin, tusks and huge spears kneeling before a dark throne, "
                    "purple fire"),
    ("kali_order", KALI + " pointing forward commanding, face clearly visible, front view, purple fire behind"),
    ("koka_face", "a giant red-skinned demon warrior with tusks and burning eyes, evil grin, close up face, front view"),
    ("demons_fly", "an army of demons riding black storm clouds across the night sky toward Himalayan mountains"),
    ("village_night", "a quiet Himalayan village asleep at midnight, snow, one lamp burning, eerie calm"),
    ("dogs_howl", "a village dog howling at a blood red moon, cold wind, dark houses"),
    ("demons_arrive", "thousands of glowing red eyes in the darkness behind snowy mountain ridges, horror"),
    ("vy_fear", VY + ", shouting in fear holding a burning torch, close up face, front view, night"),
    ("villagers_fear", "terrified village women holding children close, crying, torchlight, night"),
    ("koka_attack", "a giant red demon with a huge spear walking toward a small glowing hut through snow, night"),
    ("sumati_protect", SUMATI + ", shielding her glowing baby with her body, fierce brave face, front view"),
    ("baby_eyes", "close up of a newborn baby opening his eyes that glow with golden divine light"),
    ("divine_shield", "a dome of golden divine light exploding outward from a small hut, blasting away demons, night"),
    ("demons_burn", "demons turning into ash and embers in golden light, dramatic"),
    ("koka_shock", "a giant red demon with tusks staring in shock and fear, close up face, front view, golden light "
                   "on his face"),
    ("demons_flee", "demons fleeing into dark storm clouds over the mountains, defeated"),
    ("dawn", "first golden sunrise rays over a peaceful snowy Himalayan village, smoke from chimneys, hope"),
    ("sages_arrive", "four radiant ancient Hindu sages with white beards walking into a Himalayan village, glowing"),
    ("naming", "ancient sages blessing a glowing baby held by his mother, emotional, temple courtyard"),
    ("rishi_face", "an ancient Hindu sage with long white beard and wise eyes, smiling, close up face, front view"),
    ("brothers", "three young Indian brothers in simple clothes smiling with their glowing baby brother, village"),
    ("childhood", "a young Indian boy with glowing eyes and long hair playing in Himalayan meadows, sunlight"),
    ("child_sky", "a young Indian boy standing on a cliff looking at the stars, cosmic sky, destiny"),
    ("storm_mountain", "a lone powerful figure descending a snowy Himalayan mountain in a storm, cinematic"),
    ("parashurama", "the ancient sage warrior Parashurama with long white beard and a glowing divine axe teaching a "
                    "young warrior in a Himalayan forest"),
    ("parashurama_face", "Parashurama, ancient warrior sage with matted grey hair, white beard and a divine axe on his "
                         "shoulder, close up face, front view, intense eyes"),
    ("kalki_leaves", "a young boy touching his mother's feet goodbye at a village gate, a warrior sage waiting, "
                     "emotional dawn"),
    ("kali_watch", KALI + " watching from darkness through a magical purple orb showing a young boy"),
    ("kali_smile", KALI + ", evil smile, close up face, front view, purple glow"),
    ("army", "a vast army of dark demons with purple glowing eyes marching across a burning wasteland, millions, "
             "cinematic wide shot"),
]

# Talking faces are found automatically; Kali's mask-like face needs manual mouth points (image pixels)
TALK = {"kali_face": ("Kali", 528, 812, 140, 170, 42)}

LINES = [
    ("#", "शुरुआत"),
    (["yugas"], "N", "सृष्टि चार युगों में चलती है... सतयुग, त्रेता, द्वापर... और कलियुग।", ""),
    (["bull_four"], "N", "सतयुग में धर्म का बैल... चार पैरों पर खड़ा था। सत्य, तप, दया और दान।", ""),
    (["bull_one"], "N", "पर कलियुग आते-आते... उसके पास बस एक पैर बचा।", ""),
    ("#", "कलियुग का अंधकार"),
    (["kali_rise"], "N", "और इसी अंधकार से उठा एक असुर... कलि पुरुष।", "thunder"),
    (["kali"], "Kali", "अब इस धरती पर मेरा राज होगा... हर दिल में लालच... हर ज़ुबान पर झूठ!", ""),
    (["corrupt_king"], "N", "राजा लुटेरे बन गए... और प्रजा भूखी सोने लगी।", ""),
    (["broken_family"], "N", "भाई ने भाई को धोखा दिया... बेटे ने माँ-बाप को घर से निकाल दिया।", ""),
    (["temple_ruin"], "N", "मंदिरों के दीये बुझ गए... और यज्ञ की अग्नि ठंडी पड़ गई।", ""),
    (["burning"], "N", "धरती पर अधर्म का धुआँ इतना फैल गया... कि सूरज भी धुंधला दिखने लगा।", ""),
    ("#", "धरती माता की पुकार"),
    (["bhudevi_cow"], "N", "तब धरती माता... एक दुखी गाय का रूप लेकर ब्रह्मलोक पहुँचीं।", ""),
    (["bhudevi"], "Bhudevi", "हे ब्रह्मदेव... अब मुझसे यह बोझ नहीं सहा जाता। मेरे बच्चे एक-दूसरे का खून बहा रहे हैं।", ""),
    (["brahma"], "Brahma", "धैर्य रखो देवी... इस संकट का उत्तर केवल श्री हरि के पास है।", ""),
    (["devas_journey"], "N", "ब्रह्मा जी सभी देवताओं को लेकर... क्षीर सागर पहुँचे।", ""),
    (["kshirsagar"], "N", "जहाँ शेषनाग पर... भगवान विष्णु योगनिद्रा में लीन थे।", ""),
    (["devas_pray"], "N", "देवताओं ने हाथ जोड़कर प्रार्थना की... और तब...", ""),
    (["vishnu_awake"], "Vishnu", "मैं जानता हूँ देवताओं... कलि का अंत अब निकट है।", ""),
    (["vishnu_glow"], "Vishnu", "मैं शंभल गाँव में... विष्णुयश और सुमति के पुत्र के रूप में जन्म लूँगा।", ""),
    (["vishnu_promise"], "Vishnu", "और मेरा नाम होगा... कल्कि।", "thunder"),
    (["devas_joy"], "N", "यह सुनकर देवताओं की आँखों में आँसू आ गए... आशा के आँसू।", ""),
    ("#", "शंभल गाँव"),
    (["himalaya_wide"], "N", "हिमालय की ऊँची चोटियों के बीच... बादलों में छिपा एक गाँव था।", ""),
    (["shambhala"], "N", "शंभल। जहाँ कलियुग में भी... धर्म का दीया जल रहा था।", ""),
    (["village_life"], "N", "यहाँ लोग आज भी सच बोलते थे... और हर सुबह मंत्रों से शुरू होती थी।", ""),
    (["vishnuyasha"], "N", "इसी गाँव में रहते थे एक सरल ब्राह्मण... विष्णुयश।", ""),
    (["sumati_pray"], "N", "और उनकी पत्नी सुमति... जो रोज़ भगवान से एक ही प्रार्थना करतीं।", ""),
    (["sumati_face"], "Sumati", "हे प्रभु... इस अंधेरे संसार को एक दीपक दे दो।", ""),
    (["dream"], "N", "एक रात सुमति ने सपना देखा... एक सुनहरी रोशनी उनके भीतर समा गई।", ""),
    (["sumati_wake"], "Sumati", "स्वामी... मैंने आज रात कुछ अद्भुत देखा।", ""),
    (["vy_face"], "Vishnuyasha", "शायद... भगवान ने हमारी प्रार्थना सुन ली है सुमति।", ""),
    ("#", "दिव्य जन्म"),
    (["vaishakh_night"], "N", "वैशाख मास... शुक्ल पक्ष की द्वादशी।", ""),
    (["stars_align"], "N", "उस रात आकाश के तारे... एक अजीब सी चमक से भर गए।", ""),
    (["hut_light"], "N", "विष्णुयश की छोटी सी कुटिया से... एक सुनहरा प्रकाश फूट पड़ा।", ""),
    (["birth_light"], "N", "और सुमति ने... एक तेजस्वी बालक को जन्म दिया।", ""),
    (["baby"], "N", "उस बालक के मुख पर... सूरज जैसा तेज था।", ""),
    (["mother"], "Sumati", "मेरे लाल... तुम्हारी आँखों में इतना तेज क्यों है?", ""),
    (["flowers_rain"], "N", "आकाश से देवताओं ने फूल बरसाए...", ""),
    (["conch_bells"], "N", "और पूरे शंभल में... शंख और घंटियाँ अपने-आप बजने लगीं।", ""),
    (["villagers_bow"], "N", "गाँव वाले दौड़े चले आए... किसी को समझ नहीं आ रहा था कि यह क्या हो रहा है।", ""),
    ("#", "कलि का डर"),
    (["lightning"], "N", "पर उसी पल... दूर अंधकार के महल में...", "thunder"),
    (["kali_throne2"], "N", "कलि का सिंहासन... काँप उठा।", ""),
    (["kali_face"], "Kali", "वो आ गया है... मेरा अंत... जन्म ले चुका है!", ""),
    (["koka_vikoka"], "N", "कलि ने अपने दो सबसे भयानक सेनापतियों को बुलाया... कोक और विकोक।", ""),
    (["kali_order"], "Kali", "जाओ... उस बालक को ढूँढो। सूरज उगने से पहले... वो ज़िंदा नहीं रहना चाहिए!", ""),
    (["koka_face"], "Koka", "जैसी आज्ञा महाराज... आज रात शंभल जलेगा।", ""),
    (["demons_fly"], "N", "काले बादलों पर सवार होकर... असुरों की सेना हिमालय की ओर बढ़ी।", ""),
    ("#", "पहला हमला"),
    (["village_night"], "N", "आधी रात थी। शंभल गहरी नींद में सोया था...", ""),
    (["dogs_howl"], "N", "तभी कुत्ते रोने लगे... और हवा अचानक ठंडी हो गई।", ""),
    (["demons_arrive"], "N", "पहाड़ों के पीछे से... हज़ारों लाल आँखें चमकने लगीं।", ""),
    (["vy_fear"], "Vishnuyasha", "सुमति! बच्चे को लेकर अंदर जाओ... जल्दी!", ""),
    (["villagers_fear"], "N", "गाँव वाले डर से काँपने लगे... औरतें बच्चों को सीने से लगाए रो रही थीं।", ""),
    (["koka_attack"], "N", "कोक ने अपना भाला उठाया... और कुटिया की ओर बढ़ा।", ""),
    (["sumati_protect"], "Sumati", "मेरे बच्चे को कोई हाथ नहीं लगा सकता!", ""),
    (["baby_eyes"], "N", "तभी... बालक ने अपनी आँखें खोलीं।", ""),
    (["divine_shield"], "N", "उसके चारों ओर एक सुनहरा कवच फैल गया...", "thunder"),
    (["demons_burn"], "N", "जो भी असुर पास आया... वो रोशनी में जलकर राख हो गया।", ""),
    (["koka_shock"], "Koka", "यह... यह कोई साधारण बालक नहीं है!", ""),
    (["demons_flee"], "N", "कोक और विकोक... जान बचाकर भाग खड़े हुए।", ""),
    (["dawn"], "N", "सुबह की पहली किरण के साथ... शंभल फिर से शांत था।", ""),
    ("#", "नामकरण"),
    (["sages_arrive"], "N", "कुछ दिन बाद... गाँव में चार तेजस्वी ऋषि आए।", ""),
    (["naming"], "N", "उन्होंने बालक को देखा... और उनकी आँखें भर आईं।", ""),
    (["rishi_face"], "Rishi", "यह बालक कलियुग का अंत करेगा... इसका नाम होगा... कल्कि।", ""),
    (["brothers"], "N", "कल्कि के तीन बड़े भाई थे... कवि, प्राज्ञ और सुमंत्रक।", ""),
    (["childhood"], "N", "कल्कि बड़े होने लगे... पर उनकी आँखों में हमेशा एक गहरी चमक रहती थी।", ""),
    (["child_sky"], "N", "जैसे वो जानते हों... कि एक दिन उन्हें पूरी सृष्टि को बचाना है।", ""),
    ("#", "गुरु का आगमन"),
    (["storm_mountain"], "N", "और फिर एक दिन... हिमालय की बर्फ़ीली चोटियों से उतरकर आए...", ""),
    (["parashurama"], "N", "हाथ में दिव्य फरसा लिए... भगवान परशुराम।", "thunder"),
    (["parashurama_face"], "Parashurama",
     "मैं युगों से इसी दिन की प्रतीक्षा कर रहा था... चलो कल्कि। तुम्हारी शिक्षा का समय आ गया है।", ""),
    (["kalki_leaves"], "N", "कल्कि ने माँ के चरण छुए... और गुरु के साथ चल पड़े।", ""),
    (["kali_watch"], "N", "पर दूर अंधकार में... कलि सब देख रहा था।", ""),
    (["kali_smile"], "Kali", "सीख ले जितना सीखना है बालक... मैं भी तैयार हो रहा हूँ।", ""),
    (["army"], "N", "आगे क्या होगा? देखिए अगले भाग में... कल्कि की शिक्षा... और महादेव का वरदान।", ""),
]

MUSIC_PLAN = [(0.0, "Lightless Dawn.mp3", 0.0),             # dark, slow: yugas + Kaliyug
              ("bhudevi_cow", "Echoes of Time v2.mp3", 0.0),  # emotional build: the earth's plea, Vishnu
              ("himalaya_wide", "Ossuary 6 - Air.mp3", 30.0),  # calm, sacred: Shambhala, the birth
              ("lightning", "Darkest Child.mp3", 0.0),         # menace: Kali, the attack
              ("divine_shield", "Echoes of Time v2.mp3", 229.0),  # climax: the divine shield
              ("sages_arrive", "Ossuary 6 - Air.mp3", 60.0),   # gentle: naming, childhood
              ("storm_mountain", "Five Armies.mp3", 0.0)]      # epic: Parashurama, the threat
MUSIC_CREDIT = ('"Lightless Dawn", "Echoes of Time v2", "Ossuary 6 - Air", "Darkest Child", "Five Armies" - '
                "Kevin MacLeod (incompetech.com). Licensed under Creative Commons: By Attribution 4.0 License "
                "(CC BY 4.0)")

THUMB = dict(image="kali_face", zoom=1.0, pany=0.0,
             text=[("कलि काँप उठा!", 150, (255, 214, 60), 150), ("कल्कि का जन्म", 110, (255, 255, 255), 300)])

import kalki_seo as ks

SEO = dict(
    title="कलियुग का अंत कैसे होगा? 😱 कल्कि अवतार का जन्म | Kalki Avatar Full Story | Kalki Puran भाग 1",
    description=ks.description(
        "कलियुग का अंत कैसे होगा? भगवान विष्णु के दसवें अवतार कल्कि का जन्म कहाँ और कैसे होगा? "
        "Kalki Puran की पूरी कहानी, भाग 1।",
        "कलियुग अपने चरम पर है... धर्म का बैल एक पैर पर खड़ा है, और कलि पुरुष का राज हर दिल पर है। तब धरती माता "
        "की पुकार पर भगवान विष्णु वचन देते हैं: \"मैं शंभल गाँव में जन्म लूँगा... और मेरा नाम होगा कल्कि।\" "
        "देखिए कल्कि के दिव्य जन्म की पूरी कहानी: कलि का डर, कोक-विकोक का हमला, सुनहरा कवच, ऋषियों द्वारा "
        "नामकरण, और भगवान परशुराम का आगमन।",
        "How will Kaliyuga end? The birth of Kalki, the tenth avatar of Lord Vishnu, in the hidden village of "
        "Shambhala - Part 1 of our cinematic Kalki series, based on the Kalki Purana.", 1),
    tags=ks.tags(["kalki ka janm", "kalki avatar birth", "kalki avatar full story", "koka vikoka", "parashurama",
                  "कल्कि का जन्म"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "lightning", "to": "demons_fly"}, hook="कलि क्यों काँप उठा?", hook2=SERIES,
         music=[(0.0, "Darkest Child.mp3", 0.0)],
         seo=dict(title="कल्कि के जन्म से कलि क्यों काँप उठा? 😱 Kalki vs Kali #shorts #kalki #kaliyug",
                  description=ks.short_description("कल्कि के जन्म की खबर से कलि का सिंहासन काँप उठा... और उसने "
                                                   "भेजे अपने सबसे भयानक सेनापति, कोक और विकोक! कलियुग का अंत "
                                                   "कैसे होगा? पूरी कहानी देखिए।"),
                  tags=ks.tags(["kalki vs kali", "kali purush", "shorts", "kalki shorts"]), categoryId="24")),
    dict(**{"from": "koka_attack", "to": "demons_flee"}, hook="असुरों ने बच्चे पर हमला किया...", hook2="फिर क्या हुआ?",
         music=[(0.0, "Echoes of Time v2.mp3", 226.0)],
         seo=dict(title="असुरों ने बालक कल्कि पर हमला किया... फिर जो हुआ 🔥 Kalki Avatar #shorts #kalki",
                  description=ks.short_description("आधी रात, शंभल गाँव पर असुरों का हमला... पर जैसे ही बालक "
                                                   "कल्कि ने आँखें खोलीं, जो हुआ उसे देखकर असुर भी काँप उठे!"),
                  tags=ks.tags(["baby kalki", "shambhala", "shorts", "kalki shorts"]), categoryId="24")),
]
