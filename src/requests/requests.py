import requests

async def set_green(traffic_light_id: int | str):
    body = {
        'traffic-light-id': traffic_light_id,
    }
    response = await requests.post('http://localhost:3001/', body)
    return response
