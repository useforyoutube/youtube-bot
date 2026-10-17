"""KALKI series - Episode 8: Ghar ka Bhedi (~12 min, Hindi). Durukti, Kali's sister in the Kalki Purana, comes to
Shambhala disguised as a holy woman to divide Kalki's family and people from within (dramatized)."""
import kalki_seo as ks
from kalki01 import DISCLAIMER, DISCLAIMER_SHORT, STYLE, KALI
from kalki02 import YOUNG
from kalki07 import VOICES as V7, SPEAKERS as S7
from kalki04 import PV

SERIES = "कल्कि • भाग 8"
PLAYLIST = "kalki_hi"
HOOK = "घर का भेदी"
HOOK2 = "दुरुक्ति की माया"
NEXT = "भाग 9: पर्वत जितनी असुरी कुथोदरी"

DURUKTI = ("Durukti, a beautiful but terrifying demon queen with dark purple skin, silver crown and glowing violet "
           "eyes")
SAINT = ("a serene Indian holy woman in a plain white saree with rudraksha beads and ash on her forehead, kind smile, "
         "a faint violet glint in her eyes")
VOICES = dict(V7, Maya=("hi-IN-SwaraNeural", "-8%", "-2Hz", "soft"),
              Elder=("hi-IN-MadhurNeural", "-12%", "-26Hz", "soft"))
SPEAKERS = dict(S7, Maya=("साध्वी माया", (230, 210, 255)), Elder=("गाँव के मुखिया", (230, 210, 170)))

IMAGES = [
    ("golden_shambhala", None), ("kalki_young_face", None), ("kalki_smile", None), ("pv_warrior", None),
    ("padmavati_face", None), ("brothers", None), ("shuka", None), ("sumati_face", None), ("vy_face", None),
    ("kali", None), ("kali_smile", None), ("kali_mirror", None), ("durukti", None), ("dawn", None),
    ("victory", None), ("flowers_rain", None), ("lightning", None), ("kalki_sword_raise", None),
    ("saint_arrives", SAINT + " arriving at the golden gates of an ancient Indian city, crowd welcoming her with "
                     "flowers, morning light"),
    ("saint_face", SAINT + ", close up face, front view, temple lamps behind"),
    ("saint_preach", SAINT + " preaching under a huge banyan tree, villagers sitting and listening, peaceful"),
    ("purple_ritual", DURUKTI + " performing a secret ritual over purple fire in a dark forest at night"),
    ("kali_in_fire", "the face of a dark demon king with glowing purple eyes appearing inside violet flames, "
                     "night forest"),
    ("whisper_kavi", SAINT + " whispering into the ear of a young Indian warrior prince in a palace garden at dusk"),
    ("kavi_doubt", "a young Indian warrior prince with a troubled jealous face, close up, front view, dusk light"),
    ("brothers_argue", "three young Indian warrior brothers arguing angrily in a palace hall, one pointing"),
    ("people_murmur", "worried Indian villagers whispering in groups in a marketplace, suspicious glances"),
    ("whisper_market", SAINT + " speaking softly to a group of worried village women in a market"),
    ("well_poison", "a hooded figure dropping glowing purple powder into a village well at night, moonlight"),
    ("sick_village", "sick Indian villagers lying on mats in a courtyard, healers worried, oil lamps, night"),
    ("kalki_heal", YOUNG + " holding a glowing divine sword over a village well, golden light purifying the water"),
    ("kalki_alone", YOUNG + " standing alone on a palace terrace at night looking at the stars, thoughtful"),
    ("pv_suspect", PV + " watching a holy woman from behind a pillar, suspicious eyes, temple corridor"),
    ("shuka_spy", "a green parrot hidden on a dark tree branch at night watching a purple fire below"),
    ("shuka_report", "a green parrot speaking urgently to a young warrior prince and a princess by lamp light"),
    ("assembly", "a grand village assembly under a banyan tree, elders and people gathered, a young warrior "
                 "prince standing in the centre"),
    ("pond_reflection", SAINT + " standing by a temple pond, but her reflection in the water shows a purple-skinned "
                        "demon queen with a silver crown"),
    ("true_form", DURUKTI + " revealed in a burst of purple smoke and golden light in a temple courtyard, furious"),
    ("sword_light", "a divine sword raised high, blazing golden light flooding a temple courtyard, shadows fleeing"),
    ("durukti_flee", DURUKTI + " escaping into the night sky as a cloud of violet smoke and bats, screaming"),
    ("brothers_hug", "three young Indian warrior brothers embracing in reconciliation, tears, warm lamp light"),
    ("family_meal", "an Indian family eating together on the floor of a golden home, mother serving, warm light, "
                    "happy"),
    ("kuthodari_far", "a colossal demoness as tall as a mountain silhouetted against a red sky over distant hills, "
                      "terrifying, epic"),
]

