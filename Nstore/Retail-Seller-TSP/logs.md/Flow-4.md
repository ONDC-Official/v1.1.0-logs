**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/on_select**
- Warning: Quoted Price in /on_select INR 279 does not match with the total price of items in /select INR 358

**/init**
- City code mismatch in /search and /init
- Warning: items[1].quantity.count for item 14575 mismatches with the items quantity selected in /select

**/on_init**
- City code mismatch in search & on_init
- Warning: items[1].quantity.count for item 14575 mismatches with the items quantity selected in /select

**/confirm**
- City code mismatch in /search and /confirm
- Warning: items[1].quantity.count for item 14575 mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- City code mismatch in /search and /on_confirm

**/status**
- City code mismatch in /search and /status

**/on_status (Order-picked-up)**
- City code mismatch in search and /on_status_picked

**/on_status (Order-Delivered)**
- City code mismatch in search and /on_status_delivered
- order/updated_at timestamp can't be less than the delivery time

**/update**
- City code mismatch in /search and /update

**/on_update (Initiated)**
- City code mismatch in /search and /on_update_Return_Initiated

**/on_update (Liquidated)**
- City code mismatch in /search and /on_update_Liquidated

