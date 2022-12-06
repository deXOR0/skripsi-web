from django.core.management.base import BaseCommand
from dashboard.models import *

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('Done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Address instances")
    Pollutant.objects.all().delete()
    Timestamp.objects.all().delete()
    District.objects.all().delete()
    City.objects.all().delete()


def create_city(city_name):
    """Creates an city object combining different elements from the list"""
    print("Creating city")

    city = City(city_name=city_name)

    city.save()
    print("{} city created.".format(city))
    return city


def create_district(city_id, district_name):
    """Creates an district object combining different elements from the list"""
    print("Creating district")

    district = District(city_id=city_id, district_name=district_name)

    district.save()
    print("{} district created.".format(district))
    return district


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    cities = [
        {
            "city": "Jakarta Barat",
            "detail": [
                {
                    "kecamatan": "Cengkareng",
                    "lat": "-6.1548795",
                    "long": "106.7379741"
                },
                {
                    "kecamatan": "Grogol Petamburan",
                    "lat": "-6.1639655",
                    "long": "106.7865605"
                },
                {
                    "kecamatan": "Taman Sari",
                    "lat": "-6.1461656",
                    "long": "106.8193746"
                },
                {
                    "kecamatan": "Tambora",
                    "lat": "-6.1463209",
                    "long": "106.800685"
                },
                {
                    "kecamatan": "Kebon Jeruk",
                    "lat": "-6.1915515",
                    "long": "106.765627"
                },
                {
                    "kecamatan": "Kalideres",
                    "lat": "-6.1361466",
                    "long": "106.7088995"
                },
                {
                    "kecamatan": "Palmerah",
                    "lat": "-6.1909945",
                    "long": "106.7963735"
                },
                {
                    "kecamatan": "Kembangan",
                    "lat": "-6.1911406",
                    "long": "106.741305"
                }
            ]
        },
        {
            "city": "Jakarta Pusat",
            "detail": [
                {
                    "kecamatan": "Cempaka Putih",
                    "lat": "-6.181269",
                    "long": "106.8670735"
                },
                {
                    "kecamatan": "Gambir",
                    "lat": "-6.1715045",
                    "long": "106.8175095"
                },
                {
                    "kecamatan": "Johar Baru",
                    "lat": "-6.1830499",
                    "long": "106.85432"
                },
                {
                    "kecamatan": "Kemayoran",
                    "lat": "-6.1627705",
                    "long": "106.859259"
                },
                {
                    "kecamatan": "Menteng",
                    "lat": "-6.195169",
                    "long": "106.838157"
                },
                {
                    "kecamatan": "Sawah Besar",
                    "lat": "-6.1555405",
                    "long": "106.8326644"
                },
                {
                    "kecamatan": "Senen",
                    "lat": "-6.184885",
                    "long": "106.8454394"
                },
                {
                    "kecamatan": "Tanah Abang",
                    "lat": "-6.2054174",
                    "long": "106.8074645"
                }
            ]
        },
        {
            "city": "Jakarta Selatan",
            "detail": [
                {
                    "kecamatan": "Cilandak",
                    "lat": "-6.2898024",
                    "long": "106.7903519"
                },
                {
                    "kecamatan": "Jagakarsa",
                    "lat": "-6.3302412",
                    "long": "106.7555948"
                },
                {
                    "kecamatan": "Kebayoran Baru",
                    "lat": "-6.2432178",
                    "long": "106.76632"
                },
                {
                    "kecamatan": "Kebayoran Lama",
                    "lat": "-6.2493164",
                    "long": "106.7103374"
                },
                {
                    "kecamatan": "Mampang Prapatan",
                    "lat": "-6.2502837",
                    "long": "106.786995"
                },
                {
                    "kecamatan": "Pancoran",
                    "lat": "-6.2579464",
                    "long": "106.808621"
                },
                {
                    "kecamatan": "Pasar Minggu",
                    "lat": "-6.2898153",
                    "long": "106.8215662"
                },
                {
                    "kecamatan": "Pesanggrahan",
                    "lat": "-6.2542923",
                    "long": "106.6851439"
                },
                {
                    "kecamatan": "Setiabudi",
                    "lat": "-6.2217758",
                    "long": "106.7953685"
                },
                {
                    "kecamatan": "Tebet",
                    "lat": "-6.2255218",
                    "long": "106.8157435"
                }
            ]
        },
        {
            "city": "Jakarta Timur",
            "detail": [
                {
                    "kecamatan": "Cakung",
                    "lat": "-6.185467",
                    "long": "106.9361121"
                },
                {
                    "kecamatan": "Cipayung",
                    "lat": "-6.2449956",
                    "long": "106.8092662"
                },
                {
                    "kecamatan": "Ciracas",
                    "lat": "-6.3289265",
                    "long": "106.878975"
                },
                {
                    "kecamatan": "Duren Sawit",
                    "lat": "-6.2531506",
                    "long": "106.9039447"
                },
                {
                    "kecamatan": "Jatinegara",
                    "lat": "-6.2292747",
                    "long": "106.8587078"
                },
                {
                    "kecamatan": "Kramat Jati",
                    "lat": "-6.27475",
                    "long": "106.865344"
                },
                {
                    "kecamatan": "Makasar",
                    "lat": "-6.2709",
                    "long": "106.897179"
                },
                {
                    "kecamatan": "Matraman",
                    "lat": "-6.20383",
                    "long": "106.8620266"
                },
                {
                    "kecamatan": "Pasar Rebo",
                    "lat": "-6.3249584",
                    "long": "106.855766"
                },
                {
                    "kecamatan": "Pulo Gadung",
                    "lat": "-6.1907914",
                    "long": "106.8916284"
                }
            ]
        },
        {
            "city": "Jakarta Utara",
            "detail": [
                {
                    "kecamatan": "Cilincing",
                    "lat": "-6.127581",
                    "long": "106.9397505"
                },
                {
                    "kecamatan": "Kelapa Gading",
                    "lat": "-6.1596905",
                    "long": "106.9005624"
                },
                {
                    "kecamatan": "Koja",
                    "lat": "-6.1204935",
                    "long": "106.9062345"
                },
                {
                    "kecamatan": "Pademangan",
                    "lat": "-6.1291943",
                    "long": "106.84039"
                },
                {
                    "kecamatan": "Penjaringan",
                    "lat": "-6.1145558",
                    "long": "106.7971455"
                },
                {
                    "kecamatan": "Tanjung Priok",
                    "lat": "-6.127665",
                    "long": "106.8706644"
                }
            ]
        }
    ]

    for city_data in cities:
        city = create_city(city_data['city'])
        districts = city_data['detail']

        for district_data in districts:
            district = create_district(
                city.city_id, district_data['kecamatan'])
