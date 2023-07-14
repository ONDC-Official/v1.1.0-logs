**/on_search**
- /message/catalog/bpp~1providers/0/items/3/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/1/items/3/descriptor/images must NOT have more than 3 items
- /bpp/providers[1]/locations[0]/gps coordinates must be specified with at least six decimal places of precision.

**/on_select**
- tax line item should not be present if price=0
- Warning: Quoted Price in /on_select INR 740 does not match with the total price of items in /select INR 1080

**/init**
- City code mismatch in /search and /init
- Warning: items[1].quantity.count for item 14577 mismatches with the items quantity selected in /select

**/on_init**
- City code mismatch in search & on_init
- Warning: items[1].quantity.count for item 14577 mismatches with the items quantity selected in /select

**/confirm**
- City code mismatch in /search and /confirm
- Warning: items[1].quantity.count for item 14577 mismatches with the items quantity selected in /select

**/on_confirm**
- City code mismatch in /search and /on_confirm

**/on_status (Order-picked-up)**
- City code mismatch in search and /on_status_picked

**/on_status (Order-Delivered)**
- City code mismatch in search and /on_status_delivered

**/update**
- City code mismatch in /search and /update

**/on_update (Initiated)**
- City code mismatch in /search and /on_update_Return_Initiated

