**/select**
- City code mismatch in /search and /select

**/on_select**
- City code mismatch in /search and /on_select
- context/timestamp difference between /on_select and /select should be smaller than 5 sec

**/on_init**
- context/timestamp difference between /on_init and /init should be smaller than 5 sec

**/confirm**
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"

**/on_update (Return_Approved)**
- /fulfillments/1/start/location must have required property 'descriptor'

**/on_update (Return_Picked)**
- /fulfillments/1/start/location must have required property 'descriptor'

**/on_update (Return_Delivered)**
- /fulfillments/1/start/location must have required property 'descriptor'

**/update (Refund)**
- /message/order/items/0/tags/ttl_approval must match format "duration"

