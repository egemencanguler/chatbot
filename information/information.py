# Question Place Holders
Q_STUDENT_NO = "<StudentNo>"
Q_COURSE_CODE = "<CourceCode>"
Q_COURSE_NAME = "<CourseName>"
Q_CLASSROOM = "<Classroom>"
Q_NAME = "<Name>"

QUESTION_PLACEHOLDERS = [Q_STUDENT_NO,Q_COURSE_CODE,Q_COURSE_NAME,Q_CLASSROOM,Q_NAME]

# Answer Placeholders
A_CLASSROOM_LOC = "<ClassroomLoc>"
A_STUDENT_NO = "<StudentNo>"
A_OFFICE = "<Office>"
A_MAIL = "<Mail>"
A_TEL = "<Tel>"
A_RESEARCH_AREAS = "<ResearchAreas>"
A_WEBSITE = "<WebSite>"

ANSWER_PLACEHOLDERS = [A_CLASSROOM_LOC,A_STUDENT_NO,A_OFFICE,A_MAIL,A_TEL,A_RESEARCH_AREAS,A_WEBSITE]




class InformationManager:
    # Singleton
    __instance = None
    def __new__(cls):
        if InformationManager.__instance is None:
            InformationManager.__instance = object.__new__(cls)
            InformationManager.__instance.statementTokens = {}
        return InformationManager.__instance

    def putTokenValue(self,statementToken, value):
        self.statementTokens[statementToken] = value

    def getTokenValue(self,statementToken):
        if statementToken in self.statementTokens:
            return self.statementTokens[statementToken]
        return None

    def getInfo(self,answerToken):
        # if answerToken == ATOKEN_CLASSROOM_FLOOR_INFO:
        #     return INFOS[self.getTokenValue(STOKEN_CLASSROOM)]
        return "INFO"


PEOPLE = {
   'Fuat AKAL':{
      'title':'Yardımcı Doçent Fuat AKAL',
      'mail':'akal@hacettepe.edu.tr',
      'tel':'(0312) 780 7503',
      'office':'202',
      'website':'http://yunus.hacettepe.edu.tr/~akal/',
      'research':'Büyük Veri, Bulut Hesaplama, Bulut Veritabanları, Veri Yönetimi, Veri Analizi, Dağıtık Bilişim Sistemleri, Veritabanı Kümeleri'
   },
   'Ebru AKÇAPINAR SEZER':{
      'title':'Profesör Ebru AKÇAPINAR SEZER',
      'mail':'ebru@hacettepe.edu.tr',
      'tel':'(0312) 780 7544',
      'office':'138',
      'website':'http://yunus.hacettepe.edu.tr/~ebru/',
      'research':'Semantik Bilgi Çıkarımı Sistemleri'
   },
   'Harun ARTUNER':{
      'title':'Doçent Harun ARTUNER',
      'mail':'artuner@hacettepe.edu.tr',
      'tel':'(0312) 780 7553',
      'office':'136',
      'website':'http://yunus.hacettepe.edu.tr/~artuner/',
      'research':'--'
   },
   'Murat AYDOS':{
      'title':'Yardımcı Doçent Murat AYDOS',
      'mail':'maydos@hacettepe.edu.tr',
      'tel':'(0312) 780 7530',
      'office':'207',
      'website':'http://web.cs.hacettepe.edu.tr/~maydos/',
      'research':'Kriptografi, Bilgi ve Ağ Güvenliği, Kablosuz Ağlarda Güvenlik ve Mahremiyet, Sayısal Sertifikalar, Açık Anahtarlı Kripto Sistemleri'
   },
   'Ahmet Burak CAN':{
      'title':'Doçent Ahmet Burak CAN',
      'mail':'abc@hacettepe.edu.tr',
      'tel':'(0312) 780 7508',
      'office':'205',
      'website':'http://web.cs.hacettepe.edu.tr/~abc/',
      'research':'Bilgisayarlı Görü, Bilgi Güvenliği, Dağıtık Sistemler'
   },
   'Burcu CAN':{
      'title':'Yardımcı Doçent Burcu CAN',
      'mail':'burcucan@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7530',
      'office':'121',
      'website':'http://web.cs.hacettepe.edu.tr/~burcucan/',
      'research':'Doğal Dil İşleme, Hesaplamalı Dilbilimi, Makine Öğrenmesi, Gözetimsiz, Yarı-Gözetimli Öğrenme'
   },
   'Ufuk ÇELİKCAN':{
      'title':'Yardımcı Doçent Ufuk ÇELİKCAN',
      'mail':'celikcan@hacettepe.edu.tr',
      'tel':'(0312) 780 7533',
      'office':'204',
      'website':'http://web.cs.hacettepe.edu.tr/~celikcan/',
      'research':'Bilgisayar Grafiği, Bilgisayarlı Animasyon, 3B Görüş ve Stereoskopi, Sanal Gerçeklik, İnsan Hareketi Sentezi ve Analizi, Ciddi Oyunlar'
   },
   'İlyas ÇİÇEKLİ':{
      'title':'Profesör İlyas ÇİÇEKLİ',
      'mail':'ilyas@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7526',
      'office':'--',
      'website':'http://web.cs.hacettepe.edu.tr/~ilyas/',
      'research':'Doğal Dil İşleme, Makine Çevirisi, Hesaplamalı Dilbilimi, Veri Madenciliği, Yapay Zeka'
   },
   'Pınar DUYGULU ŞAHİN':{
      'title':'Profesör Pınar DUYGULU ŞAHİN',
      'mail':'pinar@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7532',
      'office':'123',
      'website':'http://web.cs.hacettepe.edu.tr/~pinar/',
      'research':'Bilgisayarlı Görü, Çokluortam Veri Madenciliği, Nesne-Yüz ve Hareket Tanıma, Tarihi Belgelerin Analizi'
   },
   'Mehmet Önder EFE':{
      'title':'Profesör Mehmet Önder EFE',
      'mail':'onderefe@hacettepe.edu.tr',
      'tel':'(0312) 780 7554',
      'office':'114',
      'website':'http://web.cs.hacettepe.edu.tr/~onderefe/',
      'research':'İnsansız Hava Araçları, Sensörler, Eyleyiciler, Yönlendirme, Seyrüsefer, Kontrol, Akıllı Mekatronik, Hesaplamalı Zeka'
   },
   'Mustafa EGE':{
      'title':'Yardımcı Doçent Mustafa EGE',
      'mail':'ege@hacettepe.edu.tr',
      'tel':'(0312) 780 7541',
      'office':'110',
      'website':'--',
      'research':'--'
   },
   'Gönenç ERCAN':{
      'title':'Yardımcı Doçent Gönenç ERCAN',
      'mail':'gonenc@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7548',
      'office':'213',
      'website':'http://www.gonencercan.com',
      'research':'Doğal Dil İşleme, Bilgi Getirimi, Yapay Zeka'
   },
   'Erkut ERDEM':{
      'title':'Yardımcı Doçent Erkut ERDEM',
      'mail':'erkut@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7549',
      'office':'114',
      'website':'http://web.cs.hacettepe.edu.tr/~erkut/',
      'research':'Görsel Belirginlik Kestirimi, Otomatik Görüntü Açıklama, Video/Fotoğraf Kümesi Özetleme, Görüntü Filtreleme, Görüntü Düzenleme'
   },
   'İbrahim Aykut ERDEM':{
      'title':'Yardımcı Doçent İbrahim Aykut ERDEM',
      'mail':'aykut@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7545',
      'office':'111',
      'website':'http://web.cs.hacettepe.edu.tr/~aykut/',
      'research':'İmge Düzenleme, Görsel Veri Madenciliği, Dil ve Görünün Bütünleştirilmesi'
   },
   'Vahid GAROUSI':{
      'title':'Doçent Vahid GAROUSI',
      'mail':'vahid@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7506',
      'office':'106',
      'website':'http://web.cs.hacettepe.edu.tr/~vahid/',
      'research':'Yazılım Mühendisliği, Yazılım Testi, Yazılım Test Mühendisliği ve Kalite Güvence'
   },
   'Haşmet GÜRÇAY':{
      'title':'Profesör Haşmet GÜRÇAY',
      'mail':'gurcay@hacettepe.edu.tr',
      'tel':'(0312) 297 7889 (210)',
      'office':'210',
      'website':'http://yunus.hacettepe.edu.tr/~gurcay/',
      'research':'Bilgisayar Grafiği, Bilgisayar Animasyonu, Video Oyunları, Sanal Gerçeklik, Hesaplamalı Geometri'
   },
   'Nazlı İKİZLER CİNBİŞ':{
      'title':'Yardımcı Doçent Nazlı İKİZLER CİNBİŞ',
      'mail':'nazli@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7537',
      'office':'112',
      'website':'http://web.cs.hacettepe.edu.tr/~nazli/',
      'research':'Bilgisayarlı Görü, İnsan Hareketi/Aktivitesi Tanıma'
   },
   'Kayhan İMRE':{
      'title':'Yardımcı Doçent Kayhan İMRE',
      'mail':'ki@hacettepe.edu.tr',
      'tel':'(0312) 780 7552',
      'office':'107',
      'website':'http://web.cs.hacettepe.edu.tr/~kimre/',
      'research':'--'
   },
   'Mehmet KÖSEOĞLU':{
      'title':'Yardımcı Doçent Mehmet KÖSEOĞLU',
      'mail':'mkoseoglu@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7513',
      'office':'219',
      'website':'http://web.cs.hacettepe.edu.tr/~mkoseoglu/',
      'research':'Kablosuz Ağlar, 4G/5G Kablosuz Haberleşme, Nesnelerin İnterneti, Sualtı Akustik Ağlar'
   },
   'Erhan MENGÜŞOĞLU':{
      'title':'Yardımcı Doçent Erhan MENGÜŞOĞLU',
      'mail':'emengusoglu@hacettepe.edu.tr',
      'tel':'(0312) 297 7500',
      'office':'201',
      'website':'erhan_mengusoglu_CVa.pdf',
      'research':'Konuşma Tanıma, Karmaşık Olay İşleme, Doğal Dil İşleme, Yazılım Mühendisliği, Makine Öğrenmesi'
   },
   'Lale ÖZKAHYA':{
      'title':'Doçent Lale ÖZKAHYA',
      'mail':'ozkahya@hacettepe.edu.tr',
      'tel':'(0312) 780 7551',
      'office':'203',
      'website':'http://web.cs.hacettepe.edu.tr/~ozkahya/',
      'research':'Kombinatorik, Çizge Kuramı ve Uygulamaları'
   },
   'Adnan ÖZSOY':{
      'title':'Yardımcı Doçent Adnan ÖZSOY',
      'mail':'adnan.ozsoy@hacettepe.edu.tr',
      'tel':'(0312) 780 7510',
      'office':'Z08',
      'website':'http://web.cs.hacettepe.edu.tr/~aozsoy/',
      'research':'Paralel Programlama, Yüksek Başarımlı Hesaplamalar, GPGPUs, Büyük Veri Problemleri, Dağıtık Sis. ve Uyg. Paralelleştirme Problemleri'
   },
   'Hayri SEVER':{
      'title':'Profesör Hayri SEVER',
      'mail':'sever@hacettepe.edu.tr',
      'tel':'(0312) 780 7546',
      'office':'108',
      'website':'http://yunus.hacettepe.edu.tr/~sever/',
      'research':'Çok-ortamlı Bilgi Erişim (ve Süzme) Modelleri, Veri ve Web Madenciliği, Ses Analizi, Anlamsal Analiz, Coğrafi Bilgi Sistemleri'
   },
   'Sevil ŞEN':{
      'title':'Doçent Sevil ŞEN',
      'mail':'ssen@cs.hacettepe.edu.tr',
      'tel':'(0312) 780 7538',
      'office':'148',
      'website':'http://web.cs.hacettepe.edu.tr/~ssen/',
      'research':'Ağ ve Sistem Güvenliği, Kablosuz Ağlar, Mobil Sistemler, Makina Öğrenmesi, Evrimsel Hesaplama'
   },
   'Ayça TARHAN':{
      'title':'Yardımcı Doçent Ayça TARHAN',
      'mail':'atarhan@hacettepe.edu.tr',
      'tel':'(0312) 780 7550',
      'office':'206',
      'website':'http://web.cs.hacettepe.edu.tr/~atarhan/',
      'research':'Yazılım Mühendisliği, Yazılım Kalite Yönetimi, Yazılım Metrikleri, Süreç Olgunluğu, Süreç Analizi, Sağlık Bilişim Sistemleri'
   },
   'Süleyman TOSUN':{
      'title':'Doçent Süleyman TOSUN',
      'mail':'stosun@hacettepe.edu.tr',
      'tel':'(0312) 780 7531',
      'office':'210',
      'website':'http://web.cs.hacettepe.edu.tr/~stosun/',
      'research':'Bilgisayar Mimarisi, Elektronik Tasarım Otomasyonu, Yonga-üstü-Ağ (YüA), Çoklu İşlemciler, Zamanlama'
   }
}

LOCATIONS = {
   "d1":"bodrum",
   "d2":"bodrum",
   "d3":"bodrum",
   "d4":"bodrum",
   "d5":"zemin",
   "d6":"zemin",
   "d7":"zemin",
   "d8":"1.",
   "d9":"1.",
   "d10":"2."
}
