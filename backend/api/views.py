import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_restaurants_by_postcode(request, postcode):
    try:
        if not postcode:
            return JsonResponse({'error': 'Postcode is required'}, status=400)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }


        url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return JsonResponse({'error': f'API returned status code {response.status_code}'}, status=response.status_code)

        data = response.json()

        restaurants = []
        for item in data.get('restaurants', [])[:10]: 
            restaurant_data = {
                "Name": item['name'],
                "Cuisines": ", ".join(cuisine['name'] for cuisine in item.get('cuisines', [])),
                "Rating": item.get('rating', {}).get('starRating'),
                "Address": item.get('address', '')
            }
            restaurants.append(restaurant_data)

        return JsonResponse(restaurants, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
