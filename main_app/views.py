from django.shortcuts import render

finches = [
    {
        'species': 'Galapagos finch',
        'beakLength': 13,
        'bodyWeight': 21,
        'color': 'brown',
        'habitat': 'tropical',
    },
    {
        'species': 'Zebra finch',
        'beakLength': 8,
        'bodyWeight': 12,
        'color': 'gray',
        'habitat': 'dry grasslands',
    },
    {
        'species': 'Crimson finch',
        'beakLength': 10,
        'bodyWeight': 14,
        'color': 'red',
        'habitat': 'forests',
    },
    {
        'species': 'Saffron finch',
        'beakLength': 11,
        'bodyWeight': 16,
        'color': 'yellow',
        'habitat': 'savannas',
    },
    {
        'species': 'European greenfinch',
        'beakLength': 9,
        'bodyWeight': 18,
        'color': 'green',
        'habitat': 'woodlands',
    },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })