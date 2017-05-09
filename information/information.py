# Question Place Holders
Q_STUDENT_NO = "<StudentNo>"
Q_COURSE_CODE = "<CourseCode>"
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
A_COURSE_INFO = "<CourseInfo>"
A_COURSE_CODE = "<CourseCode>"
A_COURSE_NAME = "<CourseName>"
A_COURSE_CREDIT = "<CourseCredit>"
A_TIME = "<Time>"

ANSWER_PLACEHOLDERS = [A_CLASSROOM_LOC,A_STUDENT_NO,A_OFFICE,A_MAIL,A_TEL,A_RESEARCH_AREAS,A_WEBSITE,A_COURSE_INFO,A_COURSE_CODE,A_COURSE_NAME,A_COURSE_CREDIT,A_TIME]




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
      '<Mail>':'akal@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7503',
      '<Office>':'202',
      '<WebSite>':'http://yunus.hacettepe.edu.tr/~akal/',
      '<ResearchAreas>':'Büyük Veri, Bulut Hesaplama, Bulut Veritabanları, Veri Yönetimi, Veri Analizi, Dağıtık Bilişim Sistemleri, Veritabanı Kümeleri'
   },
   'Ebru AKÇAPINAR SEZER':{
      'title':'Profesör Ebru AKÇAPINAR SEZER',
      '<Mail>':'ebru@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7544',
      '<Office>':'138',
      '<WebSite>':'http://yunus.hacettepe.edu.tr/~ebru/',
      '<ResearchAreas>':'Semantik Bilgi Çıkarımı Sistemleri'
   },
   'Harun ARTUNER':{
      'title':'Doçent Harun ARTUNER',
      '<Mail>':'artuner@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7553',
      '<Office>':'136',
      '<WebSite>':'http://yunus.hacettepe.edu.tr/~artuner/',
      '<ResearchAreas>':'--'
   },
   'Murat AYDOS':{
      'title':'Yardımcı Doçent Murat AYDOS',
      '<Mail>':'maydos@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7530',
      '<Office>':'207',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~maydos/',
      '<ResearchAreas>':'Kriptografi, Bilgi ve Ağ Güvenliği, Kablosuz Ağlarda Güvenlik ve Mahremiyet, Sayısal Sertifikalar, Açık Anahtarlı Kripto Sistemleri'
   },
   'Ahmet Burak CAN':{
      'title':'Doçent Ahmet Burak CAN',
      '<Mail>':'abc@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7508',
      '<Office>':'205',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~abc/',
      '<ResearchAreas>':'Bilgisayarlı Görü, Bilgi Güvenliği, Dağıtık Sistemler'
   },
   'Burcu CAN':{
      'title':'Yardımcı Doçent Burcu CAN',
      '<Mail>':'burcucan@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7530',
      '<Office>':'121',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~burcucan/',
      '<ResearchAreas>':'Doğal Dil İşleme, Hesaplamalı Dilbilimi, Makine Öğrenmesi, Gözetimsiz, Yarı-Gözetimli Öğrenme'
   },
   'Ufuk ÇELİKCAN':{
      'title':'Yardımcı Doçent Ufuk ÇELİKCAN',
      '<Mail>':'celikcan@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7533',
      '<Office>':'204',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~celikcan/',
      '<ResearchAreas>':'Bilgisayar Grafiği, Bilgisayarlı Animasyon, 3B Görüş ve Stereoskopi, Sanal Gerçeklik, İnsan Hareketi Sentezi ve Analizi, Ciddi Oyunlar'
   },
   'İlyas ÇİÇEKLİ':{
      'title':'Profesör İlyas ÇİÇEKLİ',
      '<Mail>':'ilyas@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7526',
      '<Office>':'--',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~ilyas/',
      '<ResearchAreas>':'Doğal Dil İşleme, Makine Çevirisi, Hesaplamalı Dilbilimi, Veri Madenciliği, Yapay Zeka'
   },
   'Pınar DUYGULU ŞAHİN':{
      'title':'Profesör Pınar DUYGULU ŞAHİN',
      '<Mail>':'pinar@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7532',
      '<Office>':'123',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~pinar/',
      '<ResearchAreas>':'Bilgisayarlı Görü, Çokluortam Veri Madenciliği, Nesne-Yüz ve Hareket Tanıma, Tarihi Belgelerin Analizi'
   },
   'Mehmet Önder EFE':{
      'title':'Profesör Mehmet Önder EFE',
      '<Mail>':'onderefe@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7554',
      '<Office>':'114',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~onderefe/',
      '<ResearchAreas>':'İnsansız Hava Araçları, Sensörler, Eyleyiciler, Yönlendirme, Seyrüsefer, Kontrol, Akıllı Mekatronik, Hesaplamalı Zeka'
   },
   'Mustafa EGE':{
      'title':'Yardımcı Doçent Mustafa EGE',
      '<Mail>':'ege@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7541',
      '<Office>':'110',
      '<WebSite>':'--',
      '<ResearchAreas>':'--'
   },
   'Gönenç ERCAN':{
      'title':'Yardımcı Doçent Gönenç ERCAN',
      '<Mail>':'gonenc@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7548',
      '<Office>':'213',
      '<WebSite>':'http://www.gonencercan.com',
      '<ResearchAreas>':'Doğal Dil İşleme, Bilgi Getirimi, Yapay Zeka'
   },
   'Erkut ERDEM':{
      'title':'Yardımcı Doçent Erkut ERDEM',
      '<Mail>':'erkut@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7549',
      '<Office>':'114',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~erkut/',
      '<ResearchAreas>':'Görsel Belirginlik Kestirimi, Otomatik Görüntü Açıklama, Video/Fotoğraf Kümesi Özetleme, Görüntü Filtreleme, Görüntü Düzenleme'
   },
   'İbrahim Aykut ERDEM':{
      'title':'Yardımcı Doçent İbrahim Aykut ERDEM',
      '<Mail>':'aykut@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7545',
      '<Office>':'111',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~aykut/',
      '<ResearchAreas>':'İmge Düzenleme, Görsel Veri Madenciliği, Dil ve Görünün Bütünleştirilmesi'
   },
   'Vahid GAROUSI':{
      'title':'Doçent Vahid GAROUSI',
      '<Mail>':'vahid@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7506',
      '<Office>':'106',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~vahid/',
      '<ResearchAreas>':'Yazılım Mühendisliği, Yazılım Testi, Yazılım Test Mühendisliği ve Kalite Güvence'
   },
   'Haşmet GÜRÇAY':{
      'title':'Profesör Haşmet GÜRÇAY',
      '<Mail>':'gurcay@hacettepe.edu.tr',
      '<Tel>':'(0312) 297 7889 (210)',
      '<Office>':'210',
      '<WebSite>':'http://yunus.hacettepe.edu.tr/~gurcay/',
      '<ResearchAreas>':'Bilgisayar Grafiği, Bilgisayar Animasyonu, Video Oyunları, Sanal Gerçeklik, Hesaplamalı Geometri'
   },
   'Nazlı İKİZLER CİNBİŞ':{
      'title':'Yardımcı Doçent Nazlı İKİZLER CİNBİŞ',
      '<Mail>':'nazli@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7537',
      '<Office>':'112',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~nazli/',
      '<ResearchAreas>':'Bilgisayarlı Görü, İnsan Hareketi/Aktivitesi Tanıma'
   },
   'Kayhan İMRE':{
      'title':'Yardımcı Doçent Kayhan İMRE',
      '<Mail>':'ki@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7552',
      '<Office>':'107',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~kimre/',
      '<ResearchAreas>':'--'
   },
   'Mehmet KÖSEOĞLU':{
      'title':'Yardımcı Doçent Mehmet KÖSEOĞLU',
      '<Mail>':'mkoseoglu@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7513',
      '<Office>':'219',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~mkoseoglu/',
      '<ResearchAreas>':'Kablosuz Ağlar, 4G/5G Kablosuz Haberleşme, Nesnelerin İnterneti, Sualtı Akustik Ağlar'
   },
   'Erhan MENGÜŞOĞLU':{
      'title':'Yardımcı Doçent Erhan MENGÜŞOĞLU',
      '<Mail>':'emengusoglu@hacettepe.edu.tr',
      '<Tel>':'(0312) 297 7500',
      '<Office>':'201',
      '<WebSite>':'erhan_mengusoglu_CVa.pdf',
      '<ResearchAreas>':'Konuşma Tanıma, Karmaşık Olay İşleme, Doğal Dil İşleme, Yazılım Mühendisliği, Makine Öğrenmesi'
   },
   'Lale ÖZKAHYA':{
      'title':'Doçent Lale ÖZKAHYA',
      '<Mail>':'ozkahya@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7551',
      '<Office>':'203',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~ozkahya/',
      '<ResearchAreas>':'Kombinatorik, Çizge Kuramı ve Uygulamaları'
   },
   'Adnan ÖZSOY':{
      'title':'Yardımcı Doçent Adnan ÖZSOY',
      '<Mail>':'adnan.ozsoy@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7510',
      '<Office>':'Z08',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~aozsoy/',
      '<ResearchAreas>':'Paralel Programlama, Yüksek Başarımlı Hesaplamalar, GPGPUs, Büyük Veri Problemleri, Dağıtık Sis. ve Uyg. Paralelleştirme Problemleri'
   },
   'Hayri SEVER':{
      'title':'Profesör Hayri SEVER',
      '<Mail>':'sever@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7546',
      '<Office>':'108',
      '<WebSite>':'http://yunus.hacettepe.edu.tr/~sever/',
      '<ResearchAreas>':'Çok-ortamlı Bilgi Erişim (ve Süzme) Modelleri, Veri ve Web Madenciliği, Ses Analizi, Anlamsal Analiz, Coğrafi Bilgi Sistemleri'
   },
   'Sevil ŞEN':{
      'title':'Doçent Sevil ŞEN',
      '<Mail>':'ssen@cs.hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7538',
      '<Office>':'148',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~ssen/',
      '<ResearchAreas>':'Ağ ve Sistem Güvenliği, Kablosuz Ağlar, Mobil Sistemler, Makina Öğrenmesi, Evrimsel Hesaplama'
   },
   'Ayça TARHAN':{
      'title':'Yardımcı Doçent Ayça TARHAN',
      '<Mail>':'atarhan@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7550',
      '<Office>':'206',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~atarhan/',
      '<ResearchAreas>':'Yazılım Mühendisliği, Yazılım Kalite Yönetimi, Yazılım Metrikleri, Süreç Olgunluğu, Süreç Analizi, Sağlık Bilişim Sistemleri'
   },
   'Süleyman TOSUN':{
      'title':'Doçent Süleyman TOSUN',
      '<Mail>':'stosun@hacettepe.edu.tr',
      '<Tel>':'(0312) 780 7531',
      '<Office>':'210',
      '<WebSite>':'http://web.cs.hacettepe.edu.tr/~stosun/',
      '<ResearchAreas>':'Bilgisayar Mimarisi, Elektronik Tasarım Otomasyonu, Yonga-üstü-Ağ (YüA), Çoklu İşlemciler, Zamanlama'
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

COURSES = {
   'Programlamaya Giriş 1':{
      '<CourseCode>':'BBM101',
      '<CourseName>':'Programlamaya Giriş 1',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bilgisayar programlamada temel kavramlar. Problem biçimselleştirme ve adımsal geliştirme yöntemiyle algoritma ve akış şemalarını geliştirme. Yapısal programlamayla ilgili temel kavramlar. Veri türleri ve değişken tanımlamaları. Temel kontrol yapıları. Şartlı dallanma ve döngüsel yapılar. İşlev kavramı ve işlevleri çağırma. Programlama dillerinde tek ve çok boyutlu diziler. Kütük işlemleri. Göstericiler.\n'
   },
   'Programlamaya Giriş Laboratuvarı 1':{
      '<CourseCode>':'BBM103',
      '<CourseName>':'Programlamaya Giriş Laboratuvarı 1',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Programlamaya Giriş 11':{
      '<CourseCode>':'BBM102',
      '<CourseName>':'Programlamaya Giriş 11',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Nesneye yönelik programlamanın temel kavramları. Nesneye yönelik programlama dillerini öğrenmeye giriş. Sınıf, nesne, sarmalama, kalıtım, çok-biçimlilik, soyut sınıf ve arayüz. Erişim denetleyiciler ve iletiler. Hata yönetme kavramları.\n'
   },
   'Programlamaya Giriş Laboratuvarı 11':{
      '<CourseCode>':'BBM104',
      '<CourseName>':'Programlamaya Giriş Laboratuvarı 11',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Veri Yapıları':{
      '<CourseCode>':'BBM201',
      '<CourseName>':'Veri Yapıları',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Veri yapılarının temelleri. Veri temsilleri arasındaki ilişkiler, algoritma tasarımı ve program verimliliği. Listeler, yığıtlar, kuyruklar, ağaçlar, öncelik kuyrukları, anahtarlama, çizgeler. Çok boyutlu/üçgensel/bant/matris gösterimleri. Tekil ve ikili dairesel bağlı listeler. Önde/arada/sonda deyimler.\n'
   },
   'Kesikli Matematiksel Yapılar':{
      '<CourseCode>':'BBM205',
      '<CourseName>':'Kesikli Matematiksel Yapılar',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Kesikli matematik üzerine temel kavramlar: Matematiksel mantık, küme teorisi, ilişkiler ve işlevler. Önermeler mantığı, birinci düzey mantık ve matematiksel tümevarım. Kesikli yapılar: modüler aritmetik, durum makineleri, çizge teorisi, ağaçlar, sayma, özyineleme ve özyineli ilişkiler. Kesikli olasılık teorisi.\n'
   },
   'Mantıksal Tasarım Laboratuvarı':{
      '<CourseCode>':'BBM233',
      '<CourseName>':'Mantıksal Tasarım Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Laboratuvar dersi aşağıda listesi verilen konular üzerinde uygulamalı ödevler içermektedir: Mantıksal kapılar, tümleşik devreler, Bool cebirinin özellikleri ve kuralları, birleşimli devreler, Bool işlevlerinin enküçüklemesi. Kod çeviriciler, çoklayıcılar, büyüklük karşılaştırıcı ve koşut toplayıcı devreler. İki durumlular ve sıralı devreler. Sayaçlar, yazmaçlar, seri toplayıcı devreler ve bellek elemanları.\n'
   },
   'Mantıksal Tasarım':{
      '<CourseCode>':'BBM231',
      '<CourseName>':'Mantıksal Tasarım',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Sayısal sistemler, sayı sistemleri, ikili kodlar, hata tespit ve hata düzeltme kodları, Bool cebiri, anahtarlamalı cebir, ikili operasyonlar ve Bool işlevleri. Bool işlevlerinin minimizasyonu. Toplamsal mantık, mantık kapıları, toplamsal devrelerin minimizasyonu, mantık kapılarıyla devre tasarımı. Tümleşim devreler, MSO çipsetleriyle tasarım, ROM, PLA. Eşzamanlı sıralı devreler, bellek elemanları, analiz ve tasarım prosedürleri. Yazmaçlar, sayaçlar, RAM. Zaman uyumsuz sıralı devreler.\n'
   },
   'Yazılım Laboratuvarı 1':{
      '<CourseCode>':'BBM203',
      '<CourseName>':'Yazılım Laboratuvarı 1',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Algoritmalar':{
      '<CourseCode>':'BBM202',
      '<CourseName>':'Algoritmalar',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Algoritmalarla ilgili temel kavramlar. Asimtotik gösterim, başarım ölçütleri, alan/zaman karmaşıklığı. Özyinelemeli algoritmalar, özyineli ilişkiler, algoritma çözümleme kavramına giriş. İkili arama ağacı, tekrarlı ve özyineli ikili ağaç tarama. Çizgeler, önce derinlik, önce genişlik tabanlı arama, yayılım ağaçları, en kısa yol problem, kenar/ayrıt ağları üzerinde işlemler. Seçimli, eklemeleri, kabarcık, sayma tabanlı, hızlı, toplamsal, yığın ve radiks sıralama algoritmaları ve çözümlemeleri.\n'
   },
   'Bilgisayar Yapısı':{
      '<CourseCode>':'BBM234',
      '<CourseName>':'Bilgisayar Yapısı',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bilgisayar mimarisine ilişkin temel matematiksel ve mantıksal kavramlar. Veri temsili. Temel bilgisayar yapısı. Merkezi işlemci yapılanması: Akümülator-tabanlı, genel yazmaç tabanlı işlemciler ve yığıt makinesi mimarileri. Makine kod komut kavramları, mikro programlama kavramı, adresleme biçimleri. Bellek yapısı. Büyük depolama aygıtları. Giriş/çıkış birimleri. Sembolik programlamaya giriş.\n'
   },
   'Yazılım Laboratuvarı 11':{
      '<CourseCode>':'BBM204',
      '<CourseName>':'Yazılım Laboratuvarı 11',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Veri Yönetimi':{
      '<CourseCode>':'BBM371',
      '<CourseName>':'Veri Yönetimi',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Temel kütük kavramları. İkincil depolama araçları ve fiziksel kütük organizasyonu. Kütük yönetim dizgeleri ve türleri. Temel kütük işleme operasyonları. Dizinler ve türleri. Anahtarlı dizinleme ve türleri. Ağaç yapısındaki dizinler. Sıralama. Uzamsal ve çok boyutlu dizinleme yapıları. Katlanmış dizinler.\n'
   },
   'Programlama Dilleri':{
      '<CourseCode>':'BBM301',
      '<CourseName>':'Programlama Dilleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Programlama dillerindeki temel prensipler ve paradigmalar. Tüm ana konular ve dil paradigmaları kapsanmaktadır. Sözdizim, anlam, adlar, atamalar, tür kontrolü, alt programlar, anlamsal ve sözdizimsel çözümleyiciler, soyut veri türleri, tutarlılık, hata yönetimi. Buyurgan ve işlevsel diller için farklı tasarım seçenekleri ile anlamsal ve sözdizimsel çözümleyicilerin tasarımı.\n'
   },
   'Sistem Programlama':{
      '<CourseCode>':'BBM341',
      '<CourseName>':'Sistem Programlama',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Sembolik dilin genel kavramları. Kaynak ve hedef program. Re-entrant ve tekrar çalıştırılabilir programlar. Adresleme teknikleri. Yordam tanımlamaları, yordam iletişim teknikleri, macro olanakları, İşletim sistemi- sembolik dil bağlantısı: Sistem çağrıları. Sistem çağrı mekanizması, giriş/çıkış arayüzleri. Yükleyiciler, bağlayıcılar. Mikro programlama. Tek ve çift geçişli birleştiriciler. Kesme mekanizması, kesme yönetimi. Temel I/O programlama teknikleri. Zamanlanmış ve kesmeye dayalı I/O programlama. Doğrudan bellek erişimi. Gömülü sistem I/O programlama örnekleri. Aygıt sürücüleri: Aygıt türleri, karakter aygıt sürücüleri ve örnekler, blok aygıt sürücüleri.\n'
   },
   'işletim Sistemleri':{
      '<CourseCode>':'BBM342',
      '<CourseName>':'işletim Sistemleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'İşletim sisteminin tanımı. Görev, süreç, toplu ve etkileşimli işleme, çoklu-görev ve gerçek-zamanlı işleme kavramları. Süreçler, bağlam ve görev değişimi, UNIX süreç durumu ve kuyruk çizenekleri, süreçlerin yönetim algoritmaları. İzlekler. Eş zamanlı süreçler. Süreçler arası iletişim, zaman-uyumlama, karşılıklı kaynak paylaşımı. Alt düzeyde zaman-uyumlama operasyonları ve semaforlar. Üst düzey zaman-uyumlama işlevleri. UNIX iletişim kanalları ve FIFOs. Kilitlenmeler. Bellek yönetimi: Tekil ve sürekli durağan bölümlemeli bellekler, değişim, sayfalama, bölütleme, sanal bellek. Kütük yönetimi: Dizin yapıları. FAT, i-node yapıları, kütük yerleşimi yöntemleri, güvenlik ve koruma. Dağıtık işleme, TCP/IP, istemci sunucu paradigması, soket programlama.\n'
   },
   'Yazılım Mühendisliği':{
      '<CourseCode>':'BBM382',
      '<CourseName>':'Yazılım Mühendisliği',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Yazılım mühendisliğinin temel kavramları. Bilgisayar sistemlerinin türleri ve bir parçası olarak yazılım. Yazılım mühendisliğinden sistem mühendisliğine uzanan ilişki. Yazılım mühendisliğinin kapsamı: Yazılım geliştirme (çözümleme, tasarım, kodlama ve sınama), yazılım mühendisliği yönetimi, yazılım yapılandırma yönetimi, yazılım mühendisliği süreçleri, araçları, yöntemleri ve kalite güvencesi. Yazılım ölçütleri ve maliyet kestirimi. Yazılım kalite maliyeti. Yazılım geliştirme süreç modelleri ve süreç referans modelleri.\n'
   },
   'Teknoloji Seminerleri 1':{
      '<CourseCode>':'BBM427',
      '<CourseName>':'Teknoloji Seminerleri 1',
      '<CourseCredit>':'0 1 0',
      '<CourseInfo>':'Öğrenci, bölüm sorumluları tarafından düzenlenecek bir dizi teknoloji seminerine katılmak zorundadır. Seminerlerin konusu mevcut teknoloji gündemine göre belirlenir. Seminerleri sunanlar bölümün içinden ya da dışından olacaktır.\n'
   },
   'Teknoloji Seminerleri 11':{
      '<CourseCode>':'BBM428',
      '<CourseName>':'Teknoloji Seminerleri 11',
      '<CourseCredit>':'0 1 0',
      '<CourseInfo>':'Öğrenci, bölüm sorumluları tarafından düzenlenecek bir dizi teknoloji seminerine katılmak zorundadır. Seminerlerin konusu mevcut teknoloji gündemine göre belirlenir. Seminerleri sunanlar bölümün içinden ya da dışından olabilir.\n'
   },
   'Veritabanı Yönetim Sistemleri':{
      '<CourseCode>':'BBM471',
      '<CourseName>':'Veritabanı Yönetim Sistemleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Veritabanı, veritabanı yönetim sistemleri, veritabanı yapısı, şemalar ve veri bağımsızlığı. Veri modelleri: Varlık-bağıntı modeli ve ilişkisel model. Bütünlük kısıtları ve ilişkisel tasarım: Alan kısıtları, referans kısıtları, nitelikler arası bağımlılıklar, normal biçimler, tasarım kriterleri. İlişkisel diller: İlişkisel cebir. SQL standard ilişkisel dili: veri tanımı, veri değişimi, veritabanı yönetim yöntemleri ve temel komutlar.Hareketler. Eşzamanlılık kontrolü ve serileştirme. Gerikazanım mekanizmaları.\n'
   },
   'Mekansal Bilgi Sistemleri':{
      '<CourseCode>':'BBM472',
      '<CourseName>':'Mekansal Bilgi Sistemleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Mekansal bilgi sistemlerininin bilimsel alanlarda ve karar vermede kullanımı. Mekansal bilgiye dayalı uygulamalar, mekansal gerçekçiliği modelleme, uzamsal veri derlemleri, mekansal veritabanları, mekansal çözümleme, kesinlik ve belirsizlik. Mekansal bilgi sistemlerinin yasal, ekonomik ve etik konular ile ilişkilendirilmesi, uydu tabanlı uzaktan algılama, akıllı taşıma sistemleri ve diğer mekansal bilgi sistemleri.\n'
   },
   'Veritabanı Laboratuvarı':{
      '<CourseCode>':'BBM473',
      '<CourseName>':'Veritabanı Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Gelişmiş veritabanı yönetim sistemleri, veri tabanı tanımı, veritabanlarında sorgu ve uygulama geliştirme. Veritabanı teknolojileri üzerine araştırma ve sunum, yedekleme ve onarım, popüler veritabanı sistemleri\n'
   },
   'Coğrafik Bilgi Dizgeleri Laboratuvarı':{
      '<CourseCode>':'BBM474',
      '<CourseName>':'Coğrafik Bilgi Dizgeleri Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Coğrafik bilgi dizgelerinin kavramları, CBD uygulamalarının girdileri, CBD uyumu, popüler coğrafik bilgi dizge araçlarının kullanımı, probleme özgü CBD veri yapıları, yeni jeo-uzamsal veri türlerinin oluşturulması, ayrıt tabanlı uzaklık işlevlerinin çözümlenmesi, jeo-uzamsal veritabanlarının tasarımı ve gerçekleştirimi, iyi bilinen CBD çözümleri\n'
   },
   'Yönetim Bilişim Dizgeleri':{
      '<CourseCode>':'BBM475',
      '<CourseName>':'Yönetim Bilişim Dizgeleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bilişim dizgelerinin temel kavramları, dizge teorisi, yönetimsel bilişim, bilişimin organizasyonlarda kavramsal modelleri, karar destek dizgeleri, kurumsal kaynak planlama dizgeleri, bilişim dizgesi projeleri için bilişim dizgeleri planlaması, bilişim sistemleri hayat döngüsü modelleri, bakım ilkeleri, yönetim ve denetim, bilişim dizgelerinim geliştirim, gerçekleştirim ve yönetimi.\n'
   },
   'Yazılım Geliştirme':{
      '<CourseCode>':'BBM481',
      '<CourseName>':'Yazılım Geliştirme',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Yazılım geliştirmenin temel aşamaları. Nesneye yönelik analiz, tasarım kavramları ve Birleşik Modelleme Dili (UML). UML görünümleri ve diyagramları. Kullanım durumu, etkinlik, durum, bileşen ve yerleşim diyagramları. Nesneye yönelik geliştirme süreçleri ve önerilen UML diyagramlarının kullanımı. Yazılım sistemlerinin örnek çözümlemeleri.\n'
   },
   'Yazılım Kalite Güvence':{
      '<CourseCode>':'BBM482',
      '<CourseName>':'Yazılım Kalite Güvence',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Yazılım geliştirme yaşam döngüsü ile yazılım kalite güvencenin temel kavramlarını sunar. Yazılım doğrulama ve geçerleme kavramları. Hata tanımı ve türleri. Yazılım doğrulama, geçerleme yöntemleri ve standartları. Yazılım gözden geçirme ve denetleme. Yazılım kalitesini ölçme için kullanılan metrikler. Yazılım test seviyeleri ve yöntemleri. İşlevsel ve yapısal test. Tümleştirme ve sistem testleri. Nesneye yönelik test.\n'
   },
   'Yazılım Geliştirme Laboratuvarı':{
      '<CourseCode>':'BBM483',
      '<CourseName>':'Yazılım Geliştirme Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Yazılım geliştirmenin temel adımlarına yönelik örnek çalışma üzerinde, UML kullanılan ödevlerden oluşur. Öğrencilerden ilk olarak kullanım durumu (use-case) analizini gerçekleştirmeleri beklenir. Ardından öğrenciler analiz ve tasarım çıktılarına dayanarak nesneye yönelik programlama uygulamaları ile sistemi gerçekleştirir.\n'
   },
   'Yazılım Kalite Güvence Laboratuvarı':{
      '<CourseCode>':'BBM484',
      '<CourseName>':'Yazılım Kalite Güvence Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Orta ölçekli yazılım sistemlerinde yazılım kalite güvencenin temel yöntemleri için uygulama yapmayı sağlar. Öğrencilere çalışan yazılım sistemleri atanır ve öğrencilerden genelde kabul görmüş yazılım test yöntemlerini kullanarak test tasarlama ve çalıştırmaları beklenir. Kod gözden geçirmesi kalite güvencenin bir parçası olarak uygulanır. Öğrenciler tasarım ve yazılım kalite güvence etkinliklerinin çıktılarını raporlar ve bu etkinlikleri gerçekleştirmenin maliyet ve faydalarını değerlendirerek rapora ekler.\n'
   },
   'Yazılım Mimarileri':{
      '<CourseCode>':'BBM485',
      '<CourseName>':'Yazılım Mimarileri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Yazılım mimarilerin temel kavramlarından bahseder. Yazılım mimari kavramları ve paydaşlar, yazılım mimarisi geliştirme süreci, mimari gereksinim analizi, yazılım mimari tasarımının modellenmesi başlıca konularıdır. Mimari görünümler ve perspektifler. İşlevsel, Bilgi, Geliştirme, Eş-zamanlı, Yayılıma ve İşletim görünümleri. Evrim, güvenilirlik, performans ve ölçeklenebilirlik, erişilebilirlik ve esneklik perspektifleri. Mimari stiller ve örüntüler. Mimari tasarım yöntemlerinin karşılaştırılması ve değerlendirilmesi. Yazılım ürün hattı mimarileri, alan modelleme ve alan mühendisliği.\n'
   },
   'Tasarım Örüntüleri':{
      '<CourseCode>':'BBM486',
      '<CourseName>':'Tasarım Örüntüleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Nesneye yönelik yazılım geliştirme sınırları içinde tasarım örüntülerini kapsar. Ders içeriği tasarım örüntülerinin faydaları, amaçları, ilkeleri; nesneye yönelik tasarımın ilkeleri; örüntü sınıflamalarını; tüm tasarım örüntülerinin, anti-örüntülerin, mimari örüntülerin incelenmesi ve önerkler içinde uygulanmasını kapsar.\n'
   },
   'Yazılım Mühendisliği Laboratuvarı':{
      '<CourseCode>':'BBM487',
      '<CourseName>':'Yazılım Mühendisliği Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Orta ölçekli bir yazılım uygulamasının yönetim ve geliştirme pratiklerini içeren mühendisliği. Yazılım projelerinin başlangıç gereksinimlerinin anlaşılması ve geliştirmelerin planlanması. Önceden tanımlanmış (Open Unified Process’i temel alan) yazılım geliştirme yaşam döngüsü içinde projelerin gereksinim analizi, mimari tasarımı ve detaylı tasarımı ve bu etkinliklerin çıktılarının (IEEE tarafından önerilen) belirli biçimlerde belgelendirilmesi. Laboratuvarın sonunda öğrenciler, bazı kritik gereksinimleri kodlanmış yazılım mimarisinin çalışan bir prototipini sunmalıdır. Yazılım tasarımı ve gerçekleştirimi boyunca J2EE teknolojilerinin kullanımı beklenmektedir.\n'
   },
   'Web Servisleri Laboratuvarı':{
      '<CourseCode>':'BBM488',
      '<CourseName>':'Web Servisleri Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Genişletilmiş İşaret Dili (XML), web servisleri, Servise Yönelik Mimari (SOA) ve İş Süreçleri Yönetimi (BPM) gibi web teknolojileri üzerine deneyler. SOA ve BPM kavramlarına temel olarak XML ve web servisleri. SOA and BPM kavramlarının niçin ve ne zaman kullanılacağının ödevler ve dönem projeleri ile öğretimi.\n'
   },
   'Web Mimarisinin Temelleri':{
      '<CourseCode>':'BBM490',
      '<CourseName>':'Web Mimarisinin Temelleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'İnternet ve istemci/sunucu tabanlı teknolojiler. Ölçeklenebilir, güvenli ve sürdürülebilir Web uygulamaları tasarlama ve geliştirme. İnternet tabanlı bilgi sistemleri, web tarayıcıları ve sunucuları, istemci ve sunucu tabanlı betik dilleri, JEE Web teknolojileri, servletler, JSPs, populer çatılar, JDBC, Hibernate, JTA, GWT, JSF, mimari ağırlıklı tasarım örüntüleri, bağımlılık enjeksyonu, spring, uygulama sunucuları.\n'
   },
   'Kişisel Yazılım Süreci':{
      '<CourseCode>':'BBM491',
      '<CourseName>':'Kişisel Yazılım Süreci',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bireysel yazılım geliştirmeye yol gösteren disiplini getiren Kişisel Yazılım Sürecinin (“Personal Software Porcess – PSP”) temel prensipleri. Öğrenciler güncel programlama uygulamalarını kullandıkları PSP0 süreci ile başlar. PSP süreci öğrencilerin her PSP versiyonunda 1 ya da 2 program yazdıkları 4 süreç versiyonu ile geliştirilmiştir. Öğrenciler geliştirdikleri her program için, ilgili süreç versiyonuna ek olarak önceki versiyonlarda öğrenilen yöntemleri de kullanırlar. Tüm PSP materyalleri daha önceden tanımlanmıştır ve Yazılım Mühendisliği Enstitüsünün resmi web sitesinden erişilebilir. (Ayrıntılı içerik)\n'
   },
   'Takım Yazılım Süreci':{
      '<CourseCode>':'BBM492',
      '<CourseName>':'Takım Yazılım Süreci',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Ekip halinde bir yazılım projesini yürütmeye kılavuzluk eden Takım Yazılım Süreci (“Team Software Process – TSPi”)’nin temel prensipleri. Küçük bir yazılım ekibi projesinin ihtiyaç duyduğu tüm formlar, betikler ve standartlar. Bir, iki ya da 3 geliştirme döngüsü. İlk döngüde sürecin uygulaması, ikinci döngüde takvim baskısı altında sürecin kullanımı, üçüncü döngüde ise ilk iki döngüde öğrenilenlerin içselleştirilmesi. Tüm TSPi materyalleri önceden tanımlanmıştır ve Yazılım Mühendisliği Enstitüsünün resmi web sitesinde yer almaktadır.\n'
   },
   'Kişisel Yazılım Süreci Laboratuvarı':{
      '<CourseCode>':'BBM493',
      '<CourseName>':'Kişisel Yazılım Süreci Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'PSP0 ve PSP1 süreçlerini temel alan deneylerin yürütüldüğü Kişisel Yazılım Süreci (Personal Software Process – PSP) dersinin tamamlayıcısı. Önceden tanımlanmış süreç versiyonlarını takip eden ve önceden tanımlanmış çıktıları üreten 6 deneyin gerçekleştirilmesi. Öğrenciler deneyleri gerçekleştirmek için iyi bildikleri herhangi bir programlama dilini kullanabilirler. Laboratuvarın sonunda, önceden tanımlanmış metrikleri kullanarak deneyleri gerçekleştirirken kendi performanslarını değerlendirdikleri bir final raporu hazırlarlar. Tüm laboratuvar materyalleri önceden tanımlanmıştır ve Yazılım Mühendisliği Enstitüsü resmi web sitesinden ulaşılabilir.\n'
   },
   'Takım Yazılım Süreci Laboratuvarı':{
      '<CourseCode>':'BBM494',
      '<CourseName>':'Takım Yazılım Süreci Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'TSPi (Team Softwar Process)’ye uygun olan deneylerin yürütüldüğü Takım Yazılım Süreci dersinin tamamlayıcısıdır. Öğrencilere önceden tanımlanmış roller atanır. Öğrenciler bir yazılım geliştirme projesini önceden tanımlanmış süreci takip ederek ve önceden tanımlanmış çıktıları üreterek bir takım olarak tamamlamak zorundadır. Tüm laboratuvara ait materyallere Yazılım Mühendisliği Enstitüsü resmi web sitesinden erişilebilir.\n'
   },
   'Görüntü işlemenin Temelleri':{
      '<CourseCode>':'BBM413',
      '<CourseName>':'Görüntü işlemenin Temelleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Görüntü oluşumu,\tNoktasal İşlemler ve histogram işleme, Uzlamsal filtreleme teknikleri,Frekans alanuı teknikleri, Görüntü düzleştirme, Kenar bulma, Görüntü bölütleme\n'
   },
   'Görüntü işleme Laboratuvarı':{
      '<CourseCode>':'BBM415',
      '<CourseName>':'Görüntü işleme Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Görüntü oluşumu, Noktasal İşlemler ve histogram işleme, Uzlamsal filtreleme teknikleri, Frekans alanı teknikleri, Görüntü düzleştirme, Kenar bulma, Görüntü bölütleme\n'
   },
   'Oyun Teknolojileri':{
      '<CourseCode>':'BBM421',
      '<CourseName>':'Oyun Teknolojileri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Oyun teknolojilerine genel bakış ve oyun üretme sürecinin öğrenilmesi.\n'
   },
   'Oyun Teknolojileri Laboratuvarı':{
      '<CourseCode>':'BBM423',
      '<CourseName>':'Oyun Teknolojileri Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Oyun teknolojilerine genel bakış ve oyun üretme sürecinin öğrenilmesi.\n'
   },
   'Bilgisayar Ağları':{
      '<CourseCode>':'BBM451',
      '<CourseName>':'Bilgisayar Ağları',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Yerel ağlar, Telli ve Telsiz Yerel Ağlar; Yineleyeci, Köprü ve Anahtar, Yönlendiriciler, Sanal Ağlar; Geniş Ağ Teknolojileri; TCP/IP Protokolu; IP Adresi Planlama; Yerel ve Geniş Ağ Tasarımı; TCP, UDP ve IP Katmanlarının İncelenmesi; DHCP; Yayın ve Küme İletişimi.\n'
   },
   'Bilgisayar Ağları Laboratuvarı':{
      '<CourseCode>':'BBM453',
      '<CourseName>':'Bilgisayar Ağları Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Ağ gereçlerini, ağ topolojilerini ve ağ uygulama yazılımlarını deney ortamında kullanma ve ağ kavramlarını pekiştirme.\n'
   },
   'Bilgi Güvenliği':{
      '<CourseCode>':'BBM463',
      '<CourseName>':'Bilgi Güvenliği',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Temel güvenlik ilkeleri, güvenlik tehditleri, güvenlik politikaları, temel şifreleme bilgisi, kullanıcı tanıma/yetkilendirme, program güvenliği, işletim sistemi güvenliği, ağ güvenliğine giriş\n'
   },
   'Bilgi Güvenliği Laboratuvarı':{
      '<CourseCode>':'BBM463',
      '<CourseName>':'Bilgi Güvenliği Laboratuvarı',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Temel şifreleme işlevleri, disk incelemesi, kod analiz araçları, çok karşılaşılan programlama hataları, web uygulama güvenliği, IPSEC /SSL protokolleri, güvenlik duvarı ayarlama, ağ tarama\n'
   },
   'Veri Yoğunluklu Uygulamalar':{
      '<CourseCode>':'BBM467',
      '<CourseName>':'Veri Yoğunluklu Uygulamalar',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Dağıtık hesaplama yaklaşımları, Koşut işlem ve yüksek başarımlı hesaplama mimarileri, Peer-to-peer sistemler, Hesaplama ızgaraları, Sanal makineler ve Internet Bulutları\n'
   },
   'Veri Yoğunluklu Uygulamalar Laboratuvarı':{
      '<CourseCode>':'BBM469',
      '<CourseName>':'Veri Yoğunluklu Uygulamalar Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'İş parçaları kullanma, koşut programlama, peer-to-peer ağlarda hesaplama, hesaplama ızgaraları, bulut hesaplama\n'
   },
   'Bilgisayar Grafiği':{
      '<CourseCode>':'BBM412',
      '<CourseName>':'Bilgisayar Grafiği',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bilgisayar grafiğine giriş. Grafik göstericilerin ve donanımlarının çalışma ilkeleri. Nokta-çizim teknikleri, Doğru-çizim teknikleri, iki boyutlu dönüşümler. Pencere teknikleri. Üç boyutlu grafiğe giriş ve dönüşüm teknikleri. Gölgeleme. Etkileşimli grafik donanımı ve yazılımları.\n'
   },
   'Bilgisayar Grafiği Laboratuvarı':{
      '<CourseCode>':'BBM414',
      '<CourseName>':'Bilgisayar Grafiği Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Bilgisayar grafiğine giriş. Grafik göstericilerin ve donanımlarının çalışma ilkeleri. Nokta-çizim teknikleri, Doğru-çizim teknikleri, iki boyutlu dönüşümler. Pencere teknikleri. Üç boyutlu grafiğe giriş ve dönüşüm teknikleri. Gölgeleme. Etkileşimli grafik donanımı ve yazılımları.\n'
   },
   'Bilgisayarlı Görünün Temelleri':{
      '<CourseCode>':'BBM416',
      '<CourseName>':'Bilgisayarlı Görünün Temelleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Görüntü oluşum fiziği, görüntü temsili, geometrik dönüşümler, ikili görüntü analizi, nokta ve nokta bulutu işleme, filtreler, konvolüsyon, kenar algılama, doku analizi ve sentezi, renk uzayları ve renk modelleri, değişimsiz görüntü özellikleri, optik akış, temel eşleştirme teknikleri.\n'
   },
   'Bilgisayarlı Görünün Temelleri Laboratuvarı':{
      '<CourseCode>':'BBM418',
      '<CourseName>':'Bilgisayarlı Görünün Temelleri Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Görüntü oluşum fiziği, görüntü temsili, geometrik dönüşümler, ikili görüntü analizi, nokta ve nokta bulutu işleme, filtreler, konvolüsyon, kenar algılama, doku analizi ve sentezi, renk uzayları ve renk modelleri, değişimsiz görüntü özellikleri, optik akış, temel eşleştirme teknikleri.\n'
   },
   'Hareketli Hesaplama':{
      '<CourseCode>':'BBM422',
      '<CourseName>':'Hareketli Hesaplama',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Hareketli ve kablosuz teknolojilere giriş,\tModern dağıtık sistemlerin tasarımı, Hareketli uygulama geliştirme teknolojiler, Üst seviye katmanları hizmet veren modern ağlardaki yöntem ve mimariler, Planlama, hareketlim sistemlerde yönetim ve güvenlik, Hareketli sistemler için oyun tasarımı.\n'
   },
   'Hareketli Hesaplama Laboratuvarı':{
      '<CourseCode>':'BBM424',
      '<CourseName>':'Hareketli Hesaplama Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Hareketli ve kablosuz teknolojilere giriş,\tModern dağıtık sistemlerin tasarımı, Hareketli uygulama geliştirme teknolojiler, Üst seviye katmanları hizmet veren modern ağlardaki yöntem ve mimariler, Planlama, hareketlim sistemlerde yönetim ve güvenlik, Hareketli sistemler için oyun tasarımı.\n'
   },
   'Gömülü Sistemler':{
      '<CourseCode>':'BBM432',
      '<CourseName>':'Gömülü Sistemler',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Mikroişleyiciler, bellek birimleri, giriş/çıkış arabirimleri, yardımcı işleyiciler, giriş/çıkış sürücüleri olarak algılayıcılar, elektromekanik güdüm araçları, mikrodenetleyiciler, gerçek-zamanlı işletim sistemleri, gerçek-zamanlı ve gömülü sistemler için yazılım geliştirme araçları.\n'
   },
   'Gömülü Sistemler Laboratuvarı':{
      '<CourseCode>':'BBM434',
      '<CourseName>':'Gömülü Sistemler Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Gömülü sistemlerin tasarımına ilişkin prensip ve algoritmalar. Örnek gömülü sistemler, haftalık deneyler.\n'
   },
   'Veri iletişimi':{
      '<CourseCode>':'BBM452',
      '<CourseName>':'Veri iletişimi',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Veri iletişimi temel tanım ve kavramlar; Veri türleri; Katmanlı ağ mimarisinde fiziksel katmana giriş; Örneksel ve sayısal imler ve özellikleri; Modülasyon; Modülasyon teknikleri; Sayısal kodlama; Çoklama; Geri-bildirim denetim allgoritmaları (Idle/Continuous IQ); Veri Bağlantı katmanı protokolları (HDLC, PPP, etc); Telli ve Telsiz Yerel ağlar; Geniş ağ teknolojileri: Frame Relay ve ATM\n'
   },
   'Özdevinirler Kuramı Ve Biçimsel Diller':{
      '<CourseCode>':'BBM401',
      '<CourseName>':'Özdevinirler Kuramı Ve Biçimsel Diller',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Özdevinirler teorisine giriş.Deterministik ve deterministik olmayan sonlu özdevinirler.Düzenli diller ve düzenli deyimler.Düzenli dillerin özellikleri ve düzenli diller için pumping lemma.Bağlamdan-bağımsız diller ve gramerler.Söz-dizim ağaçları.Yığıtlı özdevinirler.Yığıtlı özdevinirler ile bağlamdan-bağımsız gramerler arasındaki ilişki.Bağlamdan-bağımsız dillerin özellikleri ve bağlamdan-bağımsız diller için pumping lemma.Turing makineleri ve hesaplama teorisi.\n'
   },
   'Hesaplama Kuramı':{
      '<CourseCode>':'BBM402',
      '<CourseName>':'Hesaplama Kuramı',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Özdevinirler teorisi ve biçimsel diller.Biçimsel dillerin özellikleri ve biçimsel diller için pumping lemma.Church-Turing kuramı, Turing makineleri ve hesaplama kuramının modellenmesi.Çözülebilir ve çözülemeyen problemler.Karar verilebilirlik kavramı ve halting problemi.İndirgenebilirlik kavramı ve biçimsel diller teorisinde çözülemeyen problemler.Zaman karmaşıklığının ölçülmesi.P, NP, NP-Completeness kavramları ve Cook-Levin teorimi.\n'
   },
   'Kombinatorik Ve Çizge Kuramı':{
      '<CourseCode>':'BBM403',
      '<CourseName>':'Kombinatorik Ve Çizge Kuramı',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Temel kavramlar,Binom katsayıları, kapsama-dışlama kavramı.Çizge kuramında temel kavramlar, Çizge gösterimleri,Erişilebilirlilik, alt çizgeler, Eşbiçimlilik, bitişiklilik, Düzlemlilik, Boyama değeri, Eular çizgesi,Hamilton çizgesi, Çizge uygulamaları\n'
   },
   'Derleyici Gerçekleştiriminin Temelleri':{
      '<CourseCode>':'BBM404',
      '<CourseName>':'Derleyici Gerçekleştiriminin Temelleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Derleyicilerin yapıları.Sözcük çözümleme.Sözdizimsel çözümleme.Veri türü denetimi ve sözdizimsel güdümlü çeviri.Ara-kod üretimi, kod üretimi ve kod iyileştirme.Hata yönetimi.\n'
   },
   'Yapay Anlayışın Temelleri':{
      '<CourseCode>':'BBM405',
      '<CourseName>':'Yapay Anlayışın Temelleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Problem çözüm teknikleri: Durum uzayı yaklaşımı, problem-indirgeme yaklaşımı, tam kapsamlı arama algoritmaları, sezgisel arama algoritmaları, oyun tabanlı algoritmalar ve oyun ağaçları, mantık programlama ,bilgi temsili ve işleme, yapay zeka sistemlerinde öğrenme, yapay sinir ağları, önermeler mantığında ispat teorisi, birinci-derece yüklem mantığı, Bayes ağları, anlamsal ağlar, bulanık mantık, algılama, robot bilim.\n'
   },
   'Makine Öğrenmesinin Temelleri':{
      '<CourseCode>':'BBM406',
      '<CourseName>':'Makine Öğrenmesinin Temelleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Makine öğrenmesinin temel kavramları ve basit kavram öğrenme algoritmaları.Karar-ağaçları, neron ağları, bayes öğrenmesi, regresyon, destek vektör makineleri ve genetik algoritmalar gibi makine öğrenme algoritmaları.Yönetmeli ve yönetmesiz öğrenme yöntemleri.Özellik seçimi, boyut azaltması ve model seçimi.\n'
   },
   'Bulanık Mantık':{
      '<CourseCode>':'BBM407',
      '<CourseName>':'Bulanık Mantık',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bulanık mantık sisteminin genel yaklaşımı, bulanık kümeler, ilişkiler ve aritmetik. Olabilirlik ve olasılık kuramları ile bulanık mantık arası ilişkiler. Bulanık çıkarsama sistemleri ve türleri. Bulanık çıkarsamada karma yöntemler. Bulanık kümeleme. Genel uygulama alanlarının incelenmesi: Karar verme, örüntü tanıma, veri tabanı sistemleri, veri madenciliği.\n'
   },
   'Algoritma Analizi':{
      '<CourseCode>':'BBM408',
      '<CourseName>':'Algoritma Analizi',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Asimtotik gösterimler, özyineli ilişkiler, algoritma tasarımda genel teknikler, sıralama ve sıra istatistikleri, greedy/matris algoritmaları, dinamik programlama.\n'
   },
   'Makine Öğrenmesinin Laboratuvarı':{
      '<CourseCode>':'BBM409',
      '<CourseName>':'Makine Öğrenmesinin Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Makine Öğrenmesine Temel Bir Bakış, Doğrusal Regresyon, Küçük Kareler, Makine Öğrenmesi Metodolojisi, Olasılık ve Doğrusal Cebirin Temelleri, İstatistiksel Tahmin: MLE, MAP, Naif Bayes Sınıflandırıcı, Doğrusal Sınıflandırma Modelleri: Lojistik Regresyon, Doğrusal diskriminant fonksiyonu, Perceptron, Destek Vektör Makineleri, Karar Ağacı Öğrenmesi, Kolektif Öğrenme: Bagging, Boosting Clustering, Sinir Ağları, Temel Bileşenler Analizi.\n'
   },
   'Dinamik Sistemler':{
      '<CourseCode>':'BBM410',
      '<CourseName>':'Dinamik Sistemler',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Sistemler hakkında temel kavramlar.Durum-uzay gösterimleri.Kesikli ve sürekli zamanlı doğrusal dinamik sistemler.Doğrusal durum denklemleri.Doğrusal ve zamandan bağımsız sistemler.Denge noktaları. Kararlılık.Geri bildirim. Kontrol edilebilirlik. Gözlemlenebilirlik.\n'
   },
   'Proje 1':{
      '<CourseCode>':'BBM429',
      '<CourseName>':'Proje 1',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bu uygulamalı ders kapsamında, her öğrenciden danışmanlarının gözetiminde bir yazılım veya donanım geliştirmesi beklenmektedir. Donanım projelerinde CAD ve diğer donanım araçları kullanılır. Yazılım projelerinde ise kullanıcı dostu olunması ve yazılım mühendisliği tekniklerinin kullanılması gerekmektedir.\n'
   },
   'Proje 11':{
      '<CourseCode>':'BBM430',
      '<CourseName>':'Proje 11',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bu uygulamalı ders kapsamında, her öğrenciden danışmanlarının gözetiminde bir yazılım veya donanım geliştirmesi beklenmektedir. Donanım projelerinde CAD ve diğer donanım araçları kullanılır. Yazılım projelerinde ise kullanıcı dostu olunması ve yazılım mühendisliği tekniklerinin kullanılması gerekmektedir.\n'
   },
   'Gelişmiş Bilgisayar Mimarileri':{
      '<CourseCode>':'BBM431',
      '<CourseName>':'Gelişmiş Bilgisayar Mimarileri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Bilgisayar mimarilerinde temel konular ve son gelişmeler. Sanal bellek yapıları, bellek mimarileri, önbellekler, komut seti tasarımı, RISC mimarisi, işlemci mikro-mimarisi, üst ölçek mimariler, VLIW makineleri, vector bilgisayarlar, parallel bilgisayarlar.\n'
   },
   'Mikroişleyiciler':{
      '<CourseCode>':'BBM433',
      '<CourseName>':'Mikroişleyiciler',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Mikroişleyicili sistemlerde program geliştirmenin irdelenmesi. Mikroişleyicilerde arayüz birimlerinin denetim algoritmalarının geliştirilmesi. Bilgisayar sistemlerinde klavye, görüntü birimi gibi diğer birimler için denetim yazılımı geliştirme. Mikroişleyicilerde bellek ve giriş/çıkış birimleri arabirimleri bağlantıları. Donanım arabirimleri ve uygulamalar için bunların yazılımlarının geliştirilmesi.\n'
   },
   'Mikroişleyiciler Laboratuvari':{
      '<CourseCode>':'BBM436',
      '<CourseName>':'Mikroişleyiciler Laboratuvari',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Mikroişleyicili sistemlerde program geliştirme. Mikroişleyicilerde arayüz birimlerinin denetim algoritmalarının geliştirilmesi. Bilgisayar sistemlerinde klavye, görüntü birimi gibi diğer birimler için denetim yazılımı geliştirme. Mikroişleyicilerde bellek ve giriş/çıkış birimleri arabirimleri bağlantıları. Donanım arabirimleri ve uygulamalar için bunların yazılımlarının geliştirilmesi.\n'
   },
   'Koşut işlem':{
      '<CourseCode>':'BBM442',
      '<CourseName>':'Koşut işlem',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Koşut mantığa ve koşut programlamaya giriş, koşut bilgisayarlar için ağ topolojileri, GPU?lar, koşut bilgisayar mimarileri (SIMD, Shared Memory MIMD and Distributed Memory MIMD), zaman uyumlama mekanizmaları, koşut programlama modelleri, koşut algoritmaların çözümlenmesi ve tasarımı, farklı mimariler için koşut algoritma geliştirimi, koşut algoritmaların başarım ve karmaşıklığı ve seçilen bazı koşut algoritmarın vaka çalışmaları.\n'
   },
   'Hesaplamalı Fotografinin Temelleri':{
      '<CourseCode>':'BBM444',
      '<CourseName>':'Hesaplamalı Fotografinin Temelleri',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Kameralar ve görüntü oluşumu. Renk algısı.Görüntü işleme konu tekrarı.Veriye dayalı görüntü sentezleme.Görüntü düzenleme (bozma, dönüştürme, matlama, harmanlama, birleştirme) .Panoramalar, mozaikler ve kolajlar.Gürültü temizleme.Görüntü tamamlama.Yüksek dinamik aralıklı görüntüleme and ton eşleme.Derinlik and odağı bozma.Görüntü tabanlı ışıklandırma ve görsel gerçekleme.Foto gerçekçi olmayan görsel gerçekleme.\n'
   },
   'Hesaplamalı Fotografi Laboratuvarı':{
      '<CourseCode>':'BBM446',
      '<CourseName>':'Hesaplamalı Fotografi Laboratuvarı',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Kameralar ve görüntü oluşumu .Renk algısı .Görüntü işleme konu tekrarı .Veriye dayalı görüntü sentezleme .Görüntü düzenleme (bozma, dönüştürme, matlama, harmanlama, birleştirme) .Panoramalar, mozaikler ve kolajlar .Gürültü temizleme .Görüntü tamamlama .Yüksek dinamik aralıklı görüntüleme and ton eşleme .Derinlik and odağı bozma .Görüntü tabanlı ışıklandırma ve görsel gerçekleme .Goto gerçekçi olmayan görsel gerçekleme.\n'
   },
   'Bilgisayar Ve Ağ Güvenliği':{
      '<CourseCode>':'BBM456',
      '<CourseName>':'Bilgisayar Ve Ağ Güvenliği',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Şifreleme, sistem güvenliği, program güvenliği, ağ güvenliği.\n'
   },
   'Güvenli Programlama':{
      '<CourseCode>':'BBM461',
      '<CourseName>':'Güvenli Programlama',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Temel program güvenliği ilkeleri, Kabuk ve işletim sistemi kaynaklı açıklar, Taşırma saldırıları, Girdi hataları, Web güvenliği, Güvenlik çatıları, Kod analizi ve yazılım güvenlik testleri\n'
   },
   'Doğal Dil işlemeye Giriş 1':{
      '<CourseCode>':'BBM495',
      '<CourseName>':'Doğal Dil işlemeye Giriş 1',
      '<CourseCredit>':'3 0 3',
      '<CourseInfo>':'Doğal dil işlemeye giriş, Morfolojik analiz, Sözcük türlerinin etiketlenmesi, Ayrıştırma algoritmaları, Anlamsal analiz, Doğal dil işleme uygulama alanları\n'
   },
   'Doğal Dil işlemeye Giriş Laboratuvarı':{
      '<CourseCode>':'BBM497',
      '<CourseName>':'Doğal Dil işlemeye Giriş Laboratuvarı',
      '<CourseCredit>':'0 2 1',
      '<CourseInfo>':'Doğal dil işlemeye giriş, Morfolojik analiz, Sözcük türlerinin etiketlenmesi, Ayrıştırma algoritmaları, Anlamsal analiz, Doğal dil işleme uygulama alanları\n'
   }
}
