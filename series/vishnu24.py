"""VISHNU KE 24 AVATAR - one full video (~17 min, Hindi, 24 chapters) + 24 numbered Shorts (one per avatar, one a
day), each Short linking to the full video. Based on the Shrimad Bhagavatam (1.3 lists 22 avatars; the popular
list of 24 adds Hamsa and Hayagriva). Built for the searches that already bring the channel views:
"bhagwan vishnu ke 24 avatar", "24 avatars of lord vishnu"... The last avatar, Kalki, leads into the Kalki series.
    python kalki_daily.py vishnu24          (pictures -> full video -> upload, first Shorts)
    python vishnu_shorts.py                 (the rest of the 24 Shorts, one a day)"""
from kalki01 import STYLE

SERIES = "विष्णु के 24 अवतार"
PLAYLIST = "vishnu24"
HOOK = "भगवान विष्णु के 24 अवतार"
HOOK2 = "सनकादि से कल्कि तक"
NEXT = "अब देखिए: कल्कि सीरीज़ भाग 1"
DISCLAIMER = ("यह वीडियो श्रीमद्भागवत पुराण और पौराणिक मान्यताओं पर आधारित एक सिनेमैटिक प्रस्तुति है। "
              "इसमें कुछ दृश्य कल्पना पर आधारित हैं। किसी की धार्मिक भावनाओं को ठेस पहुँचाना हमारा उद्देश्य नहीं है।")
DISCLAIMER_SHORT = "श्रीमद्भागवत पर आधारित सिनेमैटिक प्रस्तुति"
KALKI_PLAYLIST = "https://www.youtube.com/playlist?list=PLP4zcN56nxME"

VOICES = {"N": ("hi-IN-SwaraNeural", "-8%", "-4Hz", "narrator")}     # female narrator: sets this series apart from Kalki
SPEAKERS = {}
TALK = {}

