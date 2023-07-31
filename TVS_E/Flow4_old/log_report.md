**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time

**/on_select**
- Warning: Quoted Price in /on_select INR 40207 does not match with the total price of items in /select INR 55216

**/init**
- Warning: items[0].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select

**/on_init**
- Warning: items[0].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select
- Quoted Price 40257 does not match with Net Breakup Price 40257.00000000001 in /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- Warning: items[0].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm
- payment object mismatches in /confirm & /on_confirm

**/on_status (Pending)**
- /fulfillments/0/start/time pickup time should not be present until order is picked
- address/area_code, address/door, address/street mismatches in /billing in /confirm and /on_status_pending

**/on_status (Order-picked-up)**
- address/area_code, address/door, address/street mismatches in /billing in /confirm and /on_status_picked

**/on_status (Order-Delivered)**
- address/area_code, address/door, address/street mismatches in /billing in /confirm and /on_status_delivered

**/on_update (Initiated)**
- /fulfillments/0/end/location/address must have required property 'locality'
- quote price should not change for return state Return_Initiated

**/on_update (Return_Approved)**
- /fulfillments/0/end/location/address must have required property 'locality'
- quote price should not change for return state Return_Approved

