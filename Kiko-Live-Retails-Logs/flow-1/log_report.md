**/search**
- /message/intent must have required property 'item'

**/on_select**
- Warning: Quoted Price in /on_select INR 147.5 does not match with the total price of items in /select INR 150

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- City code mismatch in /search and /init
- address.building should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'
- City code mismatch in search & on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing/address must have required property 'building'
- City code mismatch in /search and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- City code mismatch in /search and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm

**/status**
- City code mismatch in /search and /status

**/on_status (Pending)**
-  Invoice url must be present as part of documents objects (only in Order-picked-up state and thereafter)
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_pending

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_picked
- order/updated_at timestamp can't be less than the pickup time

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_delivered

**/update**
- City code mismatch in /search and /update

**/on_update (Initiated)**
- City code mismatch in /search and /on_update_Return_Initiated

**/on_update (Return_Approved)**
- City code mismatch in /search and /on_update_Return_Approved
- message_id of all unsolicited /on_update calls should be same for a particular /update request

**/on_update (Return_Picked)**
- City code mismatch in /search and /on_update_Return_Picked
- message_id of all unsolicited /on_update calls should be same for a particular /update request

**/on_update (Return_Delivered)**
- City code mismatch in /search and /on_update_Return_Delivered
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- delivery timestamp (/end/time/timestamp) can't be less than or equal to the pickup timestamp (start/time/timestamp)