BLUE = "with blue skin, golden crown and divine glow"
IMAGES = [
    ("vishnu_glow", None), ("vishnu_awake", None), ("vishnu_promise", None), ("parashurama_axe", None),
    ("parashurama_face", None), ("parashurama", None), ("kalki", None), ("kalki_young_face", None),
    ("kalki_sword_raise", None), ("kali_face", None),
    ("a01_kumaras", "four radiant child sages, the Kumaras, eternally five years old, meditating on glowing clouds "
                    "above a heavenly realm"),
    ("a01_gate", "four glowing child sages at the golden gates of Vaikuntha, two tall divine gatekeepers with maces "
                 "blocking them"),
    ("a02_hiranyaksha", "a giant demon in golden armour dragging planet Earth down into a dark cosmic ocean"),
    ("a02_varaha", "Lord Varaha, a colossal divine boar-headed god " + BLUE + ", lifting the Earth goddess on his "
                   "tusks out of a cosmic ocean"),
    ("a02_battle", "the boar god Varaha battling a golden-armoured demon in a stormy cosmic ocean, divine light"),
    ("a03_narada", "sage Narada with a veena, saffron robes and white topknot, floating on clouds singing, divine glow"),
    ("a03_dhruva", "a little boy meditating in a deep forest while sage Narada with a veena blesses him"),
    ("a04_naranarayana", "twin sages Nara and Narayana in deep meditation in the snowy Himalayas near a temple, "
                         "glowing aura"),
    ("a04_urvashi", "a beautiful celestial apsara emerging in light and flowers before a meditating Himalayan sage"),
    ("a05_kapila", "sage Kapila, a serene bearded yogi meditating with a glowing aura in an ashram by the sea"),
    ("a05_ashes", "a sage opening his eyes as fire from his gaze turns an army of princes to ashes, dramatic"),
    ("a06_anasuya", "a sage woman Anasuya holding three glowing divine babies in a forest hermitage"),
    ("a06_dattatreya", "Lord Dattatreya with three heads and six arms, standing with a cow and four dogs in a forest"),
    ("a07_yajna", "a radiant god rising from a sacred fire altar, golden flames, rishis chanting around it"),
    ("a07_indra", "a radiant god seated on the throne of heaven, white elephant behind him, gods bowing"),
    ("a08_rishabha", "a majestic Indian king renouncing his crown and walking calmly into a forest, serene light"),
    ("a08_bharat", "a young prince crowned king in a golden ancient Indian royal court, map of India glowing behind"),
    ("a09_prithu", "King Prithu with a divine bow chasing a radiant cow that is the Earth goddess, dramatic sky"),
    ("a09_fields", "King Prithu milking a radiant divine cow as barren land turns into green and golden fields"),
    ("a10_small_fish", "a tiny glowing golden fish in the cupped hands of an Indian king standing in a river"),
    ("a10_matsya", "Lord Matsya, a gigantic golden horned fish towing a boat with seven sages through a cosmic flood "
                   "storm"),
    ("a11_churning", "the churning of the cosmic ocean, gods and demons pulling a giant serpent wrapped around a "
                     "mountain"),
    ("a11_kurma", "Lord Kurma, a colossal divine tortoise holding a huge mountain on his shell in the ocean"),
    ("a12_dhanvantari", "Lord Dhanvantari " + BLUE + ", four arms, rising from the ocean holding a golden pot of "
                        "nectar"),
    ("a12_herbs", "an ancient Ayurvedic healer's table with glowing medicinal herbs, mortar and old palm-leaf books"),
    ("a13_mohini", "Mohini, an enchantingly beautiful divine woman in a golden saree holding a pot of nectar, gods on "
                   "one side and demons on the other"),
    ("a13_nectar", "Mohini pouring glowing nectar into the cups of shining gods while demons watch, spellbound"),
    ("a14_demons", "two giant demons stealing four glowing scriptures from a sleeping four-headed creator god"),
    ("a14_hayagriva", "Lord Hayagriva, a divine god with a radiant white horse head, four arms, holding glowing "
                      "scriptures, cosmic light"),
    ("a15_prahlad", "a calm young boy praying with folded hands while a furious demon king raises a mace in a golden "
                    "palace"),
    ("a15_narasimha", "Lord Narasimha, half lion half man, bursting out of a stone pillar in a palace at dusk, "
                      "roaring, divine fury"),
    ("a15_end", "Narasimha holding the demon king on his lap at a palace doorway at twilight, divine fury"),
    ("a16_vamana", "Lord Vamana, a small brahmin boy with an umbrella and water pot, asking a demon king for land"),
    ("a16_trivikrama", "a cosmic giant god " + BLUE + " striding across earth and sky, one foot among the stars"),
    ("a17_brahma", "the four-headed creator god Brahma on a lotus with four child sages asking him a question"),
    ("a17_hamsa", "a radiant divine white swan glowing with golden light, appearing before sages in the heavens"),
    ("a19_vyasa", "sage Vyasa, dark-skinned with long matted hair, dictating while Lord Ganesha writes on palm leaves"),
    ("a19_vedas", "four glowing ancient scriptures floating around a meditating sage, cosmic light"),
    ("a20_rama", "Lord Rama " + BLUE + ", holding a bow, with Sita and Lakshmana in a forest"),
    ("a20_ravana", "Lord Rama shooting a blazing arrow at the ten-headed demon king Ravana on a battlefield"),
    ("a21_balarama", "Lord Balarama, fair-skinned strong god with a plough on his shoulder, blue garments, riverbank"),
    ("a22_krishna", "Lord Krishna " + BLUE + ", peacock feather crown and flute, cows in Vrindavan at sunset"),
    ("a22_gita", "Lord Krishna giving the Bhagavad Gita to Arjuna on a chariot at Kurukshetra, divine light"),
    ("a23_buddha", "Lord Buddha meditating under the Bodhi tree, serene glowing aura, peaceful forest"),
]

