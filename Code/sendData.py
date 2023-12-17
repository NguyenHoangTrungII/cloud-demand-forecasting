import json
import pandas as pd
import yahoo_fin.stock_info as si
from azure.eventhub import EventHubProducerClient, EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub.exceptions import EventHubError
import asyncio
from datetime import datetime
from datetime import timedelta

connect_str = 'Endpoint=sb://stockvcb.servicebus.windows.net/;SharedAccessKeyName=stockvcb;SharedAccessKey=y+50XTX/nJ5BSNxBAYJVa8CJ4k3oQsZ1m+AEhHlunyE=;EntityPath=stockvcb'
event_hub = 'stockvcb'

def get_stock_data(stock,start_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = start_date + timedelta(days=1)
    stock_price = si.get_data(stock, start_date=start_date,end_date=end_date, index_as_date=False)
    # Convert 'date' column to string
    stock_price['date'] = stock_price['date'].dt.strftime('%Y-%m-%d')
    # Add 'time' column with current time
    stock_price['time'] = datetime.now().strftime('%H:%M:%S')

    return stock_price.to_dict('records')

async def run():
    start_date = datetime.strptime('17/11/2023', '%d/%m/%Y')
    end_date = datetime.now()
    while start_date <= end_date:
        await asyncio.sleep(30)  # Sleep for 10 seconds
        producer = EventHubProducerClient.from_connection_string(conn_str=connect_str, eventhub_name=event_hub)
        async with producer:
            event_data_batch = await producer.create_batch()
            event_data_batch.add(EventData(json.dumps(get_stock_data('VCB.VN', start_date.strftime('%Y-%m-%d')))))
            await producer.send_batch(event_data_batch)
            print("Send data to event hub at: ", datetime.now())
            print(json.dumps(get_stock_data('VCB.VN', start_date.strftime('%Y-%m-%d'))))
        if start_date.weekday() == 4:
            start_date += timedelta(days=3)
        else:
            start_date += timedelta(days=1)

loop=asyncio.get_event_loop()
try:
    asyncio.ensure_future(run())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()