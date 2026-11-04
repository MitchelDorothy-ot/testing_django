from django.shortcuts import render


# Create your views here.
def index(request):
    temp = 38.7
    humidity = 12
    wind = 14
    city = "Zanzibar"
    is_sunny = True
    users = ["Jane", "Jack", "Moha"]
    # package
    context = {
        'temperature': temp,
        'humidity': humidity,
        'wind_speed': wind,
        'city': city,
        'is_sunny': is_sunny,
        'users': users
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def students(request):
    scores = [{"names": "Garth Morton", "email": "quam.dignissim.pharetra@outlook.com", "score": 27, "age": 19},
              {"names": "Emma Short", "email": "ipsum.cursus.vestibulum@yahoo.com", "score": 87, "age": 20},
              {"names": "Kylan Mcpherson", "email": "cras@outlook.edu", "score": 37, "age": 25},
              {"names": "Josephine Roberson", "email": "dui.fusce@yahoo.com", "score": 78, "age": 22},
              {"names": "Urielle Freeman", "email": "congue.elit@outlook.net", "score": 55, "age": 25},
              {"names": "Jasper Perry", "email": "dui@icloud.couk", "score": 28, "age": 19},
              {"names": "Denton Benson", "email": "pellentesque.tellus.sem@icloud.ca", "score": 62, "age": 21},
              {"names": "Quinn Daniels", "email": "sed.tortor@protonmail.edu", "score": 23, "age": 23},
              {"names": "Axel Schwartz", "email": "sed@yahoo.net", "score": 45, "age": 24},
              {"names": "Oprah Landry", "email": "faucibus.leo@yahoo.com", "score": 25, "age": 22},
              {"names": "Keegan Lyons", "email": "accumsan.convallis.ante@protonmail.org", "score": 66, "age": 20},
              {"names": "Cara Shaw", "email": "sit.amet@google.couk", "score": 31, "age": 22},
              {"names": "Olivia Ryan", "email": "dictum@icloud.org", "score": 80, "age": 21},
              {"names": "Lawrence Finley", "email": "nunc.sollicitudin.commodo@icloud.net", "score": 54, "age": 22},
              {"names": "Charles Mccall", "email": "nulla@aol.org", "score": 23, "age": 23}]
    data = {"students":scores}
    return render(request, 'students.html')
