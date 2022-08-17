from KekikSpatula import DiscUdemy

def test_udemy():
  kurs = DiscUdemy("python")

  print(kurs.veri)
  """
  json verisi döndürür

  {'kaynak': 'discudemy.com', 'veri': [{'dil': 'English', 'baslik': 'Software development in Python: A practical approach', 'baglanti': 'https://www.udemy.com/course/software-development-in-python-a-practical-approach/?couponCode=2E8015314165C7F47BEE'}, {'dil': 'English', 'baslik': 'Machine Learning & Data Science Foundations Masterclass', 'baglanti': 'https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/?couponCode=BFGIVEAWAY'}, {'dil': 'English', 'baslik': 'The Complete Python Programmer: From Scratch to Applications', 'baglanti': 'https://www.udemy.com/course/the-complete-python-programmer-from-scratch-to-applications/?couponCode=FF6C62A12C33DA78AA00'}, {'dil': 'Spanish', 'baslik': 'Curso de Python 3.9 | Aprende el lenguaje del futuro', 'baglanti': 'https://www.udemy.com/course/curso-de-python-39-aprende-el-lenguaje-del-futuro/?couponCode=8A7174552E6B2E83C119'}, {'dil': 'English', 'baslik': 'Some Python Modules to Create AI Projects', 'baglanti': 'https://www.udemy.com/course/some-python-modules-to-create-ai-projects_by_fadi/?couponCode=LETS_DO_IT'}, {'dil': 'English', 'baslik': 'Complete Linear Regression Analysis in Python', 'baglanti': 'https://www.udemy.com/course/machine-learning-basics-building-regression-model-in-python/?couponCode=NOVXXII20'}, {'dil': 'English', 'baslik': 'Python For Beginners Course In-Depth', 'baglanti': 'https://www.udemy.com/course/python-for-beginners-course-in-depth/?couponCode=5CDE23880B08D81FC4BC'}, {'dil': 'English', 'baslik': 'Python Demonstrations For Practice Course', 'baglanti': 'https://www.udemy.com/course/python-for-beginners-demonstration-course/?couponCode=069CFA8AA03B5D6B88C2'}, {'dil': 'English', 'baslik': 'Python And Flask Framework Complete Course | [LQ]', 'baglanti': 'https://www.udemy.com/course/flask-framework-complete-course-for-beginners/?couponCode=AAADEB9B3EE4266D7B6A'}, {'dil': 'English', 'baslik': 'Support Vector Machines in Python: SVM Concepts & Code', 'baglanti': 'https://www.udemy.com/course/machine-learning-adv-support-vector-machines-svm-python/?couponCode=NOVXXII20'}, {'dil': 'English', 'baslik': 'Python Bootcamp 2020 Build 15 working Applications and Games', 'baglanti': 'https://www.udemy.com/course/python-complete-bootcamp-2019-learn-by-applying-knowledge/?couponCode=BLACKFRIDAYSALE'}, {'dil': 'English', 'baslik': 'PySpark - Python Spark Hadoop coding framework & testing', 'baglanti': 'https://www.udemy.com/course/pyspark-python-spark-hadoop-coding-framework-testing/'}, {'dil': 'English', 'baslik': 'Python | 100 programming exercises + solutions | Data Types', 'baglanti': 'https://www.udemy.com/course/python-100-programming-exercises-data-types/'}, {'dil': 'English', 'baslik': 'Learn Python from basic to advance', 'baglanti': 'https://www.udemy.com/course/learn-python-from-basic-to-advance-h/'}, {'dil': 'English', 'baslik': 'Python OOPs Concepts', 'baglanti': 'https://www.udemy.com/course/python-oops/'}]}
  """

  for nesne in kurs.nesne:
    print(nesne.baslik)
  """
  json verisini python nesnesine dönüştürür.

  Software development in Python: A practical approach
  Machine Learning & Data Science Foundations Masterclass
  The Complete Python Programmer: From Scratch to Applications
  Curso de Python 3.9 | Aprende el lenguaje del futuro
  Some Python Modules to Create AI Projects
  Complete Linear Regression Analysis in Python
  Python For Beginners Course In-Depth
  Python Demonstrations For Practice Course
  Python And Flask Framework Complete Course | [LQ]
  Support Vector Machines in Python: SVM Concepts & Code
  Python Bootcamp 2020 Build 15 working Applications and Games
  PySpark - Python Spark Hadoop coding framework & testing
  Python | 100 programming exercises + solutions | Data Types
  Learn Python from basic to advance
  Python OOPs Concepts
  """


  print(kurs.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "discudemy.com",
    "veri": [
      {
        "dil": "English",
        "baslik": "Software development in Python: A practical approach",
        "baglanti": "https://www.udemy.com/course/software-development-in-python-a-practical-approach/?couponCode=2E8015314165C7F47BEE"
      },
      {
        "dil": "English",
        "baslik": "Machine Learning & Data Science Foundations Masterclass",
        "baglanti": "https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/?couponCode=BFGIVEAWAY"
      },
      {
        "dil": "English",
        "baslik": "The Complete Python Programmer: From Scratch to Applications",
        "baglanti": "https://www.udemy.com/course/the-complete-python-programmer-from-scratch-to-applications/?couponCode=FF6C62A12C33DA78AA00"
      },
      {
        "dil": "Spanish",
        "baslik": "Curso de Python 3.9 | Aprende el lenguaje del futuro",
        "baglanti": "https://www.udemy.com/course/curso-de-python-39-aprende-el-lenguaje-del-futuro/?couponCode=8A7174552E6B2E83C119"
      },
      {
        "dil": "English",
        "baslik": "Some Python Modules to Create AI Projects",
        "baglanti": "https://www.udemy.com/course/some-python-modules-to-create-ai-projects_by_fadi/?couponCode=LETS_DO_IT"
      },
      {
        "dil": "English",
        "baslik": "Complete Linear Regression Analysis in Python",
        "baglanti": "https://www.udemy.com/course/machine-learning-basics-building-regression-model-in-python/?couponCode=NOVXXII20"
      },
      {
        "dil": "English",
        "baslik": "Python For Beginners Course In-Depth",
        "baglanti": "https://www.udemy.com/course/python-for-beginners-course-in-depth/?couponCode=5CDE23880B08D81FC4BC"
      },
      {
        "dil": "English",
        "baslik": "Python Demonstrations For Practice Course",
        "baglanti": "https://www.udemy.com/course/python-for-beginners-demonstration-course/?couponCode=069CFA8AA03B5D6B88C2"
      },
      {
        "dil": "English",
        "baslik": "Python And Flask Framework Complete Course | [LQ]",
        "baglanti": "https://www.udemy.com/course/flask-framework-complete-course-for-beginners/?couponCode=AAADEB9B3EE4266D7B6A"
      },
      {
        "dil": "English",
        "baslik": "Support Vector Machines in Python: SVM Concepts & Code",
        "baglanti": "https://www.udemy.com/course/machine-learning-adv-support-vector-machines-svm-python/?couponCode=NOVXXII20"
      },
      {
        "dil": "English",
        "baslik": "Python Bootcamp 2020 Build 15 working Applications and Games",
        "baglanti": "https://www.udemy.com/course/python-complete-bootcamp-2019-learn-by-applying-knowledge/?couponCode=BLACKFRIDAYSALE"
      },
      {
        "dil": "English",
        "baslik": "PySpark - Python Spark Hadoop coding framework & testing",
        "baglanti": "https://www.udemy.com/course/pyspark-python-spark-hadoop-coding-framework-testing/"
      },
      {
        "dil": "English",
        "baslik": "Python | 100 programming exercises + solutions | Data Types",
        "baglanti": "https://www.udemy.com/course/python-100-programming-exercises-data-types/"
      },
      {
        "dil": "English",
        "baslik": "Learn Python from basic to advance",
        "baglanti": "https://www.udemy.com/course/learn-python-from-basic-to-advance-h/"
      },
      {
        "dil": "English",
        "baslik": "Python OOPs Concepts",
        "baglanti": "https://www.udemy.com/course/python-oops/"
      }
    ]
  }
  """

  print(kurs.tablo())
  """
  tabulate verisi döndürür.

  +---------+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
  | dil     | baslik                                                       | baglanti                                                                                                                  |
  |---------+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------|
  | English | Software development in Python: A practical approach         | https://www.udemy.com/course/software-development-in-python-a-practical-approach/?couponCode=2E8015314165C7F47BEE         |
  | English | Machine Learning & Data Science Foundations Masterclass      | https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/?couponCode=BFGIVEAWAY                 |
  | English | The Complete Python Programmer: From Scratch to Applications | https://www.udemy.com/course/the-complete-python-programmer-from-scratch-to-applications/?couponCode=FF6C62A12C33DA78AA00 |
  | Spanish | Curso de Python 3.9 | Aprende el lenguaje del futuro         | https://www.udemy.com/course/curso-de-python-39-aprende-el-lenguaje-del-futuro/?couponCode=8A7174552E6B2E83C119           |
  | English | Some Python Modules to Create AI Projects                    | https://www.udemy.com/course/some-python-modules-to-create-ai-projects_by_fadi/?couponCode=LETS_DO_IT                     |
  | English | Complete Linear Regression Analysis in Python                | https://www.udemy.com/course/machine-learning-basics-building-regression-model-in-python/?couponCode=NOVXXII20            |
  | English | Python For Beginners Course In-Depth                         | https://www.udemy.com/course/python-for-beginners-course-in-depth/?couponCode=5CDE23880B08D81FC4BC                        |
  | English | Python Demonstrations For Practice Course                    | https://www.udemy.com/course/python-for-beginners-demonstration-course/?couponCode=069CFA8AA03B5D6B88C2                   |
  | English | Python And Flask Framework Complete Course | [LQ]            | https://www.udemy.com/course/flask-framework-complete-course-for-beginners/?couponCode=AAADEB9B3EE4266D7B6A               |
  | English | Support Vector Machines in Python: SVM Concepts & Code       | https://www.udemy.com/course/machine-learning-adv-support-vector-machines-svm-python/?couponCode=NOVXXII20                |
  | English | Python Bootcamp 2020 Build 15 working Applications and Games | https://www.udemy.com/course/python-complete-bootcamp-2019-learn-by-applying-knowledge/?couponCode=BLACKFRIDAYSALE        |
  | English | PySpark - Python Spark Hadoop coding framework & testing     | https://www.udemy.com/course/pyspark-python-spark-hadoop-coding-framework-testing/                                        |
  | English | Python | 100 programming exercises + solutions | Data Types  | https://www.udemy.com/course/python-100-programming-exercises-data-types/                                                 |
  | English | Learn Python from basic to advance                           | https://www.udemy.com/course/learn-python-from-basic-to-advance-h/                                                        |
  | English | Python OOPs Concepts                                         | https://www.udemy.com/course/python-oops/                                                                                 |
  +---------+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
  """

  print(kurs.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['dil', 'baslik', 'baglanti']
  """