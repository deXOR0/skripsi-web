import sys

ISPU = [
    {
        'min': 0,
        'max': 50,
        'emoji': '🙂',
        'category': 'Baik',
        'description': 'Tingkat kualitas udara yang sangat baik, tidak memberikan efek negatif terhadap manusia, hewan, tumbuhan.'
    },
    {
        'min': 51,
        'max': 100,
        'emoji': '😐',
        'category': 'Sedang',
        'description': 'Tingkat kualitas udara masih dapat diterima pada kesehatan manusia, hewan dan tumbuhan.'
    },
    {
        'min': 101,
        'max': 200,
        'emoji': '😷',
        'category': 'Tidak Sehat',
        'description': 'Tingkat kualitas udara yang bersifat merugikan pada manusia, hewan dan tumbuhan.'
    },
    {
        'min': 201,
        'max': 300,
        'emoji': '🤒',
        'category': 'Sangat Tidak Sehat',
        'description': 'Tingkat kualitas udara yang dapat mengakibatkan resiko kesehatan pada sejumlah segmen populasi yang terpapar.'
    },
    {
        'min': 300,
        'max': sys.maxsize,
        'emoji': '🤢',
        'category': 'Berbahaya',
        'description': 'Tingkat kualitas udara yang dapat merugikan kesehatan serius pada populasi dan perlu penanganan cepat.'
    },
]

day_of_week = [
    'Senin',
    'Selasa',
    'Rabu',
    'Kamis',
    'Jumat',
    'Sabtu',
    'Minggu',
]

month = [
    'Januari',
    'Februari',
    'Maret',
    'April',
    'Mei',
    'Juni',
    'Juli',
    'Agustus',
    'September',
    'Oktober',
    'November',
    'Desember',
]

def transform_to_class_name(category_name: str) -> str:
    return category_name.replace(' ', '-').lower()