LINES = [
    ("#", "पिछले भाग में"),
    (["victory"], "N", "पिछले भाग में... कल्कि ने एक ही वार से अमर असुर कोक और विकोक का अंत कर दिया।", ""),
    (["kali_mirror"], "N", "पर अंधकार के महल में... कलि ने अपनी बहन को जगा दिया था।", ""),
    (["durukti"], "Durukti", "भैया... तलवार से नहीं, मैं उसे उसके अपनों से हराऊँगी।", "thunder"),
    ("#", "शंभल में उत्सव"),
    (["golden_shambhala"], "N", "शंभल में विजय का उत्सव चल रहा था... दीपों से सजी गलियाँ, ढोल और जयकारे।", ""),
    (["golden_shambhala"], "N", "लोग कहते थे... जब तक कल्कि हैं, कोई असुर शंभल को छू भी नहीं सकता।", ""),
    (["kalki_smile"], "Kalki", "यह जीत मेरी नहीं... हर उस व्यक्ति की है, जो धर्म के साथ खड़ा रहा।", ""),
    (["sumati_face"], "Sumati", "मेरा लाल... बस अब कुछ दिन घर पर रह। माँ का मन भी तो भरने दे।", ""),
    (["kalki_young_face"], "Kalki", "जैसी आपकी आज्ञा, माँ।", ""),
    (["brothers"], "N", "भाई कवि, प्राज्ञ और सुमंत्र... हर युद्ध में कल्कि के साथ कंधे से कंधा मिलाकर लड़े थे।", ""),
    (["brothers"], "Kavi", "छोटे... अगली बार असुरों की सेना का बायाँ हिस्सा मैं सँभालूँगा। देखना!", ""),
    (["kalki_smile"], "Kalki", "भैया, आप साथ हों तो बायाँ-दायाँ क्या... पूरी सेना अकेले सँभाल लूँ।", ""),
    (["dawn"], "N", "सब कुछ सुंदर था... इतना सुंदर, कि किसी को अंधेरे की आहट सुनाई ही नहीं दी।", ""),
    ("#", "एक साध्वी का आगमन"),
    (["saint_arrives"], "N", "उसी सुबह... शंभल के द्वार पर एक साध्वी आई। सफ़ेद वस्त्र, माथे पर भस्म, होठों पर मीठी मुस्कान।", ""),
    (["saint_face"], "Maya", "मेरा नाम माया है... मैं तीर्थ करती हुई, धर्म के रक्षक के दर्शन करने आई हूँ।", ""),
    (["saint_arrives"], "N", "लोगों ने फूल बरसाए... और उसे गाँव के मंदिर में ठहरा दिया।", ""),
    (["saint_preach"], "N", "हर शाम बरगद के नीचे... वह कथा सुनाती। लोग मंत्रमुग्ध होकर सुनते।", ""),
    (["saint_preach"], "Maya", "धर्म बड़ा है... पर याद रखना, धर्म के नाम पर भी कभी-कभी अपने ही छले जाते हैं।", ""),
    (["pv_suspect"], "N", "पर सभा के पीछे खड़ी पद्मावती को... उसकी आँखों में एक अजीब सी बैंगनी चमक दिखी।", ""),
    (["pv_suspect"], "Padmavati", "ये आँखें... मैंने कहीं देखी हैं। पर कहाँ?", ""),
    (["padmavati_face"], "N", "पद्मावती ने कल्कि से कुछ नहीं कहा... बिना सबूत किसी साध्वी पर शक करना पाप होता।", ""),
    (["padmavati_face"], "Padmavati", "पहले मैं ख़ुद पता लगाऊँगी... फिर स्वामी से कहूँगी।", ""),
    ("#", "रात का रहस्य"),
    (["purple_ritual"], "N", "उसी रात... जंगल के अंधेरे में, बैंगनी आग जल रही थी।", "thunder"),
    (["purple_ritual"], "N", "और आग के सामने बैठी थी... दुरुक्ति। साध्वी माया का असली रूप।", ""),
    (["kali_in_fire"], "Kali", "बहन... कल्कि की सेना अजेय है। उसे युद्ध में हराना असंभव है।", ""),
    (["durukti"], "Durukti", "इसीलिए मैं युद्ध नहीं करूँगी भैया। हर किले की सबसे कमज़ोर दीवार... उसके अंदर होती है।", ""),
    (["durukti"], "Durukti", "पहले भाई को भाई से लड़ाऊँगी... फिर प्रजा को राजा से।", ""),
    (["kali_smile"], "Kali", "हा हा हा... यही तो कलियुग है।", ""),
    ("#", "पहला ज़हर: शक"),
    (["whisper_kavi"], "N", "अगले दिन... साध्वी ने कल्कि के बड़े भाई कवि को अकेले में बुलाया।", ""),
    (["whisper_kavi"], "Maya", "कुमार... आप बड़े हैं, फिर भी सारी प्रशंसा छोटे भाई की? सारे राजा उसी के आगे झुकते हैं।", ""),
    (["kavi_doubt"], "Kavi", "कल्कि अवतार हैं... यह तो सबको पता है।", ""),
    (["whisper_kavi"], "Maya", "अवतार हैं... या अपने भाइयों को पीछे रखने का बहाना? सोचिए कुमार, सोचिए...", ""),
    (["kavi_doubt"], "N", "वो शब्द... कवि के मन में ज़हर की तरह उतर गए।", ""),
    (["kavi_doubt"], "N", "उस रात कवि सो नहीं पाए... बचपन की हर याद, अब नए रंग में दिखने लगी।", ""),
    (["kavi_doubt"], "Kavi", "क्या सच में... सबका ध्यान हमेशा कल्कि पर ही रहता है? क्या मैं बस... बड़ा भाई हूँ?", ""),
    (["whisper_kavi"], "N", "और हर दिन... साध्वी उस ज़हर में थोड़ा और ज़हर मिला देती।", ""),
    (["brothers_argue"], "N", "कुछ ही दिनों में... युद्ध की बैठक में भाइयों की आवाज़ें ऊँची होने लगीं।", ""),
    (["brothers_argue"], "Kavi", "हर निर्णय तुम ही लोगे कल्कि? हम क्या सिर्फ़ तुम्हारी परछाई हैं?", ""),
    (["kalki_young_face"], "Kalki", "भैया... आपके बिना मैं कुछ भी नहीं। यह आप क्या कह रहे हैं?", ""),
    (["kavi_doubt"], "N", "कवि बिना कुछ कहे... सभा छोड़कर चले गए।", ""),
    (["brothers"], "N", "प्राज्ञ और सुमंत्र भी दो हिस्सों में बँट गए... कोई कवि के साथ, कोई कल्कि के साथ।", ""),
    (["kalki_young_face"], "Kalki", "जो भाई कोक-विकोक के सामने नहीं डरे... वो आज एक-दूसरे से क्यों लड़ रहे हैं?", ""),
    ("#", "दूसरा ज़हर: डर"),
    (["whisper_market"], "N", "उधर बाज़ार में... साध्वी औरतों से धीरे-धीरे बातें करती।", ""),
    (["whisper_market"], "Maya", "जहाँ कल्कि जाते हैं... वहाँ असुर आते हैं। कहीं इसी युद्ध की आग शंभल तक न पहुँच जाए।", ""),
    (["people_murmur"], "N", "डर फैलने लगा... लोग आपस में फुसफुसाने लगे।", ""),
    (["people_murmur"], "Villager", "पहले शंभल कितना शांत था... अब हर रात डर लगता है।", ""),
    (["people_murmur"], "N", "जो लोग कल तक कल्कि की जय-जयकार करते थे... आज उनकी ओर देखकर नज़रें फेर लेते।", ""),
    (["lightning"], "N", "और हर रात आकाश में... बिना बादल के बिजली कड़कती। जैसे कोई अदृश्य शक्ति डर को हवा दे रही हो।", "thunder"),
    (["well_poison"], "N", "और फिर एक रात... एक परछाई ने गाँव के कुएँ में बैंगनी धूल डाल दी।", "thunder"),
    (["sick_village"], "N", "सुबह होते-होते... आधा गाँव बीमार पड़ गया। तेज़ बुखार, बेहोशी।", ""),
    (["saint_preach"], "Maya", "मैंने कहा था न... यह युद्ध का श्राप है! जब तक कल्कि यहाँ हैं, यह विपत्ति नहीं जाएगी।", ""),
    (["people_murmur"], "N", "भीड़ में से किसी ने कहा... कल्कि को शंभल छोड़ देना चाहिए।", ""),
    ("#", "माँ का विश्वास"),
    (["kalki_alone"], "N", "उस रात कल्कि अकेले छत पर खड़े थे... जिन लोगों के लिए लड़े, वही आज उन पर शक कर रहे थे।", ""),
    (["sumati_face"], "Sumati", "बेटा... लोग डरे हुए हैं, बुरे नहीं। डर हमेशा किसी और के मुँह से बोलता है।", ""),
    (["vy_face"], "Vishnuyasha", "जहाँ अचानक फूट पड़े... वहाँ किसी बाहर वाले का हाथ ढूँढो, पुत्र।", ""),
    (["kalki_young_face"], "Kalki", "बाहर वाला... जो सबसे बाद में आया, और सबसे जल्दी सबका प्रिय बन गया।", ""),
    (["kalki_heal"], "N", "सबसे पहले... कल्कि कुएँ पर गए और महादेव का दिया हुआ दिव्य खड्ग उठाया।", ""),
    (["kalki_heal"], "N", "सुनहरी रोशनी पानी में उतरी... और पानी फिर से साफ़ हो गया।", "thunder"),
    (["sick_village"], "N", "एक-एक करके... बीमार लोग ठीक होने लगे।", ""),
    (["padmavati_face"], "Padmavati", "स्वामी... कुएँ के पास मुझे यह बैंगनी धूल मिली। ऐसी धूल मैंने कलि की सेना के जादूगरों के पास देखी थी।", ""),
    (["kalki_young_face"], "Kalki", "तो यह बीमारी नहीं... षड्यंत्र है।", ""),
    ("#", "शुक की जासूसी"),
    (["shuka"], "Kalki", "शुक... आज रात साध्वी माया पर नज़र रखना। वह कहाँ जाती है, किससे मिलती है।", ""),
    (["shuka_spy"], "N", "आधी रात को... शुक ने देखा, साध्वी जंगल की ओर जा रही थी।", ""),
    (["shuka_spy"], "N", "और पेड़ की डाल पर छिपे शुक ने... वह बैंगनी आग, और आग में कलि का चेहरा देख लिया।", ""),
    (["shuka_report"], "Shuka", "प्रभु! वह साध्वी नहीं... कलि की बहन दुरुक्ति है!", "thunder"),
    (["pv_warrior"], "Padmavati", "मुझे पहले ही शक था स्वामी... उसकी आँखें कोक-विकोक की सभा में देखी थीं।", ""),
    (["kalki_young_face"], "Kalki", "उसे पकड़ना आसान है... पर लोगों का विश्वास लौटाना ज़रूरी है। सच सबके सामने आना चाहिए।", ""),
    ("#", "सभा में सच"),
    (["assembly"], "N", "अगली सुबह... कल्कि ने पूरे शंभल की सभा बुलाई।", ""),
    (["assembly"], "Elder", "कल्कि... लोग कह रहे हैं, यह विपत्ति तुम्हारे युद्धों की वजह से है।", ""),
    (["kalki_young_face"], "Kalki", "मुखिया जी... अगर मेरी वजह से शंभल को कष्ट है, तो मैं आज ही चला जाऊँगा।", ""),
    (["kalki_young_face"], "Kalki", "पर जाने से पहले... मैं चाहता हूँ, साध्वी माया मंदिर के जल को छूकर आशीर्वाद दें।", ""),
    (["saint_face"], "Maya", "हाँ... हाँ, क्यों नहीं।", ""),
    (["pond_reflection"], "N", "साध्वी जैसे ही मंदिर के कुंड पर झुकी... पानी में उसकी परछाई दिखी।", ""),
    (["pond_reflection"], "N", "पर वह परछाई साध्वी की नहीं थी... वह थी बैंगनी त्वचा वाली, चाँदी के मुकुट वाली असुरी!", "thunder"),
    (["people_murmur"], "Villager", "हे भगवान! यह तो... असुरी है!", ""),
    (["sword_light"], "N", "कल्कि ने खड्ग उठाया... और सुनहरी रोशनी ने माया का पर्दा चीर दिया।", "thunder"),
    (["true_form"], "N", "और सबके सामने खड़ी थी... दुरुक्ति, अपने असली रूप में।", ""),
    (["true_form"], "Durukti", "चतुर हो कल्कि... पर याद रखना, जो बीज मैंने बोए हैं, वो इतनी जल्दी नहीं मरते!", ""),
    (["kalki_sword_raise"], "Kalki", "बीज तभी उगते हैं दुरुक्ति... जब मन की धरती में अंधेरा हो। और आज शंभल में प्रकाश है।", ""),
    (["true_form"], "N", "दुरुक्ति ने बैंगनी जादू का गोला फेंका... पर शुक ने झपट्टा मारकर उसकी दिशा बदल दी।", "thunder"),
    (["durukti_flee"], "N", "बैंगनी धुएँ और चमगादड़ों के झुंड में बदलकर... दुरुक्ति आकाश में भाग गई।", ""),
    ("#", "टूटे रिश्ते, फिर से जुड़े"),
    (["people_murmur"], "N", "लोग शर्म से सिर झुकाए खड़े थे...", ""),
    (["assembly"], "Elder", "हमें क्षमा करो कल्कि... डर ने हमारी आँखों पर पट्टी बाँध दी थी।", ""),
    (["kalki_smile"], "Kalki", "क्षमा कैसी मुखिया जी... आप मेरा परिवार हैं। असुर का सबसे बड़ा हथियार यही है, हमें आपस में बाँट देना।", ""),
    (["kavi_doubt"], "N", "भीड़ के पीछे खड़े कवि की आँखों में... आँसू थे।", ""),
    (["brothers_hug"], "Kavi", "छोटे... मैंने उस असुरी की बातों में आकर तुम पर शक किया। मुझे माफ़ कर दो।", ""),
    (["brothers_hug"], "Kalki", "भैया... भाई का हाथ छूट सकता है, साथ नहीं।", ""),
    (["family_meal"], "N", "उस रात... पूरा परिवार फिर से एक साथ बैठा। माँ ने अपने हाथों से भोजन परोसा।", ""),
    (["family_meal"], "Sumati", "देखा... असुर तलवार से नहीं, फूट से जीतते हैं। और हम फिर से एक हैं।", ""),
    (["vy_face"], "Vishnuyasha", "जिस घर में भाई एक-दूसरे का हाथ थामे रहें... वहाँ कलियुग का कोई दाँव नहीं चलता।", ""),
    (["flowers_rain"], "N", "अगली सुबह शंभल में फिर से उत्सव हुआ... इस बार विजय का नहीं, विश्वास का।", ""),
    (["kalki_smile"], "Kalki", "याद रखना... कलि का सबसे बड़ा अस्त्र तलवार नहीं, अफ़वाह है। सच को परखो, फिर विश्वास करो।", ""),
    ("#", "अगला संकट"),
    (["kali_mirror"], "N", "पर अंधकार के महल में... कलि का क्रोध अब सीमा पार कर चुका था।", "thunder"),
    (["kali"], "Kali", "माया भी हार गई? तो अब... वो आएगी, जिसके पेट में पूरी सेनाएँ समा जाती हैं।", ""),
    (["kuthodari_far"], "N", "दूर पहाड़ों के पीछे... कुछ हिलने लगा। पहाड़ जितनी ऊँची एक असुरी... कुथोदरी।", "thunder"),
    (["golden_shambhala"], "N", "क्या कल्कि उस विशाल असुरी को रोक पाएँगे? देखिए अगले भाग में।", ""),
]

