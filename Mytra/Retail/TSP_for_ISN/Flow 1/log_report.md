**/search**
- /message/intent must have required property 'item'

**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec

**/init**
- City code mismatch in /search and /init

**/on_init**
- City code mismatch in search & on_init
- context/timestamp difference between /on_init and /init should be smaller than 5 sec

**/confirm**
- City code mismatch in /search and /confirm
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- City code mismatch in /search and /on_confirm
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec

**/on_status (Pending)**
- City code mismatch in search and /on_status_pending

**/on_status (Order-picked-up)**
- City code mismatch in search and /on_status_picked

**/on_status (Order-Delivered)**
- City code mismatch in search and /on_status_delivered

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"
- City code mismatch in /search and /update

**/on_update (Initiated)**
- City code mismatch in /search and /on_update_Return_Initiated

**/on_update (Return_Approved)**
- /fulfillments/1/start/location must have required property 'descriptor'
- City code mismatch in /search and /on_update_Return_Approved

**/on_update (Return_Picked)**
- /fulfillments/1/start/location must have required property 'descriptor'
- City code mismatch in /search and /on_update_Return_Picked

**/on_update (Return_Delivered)**
- /fulfillments/1/start/location must have required property 'descriptor'
- City code mismatch in /search and /on_update_Return_Delivered

**/update (Refund)**
- /message/order/items/0/tags/ttl_approval must match format "duration"
- City code mismatch in /search and /update