LINES = [
    ("#", "शुरुआत"),
    (["vishnu_glow"], "N", "जब-जब धरती पर अधर्म बढ़ता है... भगवान विष्णु किसी न किसी रूप में अवतार लेते हैं।", ""),
    (["vishnu_awake"], "N", "आप दस अवतारों के बारे में जानते होंगे... पर श्रीमद्भागवत में भगवान के चौबीस अवतारों का वर्णन है।", ""),
    (["vishnu_promise"], "N", "आज देखिए... पहले अवतार से लेकर कल्कि तक, सभी चौबीस अवतारों की कथा।", ""),

    ("#", "1. सनकादि कुमार"),
    (["a01_kumaras"], "N", "पहला अवतार... सनकादि, यानी चार कुमार।", ""),
    (["a01_kumaras"], "N", "सृष्टि के आरंभ में ब्रह्मा जी के मन से चार बालक प्रकट हुए... सनक, सनंदन, सनातन और सनत्कुमार।", ""),
    (["a01_kumaras"], "N", "ब्रह्मा जी चाहते थे कि ये सृष्टि को आगे बढ़ाएँ... पर इन्होंने सदा बालक रहकर ज्ञान का मार्ग चुना।", ""),
    (["a01_gate"], "N", "वैकुंठ के द्वार पर जय-विजय ने इन्हें रोका... और इनके श्राप से ही आगे वराह और नृसिंह की कथा शुरू हुई।", ""),

    ("#", "2. वराह अवतार"),
    (["a02_hiranyaksha"], "N", "दूसरा अवतार... वराह। दैत्य हिरण्याक्ष ने पृथ्वी को प्रलय के महासागर में डुबो दिया था।", "thunder"),
    (["a02_varaha"], "N", "तब भगवान एक वराह के रूप में प्रकट हुए... और देखते ही देखते पर्वत जितने विशाल हो गए।", ""),
    (["a02_battle"], "N", "समुद्र में भयंकर युद्ध हुआ... और वराह भगवान ने हिरण्याक्ष का वध किया।", ""),
    (["a02_varaha"], "N", "फिर अपने दाँतों पर पृथ्वी को उठाकर... उसे फिर से उसके स्थान पर स्थापित किया।", ""),

    ("#", "3. देवर्षि नारद"),
    (["a03_narada"], "N", "तीसरा अवतार... देवर्षि नारद। हाथ में वीणा, होठों पर नारायण-नारायण।", ""),
    (["a03_narada"], "N", "नारद मुनि तीनों लोकों में घूमकर... भक्ति का संदेश फैलाते हैं।", ""),
    (["a03_dhruva"], "N", "उन्होंने ही बालक ध्रुव और प्रह्लाद जैसे भक्तों को... भगवान तक पहुँचने की राह दिखाई।", ""),

    ("#", "4. नर-नारायण"),
    (["a04_naranarayana"], "N", "चौथा अवतार... नर-नारायण। भगवान दो ऋषियों के रूप में आए।", ""),
    (["a04_naranarayana"], "N", "बद्रिकाश्रम में उन्होंने ऐसी घोर तपस्या की... कि इंद्र का सिंहासन डोल उठा।", ""),
    (["a04_urvashi"], "N", "इंद्र ने अप्सराएँ भेजीं... तो नारायण ने अपनी जाँघ से उर्वशी को प्रकट कर दिया, जो उन सबसे सुंदर थी।", ""),
    (["a04_naranarayana"], "N", "कहते हैं... यही नर और नारायण, आगे चलकर अर्जुन और श्रीकृष्ण बने।", ""),

    ("#", "5. कपिल मुनि"),
    (["a05_kapila"], "N", "पाँचवाँ अवतार... कपिल मुनि। उन्होंने माता देवहूति को सांख्य योग का ज्ञान दिया।", ""),
    (["a05_ashes"], "N", "राजा सगर के साठ हज़ार पुत्रों ने उन पर चोरी का झूठा आरोप लगाया... और वे उनकी दृष्टि से भस्म हो गए।", "thunder"),
    (["a05_kapila"], "N", "उन्हीं के उद्धार के लिए... आगे चलकर राजा भगीरथ गंगा को धरती पर लाए।", ""),

    ("#", "6. दत्तात्रेय"),
    (["a06_anasuya"], "N", "छठा अवतार... दत्तात्रेय। माता अनसूया की परीक्षा लेने ब्रह्मा, विष्णु और महेश आए।", ""),
    (["a06_anasuya"], "N", "अनसूया ने अपने तप से तीनों को बालक बना दिया... और इन्हीं के अंश से जन्मे दत्तात्रेय।", ""),
    (["a06_dattatreya"], "N", "तीन मुख, छह भुजाएँ... उन्होंने पृथ्वी, जल और वायु तक को अपना गुरु बनाया। कुल चौबीस गुरु।", ""),

    ("#", "7. यज्ञ"),
    (["a07_yajna"], "N", "सातवाँ अवतार... यज्ञ। स्वायंभुव मनु के समय इंद्र का पद खाली था।", ""),
    (["a07_indra"], "N", "तब भगवान यज्ञ के रूप में प्रकट हुए... और स्वयं इंद्र बनकर देवताओं की रक्षा की।", ""),
    (["a07_yajna"], "N", "यज्ञ यानी त्याग और कर्तव्य... यही इस अवतार का संदेश है।", ""),

    ("#", "8. ऋषभदेव"),
    (["a08_rishabha"], "N", "आठवाँ अवतार... ऋषभदेव। राजा नाभि और मेरुदेवी के पुत्र, एक महान धर्मात्मा राजा।", ""),
    (["a08_bharat"], "N", "उनके पुत्र भरत के नाम पर ही... हमारे देश का नाम पड़ा, भारतवर्ष।", ""),
    (["a08_rishabha"], "N", "अंत में उन्होंने राज्य त्यागकर वैराग्य का मार्ग दिखाया... जैन धर्म में इन्हें पहले तीर्थंकर के रूप में पूजा जाता है।", ""),

    ("#", "9. राजा पृथु"),
    (["a09_prithu"], "N", "नौवाँ अवतार... राजा पृथु। अत्याचारी राजा वेन के बाद धरती ने अन्न देना बंद कर दिया था।", ""),
    (["a09_prithu"], "N", "क्रोधित पृथु ने धनुष उठाया... तो धरती गाय बनकर भागने लगी।", "thunder"),
    (["a09_fields"], "N", "धरती बोली, मुझे मत मारो, मुझे दुहो... और पृथु ने धरती से फिर अन्न और औषधियाँ प्रकट कीं।", ""),
    (["a09_fields"], "N", "इसीलिए धरती का नाम पड़ा... पृथ्वी।", ""),

    ("#", "10. मत्स्य अवतार"),
    (["a10_small_fish"], "N", "दसवाँ अवतार... मत्स्य। राजा सत्यव्रत की अंजलि में एक छोटी सी मछली आ गई।", ""),
    (["a10_small_fish"], "N", "मछली बढ़ती गई... घड़े से तालाब, तालाब से नदी, और नदी से समुद्र तक।", ""),
    (["a10_matsya"], "N", "तब भगवान ने बताया... सात दिन में प्रलय आएगी।", "thunder"),
    (["a10_matsya"], "N", "प्रलय की बाढ़ में... मत्स्य भगवान ने सप्तऋषियों, बीजों और वेदों से भरी नाव को बचाया।", ""),

    ("#", "11. कूर्म अवतार"),
    (["a11_churning"], "N", "ग्यारहवाँ अवतार... कूर्म। अमृत के लिए देवता और असुर समुद्र मंथन करने लगे।", ""),
    (["a11_churning"], "N", "मंदराचल पर्वत मथानी बना, वासुकि नाग रस्सी... पर पर्वत समुद्र में डूबने लगा।", ""),
    (["a11_kurma"], "N", "तब भगवान ने विशाल कछुए का रूप लिया... और पर्वत को अपनी पीठ पर थाम लिया।", ""),

    ("#", "12. धन्वंतरि"),
    (["a12_dhanvantari"], "N", "बारहवाँ अवतार... धन्वंतरि। समुद्र मंथन से हाथ में अमृत कलश लिए भगवान प्रकट हुए।", ""),
    (["a12_herbs"], "N", "वे आयुर्वेद के जनक और देवताओं के वैद्य कहलाए।", ""),
    (["a12_dhanvantari"], "N", "धनतेरस के दिन... इन्हीं की पूजा होती है।", ""),

    ("#", "13. मोहिनी"),
    (["a13_mohini"], "N", "तेरहवाँ अवतार... मोहिनी। अमृत कलश असुरों ने छीन लिया और आपस में लड़ने लगे।", ""),
    (["a13_mohini"], "N", "तभी एक अत्यंत सुंदर स्त्री प्रकट हुई... और मोहित असुरों ने अमृत बाँटने का काम उसे ही सौंप दिया।", ""),
    (["a13_nectar"], "N", "और मोहिनी ने... सारा अमृत देवताओं को पिला दिया।", ""),

    ("#", "14. हयग्रीव"),
    (["a14_demons"], "N", "चौदहवाँ अवतार... हयग्रीव। मधु और कैटभ नाम के दैत्य ब्रह्मा जी से वेद चुराकर ले गए।", ""),
    (["a14_demons"], "N", "बिना वेदों के... सृष्टि का ज्ञान ही खो गया।", ""),
    (["a14_hayagriva"], "N", "तब भगवान घोड़े के मुख वाले हयग्रीव रूप में आए... दैत्यों का वध किया और वेद लौटा दिए।", "thunder"),

    ("#", "15. नृसिंह अवतार"),
    (["a15_prahlad"], "N", "पंद्रहवाँ अवतार... नृसिंह। हिरण्यकशिपु को वरदान था, न मनुष्य मारे न पशु, न दिन में न रात में।", ""),
    (["a15_prahlad"], "N", "पर उसका अपना पुत्र प्रह्लाद... दिन-रात नारायण का नाम जपता था।", ""),
    (["a15_prahlad"], "N", "क्रोध में उसने पूछा... कहाँ है तेरा भगवान? क्या इस खंभे में भी है?", ""),
    (["a15_narasimha"], "N", "खंभा फटा... और आधे मनुष्य, आधे सिंह के रूप में नृसिंह भगवान प्रकट हुए।", "thunder"),
    (["a15_end"], "N", "संध्या के समय, दहलीज़ पर, अपनी गोद में रखकर... उन्होंने हिरण्यकशिपु का अंत किया।", ""),

    ("#", "16. वामन अवतार"),
    (["a16_vamana"], "N", "सोलहवाँ अवतार... वामन। दानवीर असुरराज बलि ने तीनों लोक जीत लिए थे।", ""),
    (["a16_vamana"], "N", "भगवान एक छोटे ब्राह्मण बालक बनकर आए... और माँगी सिर्फ़ तीन पग भूमि।", ""),
    (["a16_trivikrama"], "N", "बलि ने हाँ कहा... और वामन इतने बढ़े कि एक पग में धरती, दूसरे में आकाश नाप लिया।", "thunder"),
    (["a16_trivikrama"], "N", "तीसरे पग के लिए बलि ने सिर झुका दिया... और भगवान ने उसे पाताल का राजा बना दिया।", ""),

    ("#", "17. हंस अवतार"),
    (["a17_brahma"], "N", "सत्रहवाँ अवतार... हंस। सनकादि कुमारों ने ब्रह्मा जी से पूछा, मन को विषयों से कैसे छुड़ाएँ?", ""),
    (["a17_hamsa"], "N", "ब्रह्मा जी भी उत्तर न दे सके... तब भगवान एक दिव्य हंस के रूप में प्रकट हुए।", ""),
    (["a17_hamsa"], "N", "जैसे हंस दूध और पानी को अलग कर देता है... वैसे ही उन्होंने आत्मा और माया का भेद समझाया।", ""),

    ("#", "18. परशुराम"),
    (["parashurama_axe"], "N", "अठारहवाँ अवतार... परशुराम। ऋषि जमदग्नि के पुत्र, जिन्हें शिव जी से दिव्य परशु मिला।", ""),
    (["parashurama"], "N", "जब अहंकारी राजा सहस्रार्जुन ने उनके पिता का वध किया... तो परशुराम ने अधर्मी राजाओं का अंत किया।", "thunder"),
    (["parashurama_face"], "N", "वे चिरंजीवी हैं... और कल्कि पुराण कहता है, वही कल्कि भगवान के गुरु बनेंगे।", ""),

    ("#", "19. वेदव्यास"),
    (["a19_vedas"], "N", "उन्नीसवाँ अवतार... वेदव्यास। उन्होंने एक वेद को चार भागों में बाँटा, ताकि मनुष्य उसे समझ सकें।", ""),
    (["a19_vyasa"], "N", "उन्होंने अठारह पुराण रचे... और महाभारत, जिसे स्वयं गणेश जी ने लिखा।", ""),

    ("#", "20. श्रीराम"),
    (["a20_rama"], "N", "बीसवाँ अवतार... श्रीराम। अयोध्या के राजकुमार, मर्यादा पुरुषोत्तम।", ""),
    (["a20_ravana"], "N", "पिता के वचन के लिए चौदह वर्ष का वनवास... और सीता माता के लिए रावण से महायुद्ध।", "thunder"),
    (["a20_rama"], "N", "राम ने दिखाया... कि सबसे कठिन समय में भी धर्म का पालन कैसे किया जाता है।", ""),

    ("#", "21. बलराम"),
    (["a21_balarama"], "N", "इक्कीसवाँ अवतार... बलराम। श्रीकृष्ण के बड़े भाई, शेषनाग के अवतार।", ""),
    (["a21_balarama"], "N", "हाथ में हल और मूसल... उन्होंने प्रलंब और धेनुक जैसे असुरों का वध किया।", ""),

    ("#", "22. श्रीकृष्ण"),
    (["a22_krishna"], "N", "बाईसवाँ अवतार... श्रीकृष्ण। कारागार में जन्म, गोकुल में माखन चोरी और बांसुरी।", ""),
    (["a22_gita"], "N", "कंस का अंत, द्रौपदी की लाज की रक्षा... और कुरुक्षेत्र में अर्जुन को गीता का उपदेश।", ""),
    (["a22_krishna"], "N", "इसीलिए कहा गया... कृष्णस्तु भगवान स्वयम्। कृष्ण स्वयं भगवान हैं।", ""),

    ("#", "23. बुद्ध"),
    (["a23_buddha"], "N", "तेइसवाँ अवतार... बुद्ध। भागवत के अनुसार कलियुग के आरंभ में भगवान बुद्ध रूप में आए।", ""),
    (["a23_buddha"], "N", "उन्होंने हिंसा छोड़ने और करुणा अपनाने का संदेश दिया।", ""),

    ("#", "24. कल्कि अवतार"),
    (["kali_face"], "N", "और चौबीसवाँ अवतार... जो अभी आना बाकी है। कल्कि।", "thunder"),
    (["kali_face"], "N", "जब कलियुग अपने चरम पर होगा... और धर्म लगभग मिट चुका होगा।", ""),
    (["kalki_young_face"], "N", "तब शंभल गाँव में... विष्णुयश के घर कल्कि जन्म लेंगे।", ""),
    (["kalki"], "N", "सफ़ेद घोड़े देवदत्त पर, हाथ में चमकती तलवार... वे कलि का अंत करेंगे, और सतयुग फिर लौटेगा।", "thunder"),
    (["kalki_sword_raise"], "N", "कल्कि की पूरी कथा... हमारी कल्कि सीरीज़ में देखिए।", ""),

    ("#", "समापन"),
    (["vishnu_glow"], "N", "चौबीस अवतार... पर संदेश एक ही। जब-जब धर्म की हानि होगी, भगवान आएँगे।", ""),
    (["vishnu_promise"], "N", "आपको कौन सा अवतार सबसे प्रिय है? कमेंट में ज़रूर बताइए... जय श्री हरि!", ""),
]