TALK = {}
MUSIC_PLAN = [(0.0, "Lightless Dawn.mp3", 0.0), ("golden_shambhala", "Heroic Age.mp3", 0.0),
              ("saint_arrives", "Long Note Four.mp3", 0.0), ("purple_ritual", "Darkest Child.mp3", 0.0),
              ("whisper_kavi", "Ossuary 6 - Air.mp3", 0.0), ("well_poison", "Dark Times.mp3", 0.0),
              ("kalki_alone", "Echoes of Time v2.mp3", 0.0), ("shuka_spy", "Darkest Child.mp3", 90.0),
              ("assembly", "Lightless Dawn.mp3", 120.0), ("sword_light", "Prelude and Action.mp3", 0.0),
              ("brothers_hug", "Echoes of Time v2.mp3", 200.0), ("kali_mirror", "Volatile Reaction.mp3", 0.0)]
MUSIC_CREDIT = ('"Lightless Dawn", "Heroic Age", "Long Note Four", "Darkest Child", "Ossuary 6 - Air", "Dark Times", '
                '"Echoes of Time v2", "Prelude and Action", "Volatile Reaction" - Kevin MacLeod (incompetech.com). '
                "Licensed under Creative Commons: By Attribution 4.0 License (CC BY 4.0)")

THUMB = dict(image="true_form", zoom=1.0, pany=0.0,
             text=[("घर का भेदी!", 150, (255, 214, 60), 150), ("दुरुक्ति की माया", 100, (255, 255, 255), 290)])
