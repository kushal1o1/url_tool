from django.shortcuts import render
from django.http import JsonResponse
import requests
from decouple import config 
from django.utils.html import escape


VIRUSTOTAL_API_KEY = config('VIRUS_TOTAL_API_KEY')


def check_url(request):
    if request.method == 'POST':
        rawurl = request.POST.get('url')
        url=escape(rawurl) 
        print(url)
        try:

            response = requests.get(url, timeout=5, allow_redirects=True)
            initial_url = response.url
            final_url = response.history[-1].url if response.history else initial_url
            status_code = response.status_code
            redirects = len(response.history)
            
           
            vt_url = f'https://www.virustotal.com/vtapi/v2/url/report'
            params = {'apikey': VIRUSTOTAL_API_KEY, 'resource': url}
            vt_response = requests.get(vt_url, params=params)
            vt_result = vt_response.json()
            
            vt_message = 'No data available.'
            if vt_result['response_code'] == 1:
                if vt_result['positives'] > 0:
                    vt_message = f'URL is malicious with {vt_result["positives"]} detections.'
                else:
                    vt_message = 'URL is clean.'
            else:
                vt_message = 'Unknown Url .'

            result_data = {
                'status': 'success',
                'message': 'URL checked.',
                'initial_url': initial_url,
                'final_url': final_url,
                'status_code': status_code,
                'redirects': redirects,
                'vt_message': vt_message,
            }
            return JsonResponse(result_data)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return render(request, 'CheckUrl/index.html')