MUSIC_PLAN = [(0.0, "Lightless Dawn.mp3", 0.0), ("a02_hiranyaksha", "Volatile Reaction.mp3", 0.0),
              ("a03_narada", "Long Note Four.mp3", 0.0), ("a09_prithu", "Heroic Age.mp3", 0.0),
              ("a10_small_fish", "Echoes of Time v2.mp3", 0.0), ("a14_demons", "Darkest Child.mp3", 0.0),
              ("a15_narasimha", "Prelude and Action.mp3", 0.0), ("a17_brahma", "Long Note Four.mp3", 60.0),
              ("a20_rama", "Undaunted.mp3", 0.0), ("kali_face", "Lightless Dawn.mp3", 60.0),
              ("kalki", "Five Armies.mp3", 60.0), ("vishnu_glow", "Echoes of Time v2.mp3", 200.0)]
MUSIC_CREDIT = ('"Lightless Dawn", "Volatile Reaction", "Long Note Four", "Heroic Age", "Echoes of Time v2", '
                '"Darkest Child", "Prelude and Action", "Undaunted", "Five Armies" - Kevin MacLeod (incompetech.com). '
                "Licensed under Creative Commons: By Attribution 4.0 License (CC BY 4.0)")

THUMB = dict(image="vishnu_glow", zoom=1.0, pany=0.0,
             text=[("24 अवतार", 170, (255, 214, 60), 150), ("भगवान विष्णु", 100, (255, 255, 255), 300)])

