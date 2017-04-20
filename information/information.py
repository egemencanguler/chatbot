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

COURSES = {  
   'Programlamaya Giriş 1':{
      'code':'BBM101',
      'name':'Programlamaya Giriş 1',
      'credit':'3 0 3',
      'info':'Bilgisayar programlamada temel kavramlar. Problem biçimselleştirme ve adımsal geliştirme yöntemiyle algoritma ve akış şemalarını geliştirme. Yapısal programlamayla ilgili temel kavramlar. Veri türleri ve değişken tanımlamaları. Temel kontrol yapıları. Şartlı dallanma ve döngüsel yapılar. İşlev kavramı ve işlevleri çağırma. Programlama dillerinde tek ve çok boyutlu diziler. Kütük işlemleri. Göstericiler.\n'
   },
   'Programlamaya Giriş Laboratuvarı 1':{
      'code':'BBM103',
      'name':'Programlamaya Giriş Laboratuvarı 1',
      'credit':'0 2 1',
      'info':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Programlamaya Giriş 11':{
      'code':'BBM102',
      'name':'Programlamaya Giriş 11',
      'credit':'3 0 3',
      'info':'Nesneye yönelik programlamanın temel kavramları. Nesneye yönelik programlama dillerini öğrenmeye giriş. Sınıf, nesne, sarmalama, kalıtım, çok-biçimlilik, soyut sınıf ve arayüz. Erişim denetleyiciler ve iletiler. Hata yönetme kavramları.\n'
   },
   'Programlamaya Giriş Laboratuvarı 11':{
      'code':'BBM104',
      'name':'Programlamaya Giriş Laboratuvarı 11',
      'credit':'0 2 1',
      'info':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Veri Yapıları':{
      'code':'BBM201',
      'name':'Veri Yapıları',
      'credit':'3 0 3',
      'info':'Veri yapılarının temelleri. Veri temsilleri arasındaki ilişkiler, algoritma tasarımı ve program verimliliği. Listeler, yığıtlar, kuyruklar, ağaçlar, öncelik kuyrukları, anahtarlama, çizgeler. Çok boyutlu/üçgensel/bant/matris gösterimleri. Tekil ve ikili dairesel bağlı listeler. Önde/arada/sonda deyimler.\n'
   },
   'Kesikli Matematiksel Yapılar':{
      'code':'BBM205',
      'name':'Kesikli Matematiksel Yapılar',
      'credit':'3 0 3',
      'info':'Kesikli matematik üzerine temel kavramlar: Matematiksel mantık, küme teorisi, ilişkiler ve işlevler. Önermeler mantığı, birinci düzey mantık ve matematiksel tümevarım. Kesikli yapılar: modüler aritmetik, durum makineleri, çizge teorisi, ağaçlar, sayma, özyineleme ve özyineli ilişkiler. Kesikli olasılık teorisi.\n'
   },
   'Mantıksal Tasarım Laboratuvarı':{
      'code':'BBM233',
      'name':'Mantıksal Tasarım Laboratuvarı',
      'credit':'0 2 1',
      'info':'Laboratuvar dersi aşağıda listesi verilen konular üzerinde uygulamalı ödevler içermektedir: Mantıksal kapılar, tümleşik devreler, Bool cebirinin özellikleri ve kuralları, birleşimli devreler, Bool işlevlerinin enküçüklemesi. Kod çeviriciler, çoklayıcılar, büyüklük karşılaştırıcı ve koşut toplayıcı devreler. İki durumlular ve sıralı devreler. Sayaçlar, yazmaçlar, seri toplayıcı devreler ve bellek elemanları.\n'
   },
   'Mantıksal Tasarım':{
      'code':'BBM231',
      'name':'Mantıksal Tasarım',
      'credit':'3 0 3',
      'info':'Sayısal sistemler, sayı sistemleri, ikili kodlar, hata tespit ve hata düzeltme kodları, Bool cebiri, anahtarlamalı cebir, ikili operasyonlar ve Bool işlevleri. Bool işlevlerinin minimizasyonu. Toplamsal mantık, mantık kapıları, toplamsal devrelerin minimizasyonu, mantık kapılarıyla devre tasarımı. Tümleşim devreler, MSO çipsetleriyle tasarım, ROM, PLA. Eşzamanlı sıralı devreler, bellek elemanları, analiz ve tasarım prosedürleri. Yazmaçlar, sayaçlar, RAM. Zaman uyumsuz sıralı devreler.\n'
   },
   'Yazılım Laboratuvarı 1':{
      'code':'BBM203',
      'name':'Yazılım Laboratuvarı 1',
      'credit':'0 2 1',
      'info':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Algoritmalar':{
      'code':'BBM202',
      'name':'Algoritmalar',
      'credit':'3 0 3',
      'info':'Algoritmalarla ilgili temel kavramlar. Asimtotik gösterim, başarım ölçütleri, alan/zaman karmaşıklığı. Özyinelemeli algoritmalar, özyineli ilişkiler, algoritma çözümleme kavramına giriş. İkili arama ağacı, tekrarlı ve özyineli ikili ağaç tarama. Çizgeler, önce derinlik, önce genişlik tabanlı arama, yayılım ağaçları, en kısa yol problem, kenar/ayrıt ağları üzerinde işlemler. Seçimli, eklemeleri, kabarcık, sayma tabanlı, hızlı, toplamsal, yığın ve radiks sıralama algoritmaları ve çözümlemeleri.\n'
   },
   'Bilgisayar Yapısı':{
      'code':'BBM234',
      'name':'Bilgisayar Yapısı',
      'credit':'3 0 3',
      'info':'Bilgisayar mimarisine ilişkin temel matematiksel ve mantıksal kavramlar. Veri temsili. Temel bilgisayar yapısı. Merkezi işlemci yapılanması: Akümülator-tabanlı, genel yazmaç tabanlı işlemciler ve yığıt makinesi mimarileri. Makine kod komut kavramları, mikro programlama kavramı, adresleme biçimleri. Bellek yapısı. Büyük depolama aygıtları. Giriş/çıkış birimleri. Sembolik programlamaya giriş.\n'
   },
   'Yazılım Laboratuvarı 11':{
      'code':'BBM204',
      'name':'Yazılım Laboratuvarı 11',
      'credit':'0 2 1',
      'info':'Laboratuvar dersi üç ya da daha fazla sayıda deneysel ödev içermektedir. Öğrencilerden ödevleriyle birlikte iyi tasarlanmış raporlar sunmaları beklenmektedir. Derleyici kullanımı, paket programlar ve güncel yazılım geliştirme ortamlarının kullanımı bu dersin birer parçası durumundadır.\n'
   },
   'Veri Yönetimi':{
      'code':'BBM371',
      'name':'Veri Yönetimi',
      'credit':'3 0 3',
      'info':'Temel kütük kavramları. İkincil depolama araçları ve fiziksel kütük organizasyonu. Kütük yönetim dizgeleri ve türleri. Temel kütük işleme operasyonları. Dizinler ve türleri. Anahtarlı dizinleme ve türleri. Ağaç yapısındaki dizinler. Sıralama. Uzamsal ve çok boyutlu dizinleme yapıları. Katlanmış dizinler.\n'
   },
   'Programlama Dilleri':{
      'code':'BBM301',
      'name':'Programlama Dilleri',
      'credit':'3 0 3',
      'info':'Programlama dillerindeki temel prensipler ve paradigmalar. Tüm ana konular ve dil paradigmaları kapsanmaktadır. Sözdizim, anlam, adlar, atamalar, tür kontrolü, alt programlar, anlamsal ve sözdizimsel çözümleyiciler, soyut veri türleri, tutarlılık, hata yönetimi. Buyurgan ve işlevsel diller için farklı tasarım seçenekleri ile anlamsal ve sözdizimsel çözümleyicilerin tasarımı.\n'
   },
   'Sistem Programlama':{
      'code':'BBM341',
      'name':'Sistem Programlama',
      'credit':'3 0 3',
      'info':'Sembolik dilin genel kavramları. Kaynak ve hedef program. Re-entrant ve tekrar çalıştırılabilir programlar. Adresleme teknikleri. Yordam tanımlamaları, yordam iletişim teknikleri, macro olanakları, İşletim sistemi- sembolik dil bağlantısı: Sistem çağrıları. Sistem çağrı mekanizması, giriş/çıkış arayüzleri. Yükleyiciler, bağlayıcılar. Mikro programlama. Tek ve çift geçişli birleştiriciler. Kesme mekanizması, kesme yönetimi. Temel I/O programlama teknikleri. Zamanlanmış ve kesmeye dayalı I/O programlama. Doğrudan bellek erişimi. Gömülü sistem I/O programlama örnekleri. Aygıt sürücüleri: Aygıt türleri, karakter aygıt sürücüleri ve örnekler, blok aygıt sürücüleri.\n'
   },
   'işletim Sistemleri':{
      'code':'BBM342',
      'name':'işletim Sistemleri',
      'credit':'3 0 3',
      'info':'İşletim sisteminin tanımı. Görev, süreç, toplu ve etkileşimli işleme, çoklu-görev ve gerçek-zamanlı işleme kavramları. Süreçler, bağlam ve görev değişimi, UNIX süreç durumu ve kuyruk çizenekleri, süreçlerin yönetim algoritmaları. İzlekler. Eş zamanlı süreçler. Süreçler arası iletişim, zaman-uyumlama, karşılıklı kaynak paylaşımı. Alt düzeyde zaman-uyumlama operasyonları ve semaforlar. Üst düzey zaman-uyumlama işlevleri. UNIX iletişim kanalları ve FIFOs. Kilitlenmeler. Bellek yönetimi: Tekil ve sürekli durağan bölümlemeli bellekler, değişim, sayfalama, bölütleme, sanal bellek. Kütük yönetimi: Dizin yapıları. FAT, i-node yapıları, kütük yerleşimi yöntemleri, güvenlik ve koruma. Dağıtık işleme, TCP/IP, istemci sunucu paradigması, soket programlama.\n'
   },
   'Yazılım Mühendisliği':{
      'code':'BBM382',
      'name':'Yazılım Mühendisliği',
      'credit':'3 0 3',
      'info':'Yazılım mühendisliğinin temel kavramları. Bilgisayar sistemlerinin türleri ve bir parçası olarak yazılım. Yazılım mühendisliğinden sistem mühendisliğine uzanan ilişki. Yazılım mühendisliğinin kapsamı: Yazılım geliştirme (çözümleme, tasarım, kodlama ve sınama), yazılım mühendisliği yönetimi, yazılım yapılandırma yönetimi, yazılım mühendisliği süreçleri, araçları, yöntemleri ve kalite güvencesi. Yazılım ölçütleri ve maliyet kestirimi. Yazılım kalite maliyeti. Yazılım geliştirme süreç modelleri ve süreç referans modelleri.\n'
   },
   'Teknoloji Seminerleri 1':{
      'code':'BBM427',
      'name':'Teknoloji Seminerleri 1',
      'credit':'0 1 0',
      'info':'Öğrenci, bölüm sorumluları tarafından düzenlenecek bir dizi teknoloji seminerine katılmak zorundadır. Seminerlerin konusu mevcut teknoloji gündemine göre belirlenir. Seminerleri sunanlar bölümün içinden ya da dışından olacaktır.\n'
   },
   'Teknoloji Seminerleri 11':{
      'code':'BBM428',
      'name':'Teknoloji Seminerleri 11',
      'credit':'0 1 0',
      'info':'Öğrenci, bölüm sorumluları tarafından düzenlenecek bir dizi teknoloji seminerine katılmak zorundadır. Seminerlerin konusu mevcut teknoloji gündemine göre belirlenir. Seminerleri sunanlar bölümün içinden ya da dışından olabilir.\n'
   },
   'Veritabanı Yönetim Sistemleri':{
      'code':'BBM471',
      'name':'Veritabanı Yönetim Sistemleri',
      'credit':'3 0 3',
      'info':'Veritabanı, veritabanı yönetim sistemleri, veritabanı yapısı, şemalar ve veri bağımsızlığı. Veri modelleri: Varlık-bağıntı modeli ve ilişkisel model. Bütünlük kısıtları ve ilişkisel tasarım: Alan kısıtları, referans kısıtları, nitelikler arası bağımlılıklar, normal biçimler, tasarım kriterleri. İlişkisel diller: İlişkisel cebir. SQL standard ilişkisel dili: veri tanımı, veri değişimi, veritabanı yönetim yöntemleri ve temel komutlar.Hareketler. Eşzamanlılık kontrolü ve serileştirme. Gerikazanım mekanizmaları.\n'
   },
   'Mekansal Bilgi Sistemleri':{
      'code':'BBM472',
      'name':'Mekansal Bilgi Sistemleri',
      'credit':'3 0 3',
      'info':'Mekansal bilgi sistemlerininin bilimsel alanlarda ve karar vermede kullanımı. Mekansal bilgiye dayalı uygulamalar, mekansal gerçekçiliği modelleme, uzamsal veri derlemleri, mekansal veritabanları, mekansal çözümleme, kesinlik ve belirsizlik. Mekansal bilgi sistemlerinin yasal, ekonomik ve etik konular ile ilişkilendirilmesi, uydu tabanlı uzaktan algılama, akıllı taşıma sistemleri ve diğer mekansal bilgi sistemleri.\n'
   },
   'Veritabanı Laboratuvarı':{
      'code':'BBM473',
      'name':'Veritabanı Laboratuvarı',
      'credit':'0 2 1',
      'info':'Gelişmiş veritabanı yönetim sistemleri, veri tabanı tanımı, veritabanlarında sorgu ve uygulama geliştirme. Veritabanı teknolojileri üzerine araştırma ve sunum, yedekleme ve onarım, popüler veritabanı sistemleri\n'
   },
   'Coğrafik Bilgi Dizgeleri Laboratuvarı':{
      'code':'BBM474',
      'name':'Coğrafik Bilgi Dizgeleri Laboratuvarı',
      'credit':'0 2 1',
      'info':'Coğrafik bilgi dizgelerinin kavramları, CBD uygulamalarının girdileri, CBD uyumu, popüler coğrafik bilgi dizge araçlarının kullanımı, probleme özgü CBD veri yapıları, yeni jeo-uzamsal veri türlerinin oluşturulması, ayrıt tabanlı uzaklık işlevlerinin çözümlenmesi, jeo-uzamsal veritabanlarının tasarımı ve gerçekleştirimi, iyi bilinen CBD çözümleri\n'
   },
   'Yönetim Bilişim Dizgeleri':{
      'code':'BBM475',
      'name':'Yönetim Bilişim Dizgeleri',
      'credit':'3 0 3',
      'info':'Bilişim dizgelerinin temel kavramları, dizge teorisi, yönetimsel bilişim, bilişimin organizasyonlarda kavramsal modelleri, karar destek dizgeleri, kurumsal kaynak planlama dizgeleri, bilişim dizgesi projeleri için bilişim dizgeleri planlaması, bilişim sistemleri hayat döngüsü modelleri, bakım ilkeleri, yönetim ve denetim, bilişim dizgelerinim geliştirim, gerçekleştirim ve yönetimi.\n'
   },
   'Yazılım Geliştirme':{
      'code':'BBM481',
      'name':'Yazılım Geliştirme',
      'credit':'3 0 3',
      'info':'Yazılım geliştirmenin temel aşamaları. Nesneye yönelik analiz, tasarım kavramları ve Birleşik Modelleme Dili (UML). UML görünümleri ve diyagramları. Kullanım durumu, etkinlik, durum, bileşen ve yerleşim diyagramları. Nesneye yönelik geliştirme süreçleri ve önerilen UML diyagramlarının kullanımı. Yazılım sistemlerinin örnek çözümlemeleri.\n'
   },
   'Yazılım Kalite Güvence':{
      'code':'BBM482',
      'name':'Yazılım Kalite Güvence',
      'credit':'3 0 3',
      'info':'Yazılım geliştirme yaşam döngüsü ile yazılım kalite güvencenin temel kavramlarını sunar. Yazılım doğrulama ve geçerleme kavramları. Hata tanımı ve türleri. Yazılım doğrulama, geçerleme yöntemleri ve standartları. Yazılım gözden geçirme ve denetleme. Yazılım kalitesini ölçme için kullanılan metrikler. Yazılım test seviyeleri ve yöntemleri. İşlevsel ve yapısal test. Tümleştirme ve sistem testleri. Nesneye yönelik test.\n'
   },
   'Yazılım Geliştirme Laboratuvarı':{
      'code':'BBM483',
      'name':'Yazılım Geliştirme Laboratuvarı',
      'credit':'0 2 1',
      'info':'Yazılım geliştirmenin temel adımlarına yönelik örnek çalışma üzerinde, UML kullanılan ödevlerden oluşur. Öğrencilerden ilk olarak kullanım durumu (use-case) analizini gerçekleştirmeleri beklenir. Ardından öğrenciler analiz ve tasarım çıktılarına dayanarak nesneye yönelik programlama uygulamaları ile sistemi gerçekleştirir.\n'
   },
   'Yazılım Kalite Güvence Laboratuvarı':{
      'code':'BBM484',
      'name':'Yazılım Kalite Güvence Laboratuvarı',
      'credit':'0 2 1',
      'info':'Orta ölçekli yazılım sistemlerinde yazılım kalite güvencenin temel yöntemleri için uygulama yapmayı sağlar. Öğrencilere çalışan yazılım sistemleri atanır ve öğrencilerden genelde kabul görmüş yazılım test yöntemlerini kullanarak test tasarlama ve çalıştırmaları beklenir. Kod gözden geçirmesi kalite güvencenin bir parçası olarak uygulanır. Öğrenciler tasarım ve yazılım kalite güvence etkinliklerinin çıktılarını raporlar ve bu etkinlikleri gerçekleştirmenin maliyet ve faydalarını değerlendirerek rapora ekler.\n'
   },
   'Yazılım Mimarileri':{
      'code':'BBM485',
      'name':'Yazılım Mimarileri',
      'credit':'3 0 3',
      'info':'Yazılım mimarilerin temel kavramlarından bahseder. Yazılım mimari kavramları ve paydaşlar, yazılım mimarisi geliştirme süreci, mimari gereksinim analizi, yazılım mimari tasarımının modellenmesi başlıca konularıdır. Mimari görünümler ve perspektifler. İşlevsel, Bilgi, Geliştirme, Eş-zamanlı, Yayılıma ve İşletim görünümleri. Evrim, güvenilirlik, performans ve ölçeklenebilirlik, erişilebilirlik ve esneklik perspektifleri. Mimari stiller ve örüntüler. Mimari tasarım yöntemlerinin karşılaştırılması ve değerlendirilmesi. Yazılım ürün hattı mimarileri, alan modelleme ve alan mühendisliği.\n'
   },
   'Tasarım Örüntüleri':{
      'code':'BBM486',
      'name':'Tasarım Örüntüleri',
      'credit':'3 0 3',
      'info':'Nesneye yönelik yazılım geliştirme sınırları içinde tasarım örüntülerini kapsar. Ders içeriği tasarım örüntülerinin faydaları, amaçları, ilkeleri; nesneye yönelik tasarımın ilkeleri; örüntü sınıflamalarını; tüm tasarım örüntülerinin, anti-örüntülerin, mimari örüntülerin incelenmesi ve önerkler içinde uygulanmasını kapsar.\n'
   },
   'Yazılım Mühendisliği Laboratuvarı':{
      'code':'BBM487',
      'name':'Yazılım Mühendisliği Laboratuvarı',
      'credit':'0 2 1',
      'info':'Orta ölçekli bir yazılım uygulamasının yönetim ve geliştirme pratiklerini içeren mühendisliği. Yazılım projelerinin başlangıç gereksinimlerinin anlaşılması ve geliştirmelerin planlanması. Önceden tanımlanmış (Open Unified Process’i temel alan) yazılım geliştirme yaşam döngüsü içinde projelerin gereksinim analizi, mimari tasarımı ve detaylı tasarımı ve bu etkinliklerin çıktılarının (IEEE tarafından önerilen) belirli biçimlerde belgelendirilmesi. Laboratuvarın sonunda öğrenciler, bazı kritik gereksinimleri kodlanmış yazılım mimarisinin çalışan bir prototipini sunmalıdır. Yazılım tasarımı ve gerçekleştirimi boyunca J2EE teknolojilerinin kullanımı beklenmektedir.\n'
   },
   'Web Servisleri Laboratuvarı':{
      'code':'BBM488',
      'name':'Web Servisleri Laboratuvarı',
      'credit':'0 2 1',
      'info':'Genişletilmiş İşaret Dili (XML), web servisleri, Servise Yönelik Mimari (SOA) ve İş Süreçleri Yönetimi (BPM) gibi web teknolojileri üzerine deneyler. SOA ve BPM kavramlarına temel olarak XML ve web servisleri. SOA and BPM kavramlarının niçin ve ne zaman kullanılacağının ödevler ve dönem projeleri ile öğretimi.\n'
   },
   'Web Mimarisinin Temelleri':{
      'code':'BBM490',
      'name':'Web Mimarisinin Temelleri',
      'credit':'3 0 3',
      'info':'İnternet ve istemci/sunucu tabanlı teknolojiler. Ölçeklenebilir, güvenli ve sürdürülebilir Web uygulamaları tasarlama ve geliştirme. İnternet tabanlı bilgi sistemleri, web tarayıcıları ve sunucuları, istemci ve sunucu tabanlı betik dilleri, JEE Web teknolojileri, servletler, JSPs, populer çatılar, JDBC, Hibernate, JTA, GWT, JSF, mimari ağırlıklı tasarım örüntüleri, bağımlılık enjeksyonu, spring, uygulama sunucuları.\n'
   },
   'Kişisel Yazılım Süreci':{
      'code':'BBM491',
      'name':'Kişisel Yazılım Süreci',
      'credit':'3 0 3',
      'info':'Bireysel yazılım geliştirmeye yol gösteren disiplini getiren Kişisel Yazılım Sürecinin (“Personal Software Porcess – PSP”) temel prensipleri. Öğrenciler güncel programlama uygulamalarını kullandıkları PSP0 süreci ile başlar. PSP süreci öğrencilerin her PSP versiyonunda 1 ya da 2 program yazdıkları 4 süreç versiyonu ile geliştirilmiştir. Öğrenciler geliştirdikleri her program için, ilgili süreç versiyonuna ek olarak önceki versiyonlarda öğrenilen yöntemleri de kullanırlar. Tüm PSP materyalleri daha önceden tanımlanmıştır ve Yazılım Mühendisliği Enstitüsünün resmi web sitesinden erişilebilir. (Ayrıntılı içerik)\n'
   },
   'Takım Yazılım Süreci':{
      'code':'BBM492',
      'name':'Takım Yazılım Süreci',
      'credit':'3 0 3',
      'info':'Ekip halinde bir yazılım projesini yürütmeye kılavuzluk eden Takım Yazılım Süreci (“Team Software Process – TSPi”)’nin temel prensipleri. Küçük bir yazılım ekibi projesinin ihtiyaç duyduğu tüm formlar, betikler ve standartlar. Bir, iki ya da 3 geliştirme döngüsü. İlk döngüde sürecin uygulaması, ikinci döngüde takvim baskısı altında sürecin kullanımı, üçüncü döngüde ise ilk iki döngüde öğrenilenlerin içselleştirilmesi. Tüm TSPi materyalleri önceden tanımlanmıştır ve Yazılım Mühendisliği Enstitüsünün resmi web sitesinde yer almaktadır.\n'
   },
   'Kişisel Yazılım Süreci Laboratuvarı':{
      'code':'BBM493',
      'name':'Kişisel Yazılım Süreci Laboratuvarı',
      'credit':'0 2 1',
      'info':'PSP0 ve PSP1 süreçlerini temel alan deneylerin yürütüldüğü Kişisel Yazılım Süreci (Personal Software Process – PSP) dersinin tamamlayıcısı. Önceden tanımlanmış süreç versiyonlarını takip eden ve önceden tanımlanmış çıktıları üreten 6 deneyin gerçekleştirilmesi. Öğrenciler deneyleri gerçekleştirmek için iyi bildikleri herhangi bir programlama dilini kullanabilirler. Laboratuvarın sonunda, önceden tanımlanmış metrikleri kullanarak deneyleri gerçekleştirirken kendi performanslarını değerlendirdikleri bir final raporu hazırlarlar. Tüm laboratuvar materyalleri önceden tanımlanmıştır ve Yazılım Mühendisliği Enstitüsü resmi web sitesinden ulaşılabilir.\n'
   },
   'Takım Yazılım Süreci Laboratuvarı':{
      'code':'BBM494',
      'name':'Takım Yazılım Süreci Laboratuvarı',
      'credit':'0 2 1',
      'info':'TSPi (Team Softwar Process)’ye uygun olan deneylerin yürütüldüğü Takım Yazılım Süreci dersinin tamamlayıcısıdır. Öğrencilere önceden tanımlanmış roller atanır. Öğrenciler bir yazılım geliştirme projesini önceden tanımlanmış süreci takip ederek ve önceden tanımlanmış çıktıları üreterek bir takım olarak tamamlamak zorundadır. Tüm laboratuvara ait materyallere Yazılım Mühendisliği Enstitüsü resmi web sitesinden erişilebilir.\n'
   },
   'Görüntü işlemenin Temelleri':{
      'code':'BBM413',
      'name':'Görüntü işlemenin Temelleri',
      'credit':'3 0 3',
      'info':'Görüntü oluşumu,\tNoktasal İşlemler ve histogram işleme, Uzlamsal filtreleme teknikleri,Frekans alanuı teknikleri, Görüntü düzleştirme, Kenar bulma, Görüntü bölütleme\n'
   },
   'Görüntü işleme Laboratuvarı':{
      'code':'BBM415',
      'name':'Görüntü işleme Laboratuvarı',
      'credit':'0 2 1',
      'info':'Görüntü oluşumu, Noktasal İşlemler ve histogram işleme, Uzlamsal filtreleme teknikleri, Frekans alanı teknikleri, Görüntü düzleştirme, Kenar bulma, Görüntü bölütleme\n'
   },
   'Oyun Teknolojileri':{
      'code':'BBM421',
      'name':'Oyun Teknolojileri',
      'credit':'3 0 3',
      'info':'Oyun teknolojilerine genel bakış ve oyun üretme sürecinin öğrenilmesi.\n'
   },
   'Oyun Teknolojileri Laboratuvarı':{
      'code':'BBM423',
      'name':'Oyun Teknolojileri Laboratuvarı',
      'credit':'0 2 1',
      'info':'Oyun teknolojilerine genel bakış ve oyun üretme sürecinin öğrenilmesi.\n'
   },
   'Bilgisayar Ağları':{
      'code':'BBM451',
      'name':'Bilgisayar Ağları',
      'credit':'3 0 3',
      'info':'Yerel ağlar, Telli ve Telsiz Yerel Ağlar; Yineleyeci, Köprü ve Anahtar, Yönlendiriciler, Sanal Ağlar; Geniş Ağ Teknolojileri; TCP/IP Protokolu; IP Adresi Planlama; Yerel ve Geniş Ağ Tasarımı; TCP, UDP ve IP Katmanlarının İncelenmesi; DHCP; Yayın ve Küme İletişimi.\n'
   },
   'Bilgisayar Ağları Laboratuvarı':{
      'code':'BBM453',
      'name':'Bilgisayar Ağları Laboratuvarı',
      'credit':'0 2 1',
      'info':'Ağ gereçlerini, ağ topolojilerini ve ağ uygulama yazılımlarını deney ortamında kullanma ve ağ kavramlarını pekiştirme.\n'
   },
   'Bilgi Güvenliği':{
      'code':'BBM463',
      'name':'Bilgi Güvenliği',
      'credit':'3 0 3',
      'info':'Temel güvenlik ilkeleri, güvenlik tehditleri, güvenlik politikaları, temel şifreleme bilgisi, kullanıcı tanıma/yetkilendirme, program güvenliği, işletim sistemi güvenliği, ağ güvenliğine giriş\n'
   },
   'Bilgi Güvenliği Laboratuvarı':{
      'code':'BBM463',
      'name':'Bilgi Güvenliği Laboratuvarı',
      'credit':'3 0 3',
      'info':'Temel şifreleme işlevleri, disk incelemesi, kod analiz araçları, çok karşılaşılan programlama hataları, web uygulama güvenliği, IPSEC /SSL protokolleri, güvenlik duvarı ayarlama, ağ tarama\n'
   },
   'Veri Yoğunluklu Uygulamalar':{
      'code':'BBM467',
      'name':'Veri Yoğunluklu Uygulamalar',
      'credit':'3 0 3',
      'info':'Dağıtık hesaplama yaklaşımları, Koşut işlem ve yüksek başarımlı hesaplama mimarileri, Peer-to-peer sistemler, Hesaplama ızgaraları, Sanal makineler ve Internet Bulutları\n'
   },
   'Veri Yoğunluklu Uygulamalar Laboratuvarı':{
      'code':'BBM469',
      'name':'Veri Yoğunluklu Uygulamalar Laboratuvarı',
      'credit':'0 2 1',
      'info':'İş parçaları kullanma, koşut programlama, peer-to-peer ağlarda hesaplama, hesaplama ızgaraları, bulut hesaplama\n'
   },
   'Bilgisayar Grafiği':{
      'code':'BBM412',
      'name':'Bilgisayar Grafiği',
      'credit':'3 0 3',
      'info':'Bilgisayar grafiğine giriş. Grafik göstericilerin ve donanımlarının çalışma ilkeleri. Nokta-çizim teknikleri, Doğru-çizim teknikleri, iki boyutlu dönüşümler. Pencere teknikleri. Üç boyutlu grafiğe giriş ve dönüşüm teknikleri. Gölgeleme. Etkileşimli grafik donanımı ve yazılımları.\n'
   },
   'Bilgisayar Grafiği Laboratuvarı':{
      'code':'BBM414',
      'name':'Bilgisayar Grafiği Laboratuvarı',
      'credit':'0 2 1',
      'info':'Bilgisayar grafiğine giriş. Grafik göstericilerin ve donanımlarının çalışma ilkeleri. Nokta-çizim teknikleri, Doğru-çizim teknikleri, iki boyutlu dönüşümler. Pencere teknikleri. Üç boyutlu grafiğe giriş ve dönüşüm teknikleri. Gölgeleme. Etkileşimli grafik donanımı ve yazılımları.\n'
   },
   'Bilgisayarlı Görünün Temelleri':{
      'code':'BBM416',
      'name':'Bilgisayarlı Görünün Temelleri',
      'credit':'3 0 3',
      'info':'Görüntü oluşum fiziği, görüntü temsili, geometrik dönüşümler, ikili görüntü analizi, nokta ve nokta bulutu işleme, filtreler, konvolüsyon, kenar algılama, doku analizi ve sentezi, renk uzayları ve renk modelleri, değişimsiz görüntü özellikleri, optik akış, temel eşleştirme teknikleri.\n'
   },
   'Bilgisayarlı Görünün Temelleri Laboratuvarı':{
      'code':'BBM418',
      'name':'Bilgisayarlı Görünün Temelleri Laboratuvarı',
      'credit':'0 2 1',
      'info':'Görüntü oluşum fiziği, görüntü temsili, geometrik dönüşümler, ikili görüntü analizi, nokta ve nokta bulutu işleme, filtreler, konvolüsyon, kenar algılama, doku analizi ve sentezi, renk uzayları ve renk modelleri, değişimsiz görüntü özellikleri, optik akış, temel eşleştirme teknikleri.\n'
   },
   'Hareketli Hesaplama':{
      'code':'BBM422',
      'name':'Hareketli Hesaplama',
      'credit':'3 0 3',
      'info':'Hareketli ve kablosuz teknolojilere giriş,\tModern dağıtık sistemlerin tasarımı, Hareketli uygulama geliştirme teknolojiler, Üst seviye katmanları hizmet veren modern ağlardaki yöntem ve mimariler, Planlama, hareketlim sistemlerde yönetim ve güvenlik, Hareketli sistemler için oyun tasarımı.\n'
   },
   'Hareketli Hesaplama Laboratuvarı':{
      'code':'BBM424',
      'name':'Hareketli Hesaplama Laboratuvarı',
      'credit':'0 2 1',
      'info':'Hareketli ve kablosuz teknolojilere giriş,\tModern dağıtık sistemlerin tasarımı, Hareketli uygulama geliştirme teknolojiler, Üst seviye katmanları hizmet veren modern ağlardaki yöntem ve mimariler, Planlama, hareketlim sistemlerde yönetim ve güvenlik, Hareketli sistemler için oyun tasarımı.\n'
   },
   'Gömülü Sistemler':{
      'code':'BBM432',
      'name':'Gömülü Sistemler',
      'credit':'3 0 3',
      'info':'Mikroişleyiciler, bellek birimleri, giriş/çıkış arabirimleri, yardımcı işleyiciler, giriş/çıkış sürücüleri olarak algılayıcılar, elektromekanik güdüm araçları, mikrodenetleyiciler, gerçek-zamanlı işletim sistemleri, gerçek-zamanlı ve gömülü sistemler için yazılım geliştirme araçları.\n'
   },
   'Gömülü Sistemler Laboratuvarı':{
      'code':'BBM434',
      'name':'Gömülü Sistemler Laboratuvarı',
      'credit':'0 2 1',
      'info':'Gömülü sistemlerin tasarımına ilişkin prensip ve algoritmalar. Örnek gömülü sistemler, haftalık deneyler.\n'
   },
   'Veri iletişimi':{
      'code':'BBM452',
      'name':'Veri iletişimi',
      'credit':'3 0 3',
      'info':'Veri iletişimi temel tanım ve kavramlar; Veri türleri; Katmanlı ağ mimarisinde fiziksel katmana giriş; Örneksel ve sayısal imler ve özellikleri; Modülasyon; Modülasyon teknikleri; Sayısal kodlama; Çoklama; Geri-bildirim denetim allgoritmaları (Idle/Continuous IQ); Veri Bağlantı katmanı protokolları (HDLC, PPP, etc); Telli ve Telsiz Yerel ağlar; Geniş ağ teknolojileri: Frame Relay ve ATM\n'
   },
   'Özdevinirler Kuramı Ve Biçimsel Diller':{
      'code':'BBM401',
      'name':'Özdevinirler Kuramı Ve Biçimsel Diller',
      'credit':'3 0 3',
      'info':'Özdevinirler teorisine giriş.Deterministik ve deterministik olmayan sonlu özdevinirler.Düzenli diller ve düzenli deyimler.Düzenli dillerin özellikleri ve düzenli diller için pumping lemma.Bağlamdan-bağımsız diller ve gramerler.Söz-dizim ağaçları.Yığıtlı özdevinirler.Yığıtlı özdevinirler ile bağlamdan-bağımsız gramerler arasındaki ilişki.Bağlamdan-bağımsız dillerin özellikleri ve bağlamdan-bağımsız diller için pumping lemma.Turing makineleri ve hesaplama teorisi.\n'
   },
   'Hesaplama Kuramı':{
      'code':'BBM402',
      'name':'Hesaplama Kuramı',
      'credit':'3 0 3',
      'info':'Özdevinirler teorisi ve biçimsel diller.Biçimsel dillerin özellikleri ve biçimsel diller için pumping lemma.Church-Turing kuramı, Turing makineleri ve hesaplama kuramının modellenmesi.Çözülebilir ve çözülemeyen problemler.Karar verilebilirlik kavramı ve halting problemi.İndirgenebilirlik kavramı ve biçimsel diller teorisinde çözülemeyen problemler.Zaman karmaşıklığının ölçülmesi.P, NP, NP-Completeness kavramları ve Cook-Levin teorimi.\n'
   },
   'Kombinatorik Ve Çizge Kuramı':{
      'code':'BBM403',
      'name':'Kombinatorik Ve Çizge Kuramı',
      'credit':'3 0 3',
      'info':'Temel kavramlar,Binom katsayıları, kapsama-dışlama kavramı.Çizge kuramında temel kavramlar, Çizge gösterimleri,Erişilebilirlilik, alt çizgeler, Eşbiçimlilik, bitişiklilik, Düzlemlilik, Boyama değeri, Eular çizgesi,Hamilton çizgesi, Çizge uygulamaları\n'
   },
   'Derleyici Gerçekleştiriminin Temelleri':{
      'code':'BBM404',
      'name':'Derleyici Gerçekleştiriminin Temelleri',
      'credit':'3 0 3',
      'info':'Derleyicilerin yapıları.Sözcük çözümleme.Sözdizimsel çözümleme.Veri türü denetimi ve sözdizimsel güdümlü çeviri.Ara-kod üretimi, kod üretimi ve kod iyileştirme.Hata yönetimi.\n'
   },
   'Yapay Anlayışın Temelleri':{
      'code':'BBM405',
      'name':'Yapay Anlayışın Temelleri',
      'credit':'3 0 3',
      'info':'Problem çözüm teknikleri: Durum uzayı yaklaşımı, problem-indirgeme yaklaşımı, tam kapsamlı arama algoritmaları, sezgisel arama algoritmaları, oyun tabanlı algoritmalar ve oyun ağaçları, mantık programlama ,bilgi temsili ve işleme, yapay zeka sistemlerinde öğrenme, yapay sinir ağları, önermeler mantığında ispat teorisi, birinci-derece yüklem mantığı, Bayes ağları, anlamsal ağlar, bulanık mantık, algılama, robot bilim.\n'
   },
   'Makine Öğrenmesinin Temelleri':{
      'code':'BBM406',
      'name':'Makine Öğrenmesinin Temelleri',
      'credit':'3 0 3',
      'info':'Makine öğrenmesinin temel kavramları ve basit kavram öğrenme algoritmaları.Karar-ağaçları, neron ağları, bayes öğrenmesi, regresyon, destek vektör makineleri ve genetik algoritmalar gibi makine öğrenme algoritmaları.Yönetmeli ve yönetmesiz öğrenme yöntemleri.Özellik seçimi, boyut azaltması ve model seçimi.\n'
   },
   'Bulanık Mantık':{
      'code':'BBM407',
      'name':'Bulanık Mantık',
      'credit':'3 0 3',
      'info':'Bulanık mantık sisteminin genel yaklaşımı, bulanık kümeler, ilişkiler ve aritmetik. Olabilirlik ve olasılık kuramları ile bulanık mantık arası ilişkiler. Bulanık çıkarsama sistemleri ve türleri. Bulanık çıkarsamada karma yöntemler. Bulanık kümeleme. Genel uygulama alanlarının incelenmesi: Karar verme, örüntü tanıma, veri tabanı sistemleri, veri madenciliği.\n'
   },
   'Algoritma Analizi':{
      'code':'BBM408',
      'name':'Algoritma Analizi',
      'credit':'3 0 3',
      'info':'Asimtotik gösterimler, özyineli ilişkiler, algoritma tasarımda genel teknikler, sıralama ve sıra istatistikleri, greedy/matris algoritmaları, dinamik programlama.\n'
   },
   'Makine Öğrenmesinin Laboratuvarı':{
      'code':'BBM409',
      'name':'Makine Öğrenmesinin Laboratuvarı',
      'credit':'0 2 1',
      'info':'Makine Öğrenmesine Temel Bir Bakış, Doğrusal Regresyon, Küçük Kareler, Makine Öğrenmesi Metodolojisi, Olasılık ve Doğrusal Cebirin Temelleri, İstatistiksel Tahmin: MLE, MAP, Naif Bayes Sınıflandırıcı, Doğrusal Sınıflandırma Modelleri: Lojistik Regresyon, Doğrusal diskriminant fonksiyonu, Perceptron, Destek Vektör Makineleri, Karar Ağacı Öğrenmesi, Kolektif Öğrenme: Bagging, Boosting Clustering, Sinir Ağları, Temel Bileşenler Analizi.\n'
   },
   'Dinamik Sistemler':{
      'code':'BBM410',
      'name':'Dinamik Sistemler',
      'credit':'3 0 3',
      'info':'Sistemler hakkında temel kavramlar.Durum-uzay gösterimleri.Kesikli ve sürekli zamanlı doğrusal dinamik sistemler.Doğrusal durum denklemleri.Doğrusal ve zamandan bağımsız sistemler.Denge noktaları. Kararlılık.Geri bildirim. Kontrol edilebilirlik. Gözlemlenebilirlik.\n'
   },
   'Proje 1':{
      'code':'BBM429',
      'name':'Proje 1',
      'credit':'3 0 3',
      'info':'Bu uygulamalı ders kapsamında, her öğrenciden danışmanlarının gözetiminde bir yazılım veya donanım geliştirmesi beklenmektedir. Donanım projelerinde CAD ve diğer donanım araçları kullanılır. Yazılım projelerinde ise kullanıcı dostu olunması ve yazılım mühendisliği tekniklerinin kullanılması gerekmektedir.\n'
   },
   'Proje 11':{
      'code':'BBM430',
      'name':'Proje 11',
      'credit':'3 0 3',
      'info':'Bu uygulamalı ders kapsamında, her öğrenciden danışmanlarının gözetiminde bir yazılım veya donanım geliştirmesi beklenmektedir. Donanım projelerinde CAD ve diğer donanım araçları kullanılır. Yazılım projelerinde ise kullanıcı dostu olunması ve yazılım mühendisliği tekniklerinin kullanılması gerekmektedir.\n'
   },
   'Gelişmiş Bilgisayar Mimarileri':{
      'code':'BBM431',
      'name':'Gelişmiş Bilgisayar Mimarileri',
      'credit':'3 0 3',
      'info':'Bilgisayar mimarilerinde temel konular ve son gelişmeler. Sanal bellek yapıları, bellek mimarileri, önbellekler, komut seti tasarımı, RISC mimarisi, işlemci mikro-mimarisi, üst ölçek mimariler, VLIW makineleri, vector bilgisayarlar, parallel bilgisayarlar.\n'
   },
   'Mikroişleyiciler':{
      'code':'BBM433',
      'name':'Mikroişleyiciler',
      'credit':'3 0 3',
      'info':'Mikroişleyicili sistemlerde program geliştirmenin irdelenmesi. Mikroişleyicilerde arayüz birimlerinin denetim algoritmalarının geliştirilmesi. Bilgisayar sistemlerinde klavye, görüntü birimi gibi diğer birimler için denetim yazılımı geliştirme. Mikroişleyicilerde bellek ve giriş/çıkış birimleri arabirimleri bağlantıları. Donanım arabirimleri ve uygulamalar için bunların yazılımlarının geliştirilmesi.\n'
   },
   'Mikroişleyiciler Laboratuvari':{
      'code':'BBM436',
      'name':'Mikroişleyiciler Laboratuvari',
      'credit':'3 0 3',
      'info':'Mikroişleyicili sistemlerde program geliştirme. Mikroişleyicilerde arayüz birimlerinin denetim algoritmalarının geliştirilmesi. Bilgisayar sistemlerinde klavye, görüntü birimi gibi diğer birimler için denetim yazılımı geliştirme. Mikroişleyicilerde bellek ve giriş/çıkış birimleri arabirimleri bağlantıları. Donanım arabirimleri ve uygulamalar için bunların yazılımlarının geliştirilmesi.\n'
   },
   'Koşut işlem':{
      'code':'BBM442',
      'name':'Koşut işlem',
      'credit':'3 0 3',
      'info':'Koşut mantığa ve koşut programlamaya giriş, koşut bilgisayarlar için ağ topolojileri, GPU?lar, koşut bilgisayar mimarileri (SIMD, Shared Memory MIMD and Distributed Memory MIMD), zaman uyumlama mekanizmaları, koşut programlama modelleri, koşut algoritmaların çözümlenmesi ve tasarımı, farklı mimariler için koşut algoritma geliştirimi, koşut algoritmaların başarım ve karmaşıklığı ve seçilen bazı koşut algoritmarın vaka çalışmaları.\n'
   },
   'Hesaplamalı Fotografinin Temelleri':{
      'code':'BBM444',
      'name':'Hesaplamalı Fotografinin Temelleri',
      'credit':'3 0 3',
      'info':'Kameralar ve görüntü oluşumu. Renk algısı.Görüntü işleme konu tekrarı.Veriye dayalı görüntü sentezleme.Görüntü düzenleme (bozma, dönüştürme, matlama, harmanlama, birleştirme) .Panoramalar, mozaikler ve kolajlar.Gürültü temizleme.Görüntü tamamlama.Yüksek dinamik aralıklı görüntüleme and ton eşleme.Derinlik and odağı bozma.Görüntü tabanlı ışıklandırma ve görsel gerçekleme.Foto gerçekçi olmayan görsel gerçekleme.\n'
   },
   'Hesaplamalı Fotografi Laboratuvarı':{
      'code':'BBM446',
      'name':'Hesaplamalı Fotografi Laboratuvarı',
      'credit':'3 0 3',
      'info':'Kameralar ve görüntü oluşumu .Renk algısı .Görüntü işleme konu tekrarı .Veriye dayalı görüntü sentezleme .Görüntü düzenleme (bozma, dönüştürme, matlama, harmanlama, birleştirme) .Panoramalar, mozaikler ve kolajlar .Gürültü temizleme .Görüntü tamamlama .Yüksek dinamik aralıklı görüntüleme and ton eşleme .Derinlik and odağı bozma .Görüntü tabanlı ışıklandırma ve görsel gerçekleme .Goto gerçekçi olmayan görsel gerçekleme.\n'
   },
   'Bilgisayar Ve Ağ Güvenliği':{
      'code':'BBM456',
      'name':'Bilgisayar Ve Ağ Güvenliği',
      'credit':'3 0 3',
      'info':'Şifreleme, sistem güvenliği, program güvenliği, ağ güvenliği.\n'
   },
   'Güvenli Programlama':{
      'code':'BBM461',
      'name':'Güvenli Programlama',
      'credit':'3 0 3',
      'info':'Temel program güvenliği ilkeleri, Kabuk ve işletim sistemi kaynaklı açıklar, Taşırma saldırıları, Girdi hataları, Web güvenliği, Güvenlik çatıları, Kod analizi ve yazılım güvenlik testleri\n'
   },
   'Doğal Dil işlemeye Giriş 1':{
      'code':'BBM495',
      'name':'Doğal Dil işlemeye Giriş 1',
      'credit':'3 0 3',
      'info':'Doğal dil işlemeye giriş, Morfolojik analiz, Sözcük türlerinin etiketlenmesi, Ayrıştırma algoritmaları, Anlamsal analiz, Doğal dil işleme uygulama alanları\n'
   },
   'Doğal Dil işlemeye Giriş Laboratuvarı':{
      'code':'BBM497',
      'name':'Doğal Dil işlemeye Giriş Laboratuvarı',
      'credit':'0 2 1',
      'info':'Doğal dil işlemeye giriş, Morfolojik analiz, Sözcük türlerinin etiketlenmesi, Ayrıştırma algoritmaları, Anlamsal analiz, Doğal dil işleme uygulama alanları\n'
   }
}