THUMB2 = dict(hero=("kalki_young_face", 0.5), other=("true_form", 0.5), big="घर का भेदी!", small="दुरुक्ति की माया")

SEO = dict(
    title="कलि की बहन दुरुक्ति 😱 साध्वी बनकर आई असुरी! घर का भेदी | Kalki vs Kali | Kalki Puran भाग 8",
    description=ks.description(
        "कलि की बहन दुरुक्ति कौन थी? साध्वी बनकर शंभल आई इस असुरी ने कल्कि के परिवार और प्रजा में फूट कैसे डाली? "
        "Kalki Puran की पूरी कहानी, भाग 8।",
        "कोक-विकोक के अंत के बाद, कलि की बहन दुरुक्ति 'साध्वी माया' बनकर शंभल आती है। भाई को भाई से लड़ाती है, "
        "कुएँ में ज़हर डालती है और लोगों में डर फैलाती है... पर शुक की जासूसी और मंदिर के कुंड की परछाई "
        "उसका असली रूप सबके सामने ले आती है।",
        "Durukti, Kali's sister, arrives in Shambhala disguised as a holy woman to divide Kalki's family and people "
        "from within. Part 8 of our cinematic Kalki series.", 8),
    tags=ks.tags(["durukti", "kali ki behan", "kalki durukti", "ghar ka bhedi", "दुरुक्ति", "कलि की बहन",
                  "kalki new episode"]),
    categoryId="24",
)