CORE_TAGS = ["bhagwan vishnu ke 24 avatar", "24 avatars of lord vishnu", "vishnu 24 avatar", "vishnu ke 24 avatar",
             "24 avatar", "24 avatars of vishnu", "bhagwan ke 24 avatar", "vishnu avatar", "avatars of vishnu",
             "vishnu 24 avatar name", "dashavatar", "lord vishnu", "srimad bhagavatam", "hindu mythology",
             "भगवान विष्णु के 24 अवतार", "विष्णु के अवतार", "विष्णु अवतार", "kalki avatar"]


def tags(extra):
    out, total = [], 0
    for t in dict.fromkeys(extra + CORE_TAGS):
        cost = len(t) + (2 if " " in t else 0) + 1
        if total + cost <= 490:
            out.append(t)
            total += cost
    return out


SEO = dict(
    title="भगवान विष्णु के 24 अवतार 🔱 पूरी कथा | Bhagwan Vishnu Ke 24 Avatar | सनकादि से कल्कि तक",
    description=f"""भगवान विष्णु के 24 अवतार कौन से हैं? मत्स्य, कूर्म, वराह, नृसिंह से लेकर राम, कृष्ण और कल्कि तक... श्रीमद्भागवत पुराण के अनुसार सभी 24 अवतारों की पूरी कथा, एक वीडियो में।

24 avatars of Lord Vishnu explained in Hindi: the story of every avatar from the Kumaras to Kalki, based on the Srimad Bhagavatam (Canto 1, Chapter 3 lists 22; the popular list of 24 adds Hamsa and Hayagriva).

⏱️ अवतार / Chapters
{{CHAPTERS}}

📖 स्रोत / Source: श्रीमद्भागवत पुराण 1.3, 2.7 और पौराणिक परंपरा
⚔️ कल्कि अवतार की पूरी कहानी - कल्कि सीरीज़: {KALKI_PLAYLIST}

🔔 चैनल को सब्सक्राइब करें और बेल आइकन दबाएँ!
📤 इस वीडियो को अपने परिवार और दोस्तों के साथ शेयर करें।
💬 कमेंट में लिखिए... आपका प्रिय अवतार कौन सा है? जय श्री हरि! 🙏

⚠️ Disclaimer: {{DISCLAIMER}}

🎵 Music: {{MUSIC_CREDIT}}

#vishnu #24avatar #bhagwanvishnu #vishnuavatar #kalki #sanatandharma #hindumythology #bhagavatam

© 2026 Sujay Ganguly Creations. All rights reserved. Story adaptation, script, artwork and video are by Sujay Ganguly Creations. Re-uploading or copying this video without permission is strictly prohibited.""",
    tags=tags(["24 avatars of vishnu in hindi", "vishnu ke avatar ki katha"]),
    categoryId="24",
)

