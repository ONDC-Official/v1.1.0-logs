**/on_search**
- category in serviceability construct should be one of the category ids bpp/providers[0]/items/category_id

**/on_select**
- Count of item with id: ba3ca63c-927e-4ca3-8694-19e2c7b32911 does not match in select & on_select (suitable domain error should be provided)
- Warning: Quoted Price in /on_select INR 67815 does not match with the total price of items in /select INR 82824

**/init**
- Warning: items[0].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select

**/on_init**
- Warning: items[1].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select
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

**/on_update (Return_Picked)**
- /fulfillments/0/end/location/address must have required property 'locality'

**/on_update (Return_Delivered)**
- /fulfillments/0/end/location/address must have required property 'locality'
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id 1