SHORTS = [
    dict(**{"from": "pond_reflection", "to": "durukti_flee"}, hook="साध्वी नहीं, असुरी!", hook2=SERIES,
         music=[(0.0, "Prelude and Action.mp3", 0.0)],
         seo=dict(title="पानी में दिखा साध्वी का असली रूप 😱 कलि की बहन दुरुक्ति #shorts #kalki #kalkipuran",
                  description=ks.short_description("मंदिर के कुंड पर झुकी साध्वी माया... और पानी में दिखी उसकी असली "
                                                   "परछाई! कौन थी वो?"),
                  tags=ks.tags(["durukti", "kali ki behan", "shorts", "kalki shorts"]), categoryId="24")),
    dict(**{"from": "well_poison", "to": "sick_village"}, hook="कुएँ में ज़हर किसने डाला?", hook2=SERIES,
         music=[(0.0, "Dark Times.mp3", 0.0)],
         seo=dict(title="आधी रात कुएँ में किसने डाला ज़हर? 😱 कल्कि ने कैसे बचाया गाँव #shorts #kalki",
                  description=ks.short_description("एक रात शंभल के कुएँ में बैंगनी धूल डाली गई... और सुबह आधा गाँव "
                                                   "बीमार। फिर कल्कि ने महादेव का खड्ग उठाया..."),
                  tags=ks.tags(["kalki", "kalki puran", "shorts", "kalki shorts"]), categoryId="24")),
]