# num, name (Hindi), Short hook (big text), first key, last key, music, title hook, extra tags
AVATARS = [
    (1, "सनकादि कुमार", "जो कभी बड़े नहीं हुए!", "a01_kumaras", "a01_gate", "Long Note Four.mp3",
     "वो 4 बालक जो कभी बड़े नहीं हुए 😮", ["sanakadi", "4 kumaras"]),
    (2, "वराह", "जब धरती डूब गई!", "a02_hiranyaksha", "a02_varaha", "Volatile Reaction.mp3",
     "जब पूरी धरती समुद्र में डूब गई 😱", ["varaha avatar", "varah avatar"]),
    (3, "नारद", "नारायण-नारायण!", "a03_narada", "a03_dhruva", "Long Note Four.mp3",
     "नारद मुनि भी विष्णु के अवतार हैं? 🤔", ["narad muni", "narada"]),
    (4, "नर-नारायण", "अर्जुन और कृष्ण का रहस्य", "a04_naranarayana", "a04_naranarayana", "Lightless Dawn.mp3",
     "अर्जुन और कृष्ण पिछले जन्म में कौन थे? 😮", ["nar narayan", "nara narayana"]),
    (5, "कपिल मुनि", "60,000 राजकुमार भस्म!", "a05_kapila", "a05_kapila", "Darkest Child.mp3",
     "एक नज़र से 60,000 राजकुमार भस्म 😱", ["kapil muni", "kapila"]),
    (6, "दत्तात्रेय", "3 देवता, 1 बालक!", "a06_anasuya", "a06_dattatreya", "Long Note Four.mp3",
     "जब ब्रह्मा विष्णु महेश बन गए बालक 😮", ["dattatreya", "datta jayanti"]),
    (7, "यज्ञ", "जब भगवान बने इंद्र!", "a07_yajna", "a07_yajna", "Heroic Age.mp3",
     "जब भगवान विष्णु स्वयं इंद्र बन गए 🔥", ["yajna avatar"]),
    (8, "ऋषभदेव", "भारत नाम कैसे पड़ा?", "a08_rishabha", "a08_rishabha", "Echoes of Time v2.mp3",
     "हमारे देश का नाम भारत कैसे पड़ा? 🇮🇳", ["rishabhdev", "bharat naam"]),
    (9, "पृथु", "धरती बन गई गाय!", "a09_prithu", "a09_fields", "Heroic Age.mp3",
     "जब धरती गाय बनकर भागी 😮 पृथ्वी नाम का रहस्य", ["prithu", "prithvi"]),
    (10, "मत्स्य", "मछली ने बचाई सृष्टि!", "a10_small_fish", "a10_matsya", "Echoes of Time v2.mp3",
     "जब एक मछली ने बचाई पूरी सृष्टि 🐟", ["matsya avatar", "pralay"]),
    (11, "कूर्म", "पर्वत डूबने लगा!", "a11_churning", "a11_kurma", "Volatile Reaction.mp3",
     "समुद्र मंथन में पर्वत डूबने लगा, तब 🐢", ["kurma avatar", "samudra manthan"]),
    (12, "धन्वंतरि", "अमृत कलश का रहस्य", "a12_dhanvantari", "a12_dhanvantari", "Long Note Four.mp3",
     "धनतेरस पर किसकी पूजा होती है? 🪔", ["dhanvantari", "dhanteras"]),
    (13, "मोहिनी", "असुरों को कैसे ठगा?", "a13_mohini", "a13_nectar", "Lightless Dawn.mp3",
     "जब विष्णु बने सबसे सुंदर स्त्री 😮 मोहिनी", ["mohini avatar", "amrit"]),
    (14, "हयग्रीव", "घोड़े के मुख वाले भगवान!", "a14_demons", "a14_hayagriva", "Darkest Child.mp3",
     "घोड़े के मुख वाले भगवान कौन हैं? 🐴", ["hayagriva", "madhu kaitabh"]),
    (15, "नृसिंह", "खंभे से निकले भगवान!", "a15_prahlad", "a15_end", "Prelude and Action.mp3",
     "जब खंभा फाड़कर निकले भगवान 🦁 नृसिंह", ["narasimha avatar", "prahlad", "holi"]),
    (16, "वामन", "3 पग में 3 लोक!", "a16_vamana", "a16_trivikrama", "Heroic Age.mp3",
     "3 पग में नाप लिए 3 लोक 😱 वामन अवतार", ["vamana avatar", "raja bali", "onam"]),
    (17, "हंस", "दूध और पानी का रहस्य", "a17_brahma", "a17_hamsa", "Long Note Four.mp3",
     "जब ब्रह्मा जी के पास भी उत्तर नहीं था 🦢", ["hamsa avatar"]),
    (18, "परशुराम", "कल्कि के गुरु!", "parashurama_axe", "parashurama_face", "Prelude and Action.mp3",
     "परशुराम आज भी जीवित हैं? 🪓 कल्कि के गुरु", ["parshuram", "chiranjeevi"]),
    (19, "वेदव्यास", "महाभारत किसने लिखी?", "a19_vedas", "a19_vyasa", "Echoes of Time v2.mp3",
     "महाभारत गणेश जी ने क्यों लिखी? 📜", ["ved vyas", "mahabharat"]),
    (20, "श्रीराम", "मर्यादा पुरुषोत्तम", "a20_rama", "a20_rama", "Undaunted.mp3",
     "श्रीराम विष्णु के कौन से अवतार हैं? 🏹", ["shri ram", "ramayan"]),
    (21, "बलराम", "हल वाले भगवान!", "a21_balarama", "a21_balarama", "Heroic Age.mp3",
     "बलराम किसके अवतार थे? 😮", ["balram", "sheshnag"]),
    (22, "श्रीकृष्ण", "स्वयं भगवान!", "a22_krishna", "a22_krishna", "Echoes of Time v2.mp3",
     "कृष्ण को स्वयं भगवान क्यों कहते हैं? 🦚", ["shri krishna", "bhagavad gita"]),
    (23, "बुद्ध", "क्या बुद्ध भी अवतार थे?", "a23_buddha", "a23_buddha", "Long Note Four.mp3",
     "क्या बुद्ध विष्णु के अवतार थे? 🙏", ["buddha avatar"]),
    (24, "कल्कि", "अभी आना बाकी है!", "kali_face", "kalki_sword_raise", "Five Armies.mp3",
     "विष्णु का आखिरी अवतार अभी आना बाकी है ⚔️ कल्कि", ["kalki avatar", "kalyug ka ant"]),
]


def _short(num, name, hook, first, last, music, title, extra):
    return dict(**{"from": first, "to": last}, hook=hook, hook2=f"अवतार {num}/24: {name}",
                music=[(0.0, music, 0.0)],
                seo=dict(title=f"{title} | विष्णु अवतार {num}/24 #shorts #vishnu",
                         description=f"""भगवान विष्णु के 24 अवतार - {num}/24: {name}।

🎬 सभी 24 अवतारों की पूरी कथा: {{FULL_EPISODE}}
⚔️ कल्कि सीरीज़: {KALKI_PLAYLIST}
🔔 रोज़ एक नया अवतार - चैनल को सब्सक्राइब करें और शेयर करें!

⚠️ {{DISCLAIMER}}
🎵 Music: {{MUSIC_CREDIT}}

#shorts #vishnu #24avatar #bhagwanvishnu #sanatan

© 2026 Sujay Ganguly Creations. All rights reserved.""",
                         tags=tags(extra + ["shorts", "vishnu shorts"]), categoryId="24"))


SHORTS = [_short(*a) for a in AVATARS]
